/* ---------- FDT – NPN vs PNP: "Sensor LED ON, PLC X0 OFF" (Factory Decode Tamil, owner narration) ----------
   Motion-graphics explainer: rails, glowing wires, current dots along the real path, switches that flip, voltage tags.
   Timing = pause-based alignment of the owner's Tanglish recording (FDT_NPN_A: [start, end, paragraph] per sentence).
   Load the long narration (5:20) for 'fdtnpn', the Shorts narration (0:46) for 'fdtnpns'. */
const FDT_NPN_A=__LONG_A__;
const FDT_NPN_SA=__SHORT_A__;
function fdtKit(s,A){
  const ng=(kind,o,win)=>{const e={id:uid++,type:'ngd',kind,name:o.name||kind,draw:.1,delay:0,withPrev:true,entrance:'draw',motion:'none',x:0,y:0,w:10,h:10,...o,win};s.els.push(e);return e};
  const P=p=>A.filter(a=>a[2]===p),T=(p,k=0)=>{const q=P(p);return q.length?q[Math.min(k,q.length-1)][0]:0};
  const PS=p=>Math.max(0,T(p)-.25);
  const seg=(x1,y1,x2,y2,win,o={})=>ng('arrow',{x1,y1,x2,y2,x:Math.min(x1,x2),y:Math.min(y1,y2),w:Math.abs(x2-x1)+1,h:Math.abs(y2-y1)+1,noPop:true,noHead:!o.head,lw:o.lw||6,dur:o.dur??.3,...o},win);
  /* wire through points; o.flow = time current starts (dots follow point order), o.glow adds a glow under it */
  const wire=(pts,col,win,o={})=>{for(let i=0;i+1<pts.length;i++){const[a,b]=[pts[i],pts[i+1]],L=Math.hypot(b[0]-a[0],b[1]-a[1])||1;
      if(o.flow!=null)seg(a[0],a[1],b[0],b[1],[Math.max(win[0],o.flow),win[1]],{color:'#ffe27a',lw:16,dur:.01});
      seg(a[0],a[1],b[0],b[1],win,{color:col,lw:o.lw||6,dur:o.dur??.25,flow:o.flow!=null,flowFrom:o.flow,flowColor:o.dot||'#22b35e',speed:110/L})}};
  const pill=(text,cx,y,win,o={})=>ng('title',{x:cx-(o.w??300)/2,y,w:o.w??300,h:o.h??52,text,size:o.size||24,bg:o.bg||NG.navy},win);
  const label=(text,cx,cy,win,o={})=>ng('label',{x:cx-(o.w??300)/2,y:cy-20,w:o.w??300,h:40,text,size:o.size||22,color:o.color||NG.navy},win);
  const lamp=(cx,cy,d,on,win,o={})=>ng('lamp',{x:cx-d/2,y:cy-d/2,w:d,h:d,on,...o},win);
  const box=(o,win)=>ng('box',o,win);
  const eq=(n,cx,y,h,win,o={})=>{const m=addStick({scene:s,quiet:true,look:'equip',action:n,size:h,x:0,y,facing:o.facing||1,entrance:'pop',delay:0,withPrev:true,draw:.35,name:n});m.x=cx-m.w/2;m.win=win;return m};
  const mg=(type,o,win)=>ng('mg',{mg:type,...o},win);
  return{ng,P,T,PS,seg,wire,pill,label,lamp,box,eq,mg};
}
async function buildFdtNpn(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('16:9');S.narrOff=0;
  const A=FDT_NPN_A,END=320.4;
  const s=newScene({name:'FDT – Sensor LED ON, PLC X0 OFF (NPN vs PNP)',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=fdtKit(s,A),{ng,T,PS,seg,wire,pill,label,lamp,box,mg}=K;
  const RED='#e5484d',BN='#8b5a2b',BU='#2f6fd6',BK='#1d1d1f',YEL='#ffd23f',AMB='#ffb020';
  const W=(p,q=p)=>[PS(p),q>=24?END:PS(q+1)];
  s.capBeats=[];
  /* ---------- host ---------- */
  const host=addStick({scene:s,quiet:true,look:'office',action:'question',size:440,x:0,y:270,facing:1,entrance:'none',delay:0,withPrev:true,draw:.1,name:'Host'});
  const HB=[[0,'question'],[6,'worriedlook'],[9.4,'swap'],[13.6,'screwdriver'],[19.4,'holdsensor'],[26,'scratchhead'],[28,'talkneutral'],[31.9,'pointboard'],[36,'count1'],[39.2,'count2'],[42.2,'pointboard'],
    [44.7,'talkneutral'],[50,'trace'],[57.3,'pointboard'],[59.6,'thumbsup'],[61.8,'trace'],[67.2,'onefinger'],[69.6,'pointboard'],[83.3,'talkneutral'],[90.5,'trace'],[97.1,'thumbsup'],
    [99.4,'question'],[112.2,'count1'],[114.2,'count2'],[116.9,'talkneutral'],[121.8,'pointboard'],[130.2,'pointboard'],[143,'trace'],[153.4,'thumbsup'],[154.3,'present'],[159.4,'pointboard'],
    [163.5,'worriedlook'],[169.3,'swap'],[175.9,'pointboard'],[183.6,'probes'],[192.1,'question'],[196.1,'scratchhead'],[200.6,'chinthink'],[205.2,'onefinger'],[208,'trace'],[220.5,'thumbsup'],
    [222.5,'talkneutral'],[237,'question'],[239.5,'holdsensor'],[241.9,'pointboard'],[245.1,'count1'],[248.4,'count2'],[251.2,'holdsensor'],[256.7,'pointboard'],[261.8,'trace'],[266.5,'thumbsup'],
    [269.6,'talkneutral'],[277.9,'swap'],[286.4,'chinthink'],[287.5,'count1'],[290.1,'count2'],[297,'count3'],[303.2,'askviewer'],[308,'probes'],[312.9,'trace'],[316.2,'wavebye']];
  host.beats=HB.map(([t,pose])=>({t,pose,blend:.22}));host.speak=[[0,END]];
  /* ---------- geometry ---------- */
  const YP=140,YN=610,X0R=400,X1R=1240,cx=560,cy=375,bx0=480,bx1=640,by0=290,by1=460,yBk=400;
  const rails=(win)=>{seg(X0R,YP,X1R,YP,win,{color:RED,lw:8,dur:.4});ng('title',{x:X0R-6,y:YP-46,w:110,h:38,text:'+24 V',size:19,bg:RED},win);
    seg(X0R,YN,X1R,YN,win,{color:BU,lw:8,dur:.4});ng('title',{x:X0R-6,y:YN+8,w:90,h:38,text:'0 V',size:19,bg:BU},win)};
  /* sensor block. kind npn|pnp; tClose = output switch closes; returns terminal points */
  const sensor=(kind,win,tClose,o={})=>{const npn=kind==='npn',SX=cx+35,xb=npn?cx-50:SX,xu=npn?SX:cx-50;
    box({x:bx0,y:by0,w:bx1-bx0,h:by1-by0,head:npn?'NPN':'PNP',color:npn?NG.org:NG.teal,lines:[],headSize:22},win);
    lamp(bx1-22,by0+66,20,o.led??tClose,win,{color:AMB});ng('label',{x:bx1-62,y:by0+82,w:80,h:24,text:'LED',size:13},win);
    const sw=npn?[[SX,yBk],[SX,yBk+42]]:[[SX,yBk-50],[SX,yBk]];
    // fixed internal wiring
    if(npn){seg(bx1,yBk,SX,yBk,win,{color:BK,lw:4});seg(SX,yBk+42,SX,by1,win,{color:BU,lw:4});seg(xb,by0,xb,by0+60,win,{color:BN,lw:4})}
    else{seg(xb,by0,xb,yBk-50,win,{color:BN,lw:4});seg(SX,yBk,bx1,yBk,win,{color:BK,lw:4});seg(xu,by1,xu,by1-40,win,{color:BU,lw:4})}
    ng('label',{x:(npn?xb:xu)-50,y:npn?by0+66:by1-74,w:100,h:24,text:'power',size:13,color:'#8e98a3'},win);
    // switch blade: open → closed at tClose (never closes if tClose is null)
    const[a,b]=sw,tc=tClose??1e9;
    seg(a[0],a[1],b[0]+26,b[1]-12,[win[0],Math.min(tc,win[1])],{color:NG.ink,lw:5});
    if(tc<win[1])seg(a[0],a[1],b[0],b[1],[tc,win[1]],{color:NG.ink,lw:5,dur:.15});
    ng('label',{x:cx-75,y:sw[0][1]+(npn?6:-2),w:70,h:22,text:'switch',size:13,color:'#5d6b7a'},[win[0]+.4,win[1]]);
    return{brown:[xb,by0],blue:[xu,by1],black:[bx1,yBk],sw,xb,xu};
  };
  /* PLC input block (X0 top, S/S bottom) */
  const PX=800,PY=200,X0Y=310,SSY=440,LX=1010;
  const plc=(win,xOn,o={})=>{box({x:PX,y:PY,w:420,h:320,head:'MITSUBISHI PLC · INPUT',color:NG.navy,lines:[],headSize:20},win);
    box({x:930,y:280,w:160,h:190,head:'INPUT CIRCUIT',color:'#5d6b7a',headH:30,headSize:13,lw:3,lines:[]},[win[0]+.3,win[1]]);
    ng('title',{x:PX-34,y:X0Y-20,w:68,h:40,text:'X0',size:20,bg:NG.ink},win);ng('title',{x:PX-34,y:SSY-20,w:68,h:40,text:'S/S',size:18,bg:NG.ink},win);
    lamp(LX,370,52,xOn??1e9,[win[0]+.3,win[1]],{color:NG.grn});
    lamp(1180,250,28,xOn??1e9,win,{color:NG.grn});ng('label',{x:1140,y:270,w:80,h:26,text:'X0 LED',size:13},win);
    return{x0:[PX+34,X0Y],ss:[PX+34,SSY]};
  };
  const ledLabelOn=(t,win,text,col)=>ng('title',{x:1035,y:530,w:180,h:44,text,size:20,bg:col},[t,win[1]]);

  /* ===== 0–1 HOOK (0 – 28) ===== */
  const H=W(0,1);
  mg('conv',{x:440,y:470,w:520,h:44,run:[[0,2.3]]},H);mg('box',{x:600,y:390,w:90,h:80,fromX:430,mv:[0.2,2.3]},[0.2,H[1]]);
  mg('sensor',{x:720,y:405,w:170,h:46,led:2.3,det:2.3},[0.3,H[1]]);label('SENSOR LED ON',840,360,[3.4,H[1]],{w:240,size:20,color:'#d88a00'});
  mg('plc',{x:1010,y:170,w:230,h:150,label:'PLC',on:null},[1.0,H[1]]);label('X0 OFF',1180,345,[6.0,H[1]],{w:140,color:RED});
  seg(895,428,1040,325,[1.4,H[1]],{color:BK,lw:4,dash:[10,8]});ng('cross',{x:942,y:350,w:50,h:50},[6.4,H[1]]);
  pill('LED ON · PLC X0 OFF – YEN?',820,30,[6.0,9.4],{w:520,bg:RED});
  pill('SPARE SENSOR POTTADHUKKU APPURAM',820,30,[9.4,H[1]],{w:560,bg:NG.navy,size:22});
  [['BROWN → +24 V',BN,T(1,1)],['BLUE → 0 V',BU,T(1,2)],['BLACK → X0',BK,T(1,3)]].forEach(([t,c,at],i)=>{ng('title',{x:420+i*270,y:640,w:220,h:46,text:t,size:19,bg:c},[at,H[1]]);ng('tick',{x:645+i*270,y:644,w:34,h:34,lw:8},[T(1,4)+i*.2,H[1]])});
  ng('title',{x:1060,y:440,w:130,h:110,text:'?',size:90,bg:RED},[T(1,6),H[1]]);

  /* ===== 2 THE LAMP EXPERIMENT (28 – 31.9) ===== */
  const L2=W(2);
  mg('sensor',{x:520,y:310,w:220,h:60,wires:true},L2);ng('label',{x:540,y:420,w:200,h:30,text:'SENSOR',size:22},L2);
  mg('bulb',{x:905,y:295,w:90,on:null},[T(2,0)+.6,L2[1]]);ng('label',{x:850,y:440,w:200,h:30,text:'24 V LAMP',size:22},[T(2,0)+.6,L2[1]]);
  pill('LAMP = NAMMA LOAD',820,40,[T(2,1),L2[1]],{w:380,bg:NG.teal});

  /* ===== 3–5 NPN + LAMP (31.9 – 69.6) ===== */
  const N=W(3,5),tN=T(4,0)+.6,fN=T(4,3);
  pill('NPN SENSOR + LAMP',820,24,N,{w:400,bg:NG.org});rails(N);
  const sn=sensor('npn',N,tN);
  wire([[sn.brown[0],YP],sn.brown],BN,[T(3,1),N[1]]);
  wire([sn.blue,[sn.blue[0],YN]],BU,[T(3,2),N[1]],{flow:fN});
  mg('bulb',{x:872,y:242,w:56,on:T(4,6)},[T(3,3),N[1]]);label('24V LAMP',1000,270,[T(3,3),N[1]],{w:140,size:18});
  wire([[900,YP],[900,242]],RED,[T(3,3),N[1]],{flow:fN});
  wire([[900,298],[900,yBk],sn.black],BK,[T(3,4),N[1]],{flow:fN});
  // internal current path (black → switch → blue) once the switch is closed
  wire([sn.black,[cx+35,yBk],[cx+35,by1]],'rgba(0,0,0,0)',[fN,N[1]],{flow:fN,lw:1});
  label('TARGET VANDHAA → SWITCH ON',560,230,[T(4,0),T(4,2)],{w:400,size:20,color:NG.org});
  label('BLACK → 0 V',720,500,[T(4,1),N[1]],{w:200,size:20,color:BU});
  pill('CURRENT ENGA POGUM?',820,24,[T(4,2),T(4,3)],{w:400,bg:RED});
  label('CURRENT PATH COMPLETE ✓',1060,560,[T(4,5),N[1]],{w:340,size:22,color:NG.grn});
  ng('arrow',{x1:800,y1:yBk+38,x2:690,y2:yBk+38,x:690,y:yBk+20,w:110,h:36,noPop:true,color:NG.grn,lw:6,label:'INTO SENSOR'},[T(5,1),N[1]]);
  pill('NPN = SINKING OUTPUT',1050,470,[T(5,2),N[1]],{w:330,bg:NG.org});
  s.cam=[{t:0,x:640,y:360,z:1},{t:T(5,0),x:700,y:400,z:1.3,d:.9},{t:T(5,2)+.2,x:640,y:360,z:1,d:.8}];

  /* ===== 6–7 PNP + LAMP (69.6 – 99.4) ===== */
  const Pq=W(6,7),tP=T(7,0)+.6,fP=T(7,2);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[Pq[0],Pq[0]+.5]);
  pill('PNP SENSOR + LAMP',820,24,Pq,{w:400,bg:NG.teal});rails(Pq);
  const sp=sensor('pnp',Pq,tP);
  wire([[sp.brown[0],YP],sp.brown],BN,[T(6,1),Pq[1]],{flow:fP});
  wire([sp.blue,[sp.blue[0],YN]],BU,[T(6,1),Pq[1]]);
  wire([sp.brown,[cx+35,yBk-50],[cx+35,yBk],sp.black],'rgba(0,0,0,0)',[fP,Pq[1]],{flow:fP,lw:1});
  wire([sp.black,[900,yBk],[900,472]],BK,[T(6,3),Pq[1]],{flow:fP});
  mg('bulb',{x:872,y:472,w:56,on:T(7,4)},[T(6,3),Pq[1]]);label('24V LAMP',1000,500,[T(6,3),Pq[1]],{w:140,size:18});
  wire([[900,528],[900,YN]],BU,[T(6,4),Pq[1]],{flow:fP});
  label('BLACK → +24 V',720,250,[T(7,1),Pq[1]],{w:220,size:20,color:RED});
  ng('arrow',{x1:690,y1:yBk-36,x2:800,y2:yBk-36,x:690,y:yBk-54,w:110,h:36,noPop:true,color:NG.grn,lw:6,label:'OUT OF SENSOR'},[T(7,2)+.5,Pq[1]]);

  /* ===== 8 COMPARE (99.4 – 116.9) ===== */
  const C8=W(8);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[C8[0],C8[0]+.5]);
  pill('RENDU-LAYUM LAMP ERIYUDHU',820,24,C8,{w:480,bg:NG.navy});
  const card=(x,head,col,txt,dir,at)=>{box({x,y:120,w:360,h:380,head,color:col,lines:[]},[at,C8[1]]);mg('sensor',{x:x+90,y:230,w:180,h:48,led:at+.6,det:at+.6},[at+.2,C8[1]]);
    ng('arrow',{x1:dir>0?x+330:x+230,y1:350,x2:dir>0?x+230:x+330,y2:350,x:x+230,y:330,w:100,h:40,noPop:true,color:NG.grn,lw:8,flow:true,flowFrom:at+.6,speed:.9},[at+.4,C8[1]]);
    ng('label',{x:x+10,y:400,w:340,h:40,text:txt,size:20,color:col},[at+.6,C8[1]])};
  card(430,'NPN',NG.org,'CURRENT ULLA → SINKS',1,T(8,2));card(840,'PNP',NG.teal,'CURRENT VELIYA → SOURCES',-1,T(8,3));
  pill('NPN SINKS · PNP SOURCES',820,560,[T(8,4),C8[1]],{w:480,bg:NG.ink,size:26});

  /* ===== 9 PLC INPUT = LAMP (116.9 – 130.2) ===== */
  const P9=W(9);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P9[0],P9[0]+.5]);
  pill('LAMP → PLC INPUT',820,24,P9,{w:380,bg:NG.navy});
  plc([T(9,1),P9[1]],T(9,4)+2.5);
  mg('bulb',{x:485,y:335,w:70,on:T(9,3)+.6},[T(9,3),P9[1]]);ng('label',{x:600,y:350,w:80,h:40,text:'≈',size:44},[T(9,4),P9[1]]);
  wire([[PX+34,X0Y],[LX,X0Y],[LX,344]],BK,[T(9,4),P9[1]],{flow:T(9,4)+1.2});wire([[LX,396],[LX,SSY],[PX+34,SSY]],BK,[T(9,4),P9[1]],{flow:T(9,4)+1.2});

  /* PLC circuit helper for 10–17 & quiz */
  const plcCircuit=(win,kind,ssTo,tClose,flowT,xOn,o={})=>{rails(win);const sv=sensor(kind,win,tClose,{led:o.led});const pl=plc(win,xOn);
    const fl=flowT;const pnp=kind==='pnp';
    wire([[sv.brown[0],YP],sv.brown],BN,win,pnp&&fl!=null?{flow:fl}:{});
    wire([sv.blue,[sv.blue[0],YN]],BU,win,!pnp&&fl!=null?{flow:fl}:{});
    const blackPts=[sv.black,[730,yBk],[730,X0Y],pl.x0];
    wire(pnp?blackPts:blackPts.slice().reverse(),BK,win,fl!=null?{flow:fl}:{});
    const ssPts=ssTo==='0v'?[pl.ss,[770,SSY],[770,YN]]:[[770,YP],[770,SSY],pl.ss];
    wire(ssPts,ssTo==='0v'?BU:RED,win,fl!=null?{flow:fl}:{});
    ng('label',{x:700,y:ssTo==='0v'?530:180,w:140,h:28,text:'COM',size:16},win);
    const inner=[[PX+34,X0Y],[LX,X0Y],[LX,344]],inner2=[[LX,396],[LX,SSY],[PX+34,SSY]];
    if(pnp){wire(inner,BK,win,fl!=null?{flow:fl,lw:4}:{lw:4});wire(inner2,BK,win,fl!=null?{flow:fl,lw:4}:{lw:4})}
    else{wire(inner2.slice().reverse(),BK,win,fl!=null?{flow:fl,lw:4}:{lw:4});wire(inner.slice().reverse(),BK,win,fl!=null?{flow:fl,lw:4}:{lw:4})}
    if(fl!=null){const ip=pnp?[sv.brown,[cx+35,yBk-50],[cx+35,yBk],sv.black]:[sv.black,[cx+35,yBk],[cx+35,by1]];wire(ip,'rgba(0,0,0,0)',[fl,win[1]],{flow:fl,lw:1})}
    return{sv,pl}};

  /* ===== 10–12 PNP → X0, S/S at 0 V (130.2 – 163.5) ===== */
  const P10=W(10,12);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P10[0],P10[0]+.5]);
  pill('PNP SENSOR → X0 · S/S = 0 V',820,24,P10,{w:500,bg:NG.teal});
  plcCircuit(P10,'pnp','0v',T(10,3)+.4,T(11,1),T(11,4));
  label('X0 → +24 V',700,270,[T(10,3)+.4,P10[1]],{w:180,size:18,color:RED});
  ledLabelOn(T(11,4),P10,'X0 ON ✓',NG.grn);
  pill('SENSOR = SOURCING OUTPUT',560,560,[T(12,2),P10[1]],{w:330,size:19,bg:NG.teal});
  pill('PLC X0 = SINKING INPUT',1010,600,[T(12,4),P10[1]],{w:330,size:19,bg:NG.navy});

  /* ===== 13–15 THE FAULT: NPN, S/S still at 0 V (163.5 – 200.6) ===== */
  const P13=W(13,15);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P13[0],P13[0]+.5]);
  pill('OPENING FAULT: OLD PNP → SPARE NPN',820,24,[P13[0],T(14,0)],{w:560,bg:RED,size:22});
  pill('NPN SENSOR → X0 · S/S = 0 V',820,24,[T(14,0),P13[1]],{w:500,bg:RED});
  plcCircuit(P13,'npn','0v',T(14,0)+.5,null,null,{led:T(14,1)});
  label('LED ON',cx-10,by0-46,[T(14,1),P13[1]],{w:120,size:20,color:'#d88a00'});
  label('X0 → 0 V',725,270,[T(14,2),P13[1]],{w:160,size:18,color:BU});
  ng('title',{x:PX+40,y:X0Y-56,w:120,h:38,text:'X0 ≈ 0 V',size:17,bg:BU},[T(15,1),P13[1]]);
  ng('title',{x:PX+40,y:SSY+14,w:120,h:38,text:'S/S = 0 V',size:17,bg:BU},[T(15,2),P13[1]]);
  ng('title',{x:860,y:540,w:340,h:46,text:'ORE VOLTAGE → CURRENT ILLA',size:19,bg:RED},[T(15,3),P13[1]]);
  ng('cross',{x:985,y:345,w:50,h:50},[T(15,4),P13[1]]);
  ng('title',{x:420,y:655,w:420,h:46,text:'SENSOR LED ON · PLC X0 OFF',size:20,bg:RED},[T(15,5),P13[1]]);
  s.cam.push({t:T(15,0),x:820,y:380,z:1.25,d:.9},{t:T(15,5),x:640,y:360,z:1,d:.8});

  /* ===== 16–17 THE FIX: S/S to +24 V (200.6 – 237) ===== */
  const P16=W(16,17);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P16[0],P16[0]+.5]);
  pill('NPN SENSOR → S/S = +24 V',820,24,P16,{w:480,bg:NG.org});
  plcCircuit(P16,'npn','24v',P16[0]+.6,T(16,2),T(16,5));
  ledLabelOn(T(16,5),P16,'X0 ON ✓',NG.grn);
  pill('PLC X0 = SOURCING INPUT',1010,600,[T(17,1),P16[1]],{w:330,size:19,bg:NG.navy});
  pill('SENSOR = SINKING OUTPUT',560,560,[T(17,3),P16[1]],{w:330,size:19,bg:NG.org});

  /* ===== 18 THE RULE (237 – 251.2) ===== */
  const P18=W(18);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P18[0],P18[0]+.5]);
  pill('SINK-AA? SOURCE-AA?',820,24,P18,{w:420,bg:NG.navy});
  box({x:430,y:110,w:380,h:200,head:'ENDHA DEVICE?',color:NG.navy,align:'left',lines:[{t:'Sensor → black OUT terminal',at:T(18,1)},{t:'PLC → X0 terminal',at:T(18,2)}],lh:54},P18);
  box({x:840,y:110,w:380,h:200,head:'CURRENT DIRECTION',color:NG.teal,align:'left',lines:[{t:'Device-kulla → SINK',at:T(18,3),color:NG.org},{t:'Device-lendhu veliya → SOURCE',at:T(18,4),color:NG.teal}],lh:54},P18);
  ng('arrow',{x1:640,y1:450,x2:540,y2:450,x:540,y:430,w:100,h:40,noPop:true,color:NG.org,lw:8,flow:true,flowFrom:T(18,3),speed:.9,label:'SINK'},[T(18,3),P18[1]]);
  mg('sensor',{x:410,y:430,w:120,h:34},[T(18,3),P18[1]]);
  ng('arrow',{x1:960,y1:450,x2:1060,y2:450,x:960,y:430,w:100,h:40,noPop:true,color:NG.teal,lw:8,flow:true,flowFrom:T(18,4),speed:.9,label:'SOURCE'},[T(18,4),P18[1]]);
  mg('sensor',{x:830,y:430,w:120,h:34},[T(18,4),P18[1]]);

  /* ===== 19 TROUBLESHOOT CHECKLIST (251.2 – 269.6) ===== */
  const P19=W(19);
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P19[0],P19[0]+.5]);
  pill('LED ON, X0 VARALA-NA',820,24,P19,{w:420,bg:RED});
  [['① SENSOR LABEL: PNP-AA? NPN-AA?',T(19,0)],['② INPUT GROUP COMMON (S/S) ENGA?',T(19,1)],['③ +24 V → 0 V CURRENT PATH TRACE',T(19,2)]].forEach(([t,at],i)=>{
    box({x:440,y:120+i*130,w:700,h:100,color:[NG.teal,NG.navy,NG.org][i],lines:[{t,size:26}]},[at,P19[1]]);ng('tick',{x:1160,y:140+i*130,w:56,h:56},[at+1.4,P19[1]])});
  label('ENDHA CONNECTION MATCH AAGALA-NU THERIYUM',790,560,[T(19,3),P19[1]],{w:700,size:22,color:NG.grn});

  /* ===== 20–24 QUIZ: PNP + S/S at +24 V (269.6 – end) ===== */
  const P20=[PS(20),END];
  ng('flash',{x:0,y:0,w:1280,h:720,noPop:true},[P20[0],P20[0]+.5]);
  pill('QUICK QUIZ',820,24,[P20[0],T(20,2)],{w:300,bg:NG.org});
  pill('PNP SENSOR → X0 · S/S = +24 V',820,24,[T(20,2),PS(21)],{w:520,bg:NG.org});
  const qz=[T(20,2),PS(21)];
  plcCircuit(qz,'pnp','24v',T(20,5)+.3,null,null,{led:T(20,6)});
  ng('title',{x:PX+40,y:X0Y-56,w:120,h:38,text:'X0 = ? V',size:17,bg:NG.ink},[T(20,6),qz[1]]);
  ng('title',{x:PX+40,y:SSY+14,w:120,h:38,text:'S/S = ? V',size:17,bg:NG.ink},[T(20,6)+.3,qz[1]]);
  ng('title',{x:960,y:540,w:240,h:56,text:'X0 = ?',size:30,bg:RED},[T(20,7),qz[1]]);
  const QW=[PS(21),END];
  pill('UNGA ANSWER?',820,24,QW,{w:340,bg:NG.org});
  [['A','X0 ON aagum',NG.grn,PS(21)],['B','X0 OFF-la irukkum',RED,PS(22)],['C','X0 ON / OFF maaritte irukkum',NG.blue,PS(23)]].forEach(([l,t,c,at],i)=>{
    ng('title',{x:440,y:110+i*120,w:90,h:90,text:l,size:48,bg:c},[at,END]);box({x:550,y:110+i*120,w:640,h:90,color:c,lines:[{t,size:28}]},[at,END])});
  box({x:440,y:480,w:750,h:150,head:'COMMENT-LA REASONING SOLLUNGA',color:NG.navy,lines:[{t:'X0, S/S enna voltage?',at:T(24,2)},{t:'Input circuit vazhiya current odumaa?',at:T(24,3)}],lh:42},[T(24,1),END]);
  S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
/* ---------- FDT Short (9:16, 0:46) ---------- */
async function buildFdtNpnShort(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('9:16');S.narrOff=0;
  const A=FDT_NPN_SA,END=46.4;
  const s=newScene({name:'FDT Short – LED ON, X0 OFF?',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const{ng,T,PS,seg,wire,pill,label,lamp,box,mg}=fdtKit(s,A);
  const RED='#e5484d',BN='#8b5a2b',BU='#2f6fd6',BK='#1d1d1f',AMB='#ffb020';
  const host=addStick({scene:s,quiet:true,look:'office',action:'question',size:440,x:-10,y:820,facing:1,entrance:'none',delay:0,withPrev:true,draw:.1,name:'Host'});
  host.beats=[[0,'question'],[3.4,'worriedlook'],[7.6,'scratchhead'],[9.3,'swap'],[15.5,'screwdriver'],[17.7,'holdsensor'],[20.6,'scratchhead'],[21.3,'onefinger'],[24.6,'trace'],[30.3,'pointdownright'],[36,'askviewer'],[41,'thumbsup'],[43.4,'wavebye']].map(([t,pose])=>({t,pose,blend:.22}));host.speak=[[0,END]];
  /* 0 hook */
  const H=[0,PS(1)];
  pill('LED ON · X0 OFF?',360,70,[0.2,PS(2)],{w:560,h:70,size:36,bg:RED});
  mg('conv',{x:40,y:450,w:640,h:52,run:[[0,2.4]]},[0,PS(2)]);mg('box',{x:220,y:350,w:120,h:100,fromX:40,mv:[0.2,2.4]},[0.2,PS(2)]);mg('sensor',{x:370,y:372,w:230,h:58,led:2.5,det:2.5},[0.2,PS(2)]);
  label('SENSOR LED ON',500,320,[T(0,1),PS(2)],{w:320,size:30,color:'#d88a00'});
  mg('plc',{x:380,y:700,w:300,h:190,label:'PLC',on:null},[T(0,2)-.2,PS(1)]);label('X0 OFF',540,925,[T(0,2),PS(1)],{w:220,size:34,color:RED});
  ng('title',{x:440,y:1010,w:220,h:150,text:'YEN?',size:64,bg:RED},[T(0,3),PS(1)]);
  /* 1 swap */
  const P1=[PS(1),PS(2)];
  box({x:410,y:620,w:280,h:110,head:'OLD',color:NG.teal,lines:[{t:'PNP',size:34,color:NG.teal}]},[T(1,0),P1[1]]);
  box({x:410,y:750,w:280,h:110,head:'NEW SPARE',color:NG.org,lines:[{t:'NPN',size:34,color:NG.org}]},[T(1,1),P1[1]]);
  [['BROWN',BN],['BLUE',BU],['BLACK',BK]].forEach(([t,c],i)=>{ng('title',{x:420,y:880+i*62,w:200,h:50,text:t,size:22,bg:c},[T(1,2)+i*.3,P1[1]]);ng('tick',{x:630,y:884+i*62,w:40,h:40,lw:8},[T(1,2)+.6+i*.3,P1[1]])});
  pill('APPO X0 YEN ON AAGALA?',360,1120,[T(1,4)-.4,P1[1]],{w:600,h:64,size:30,bg:RED});
  /* 2 clue: black wire current direction */
  const P2=[PS(2),PS(3)];
  pill('CLUE',360,70,P2,{w:240,h:64,size:34,bg:NG.org});
  mg('sensor',{x:40,y:262,w:300,h:76},P2);
  seg(340,300,690,300,P2,{color:BK,lw:14});label('BLACK WIRE',520,360,P2,{w:320,size:32});
  ng('arrow',{x1:380,y1:440,x2:660,y2:440,x:380,y:420,w:280,h:40,noPop:true,color:NG.teal,lw:9,flow:true,flowFrom:T(2,0)+.5,speed:.7,label:'VELIYA?',lsize:30},[T(2,0)+.3,P2[1]]);
  ng('arrow',{x1:660,y1:540,x2:380,y2:540,x:380,y:520,w:280,h:40,noPop:true,color:NG.org,lw:9,flow:true,flowFrom:T(2,0)+1,speed:.7,label:'ULLA?',lsize:30},[T(2,0)+.8,P2[1]]);
  box({x:330,y:620,w:370,h:170,head:'TRACE PANNUNGA',color:NG.navy,lines:[{t:'SINK  vs  SOURCE',at:T(2,1),size:26}]},[T(2,1),P2[1]]);
  pill('FULL VIDEO ↓ LINKED',520,1080,[T(2,2),P2[1]],{w:380,h:64,size:28,bg:RED});
  /* 3 CTA */
  const P3=[PS(3),END];
  ng('flash',{x:0,y:0,w:720,h:1280,noPop:true},[P3[0],P3[0]+.5]);
  label('FACTORY DECODE TAMIL',360,140,P3,{w:640,size:40});
  pill('▶ SUBSCRIBE',480,360,[T(3,0)+1.5,END],{w:320,h:84,size:36,bg:RED});
  pill('👍 LIKE',480,500,[T(3,1),END],{w:320,h:84,size:36,bg:NG.blue});
  pill('↗ SHARE',480,640,[T(3,2),END],{w:320,h:84,size:36,bg:NG.teal});
  label('Sensor wiring doubt friend-kku',480,760,[T(3,2)+.6,END],{w:440,size:24,color:NG.navy});
  S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
