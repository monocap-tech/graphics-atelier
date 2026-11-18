import base64, io, json, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright
root=Path(__file__).parent
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=os.environ.get('CHROMIUM','/usr/bin/chromium'),args=['--no-sandbox'])
    page=b.new_page(); errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
    page.set_content((root/'preview.html').read_text())
    results=page.evaluate('''() => {
    const ctx=document.querySelector('canvas').getContext('2d'), pixel=(x,y)=>Array.from(ctx.getImageData(4*x+2,4*y+2,1,1).data), summaries={}; let cases=0,gridViolations=0,traceMismatches=0; const probe={};
    for (const s of ['abstract','hit','miss','cancel','moving']) {
      for(let t=0;t<72;t++) {const a=renderAt(s,t,true);const b=renderAt(s,t,false);cases+=2;if(JSON.stringify(a)!==JSON.stringify(b))traceMismatches++;if([12,18,27,36,51].includes(t)) {for(const fx of [true,false]) {renderAt(s,t,fx);const d=ctx.getImageData(0,0,640,360).data;for(let y=0;y<360;y+=4)for(let x=0;x<640;x+=4){let k=(y*640+x)*4,bad=false;for(let v=0;v<4;v++)for(let u=0;u<4;u++)for(let c=0;c<4;c++)if(d[k+c]!==d[((y+v)*640+x+u)*4+c])bad=true;gridViolations+=Number(bad);}}}}
      if(s!=='abstract'){const r=traces[s];summaries[s]={activeTicks:r.filter(f=>f.active).length,impacts:r.filter(f=>f.impact).map(f=>f.t),terminal:r[71].phase,event:r[71].event};}
    }
    for(const fx of [true,false]){let key=fx?'on':'off';renderAt('hit',12,fx);probe[key+'_flight']=pixel(36,45);renderAt('hit',27,fx);probe[key+'_impact']=pixel(96,45);renderAt('cancel',18,fx);probe[key+'_cancel']=pixel(56,45);renderAt('miss',27,fx);probe[key+'_miss_flight']=pixel(96,45);}
    const bright=p=>p[0]>170&&p[1]>150;const checks={same_state_with_fx:traceMismatches===0,expected_hit:summaries.hit.impacts.join()==='27'&&summaries.hit.activeTicks===21,expected_moving:summaries.moving.impacts.join()==='27',expected_miss:summaries.miss.impacts.length===0&&summaries.miss.event===43,expected_cancel:summaries.cancel.impacts.length===0&&summaries.cancel.event===18&&summaries.cancel.activeTicks===12,grid_samples:gridViolations===0,active_core_both_modes:['on','off'].every(k=>bright(probe[k+'_flight'])&&bright(probe[k+'_miss_flight'])),impact_mark_both_modes:['on','off'].every(k=>bright(probe[k+'_impact'])),cancel_no_bright_core:['on','off'].every(k=>!bright(probe[k+'_cancel']))};return {cases,gridSamples:50,gridViolations,traceMismatches,summaries,probe,checks};}''')
    results['browser']=b.version;results['pageErrors']=errors
    assert all(results['checks'].values()) and not errors,results
    # Actual pixel renders, four scenes. Keep 2x logical pixels in output.
    frames=page.evaluate('''() => Array.from({length:72},(_,t)=>['abstract','hit','miss','cancel'].map(s=>{renderAt(s,t,true);return document.querySelector('canvas').toDataURL('image/png').split(',')[1]}))''')
    b.close()
(root/'results.json').write_text(json.dumps(results,indent=2)+'\n')
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
labels=['ABSTRACT / RECURRENCE','INTERCEPT / CONTACT','MISS / CONTINUATION','CANCEL / NO IMPACT']
seq=[]
for t,images in enumerate(frames):
    im=Image.new('RGB',(672,450),(18,27,38));d=ImageDraw.Draw(im);d.text((12,7),f'INTERLEAVE  /  G06-P07     {t:02d}/71',font=font,fill=(229,240,238))
    for i,s in enumerate(images):
        x=12+(i%2)*328;y=35+(i//2)*204;d.text((x,y),labels[i],font=font,fill=(150,182,195));im.paste(Image.open(io.BytesIO(base64.b64decode(s))).convert('RGB').resize((320,180),Image.Resampling.NEAREST),(x,y+20))
    seq.append(im)
seq[0].save(root/'interleave.gif',save_all=True,append_images=seq[1:],duration=[50 if t%6==5 else 40 for t in range(72)],loop=0,disposal=2)
contact=Image.new('RGB',(1344,900),(18,27,38))
for i,t in enumerate([12,27,36,48]):contact.paste(seq[t],((i%2)*672,(i//2)*450))
contact.save(root/'contact-sheet.png')
print(json.dumps(results,indent=2))
