from PIL import Image;import numpy as np,json,potrace
from scipy import ndimage as nd
K=3
def trace(mask,ox,oy,S):
    try:pl=potrace.Bitmap(~mask).trace(turdsize=30,alphamax=1.0,opticurve=True,opttolerance=0.5)
    except ValueError:pl=potrace.Bitmap(~mask).trace(turdsize=30,alphamax=1.0,opticurve=False)
    f=lambda p:f"{(p.x/K-ox)*S:.1f} {(p.y/K-oy)*S:.1f}"
    o=[]
    for c in pl:
        o.append("M"+f(c.start_point))
        for s in c.segments:o.append(("L"+f(s.c)+"L"+f(s.end_point)) if s.is_corner else ("C"+f(s.c1)+" "+f(s.c2)+" "+f(s.end_point)))
        o.append("Z")
    return "".join(o)
def classes(a):
    a=a.astype(int);r,g,b=a[...,0],a[...,1],a[...,2];mx=a.max(2);mn=a.min(2);ch=mx-mn
    red=(r>150)&(g<85)&(b<95)&(r-g>100)
    orange=(r>190)&(g>=95)&(g<175)&(b<90)
    yellow=(r>190)&(g>=175)&(b<120)
    beam=(r>215)&(g>205)&(b>=120)&(b<215)&(r-b>25)
    blue=(b-r>=55)&(b>=100)
    black=(mx<52)
    dgray=(mx>=52)&(mx<112)&(ch<28)
    g2=(mn>=112)&(mx<170)&(ch<30)
    g1=(mn>=170)&(mx<236)&(ch<30)
    return dict(g1=g1,beam=beam,g2=g2,dgray=dgray,yellow=yellow,orange=orange,blue=blue,red=red,black=black)
COL=dict(g1='#cfd1d4',beam='#f7efb0',g2='#8e9196',dgray='#4a4b4e',yellow='#f2c418',orange='#f07a1c',blue='#2f55c8',red='#d23a2e',black='@ink')
ORDER=['g1','beam','g2','dgray','yellow','orange','blue','red','black']
def run(f,cells,names,charfrac):
    SRC=Image.open(f).convert('RGB');tmp=[]
    for nm,(x0,y0,x1,y1),cf in zip(names,cells,charfrac):
        A=np.array(SRC);nwA=A.min(2)<232;lb,_=nd.label(nd.binary_dilation(nwA,iterations=3));bb=None
        for sl in nd.find_objects(lb):
            if sl is None:continue
            cyy=(sl[0].start+sl[0].stop)/2;cxx=(sl[1].start+sl[1].stop)/2
            if y0<=cyy<y1 and x0<=cxx<x1 and (sl[0].stop-sl[0].start)>12 and (sl[0].stop-sl[0].start)<(y1-y0)*1.2:
                if sl[0].start>=y1-6:continue
                b=(sl[1].start,sl[0].start,sl[1].stop,sl[0].stop);bb=b if bb is None else (min(bb[0],b[0]),min(bb[1],b[1]),max(bb[2],b[2]),max(bb[3],b[3]))
        P=8;cr=SRC.crop((bb[0]-P,bb[1]-P,bb[2]+P,min(bb[3]+P,y1)));a=np.array(cr);W,H=cr.size
        if bb[2]+P>=SRC.size[0]-2:a[:,-(P+5):]=255;cr=Image.fromarray(a)
        nonw=a.min(2)<232;dark=a.max(2)<60
        xl=int(W*cf[0]);xr=int(W*cf[1])   # character column range (fraction of crop)
        cm=np.zeros_like(nonw);cm[:,xl:xr]=True
        ys2=np.where((dark&cm).any(1))[0];top,bot=ys2[0],ys2[-1]
        tx=np.where(dark[top+2]&cm[top+2])[0].mean()
        tmp.append((nm,cr,a,W,H,nonw,dark,top,bot,tx))
    hmax=max(t[8]-t[7] for t in tmp)
    out=[]
    for nm,cr,a,W,H,nonw,dark,top,bot,tx in tmp:
        fz=hmax/476;S=1/fz;ax,ay=tx,bot;RC=top+int(62*fz)
        lab,n=nd.label(~nonw);bl=np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]]));bl=bl[bl>0];outside=np.isin(lab,bl)
        sil=nd.binary_closing(~outside,iterations=1)
        big=np.array(cr.resize((W*K,H*K),Image.LANCZOS))
        silb=np.array(Image.fromarray((sil*255).astype(np.uint8)).resize((W*K,H*K),Image.LANCZOS))>127
        cl=classes(big);nearB=nd.binary_dilation(cl['black'],iterations=4);layers=[]
        for k in ORDER:
            m=cl[k]&silb
            if k in('g1','g2','dgray','beam'):m=nd.binary_opening(m&~nearB,iterations=3);m=nd.binary_dilation(m,iterations=4)&silb
            elif k!='black':m=nd.binary_opening(m,iterations=1);m=nd.binary_dilation(m,iterations=2)&silb
            if m.sum()<60:continue
            layers.append([COL[k],trace(m,ax,ay,S)])
        silp=trace(silb,ax,ay,S)
        lab2,n2=nd.label(dark);hl=lab2[top+2,int(tx)] or lab2[top+3,int(tx)]
        hr=np.where(lab2[RC]==hl)[0];hr=hr[np.abs(hr-tx)<0.22*hmax]
        r=(hr[-1]-hr[0])/2;cx=(hr[-1]+hr[0])/2;cy=top+r
        feats=[]
        for i,sl in enumerate(nd.find_objects(lab2)):
            if i+1==hl or sl is None:continue
            fy=(sl[0].start+sl[0].stop)/2;fx=(sl[1].start+sl[1].stop)/2
            if (fx-cx)**2+(fy-cy)**2<(r-8*fz)**2:feats.append([sl[1].start,sl[0].start,sl[1].stop,sl[0].stop])
        cyc=lambda b:(b[1]+b[3])/2
        ec=[b for b in feats if cy-28*fz<cyc(b)<cy+30*fz and b[3]-b[1]>=18*fz and b[3]-b[1]<60*fz and b[2]-b[0]<40*fz]
        ec.sort(key=lambda b:-(b[2]-b[0])*(b[3]-b[1]));eyes=sorted(ec[:2],key=lambda b:b[0])
        eb=max([b[3] for b in eyes],default=cy)
        mo=[b for b in feats if cyc(b)>eb and b not in eyes and b[2]-b[0]<45*fz and b[3]-b[1]<34*fz]
        exc=np.mean([(b[0]+b[2])/2 for b in eyes]) if eyes else cx
        mo=[b for b in mo if b[2]-b[0]>=10*fz] or mo
        mouth=min(mo,key=lambda b:((b[0]+b[2])/2-exc)**2+(cyc(b)-eb-20*fz)**2) if mo else None
        rel=lambda b:[round(float(b[0]-ax)*S,1),round(float(b[1]-ay)*S,1),round(float(b[2]-ax)*S,1),round(float(b[3]-ay)*S,1)]
        out.append(dict(n=nm,h=476,dir=1,head=[round(float(cx-ax)*S,1),round(float(cy-ay)*S,1),round(float(r)*S,1)],eyes=[rel(b) for b in eyes] if len(eyes)==2 else [],mouth=rel(mouth) if mouth else None,sil=silp,layers=layers))
        print(nm,[(l[0],len(l[1])) for l in layers],out[-1]['head'],len(out[-1]['eyes']),out[-1]['mouth'])
    return out
C1=[(c*384,y0,(c+1)*384,y1) for (y0,y1) in [(0,450),(498,958)] for c in range(4)]
T1=run('refT1.png',C1,['inspect','panelcheck','think','explain','resetpress','listen','wait','resolved'],[(0,1)]*8)
C2=[(c*512,y0,(c+1)*512,y1) for (y0,y1) in [(0,458),(498,958)] for c in range(3)]
T2=run('refT2.png',C2,['stopsign','isolate','flashlight','clearjam','protreset','ready'],[(0,1),(0,.62),(0,.55),(0,.62),(0,.6),(0,1)])
open('tech_sprites.js','w').write('const TECH_SPR='+json.dumps(T1+T2,separators=(',',':'))+';\n')
