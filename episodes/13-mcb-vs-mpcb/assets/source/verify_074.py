import json,hashlib
from pathlib import Path
from PIL import Image,ImageDraw
import numpy as np
Path('output/ep13-074').mkdir(parents=True,exist_ok=True)
p=Path(__file__).resolve().parent.parent;d=json.loads((p/'assets-074.json').read_text())
order=['housing','terminals','coil','bimetal-heater','fixed-contact','arcchamber','moving-contact','plunger','phaseloss-slide','knob-mechanism','dial-cam']
lookup={r['file']:r for r in d['layers']};d['layers']=[lookup[f'mpcb-cut-{g}-v2.png'] for g in order]
for i,r in enumerate(d['layers']):r['composite_order']=i
im=Image.new('RGBA',(1536,1536))
for row in d['layers']:im=Image.alpha_composite(im,Image.open(p/row['file']))
im.save('output/ep13-074/cut-composite.png')
a=np.array(Image.open(p/'mpcb-front-v2.png'))[:,:,3];b=np.array(im)[:,:,3]
mask_mismatch=int(np.count_nonzero((a>128)!=(b>128)));assert mask_mismatch==0,mask_mismatch
files=['factory-panel-3p.png','mpcb-front-v2.png']+[r['file'] for r in d['layers']];rows=[]
for f in files:
 img=Image.open(p/f);ex=(1920,1080) if f.startswith('factory-') else (1536,1536);assert img.size==ex,(f,img.size);assert img.mode=='RGBA';aa=np.array(img)[:,:,3];assert aa.min()==0 and aa.max()==255;assert np.count_nonzero(aa>128)>20
 y,x=np.where(aa>128);rows.append({'file':f,'size_px':list(img.size),'sha256':hashlib.sha256((p/f).read_bytes()).hexdigest(),'alpha_bbox_px':[int(x.min()),int(y.min()),int(x.max()),int(y.max())]})
# Verify hidden pole heater surfaces do not bleed through static retained covers.
heater=np.array(Image.open(p/'mpcb-cut-bimetal-heater-v2.png'))[:,:,3]
assert heater[970,768]==0 and heater[970,966]==0
assert heater[970,570]>128
bounds=rows[1]['alpha_bbox_px'];d['files']=rows;d['validation']={'png_count':13,'dimensions_modes_transparency_nonempty':'passed','front_cut_alpha_silhouette_mismatch_pixels':mask_mismatch,'hidden_pole_heater_occlusion':'passed at3pole centres','front_alpha_bbox_px':bounds,'inspection':'front, panel and complete cutaway composite inspected as still images; final video not reviewed'}
d['notes']=['Static layer occlusion uses housing and terminal holdouts.','Phase-loss slider composites before the nearer knob/dial, so it does not draw over the handle.','Travel values are illustrative, not OEM mechanism measurements.']
(p/'assets-074.json').write_text(json.dumps(d,indent=2)+'\n')
frames=[Image.open(p/'mpcb-front-v2.png'),im,Image.open(p/'factory-panel-3p.png')];out=Image.new('RGB',(1500,650),'#e3e8ed');draw=ImageDraw.Draw(out)
for i,(img,label) in enumerate(zip(frames,['front v2','registered cutaway v2','panel3p'])):
 img.thumbnail((490,610));out.paste(img,(i*500+(500-img.width)//2,35+(610-img.height)//2),img);draw.text((i*500+10,10),label,fill='black')
out.save('output/ep13-074/final-qa.jpg')
print(json.dumps(d['validation']))
