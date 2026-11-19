/* ================= G3: real 3D shots inside Inkstroke (v17) =================
   ngd kind 'g3', e.shot = lift | switches | fx3u | mixie. Uses vendor/three.iife.js (window.THREE).
   One shared WebGL renderer draws the shot for the element's scene time, then it is drawn onto the 2D canvas,
   so 3D, 2.5D graphics and the stickman share one timeline and camera. Times are scene-local seconds. */
const G3={r:null,shots:{},w:0,h:0};
function g3R(w,h){const T=window.THREE;if(!T)return null;
  if(!G3.r){const r=new T.WebGLRenderer({antialias:true,alpha:false,preserveDrawingBuffer:true});r.shadowMap.enabled=true;r.shadowMap.type=T.PCFSoftShadowMap;r.toneMapping=T.ACESFilmicToneMapping;r.outputColorSpace=T.SRGBColorSpace;G3.r=r}
  if(G3.w!==w||G3.h!==h){G3.r.setSize(w,h,false);G3.w=w;G3.h=h}return G3.r}
const g3ease=k=>k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2,g3c=v=>Math.max(0,Math.min(1,v)),g3in=(w,t)=>(w||[]).some(([a,b])=>t>=a&&t<b),g3val=(tl,t,d)=>{let v=d;(tl||[]).forEach(([a,x])=>{if(t>=a)v=x});return v};
function g3Base(bg='#eef2f6'){const T=THREE,S=new T.Scene();S.background=new T.Color(bg);
  const hemi=new T.HemisphereLight('#ffffff','#b8c4d2',1.1);S.add(hemi);
  const key=new T.DirectionalLight('#ffffff',2.0);key.position.set(4,7,8);key.castShadow=true;key.shadow.mapSize.set(1024,1024);key.shadow.radius=5;['left','bottom'].forEach(k=>key.shadow.camera[k]=-10);['right','top'].forEach(k=>key.shadow.camera[k]=10);S.add(key);
  const rim=new T.DirectionalLight('#dbe8ff',.6);rim.position.set(-5,3,-4);S.add(rim);
  const cam=new T.PerspectiveCamera(32,16/9,.1,100);
  const M=(c,o={})=>new T.MeshStandardMaterial({color:c,roughness:o.r??.6,metalness:o.m??0,emissive:o.e||'#000',emissiveIntensity:o.ei??0,transparent:o.op!=null,opacity:o.op??1});
  const box=(w,h,d,m,x,y,z,p=S)=>{const k=new T.Mesh(new T.BoxGeometry(w,h,d),m);k.position.set(x,y,z);k.castShadow=k.receiveShadow=true;p.add(k);return k};
  const cyl=(r1,r2,h,m,x,y,z,p=S,seg=32)=>{const k=new T.Mesh(new T.CylinderGeometry(r1,r2,h,seg),m);k.position.set(x,y,z);k.castShadow=k.receiveShadow=true;p.add(k);return k};
  const tex=(draw,w=512,h=128)=>{const c=document.createElement('canvas');c.width=w;c.height=h;const t=new T.CanvasTexture(c);t.colorSpace=T.SRGBColorSpace;t._c=c;t._draw=draw;draw(c.getContext('2d'),w,h);return t};
  const label=(txt,w,h,x,y,z,p=S,o={})=>{const t=tex((c,W_,H_)=>{c.clearRect(0,0,W_,H_);c.font=`800 ${o.size||64}px "IBM Plex Sans",Arial`;c.fillStyle=o.color||'#2b2f36';c.textAlign='center';c.textBaseline='middle';c.fillText(txt,W_/2,H_/2)});const m=new T.Mesh(new T.PlaneGeometry(w,h),new T.MeshBasicMaterial({map:t,transparent:true}));m.position.set(x,y,z);p.add(m);return m};
  return{T,S,cam,key,hemi,rim,M,box,cyl,tex,label};
}
/* ---- shot: lift call panel + doors ---- */
function g3Lift(){const B=g3Base('#e9edf2'),{T,S,cam,M,box,cyl,tex,label}=B;
  box(14,8,.2,M('#e7e1d6',{r:.85}),0,2,-1);box(14,.1,6,M('#d5d9df',{r:.8}),0,-1.95,1.6);
  box(3.2,4.6,.25,M('#9aa3af',{m:.7,r:.3}),0,.4,-.8);                           // frame
  const dl=box(1.42,4.2,.12,M('#c7ccd2',{m:.85,r:.22}),-.72,.3,-.62),dr=box(1.42,4.2,.12,M('#c7ccd2',{m:.85,r:.22}),.72,.3,-.62);
  const disp=tex((c,W_,H_)=>{c.fillStyle='#0b0e12';c.fillRect(0,0,W_,H_)},256,128),dm=new T.Mesh(new T.PlaneGeometry(.9,.45),new T.MeshBasicMaterial({map:disp}));dm.position.set(0,3.05,-.66);S.add(dm);
  const plate=box(.7,1.3,.08,M('#b9c2cc',{m:.8,r:.25}),2.3,.6,-.82);
  const ring=new T.Mesh(new T.TorusGeometry(.2,.04,16,48),M('#9aa3af',{m:.8,r:.3}));ring.position.set(2.3,.75,-.74);S.add(ring);
  const btnM=M('#d9dde3',{r:.35,e:'#ff8a1f',ei:0}),btn=cyl(.17,.17,.08,btnM,2.3,.75,-.74,S,40);btn.rotation.x=Math.PI/2;
  label('▲',.3,.3,2.3,.75,-.69,S,{size:90,color:'#5d6b7a'});
  const glow=new T.PointLight('#ff9a30',0,2.2);glow.position.set(2.3,.75,-.3);S.add(glow);
  let lastFloor=null;
  return{B,update(tl,e){const on=tl>=e.press&&tl<e.arrive,pr=tl>=e.press&&tl<e.press+.35;
    btnM.emissiveIntensity=on?2.6:0;btnM.color.set(on?'#fff1db':'#d9dde3');glow.intensity=on?3:0;btn.position.z=-.74-(pr?.04:0);
    const k=g3ease(g3c((tl-e.arrive)/1.3));dl.position.x=-.72-k*1.3;dr.position.x=.72+k*1.3;
    const f=tl<e.press?5:tl>=e.arrive?1:Math.max(1,5-Math.floor((tl-e.press)/((e.arrive-e.press)/4)));
    if(f!==lastFloor){lastFloor=f;const c=disp._c.getContext('2d');c.fillStyle='#0b0e12';c.fillRect(0,0,256,128);c.font='800 96px Arial';c.fillStyle='#ff5a3c';c.textAlign='center';c.textBaseline='middle';c.fillText((tl<e.arrive&&tl>=e.press?'▼ ':'')+f,128,68);disp.needsUpdate=true}
    const z=e.zoom?g3ease(g3c((tl-e.zoom[0])/(e.zoom[1]-e.zoom[0]))):0;
    cam.position.set(1.2+z*1.0,1.1,8.2-z*4.6-tl*.02);cam.lookAt(.9+z*1.3,.9-z*.1,-.8)}}
}
/* ---- shot: doorbell (momentary) vs fan switch (maintained) ---- */
function g3Switches(){const B=g3Base('#eef2f6'),{T,S,cam,M,box,cyl,label}=B;
  box(14,8,.2,M('#efe9df',{r:.9}),0,2,-1.2);
  [-2.2,2.2].forEach(x=>box(1.1,1.5,.1,M('#f7f7f5',{r:.4}),x,.4,-1.05));
  const bellBtnM=M('#f2f2f0',{r:.3}),bellBtn=cyl(.22,.22,.12,bellBtnM,-2.2,.4,-.97,S,40);bellBtn.rotation.x=Math.PI/2;
  const rock=box(.38,.62,.1,M('#f2f2f0',{r:.3}),2.2,.4,-.95);
  // bell
  const bell=new T.Group();const bm=M('#e3b341',{m:.8,r:.25});const bc=new T.Mesh(new T.ConeGeometry(.55,.7,32,1,true),bm);bc.rotation.x=Math.PI;bc.material.side=T.DoubleSide;bell.add(bc);const bk=new T.Mesh(new T.SphereGeometry(.1,16,16),bm);bk.position.y=-.35;bell.add(bk);bell.position.set(-2.2,2.6,-.6);S.add(bell);
  const waves=[0,1,2].map(i=>{const m=new T.Mesh(new T.TorusGeometry(.7+i*.25,.02,8,48,Math.PI*.6),new T.MeshBasicMaterial({color:'#e3b341',transparent:true,opacity:0}));m.position.set(-2.2,2.55,-.6);m.rotation.z=Math.PI*.2;S.add(m);return m});
  // ceiling fan
  const fan=new T.Group();const hub=new T.Mesh(new T.CylinderGeometry(.2,.25,.25,24),M('#8e98a3',{m:.6,r:.35}));fan.add(hub);
  for(let i=0;i<3;i++){const bl=new T.Mesh(new T.BoxGeometry(1.4,.04,.32),M('#a9805a',{r:.6}));bl.position.x=.8;const g=new T.Group();g.add(bl);g.rotation.y=i*Math.PI*2/3;fan.add(g)}
  fan.position.set(2.2,3.0,-.2);fan.rotation.x=.35;S.add(fan);const rod=cyl(.04,.04,.9,M('#8e98a3',{m:.6}),2.2,3.5,-.35);
  label('DOORBELL',1.6,.4,-2.2,-.65,-1.04,S,{size:62,color:'#2b2f36'});label('FAN SWITCH',1.8,.4,2.2,-.65,-1.04,S,{size:62,color:'#2b2f36'});
  let fanA=0,lastT=0;
  return{B,update(tl,e){const ring=g3in(e.bell,tl);bellBtn.position.z=ring?-1.0:-.97;bellBtnM.color.set(ring?'#ffe08a':'#f2f2f0');
    bell.rotation.z=ring?Math.sin(tl*40)*.18:0;waves.forEach((w,i)=>{w.material.opacity=ring?(.6-.18*i)*(.5+.5*Math.sin(tl*12-i)):0});
    const fon=g3in(e.fan,tl);rock.rotation.x=fon?-.28:.28;const dt=Math.max(0,Math.min(.1,tl-lastT));lastT=tl;fanA+=dt*(fon?14:0);fan.rotation.y=fanA;
    const fz=e.focus?g3val(e.focus,tl,0):0;cam.position.set(fz*1.6,1.6,8.4-Math.abs(fz)*1.6);cam.lookAt(fz*1.9,1.4,-.8)}}
}
/* ---- shot: FX3U-32MR/ES (model text only, no brand) with LED timelines, BATT zoom and X-ray "DECODE MOMENT" ---- */
function g3Fx3u(){const B=g3Base('#e9eef4'),{T,S,cam,M,box,cyl,label}=B;
  box(14,7,.1,M('#dfe5ec',{r:.85}),0,0,-.9);box(12,.35,.08,M('#b9c2cc',{m:.7,r:.3}),0,0,-.8);
  const P=new T.Group();S.add(P);const BW=3.64,BH=1.8,BD=1.5,mats=[];const mm=(c,o)=>{const m=M(c,o);mats.push(m);return m};
  const body=box(BW,BH,BD,mm('#d9dbd5',{r:.55}),0,0,0,P);box(BW-.1,.62,.08,mm('#e6e8e2',{r:.5}),0,0,BD/2+.02,P);
  box(BW-.08,.5,.12,mm('#c9cbc4',{r:.5}),0,.6,BD/2+.02,P);box(BW-.08,.5,.12,mm('#c9cbc4',{r:.5}),0,-.6,BD/2+.02,P);
  const sm=mm('#c7ccd2',{m:.85,r:.25});const scr=(y0,row)=>{for(let i=0;i<12;i++){const s=cyl(.036,.036,.03,sm,-1.62+i*.27+(row?.135:0),y0,BD/2+.1,P,20);s.rotation.x=Math.PI/2}};scr(.68,0);scr(.55,1);scr(-.55,0);scr(-.68,1);
  const L=(t,w,h,x,y,s=40)=>label(t,w*1.5,h*1.5,x,y,BD/2+.11,P,{size:s});
  [['S/S',-1.08,.8],['0V',-.81,.8],['X0',-.54,.8],['24V',-.675,.43],['X1',-.405,.43]].forEach(([t,x,y])=>L(t,.32,.08,x,y));L('Y0',.36,.08,-1.35,-.43);L('COM1',.36,.08,-1.485,-.8);
  const leds={};const lm=c=>new T.MeshStandardMaterial({color:'#2f343b',emissive:c,emissiveIntensity:0,roughness:.3});
  [['POWER','#22ff77'],['RUN','#22ff77'],['BATT','#ff3b3b'],['ERROR','#ff3b3b']].forEach(([n,c],i)=>{const l=box(.07,.05,.03,lm(c),-1.55,.2-i*.13,BD/2+.07,P);leds[n]=l;L(n,.24,.06,-1.36,.2-i*.13,38)});
  const ids=['0','1','2','3','4','5','6','7','10','11','12','13','14','15','16','17'];
  const grid=(p,y)=>ids.forEach((id,i)=>{leds[p+id]=box(.05,.04,.03,lm('#22ff77'),-.5+(i%8)*.13,y-Math.floor(i/8)*.1,BD/2+.07,P)});
  L('IN',.12,.05,-.68,.17,38);grid('X',.17);L('OUT',.14,.05,-.68,-.09,38);grid('Y',-.09);
  label('FX3U-32MR/ES',1.12,.18,1.05,-.12,BD/2+.11,P,{size:60});
  box(.3,.5,.04,mm('#cfd1ca',{r:.5}),-.95,0,BD/2+.06,P);box(.07,.12,.05,M('#2b2f36',{r:.4}),-.95,.05,BD/2+.1,P);L('RUN',.16,.05,-.95,.2,30);L('STOP',.18,.05,-.95,-.13,30);
  box(.05,1.2,1.0,mm('#cfd1ca',{r:.5}),BW/2+.02,0,0,P);
  // inside (visible in X-ray): CPU board, memory chip, battery
  const inner=new T.Group();P.add(inner);inner.visible=false;
  box(3.2,1.4,.06,M('#1e7a4a',{r:.6}),0,0,-.2,inner);const cpu=box(.7,.5,.12,M('#20242a',{r:.4,e:'#38bdf8',ei:0}),.5,.15,-.1,inner);
  const mem=box(.9,.3,.12,M('#20242a',{r:.4,e:'#a78bfa',ei:0}),.5,-.4,-.1,inner);const bat=cyl(.18,.18,.5,M('#3b82f6',{m:.4,r:.4,e:'#3b82f6',ei:0}),-1.2,-.2,.1,inner);bat.rotation.z=Math.PI/2;
  label('CPU',.5,.14,.5,.15,-.03,inner,{size:56,color:'#e0f2fe'});label('LATCHED MEMORY',.9,.14,.5,-.4,-.03,inner,{size:44,color:'#ede9fe'});label('BATTERY',.7,.16,-1.2,.12,.32,inner,{size:52,color:'#1e3a8a'});
  const scan=new T.Mesh(new T.PlaneGeometry(BW+.4,.04),new T.MeshBasicMaterial({color:'#38e8ff',transparent:true,opacity:.9}));scan.position.z=BD/2+.2;P.add(scan);scan.visible=false;
  const scanGlow=new T.Mesh(new T.PlaneGeometry(BW+.4,.35),new T.MeshBasicMaterial({color:'#38e8ff',transparent:true,opacity:.18}));P.add(scanGlow);scanGlow.position.z=BD/2+.19;scanGlow.visible=false;
  const CAM={front:[0,.25,6.6,0,0,0],wide:[2.4,1.3,7.4,0,0,0],batt:[-1.6,.2,2.6,-1.3,.0,0],leds:[-.6,.25,3.2,-.4,.05,0],model:[1.6,.2,3.4,1.0,-.1,0]};
  let cprev=null;
  return{B,update(tl,e){const st=e.leds||{};Object.entries(leds).forEach(([k,l])=>{const on=!!g3val(st[k],tl,k==='POWER'||k==='RUN'?1:0);l.material.emissiveIntensity=on?3.2:0;l.material.color.set(on?'#0d3b1f':'#2f343b')});
    const dim=g3val(e.dim,tl,0);B.hemi.intensity=1.1*(1-dim*.85);B.key.intensity=2*(1-dim*.9);B.S.background.set(dim?'#1a1f27':'#e9eef4');
    const xr=e.xray&&tl>=e.xray[0]&&tl<e.xray[1],xk=xr?g3c((tl-e.xray[0])/.6)*g3c((e.xray[1]-tl)/.5):0;
    mats.forEach(m=>{m.transparent=true;m.opacity=1-xk*.82;m.depthWrite=xk<.5});inner.visible=xk>.05;
    [cpu,mem,bat].forEach(o=>o.material.emissiveIntensity=xk*1.2);scan.visible=scanGlow.visible=xk>.05;const sy=.9-(((tl-(e.xray?e.xray[0]:0))*.9)%1)*1.8;scan.position.y=sy;scanGlow.position.y=sy+.17;
    const K=g3val(e.cam,tl,'front'),cur=CAM[K];if(!cprev||cprev.k!==K)cprev={k:K,t:tl,from:cprev?cprev.now:cur};
    const f=g3ease(g3c((tl-cprev.t)/.9)),now=cprev.from.map((v,i)=>v+(cur[i]-v)*f);cprev.now=now;
    cam.position.set(now[0]+Math.sin(tl*.25)*.08,now[1],now[2]);cam.lookAt(now[3],now[4],now[5])}}
}
/* ---- shot: mixie (mixer grinder) + room lamp, power cut and restart ---- */
function g3Mixie(){const B=g3Base('#f1ece4'),{T,S,cam,M,box,cyl,label}=B;
  box(14,.3,6,M('#cfc6b8',{r:.8}),0,-1.05,0);box(14,8,.2,M('#ece4d6',{r:.9}),0,2.5,-2.6);
  const base=box(1.6,1.0,1.3,M('#f3f4f6',{r:.35}),0,-.4,0);const knob=cyl(.16,.16,.1,M('#e5484d',{r:.4}),0,-.35,.68,S,32);knob.rotation.x=Math.PI/2;
  const jar=cyl(.55,.45,1.4,M('#dbeafe',{r:.05,op:.35}),0,.8,0,S,40);const lid=cyl(.58,.58,.15,M('#1f2937',{r:.5}),0,1.55,0,S,40);
  const blades=new T.Group();for(let i=0;i<2;i++){const b=new T.Mesh(new T.BoxGeometry(.7,.03,.1),M('#cbd5e1',{m:.9,r:.2}));b.rotation.y=i*Math.PI/2;blades.add(b)}blades.position.set(0,.25,0);S.add(blades);
  const fill=cyl(.48,.42,.55,M('#f59e0b',{r:.7,op:.85}),0,.45,0,S,32);
  const lamp=new T.PointLight('#fff4d6',0,10);lamp.position.set(-2.5,3.5,2);S.add(lamp);const bulb=new T.Mesh(new T.SphereGeometry(.2,16,16),new T.MeshBasicMaterial({color:'#fff4d6'}));bulb.position.copy(lamp.position);S.add(bulb);
  let ang=0,lastT=0;
  return{B,update(tl,e){const dark=g3in(e.cut,tl);const run=g3in(e.run,tl)&&!dark;
    B.hemi.intensity=dark?.12:1.1;B.key.intensity=dark?.08:2;lamp.intensity=dark?0:8;bulb.material.color.set(dark?'#3a3a3a':'#fff4d6');B.S.background.set(dark?'#15181d':'#f1ece4');
    const dt=Math.max(0,Math.min(.1,tl-lastT));lastT=tl;ang+=dt*(run?40:0);blades.rotation.y=ang;fill.rotation.y=ang*.3;
    const sh=run?Math.sin(tl*60)*.012:0;jar.position.x=sh;lid.position.x=sh;fill.position.x=sh;knob.rotation.z=g3in(e.knobOn,tl)?-.9:0;
    cam.position.set(2.6-tl*.01,1.5,5.2);cam.lookAt(0,.3,0)}}
}
const G3_BUILD={lift:g3Lift,switches:g3Switches,fx3u:g3Fx3u,mixie:g3Mixie};
function drawG3(e,c,tl){if(!window.THREE){ngTxt(c,'3D: '+e.shot,e.x+e.w/2,e.y+e.h/2,28,NG.navy,800);return}
  const sc=typeof curScale==='number'?curScale:1,w=Math.max(64,Math.round(e.w*sc)),h=Math.max(36,Math.round(e.h*sc)),r=g3R(w,h);
  const key=e.shot+'#'+e.id,s=G3.shots[key]||(G3.shots[key]=G3_BUILD[e.shot]());s.B.cam.aspect=w/h;s.B.cam.updateProjectionMatrix();s.update(tl,e);r.render(s.B.S,s.B.cam);
  c.save();if(e.rr){ngRR(c,e.x,e.y,e.w,e.h,e.rr);c.clip()}c.drawImage(r.domElement,e.x,e.y,e.w,e.h);c.restore();
  if(e.frame){c.lineWidth=4;c.strokeStyle=e.frame;ngRR(c,e.x,e.y,e.w,e.h,e.rr||0);c.stroke()}}
/* 3-second guess ring: shows 3,2,1 across [t0,t1], then a check flash */
function drawCount3(e,c,tl){const t0=e.t0,t1=e.t1,cx=e.x+e.w/2,cy=e.y+e.h/2,r=e.w/2,f=g3c((tl-t0)/(t1-t0)),n=Math.max(1,3-Math.floor(f*3));
  c.save();c.beginPath();c.arc(cx,cy,r,0,7);c.fillStyle='rgba(255,255,255,.94)';c.fill();c.lineWidth=10;c.strokeStyle='#e5e7eb';c.stroke();
  c.beginPath();c.arc(cx,cy,r,-Math.PI/2,-Math.PI/2+Math.PI*2*(1-f));c.strokeStyle=f<1?NG.org:NG.grn;c.lineWidth=10;c.lineCap='round';c.stroke();
  ngTxt(c,f<1?String(n):'✓',cx,cy+2,r*1.05,f<1?NG.navy:NG.grn,800);ngTxt(c,e.label||'GUESS!',cx,cy+r+26,22,NG.org,800);c.restore()}
