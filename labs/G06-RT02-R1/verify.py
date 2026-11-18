"""Validate the frozen S04a fixture, not audience interpretation.
Run: python verify.py STUDY_DIR OUTPUT_JSON
"""
import argparse, hashlib, json, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image
import numpy as np

ANCHORS={'ornament':(167,212),'field':(225,84),'device':(353,142),'ui':(432,246)}
BASE='763cfa4ba5ebf125454bd760c46f517607826d04572687aa7f6957ca17d0ec3d'
MOTIF='eb0e402660c4bd8dfeb5d87982e5486404028bafd19677f5b28b937d757a560d'
PATCH='c4ac1689614ba8aedca9ee147880248f388c9f7c1b7bab164032ba1dc465b83b'
def digest(im):return hashlib.sha256(np.asarray(im).tobytes()).hexdigest()
def require(ok,what):
    if not ok:raise ValueError(what)
def validate(d):
    def read(n,size=(480,300)):
        im=Image.open(d/(n+'.png')).convert('RGBA');require(im.size==size,n+' dimension');return im
    b=read('base');m=read('motif');require(digest(b)==BASE,'base identity');require(digest(m)==MOTIF,'motif identity')
    patch=m.crop((220,130,260,170));require(digest(patch)==PATCH,'patch identity')
    support=np.asarray(patch)[:,:,3]>0;require(int(support.sum())==250,'nonempty support')
    rpt=json.loads((d/'results.json').read_text());rows=rpt['anchors'];require(len(rows)==4 and {r['variant'] for r in rows}==set(ANCHORS),'variant set')
    by={r['variant']:r for r in rows};dist={}
    for n,(x,y) in ANCHORS.items():
        r=by[n];require(r['anchor']==[x,y],n+' anchor');require(r['motif_support_pixels']==250 and r['changed_pixels']==250 and r['outside_changes']==0 and r['motif_patch_sha256']==PATCH,n+' recorded invariants')
        got=np.asarray(read(n));expected=b.copy();expected.alpha_composite(patch,(x-20,y-20));expected=np.asarray(expected)
        allowed=np.zeros((300,480),bool);allowed[y-20:y+20,x-20:x+20]=support
        changed=np.any(got!=np.asarray(b),axis=2);require(np.array_equal(changed,allowed),n+' exact changed support')
        err=np.abs(got.astype(int)-expected.astype(int));require(err.max()<=1,n+' source-over residual');dist[n]=int(err.max())
    plate=read('comparison',(1500,735));names=['base','ornament','field','device','ui','motif']
    for i,n in enumerate(names):
        im=read(n)
        if n=='motif':im=Image.alpha_composite(Image.new('RGBA',im.size,(36,57,68,255)),im)
        x=15+i%3*495;y=81+i//3*337
        require(np.array_equal(np.asarray(plate.crop((x,y,x+480,y+300))),np.asarray(im.convert('RGB').convert('RGBA'))),n+' plate consistency')
    return dist

def main():
    p=argparse.ArgumentParser();p.add_argument('study',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    source=(a.study/'scene.svg').read_text();runner=(a.study/'render.py').read_text()
    def edit(s,old,new):
        require(s.count(old)==1,'mutation match');return s.replace(old,new,1)
    base='<use xlink:href="#base"/>'
    # Exact RT02 mutation definitions, retained as literal code.
    mutations={
     'baseline':(source,runner),
     'blank_motif':(edit(source,'<g id="motif">','<g id="motif" opacity="0">'),runner),
     'all_four_same_anchor':(source,edit(runner,"anchors={'ornament':(167,212),'field':(225,84),'device':(353,142),'ui':(432,246)}","anchors={k:(167,212) for k in ('ornament','field','device','ui')}")),
     'swap_ornament_device':(source,edit(runner,"'ornament':(167,212),'field':(225,84),'device':(353,142)","'ornament':(353,142),'field':(225,84),'device':(167,212)")),
     'omit_motif_from_composite':(source,edit(runner,'im=render(insert(use(x,y)));','im=render(src);')),
     'remove_base_scene':(edit(source,base,''),runner),
     'uniform_unintended_motif_color':(source.replace('#e8c480','#777777').replace('#fff3cf','#aaaaaa'),runner),
     'misplace_composite_only':(source,edit(runner,'im=render(insert(use(x,y)));','im=render(insert(use(x+30,y)));')),
     'change_one_overlay_color':(source,edit(runner,'overlay=render(insert(use(x,y)).replace','overlay=render(insert(use(x,y)).replace("#e8c480","#222222" if name=="field" else "#e8c480").replace')),
    }
    extras=['missing_output','stale_other_variant','tampered_report','stale_plate','wrong_motif_only_position','one_channel_corrupt']
    rows=[]
    for name,(s,r) in list(mutations.items())+[(n,(source,runner)) for n in extras]:
        with tempfile.TemporaryDirectory() as tmp:
            d=Path(tmp);(d/'scene.svg').write_text(s);(d/'render.py').write_text(r)
            run=subprocess.run([sys.executable,str(d/'render.py')],capture_output=True,text=True)
            if run.returncode:
                rows.append({'name':name,'old_pass':False,'new_pass':False,'reason':'original assertion','max_channel_error':None});continue
            if name=='missing_output':(d/'field.png').unlink()
            if name=='stale_other_variant':(d/'field.png').write_bytes((d/'ornament.png').read_bytes())
            if name=='tampered_report':
                q=json.loads((d/'results.json').read_text());q['anchors'][0]['changed_pixels']=0;(d/'results.json').write_text(json.dumps(q))
            if name=='stale_plate':
                q=Image.open(d/'comparison.png').convert('RGBA');q.paste(Image.open(d/'base.png'),(510,81));q.save(d/'comparison.png')
            if name=='wrong_motif_only_position':
                q=Image.open(d/'motif.png').convert('RGBA');z=Image.new('RGBA',q.size);z.paste(q,(1,0));z.save(d/'motif.png')
            if name=='one_channel_corrupt':
                q=Image.open(d/'device.png').convert('RGBA');v=q.getpixel((353,142));q.putpixel((353,142),(v[0]-10,v[1],v[2],v[3]));q.save(d/'device.png')
            try:dist=validate(d);reason=None
            except FileNotFoundError as e:dist=None;reason="missing "+Path(e.filename).name
            except (ValueError,OSError,KeyError) as e:dist=None;reason=str(e)
            rows.append({'name':name,'old_pass':True,'new_pass':reason is None,'reason':reason,'max_channel_error':dist})
    require(rows[0]['new_pass'] and not any(r['new_pass'] for r in rows[1:]),'regression failed')
    result={'rows':rows,'detected_original':sum(not r['new_pass'] for r in rows[1:9]),'detected_additional':sum(not r['new_pass'] for r in rows[9:]),'limits':'Pinned decoded identity is fixture/version specific. Post-export mutations occurred after original checks. No semantic or general defect-coverage claim.'}
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
