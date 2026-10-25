from PIL import Image;import numpy as np,json,potrace
from scipy import ndimage as nd
import sys
SETS=[]
B=[(17,130,493,326),(14,475,493,683),(14,821,493,1031),(14,1166,493,1407),(511,123,988,397),(511,447,988,779),(510,817,989,1096),(509,1188,988,1408)]
NAMES=['idle','chin','crossarms','hips','present','pointhip','worry','cheek']
K=3;P=8
def trace(mask,ox,oy,K,S):
    bm=potrace.Bitmap(~mask);pl=bm.trace(turdsize=6,alphamax=1.0,opticurve=True,opttolerance=0.25)
    f=lambda p:f"{(p.x/K-ox)*S:.1f} {(p.y/K-oy)*S:.1f}"
    out=[]
    for c in pl:
        out.append("M"+f(c.start_point))
        for s in c.segments:
            if s.is_corner:out.append("L"+f(s.c)+"L"+f(s.end_point))
            else:out.append("C"+f(s.c1)+" "+f(s.c2)+" "+f(s.end_point))
        out.append("Z")
    return "".join(out)
res=[]
def run(SRC,B,NAMES,K):
    for nm,(y0,x0,y1,x1) in zip(NAMES,B):
        cr=SRC.crop((x0-P,y0-P,x1+P,y1+P));W,H=cr.size
        a=np.array(cr);dark=a<140
        # anchor: head centre x, ground = lowest dark row
        ys=np.where(dark.any(1))[0];top,bot=ys[0],ys[-1];fz=(bot-top)/476;S=1/fz;RC=top+int(62*fz)
        row=dark[RC];xs=np.where(row)[0]
        # head row: take outermost pair around the head (first & last dark in central 200px)
        hx=(xs[0]+xs[-1])/2
        # better: use top point of head
        tx=np.where(dark[top+2])[0].mean()
        ax,ay=tx,bot
        # silhouette = not reachable from border through non-dark
        lab,n=nd.label(~dark);outside=np.isin(lab,np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))
        sil=nd.binary_closing(~outside,iterations=1)
        up=lambda m:np.array(Image.fromarray((m*255).astype(np.uint8)).resize((W*K,H*K),Image.LANCZOS))>127
        big=np.array(cr.resize((W*K,H*K),Image.LANCZOS))<140
        ink=trace(big,ax,ay,K,S);silp=trace(up(sil),ax,ay,K,S)
        # face features: components inside head circle
        lab2,n2=nd.label(dark);hl=lab2[top+1,int(tx)] if dark[top+1,int(tx)] else lab2[top+2,int(tx)]
        # head radius from width at row top+62 restricted to head component
        hr=np.where(lab2[RC]==hl)[0];r=(hr[-1]-hr[0])/2;cx=(hr[-1]+hr[0])/2;cy=top+r
        feats=[]
        for i,sl in enumerate(nd.find_objects(lab2)):
            if i+1==hl or sl is None:continue
            fy=(sl[0].start+sl[0].stop)/2;fx=(sl[1].start+sl[1].stop)/2
            if (fx-cx)**2+(fy-cy)**2<(r-8*fz)**2:feats.append([sl[1].start,sl[0].start,sl[1].stop,sl[0].stop])
        cyc=lambda b:(b[1]+b[3])/2
        ec=[b for b in feats if cy-28*fz<cyc(b)<cy+10*fz and b[3]-b[1]>=18*fz and b[3]-b[1]<40*fz and b[2]-b[0]<30*fz]
        ec.sort(key=lambda b:-(b[2]-b[0])*(b[3]-b[1]));eyes=sorted(ec[:2],key=lambda b:b[0])
        mouth=[b for b in feats if cyc(b)>cy+14*fz and b not in eyes]
        mouth=[min(b[0] for b in mouth),min(b[1] for b in mouth),max(b[2] for b in mouth),max(b[3] for b in mouth)] if mouth else None
        rel=lambda b:[round(float(b[0]-ax)*S,1),round(float(b[1]-ay)*S,1),round(float(b[2]-ax)*S,1),round(float(b[3]-ay)*S,1)]
        res.append(dict(n=nm,h=476,head=[round(float(cx-ax)*S,1),round(float(cy-ay)*S,1),round(float(r)*S,1)],eyes=[rel(b) for b in eyes],mouth=rel(mouth) if mouth else None,sil=silp,ink=ink))
        print(nm,len(ink),len(silp),res[-1]['head'],res[-1]['eyes'],res[-1]['mouth'])
run(Image.open('ref.png').convert('L'),B,NAMES,3)
B2=[(21,50,310,335),(17,530,310,741),(18,921,310,1100),(18,1354,310,1602),(322,116,616,279),(322,451,616,774),(323,946,616,1141),(324,1352,616,1520),(630,56,926,335),(629,522,926,776),(629,939,926,1180),(629,1360,926,1514)]
N2=['shrug','presentup','onefinger','pointfar','clap','welcome','count','stop','palmsup','heart','presenttwo','clasp']
run(Image.open('ref2.png').convert('L'),B2,N2,5)
open('office_sprites.js','w').write('const OFFICE_SPR='+json.dumps(res,separators=(',',':'))+';\n')
