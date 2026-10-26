import sys,json,numpy as np,potrace
from PIL import Image
from scipy import ndimage as nd
from sklearn.cluster import KMeans
K=3;D='/mnt/user-data/uploads/electricity/_ngd_in/'
def trace(mask,ox,oy,S,turd=30):
    try:pl=potrace.Bitmap(~mask).trace(turdsize=turd,alphamax=1.0,opticurve=True,opttolerance=0.5)
    except ValueError:pl=potrace.Bitmap(~mask).trace(turdsize=turd,alphamax=1.0,opticurve=False)
    q=(lambda v:f"{v:.0f}") if S==1.0 else (lambda v:f"{v:.1f}")
    f=lambda p:q((p.x/K-ox)*S)+" "+q((p.y/K-oy)*S)
    o=[]
    for c in pl:
        o.append("M"+f(c.start_point))
        for s in c.segments:o.append(("L"+f(s.c)+"L"+f(s.end_point)) if s.is_corner else ("C"+f(s.c1)+" "+f(s.c2)+" "+f(s.end_point)))
        o.append("Z")
    return "".join(o)
def cells(img,cols,rows):
    a=np.array(img);H,W=a.shape[:2];nw=a.min(2)<232
    lb,n=nd.label(nd.binary_dilation(nw,iterations=2));sls=nd.find_objects(lb)
    comps=[]
    for i,sl in enumerate(sls):
        if sl is None:continue
        h=sl[0].stop-sl[0].start;w=sl[1].stop-sl[1].start;area=(lb[sl]==i+1).sum()
        comps.append(dict(i=i+1,sl=sl,h=h,w=w,area=area,cy=(sl[0].start+sl[0].stop)/2,cx=(sl[1].start+sl[1].stop)/2))
    # label text: short wide-ish rows of glyphs -> detect by height small; group glyph comps per line later
    out=[[None]*cols for _ in range(rows)]
    for c in comps:
        col=min(cols-1,int(c['cx']/W*cols));row=min(rows-1,int(c['cy']/H*rows))
        out[row][col]=(out[row][col] or [])+[c]
    return a,lb,out
def classify_label(cs,cellH):
    # label = comps in the lowest band whose height < 0.12*cellH; find the label band as the lowest cluster of small comps
    small=[c for c in cs if c['h']<0.11*cellH]
    if not small:return cs,[]
    big=[c for c in cs if c['h']>=0.11*cellH]
    bigbot=max([c['sl'][0].stop for c in big],default=0)
    band=[c for c in small if c['sl'][0].start>bigbot-2]
    keep=[c for c in cs if c not in band]
    return keep,band
def palette_layers(cr,sil,ink,k):
    a=cr.astype(int);mx=a.max(2);mn=a.min(2)
    near=nd.binary_dilation(ink,iterations=4)
    cand=sil&~ink&~near&(mn<238)
    px=a[cand]
    if len(px)<50:return []
    k=min(k,max(1,len(px)//400))
    km=KMeans(n_clusters=k,n_init=3,random_state=0).fit(px[::max(1,len(px)//20000)].astype(float))
    lab=np.full(a.shape[:2],-1);
    allc=sil&~ink&(mn<238)
    lab[allc]=km.predict(a[allc].astype(float))
    cen=km.cluster_centers_
    order=np.argsort(-(cen@np.array([.3,.59,.11])))
    L=[]
    for j in order:
        m=(lab==j)&~near
        chroma=cen[j].max()-cen[j].min()
        m=nd.binary_opening(m,iterations=1 if chroma>40 else 2)
        m=nd.binary_dilation(m,iterations=4)&sil
        if m.sum()<120:continue
        col='#%02x%02x%02x'%tuple(int(v) for v in np.clip(cen[j],0,255))
        L.append((col,m))
    return L
def faces(dark,top,tx,hmaxpx,fz):
    lab2,n2=nd.label(dark);colv=lab2[top:top+8,max(0,int(round(tx))-2):int(round(tx))+3].ravel();colv=colv[colv>0];hl=int(np.bincount(colv).argmax()) if len(colv) else 0
    RC=top+int(62*fz)
    hr=np.where(lab2[RC]==hl)[0];hr=hr[np.abs(hr-tx)<0.22*hmaxpx]
    if len(hr)<2:return None,[],None
    r=(hr[-1]-hr[0])/2;cx=(hr[-1]+hr[0])/2;cy=top+r
    feats=[]
    for i,sl in enumerate(nd.find_objects(lab2)):
        if i+1==hl or sl is None:continue
        fy=(sl[0].start+sl[0].stop)/2;fx=(sl[1].start+sl[1].stop)/2
        if (fx-cx)**2+(fy-cy)**2<(r-8*fz)**2:feats.append([sl[1].start,sl[0].start,sl[1].stop,sl[0].stop])
    cyc=lambda b:(b[1]+b[3])/2
    ec=[b for b in feats if cy-30*fz<cyc(b)<cy+30*fz and b[3]-b[1]>=16*fz and b[3]-b[1]<60*fz and b[2]-b[0]<40*fz]
    ec.sort(key=lambda b:-(b[2]-b[0])*(b[3]-b[1]));eyes=sorted(ec[:2],key=lambda b:b[0])
    eb=max([b[3] for b in eyes],default=cy)
    mo=[b for b in feats if cyc(b)>eb and b not in eyes and b[2]-b[0]<75*fz and b[3]-b[1]<45*fz]
    mo=[b for b in mo if b[2]-b[0]>=10*fz] or mo
    exc=np.mean([(b[0]+b[2])/2 for b in eyes]) if eyes else cx
    mouth=min(mo,key=lambda b:((b[0]+b[2])/2-exc)**2+(cyc(b)-eb-20*fz)**2) if mo else None
    return (cx,cy,r),eyes,mouth
def run(fname,cols,rows,names,kind,kcol=8):
    img=Image.open(D+fname).convert('RGB');a,lb,grid=cells(img,cols,rows);H,W=a.shape[:2];cellH=H/rows
    items=[]
    for r in range(rows):
        for c in range(cols):
            cs=grid[r][c] or []
            if kind!='brand':
                cx0,cx1=int(c*W/cols),int((c+1)*W/cols);cy0,cy1=int(r*H/rows),int((r+1)*H/rows)
                prof=(a[cy0:cy1,cx0:cx1].min(2)<232).any(1);ys_=np.where(prof)[0];cut=None
                if len(ys_):
                    e=ys_[-1];s0=e
                    while s0>0 and prof[s0-1]:s0-=1
                    if e-s0<0.11*cellH and not prof[max(0,s0-3):s0].any():cut=cy0+s0-2
                keep=[x for x in cs if cut is None or x['sl'][0].start<cut]
                keep,_=classify_label(keep,cellH)
                if cut is not None:
                    for x in keep:x['cut']=cut
            else:keep=cs
            keep=[x for x in keep if x['area']>30]
            if not keep:items.append(None);continue
            x0=min(x['sl'][1].start for x in keep);x1=max(x['sl'][1].stop for x in keep);y0=min(x['sl'][0].start for x in keep);y1=max(x['sl'][0].stop for x in keep)
            P=6;bx=(max(0,x0-P),max(0,y0-P),min(W,x1+P),min(H,y1+P))
            m=np.zeros(lb.shape,bool)
            for x in keep:m|=lb==x['i']
            if keep and 'cut' in keep[0]:m[keep[0]['cut']:,:]=False;bx=(bx[0],bx[1],bx[2],min(bx[3],keep[0]['cut']))
            items.append((bx,m))
    # sizes
    hs=[it[0][3]-it[0][1] for it in items if it]
    hmax=float(np.median(hs)) if kind=='char' else max(hs);out=[]
    for nm,it in zip(names,items):
        if it is None or nm is None:continue
        (bx0,by0,bx1,by1),m=it
        cr=img.crop((bx0,by0,bx1,by1));ca=np.array(cr);w,h=cr.size
        mm=m[by0:by1,bx0:bx1]
        ca[~nd.binary_dilation(mm,iterations=2)]=255
        nonw=ca.min(2)<232;dark=ca.max(2)<70
        lab,n=nd.label(~nonw);bl=np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]]));bl=bl[bl>0]
        sil=nd.binary_closing(~np.isin(lab,bl),iterations=1)
        ys=np.where(nonw.any(1))[0];top,bot=ys[0],ys[-1]
        if kind=='char':
            fz=hmax/476;S=1/fz;tx=None
            yh=int(bot-0.97*hmax)
            if 0<=yh<h:
                xs=np.where(dark[yh])[0]
                if len(xs):
                    cl=np.split(xs,np.where(np.diff(xs)>8)[0]+1);bc=w/2
                    g=min(cl,key=lambda q:abs((q[0]+q[-1])/2-bc));tx=(g[0]+g[-1])/2
                    if g[-1]-g[0]>0.3*hmax:tx=None
            if tx is None:tx=np.where(dark[top+2])[0].mean() if dark[top+2].any() else w/2
            near=np.abs(np.arange(w)-tx)<0.1*hmax
            top=int(np.where((dark&near[None,:]).any(1))[0][0])
            ax,ay=tx,bot;hh=476
        else:
            S=1.0;ax=w/2;ay=bot;hh=float(bot-top)
        big=np.array(Image.fromarray(ca).resize((w*K,h*K),Image.LANCZOS))
        silb=np.array(Image.fromarray((sil*255).astype(np.uint8)).resize((w*K,h*K),Image.LANCZOS))>127
        inkb=(big.max(2)<70)&silb
        layers=[(c,trace(mk,ax,ay,S)) for c,mk in palette_layers(big,silb,inkb,kcol)]
        layers.append(('@ink',trace(inkb,ax,ay,S,turd=12)))
        d=dict(n=nm,h=hh,dir=1,sil=trace(silb,ax,ay,S),layers=[list(l) for l in layers],eyes=[],mouth=None,w=round(w*S,1))
        if kind=='char':
            hd,eyes,mo=faces(dark,top,tx,hmax,fz)
            rel=lambda b:[round(float(b[0]-ax)*S,1),round(float(b[1]-ay)*S,1),round(float(b[2]-ax)*S,1),round(float(b[3]-ay)*S,1)]
            d['eyes']=[rel(b) for b in eyes] if len(eyes)==2 else [];d['mouth']=rel(mo) if mo else None
        else:d['prop']=1
        out.append(d);print(fname,nm,len(layers),sum(len(l[1]) for l in layers),len(d['eyes']),d['mouth'] is not None,flush=True)
    return out
SHEETS={
 'host1':('ngd-host-1.png',4,2,['talking','pointright','pointup','counting','palmsup','thumbsup','thinking','surprised'],'char'),
 'host2':('ngd-host-2.png',4,2,['listening','explaining','waving','crossarms','tablet','writing','pressing','walking'],'char'),
 'tools':('ngd-tech-tools.png',4,2,['multimeter','screwdriver','spanner','clipboard','phonecall','laptop','kneelmotor','celebrate'],'char'),
 'panel':('ngd-panel-parts.png',4,3,['plc_rack','hmi','vfd','contactor','mcb','overload_relay','relay','terminal_block','psu_24v','estop','pushbuttons','cabinet_open'],'prop'),
 'field':('ngd-field-devices.png',4,3,['prox_sensor','photo_eye','limit_switch','pressure_tx','temp_sensor','flow_meter','encoder','solenoid_valve','pneumatic_cyl','motor_3ph','gearbox','pump'],'prop'),
 'mach':('ngd-machines.png',4,2,['conveyor','packing_machine','filling_machine','mixing_tank','compressor','boiler','robot_arm','pallet_wrapper'],'prop'),
 'iot':('ngd-iot.png',4,3,['iot_gateway','wifi_router','cloud','server_rack','laptop_dash','tablet_dash','phone_alarm','net_switch','eth_cable','antenna','data_packet','padlock'],'prop'),
 'bg':('ngd-backgrounds.png',2,2,['bg_factory','bg_control','bg_workshop','bg_electrical'],'prop'),
 'brand':('ngd-brand.png',3,1,['face_smile','face_surprised','face_point'],'brand'),
}
key=sys.argv[1];f,c,r,n,kd=SHEETS[key]
res=run(f,c,r,n,'prop' if kd=='brand' else kd,kcol=6 if kd=='char' else 9)
json.dump(res,open(f'out_{key}.json','w'),separators=(',',':'))
