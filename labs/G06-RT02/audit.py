from pathlib import Path
import argparse, hashlib, json, subprocess, sys, tempfile
from PIL import Image
import numpy as np
p=argparse.ArgumentParser();p.add_argument('study',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
source=(a.study/'scene.svg').read_text(); runner=(a.study/'render.py').read_text()
def edit(s,old,new):
    assert s.count(old)==1,(old,s.count(old));return s.replace(old,new,1)
base='<use xlink:href="#base"/>'
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
rows=[]
for name,(s,r) in mutations.items():
    with tempfile.TemporaryDirectory() as tmp:
        d=Path(tmp);(d/'scene.svg').write_text(s);(d/'render.py').write_text(r)
        proc=subprocess.run([sys.executable,str(d/'render.py')],capture_output=True,text=True)
        report=json.loads((d/'results.json').read_text()) if (d/'results.json').exists() else None
        rows.append({'name':name,'survived':proc.returncode==0 and report is not None and all(report['checks'].values()),'exit':proc.returncode,'support':[v['motif_support_pixels'] for v in report['anchors']] if report else None,'changed':[v['changed_pixels'] for v in report['anchors']] if report else None,'last_error':proc.stderr.splitlines()[-1] if proc.stderr else None})
        if name=='baseline':
            b=np.array(Image.open(d/'base.png').convert('RGBA'));contrast=[]
            def lum(z):
                z=z[...,:3].astype(float)/255
                return np.where(z<=.04045,z/12.92,((z+.055)/1.055)**2.4)@np.array([.2126,.7152,.0722])
            for v in report['anchors']:
                im=np.array(Image.open(d/(v['variant']+'.png')).convert('RGBA'));m=np.any(b!=im,axis=2);lb,li=lum(b)[m],lum(im)[m]
                contrast.append({'variant':v['variant'],'mean_base_luminance':round(float(lb.mean()),5),'mean_composite_luminance':round(float(li.mean()),5),'mean_abs_luminance_change':round(float(np.abs(li-lb).mean()),5)})
result={'source_sha256':hashlib.sha256(source.encode()).hexdigest(),'runner_sha256':hashlib.sha256(runner.encode()).hexdigest(),'mutations':rows,'baseline_changed_support_luminance':contrast,'limitations':'Constructed mutations; not an estimate of general error coverage. Mean linear sRGB luma on changed pixels is not a perceptual contrast score or audience evidence.'}
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
