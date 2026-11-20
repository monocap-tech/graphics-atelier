from pathlib import Path
import io,json,hashlib
import cairosvg
import numpy as np
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parent
src=(root/'scene.svg').read_text()
anchors={'ornament':(167,212),'field':(225,84),'device':(353,142),'ui':(432,246)}
# acceptance: identical original symbol, integer translation, stationary base,
# no pixels outside the independently rendered motif support may change.
def render(xml):
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=xml.encode()))).convert('RGBA')
def insert(s):return src.replace('<!-- Instance chosen by renderer. -->',s)
def use(x,y):return f'<use xlink:href="#motif" transform="translate({x} {y})"/>'
base=render(src);base.save(root/'base.png');b=np.array(base)
images={'base':base}; rows=[];normalized=[]
for name,(x,y) in anchors.items():
    overlay=render(insert(use(x,y)).replace('<use xlink:href="#base"/>',''))
    im=render(insert(use(x,y))); images[name]=im;im.save(root/f'{name}.png')
    a=np.array(im);m=np.array(overlay);support=m[:,:,3]>0;diff=np.any(a!=b,axis=2)
    patch=m[y-20:y+20,x-20:x+20];normalized.append(patch)
    assert not np.any(diff & ~support),name
    rows.append({'variant':name,'anchor':[x,y],'motif_support_pixels':int(support.sum()),'changed_pixels':int(diff.sum()),'outside_changes':int((diff&~support).sum()),'motif_patch_sha256':hashlib.sha256(patch.tobytes()).hexdigest()})
assert all(np.array_equal(normalized[0],x) for x in normalized[1:])
only=render(insert(use(240,150)).replace('<use xlink:href="#base"/>',''));only.save(root/'motif.png');images['motif']=Image.alpha_composite(Image.new('RGBA',base.size,(36,57,68,255)),only)
# Presentation labels are not part of test stimuli. Individual PNGs are unlabelled.
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';f=ImageFont.truetype(font,18);h=ImageFont.truetype(font,25)
plate=Image.new('RGB',(1500,735),'#101e2b');d=ImageDraw.Draw(plate);d.text((20,12),'RADIANCE / S04a     One motif, four hosts',font=h,fill='#e7e9df')
labels={'base':'A   Context only','ornament':'B   Ornament','field':'C   Expressive field','device':'D   Sentinel aperture','ui':'E   Interface','motif':'F   Motif only'}
for i,name in enumerate(['base','ornament','field','device','ui','motif']):
    x=15+(i%3)*495;y=54+(i//3)*337;d.text((x,y),labels[name],font=f,fill='#c4d1d2');plate.paste(images[name].convert('RGB'),(x,y+27))
plate.save(root/'comparison.png')
report={'renderer':cairosvg.__version__,'viewport':[480,300],'anchors':rows,'checks':{'six_unlabelled_images_exported':all((root/(n+'.png')).exists() for n in images),'identical_translated_motif_rgba':True,'no_changes_outside_motif':True},'limits':'No audience data; placement and underlying contrast vary; no animation or real runtime. All intended meanings are hypotheses.'}
(root/'results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
