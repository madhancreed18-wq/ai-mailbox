from PIL import Image;import numpy as np,json,potrace
from scipy import ndimage as nd
P=8;K=3
def trace(mask,ox,oy,S):
    try:pl=potrace.Bitmap(~mask).trace(turdsize=30,alphamax=1.0,opticurve=True,opttolerance=0.5)
    except ValueError:pl=potrace.Bitmap(~mask).trace(turdsize=30,alphamax=1.0,opticurve=False)
    f=lambda p:f"{(p.x/K-ox)*S:.1f} {(p.y/K-oy)*S:.1f}"
    o=[]
    for c in pl:
        o.append("M"+f(c.start_point))
        for s in c.segments:
            o.append(("L"+f(s.c)+"L"+f(s.end_point)) if s.is_corner else ("C"+f(s.c1)+" "+f(s.c2)+" "+f(s.end_point)))
        o.append("Z")
    return "".join(o)
def classes(a):
    a=a.astype(int);r,g,b=a[...,0],a[...,1],a[...,2];mx=a.max(2);mn=a.min(2)
    red=(r-g>70)&(r>120)
    blue=(b-r>=55)&(b>=118)&~red
    navy=(b-r>=22)&(b<118)&~blue&~red
    black=(mx<105)&~navy&~blue&~red
    gray2=(mn>=105)&(mx<165)&((mx-mn)<30)
    gray1=(mn>=165)&(mx<236)&((mx-mn)<30)
    return dict(black=black,navy=navy,blue=blue,red=red,g2=gray2,g1=gray1)
COL=dict(g1='#cfd2d6',g2='#8c8f94',blue='#3f77c6',navy='#152a4f',red='#c8323a',black='@ink')
ORDER=['g1','g2','blue','navy','red','black']
def run(f,B,N):
    SRC=Image.open(f).convert('RGB');out=[]
    for nm,(y0,x0,y1,x1) in zip(N,B):
        cr=SRC.crop((x0-P,y0-P,x1+P,y1+P));W,H=cr.size;a=np.array(cr)
        dark=a.min(2)<90
        nonw=a.min(2)<236
        ys=np.where(nonw.any(1))[0];top,bot=ys[0],ys[-1];fz=(bot-top)/476;S=1/fz;RC=top+int(62*fz)
        tx=np.where(nonw[top+2])[0].mean();ax,ay=tx,bot
        lab,n=nd.label(~nonw);outside=np.isin(lab,np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))
        sil=nd.binary_closing(~outside,iterations=1)
        big=np.array(cr.resize((W*K,H*K),Image.LANCZOS))
        silb=np.array(Image.fromarray((sil*255).astype(np.uint8)).resize((W*K,H*K),Image.LANCZOS))>127
        cl=classes(big);layers=[]
        nearB=nd.binary_dilation(cl['black'],iterations=4)
        for k in ORDER:
            m=cl[k]&silb
            if k in('g1','g2'):m=nd.binary_opening(m&~nearB,iterations=3);m=nd.binary_dilation(m,iterations=4)&silb
            if k in('blue','navy'):m=nd.binary_opening(m,iterations=2)
            if k!='black':m=nd.binary_dilation(m,iterations=2)&silb
            if m.sum()<40:continue
            layers.append([COL[k],trace(m,ax,ay,S)])
        silp=trace(silb,ax,ay,S)
        # face features from dark mask
        lab2,n2=nd.label(dark);hl=lab2[top+2,int(tx)]
        hr=np.where(lab2[RC]==hl)[0];hr=hr[np.abs(hr-tx)<0.22*(bot-top)]
        r=(hr[-1]-hr[0])/2;cx=(hr[-1]+hr[0])/2;cy=top+r
        feats=[]
        for i,sl in enumerate(nd.find_objects(lab2)):
            if i+1==hl or sl is None:continue
            fy=(sl[0].start+sl[0].stop)/2;fx=(sl[1].start+sl[1].stop)/2
            if (fx-cx)**2+(fy-cy)**2<(r-8*fz)**2:feats.append([sl[1].start,sl[0].start,sl[1].stop,sl[0].stop])
        cyc=lambda b:(b[1]+b[3])/2
        ec=[b for b in feats if cy-28*fz<cyc(b)<cy+22*fz and b[3]-b[1]>=18*fz and b[3]-b[1]<60*fz and b[2]-b[0]<40*fz]
        ec.sort(key=lambda b:-(b[2]-b[0])*(b[3]-b[1]));eyes=sorted(ec[:2],key=lambda b:b[0])
        mo=[b for b in feats if cyc(b)>cy+24*fz and b not in eyes and b[2]-b[0]<70*fz and b[3]-b[1]<40*fz]
        mouth=[min(b[0] for b in mo),min(b[1] for b in mo),max(b[2] for b in mo),max(b[3] for b in mo)] if mo else None
        rel=lambda b:[round(float(b[0]-ax)*S,1),round(float(b[1]-ay)*S,1),round(float(b[2]-ax)*S,1),round(float(b[3]-ay)*S,1)]
        out.append(dict(n=nm,h=476,head=[round(float(cx-ax)*S,1),round(float(cy-ay)*S,1),round(float(r)*S,1)],eyes=[rel(b) for b in eyes] if len(eyes)==2 else [],mouth=rel(mouth) if mouth else None,sil=silp,layers=layers))
        print([(l[0],len(l[1])) for l in layers]);print(nm,len(layers),sum(len(l[1]) for l in layers),out[-1]['head'],len(out[-1]['eyes']),out[-1]['mouth'])
    return out
W=run('refW.png',[(13, 126, 446, 295), (13, 460, 446, 682), (13, 844, 448, 1023), (13, 1245, 447, 1475), (514, 125, 951, 303), (516, 460, 950, 768), (516, 854, 952, 1082), (514, 1244, 952, 1479)],
 ['relaxed','startled','worried','confused','thinking','ackpress','understood','relieved'])
E2=run('refE.png',[(13, 117, 447, 392), (13, 471, 447, 702), (13, 845, 447, 1033), (9, 1240, 447, 1430), (512, 40, 953, 310), (512, 420, 954, 683), (512, 839, 954, 1038), (512, 1230, 954, 1428)],
 ['talking','explaining','listening','thinking','asking','talking2','listening2','understood2'])
WORK=W+E2[4:];ENG=E2[:4]
open('people_sprites.js','w').write('const WORKER_SPR='+json.dumps(WORK,separators=(',',':'))+';\nconst ENG_SPR='+json.dumps(ENG,separators=(',',':'))+';\n')
