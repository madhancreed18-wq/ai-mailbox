/* ---------- EP10 – Star-Delta starter (Factory Decode Tamil) ----------
   Presenter (office stickman, natural-motion poses, old mouths) explains; Ravi (operator, look:'worker')
   and Kumar (technician, look:'tech') act the factory scenes. Hand off. Sketch art cards.
   Timing: ChatGPT paragraph times (mailbox 049) → sentence times EP10_A / EP10_SA. */
const EP10_A=__EP10_A__;
const EP10_SA=__EP10_SA__;
const EP10_POSE=__EP10_POSE__;
const EP10_SPOSE=__EP10_SPOSE__;
/* star / delta winding diagram: e.mode 'star'|'delta', e.live = [[t,0|1]] current dots */
function drawSD(e,c,tl){const cx=e.x+e.w/2,cy=e.y+e.h/2,R=Math.min(e.w,e.h)*.36,ink=O2,live=o2t(tl,e.live);
  const coil=(x1,y1,x2,y2,lab)=>{const L=Math.hypot(x2-x1,y2-y1),ux=(x2-x1)/L,uy=(y2-y1)/L,nx=-uy,ny=ux,a=L*.25,b=L*.75,n=8;
    c.beginPath();c.moveTo(x1,y1);c.lineTo(x1+ux*a,y1+uy*a);for(let i=1;i<=n;i++){const t=a+(b-a)*i/n,s=(i%2?1:-1)*12;c.lineTo(x1+ux*t+nx*s,y1+uy*t+ny*s)}c.lineTo(x2,y2);c.lineWidth=5;c.strokeStyle=e.col||'#b45309';c.stroke();
    if(lab)ngTxt(c,lab,(x1+x2)/2+nx*34,(y1+y2)/2+ny*34,22,'#b45309',800)};
  const node=(x,y,t,dx=0,dy=0)=>{c.beginPath();c.arc(x,y,9,0,7);c.fillStyle=ink;c.fill();if(t)ngTxt(c,t,x+dx,y+dy,22,ink,800)};
  const dots=(pts)=>{if(!live)return;const k=(tl*1.2)%1;for(let i=0;i<pts.length-1;i++){const[a,b]=[pts[i],pts[i+1]];const x=a[0]+(b[0]-a[0])*k,y=a[1]+(b[1]-a[1])*k;c.beginPath();c.arc(x,y,7,0,7);c.fillStyle='#f59e0b';c.fill()}};
  const ang=[-90,30,150].map(d=>d*Math.PI/180);
  if(e.mode==='star'){const P=ang.map(a=>[cx+Math.cos(a)*R,cy+Math.sin(a)*R]),L=ang.map(a=>[cx+Math.cos(a)*R*1.45,cy+Math.sin(a)*R*1.45]);
    P.forEach((p,i)=>coil(p[0],p[1],cx,cy,i===0?e.vlab:null));P.forEach((p,i)=>{c.beginPath();c.moveTo(p[0],p[1]);c.lineTo(L[i][0],L[i][1]);c.lineWidth=4;c.strokeStyle=ink;c.stroke()});
    ['U1','V1','W1'].forEach((t,i)=>node(P[i][0],P[i][1],t,i===0?36:0,i===0?0:30));['L1','L2','L3'].forEach((t,i)=>ngTxt(c,t,L[i][0],L[i][1]+(i?24:-22),22,NG.navy,800));
    node(cx,cy,'U2 V2 W2',0,36);dots([L[0],P[0],[cx,cy],P[1],L[1]])}
  else{const P=ang.map(a=>[cx+Math.cos(a)*R*1.15,cy+Math.sin(a)*R*1.15]),L=ang.map(a=>[cx+Math.cos(a)*R*1.6,cy+Math.sin(a)*R*1.6]);
    coil(P[0][0],P[0][1],P[1][0],P[1][1],e.vlab);coil(P[1][0],P[1][1],P[2][0],P[2][1]);coil(P[2][0],P[2][1],P[0][0],P[0][1]);
    P.forEach((p,i)=>{c.beginPath();c.moveTo(p[0],p[1]);c.lineTo(L[i][0],L[i][1]);c.lineWidth=4;c.strokeStyle=ink;c.stroke();node(p[0],p[1])});
    ['L1','L2','L3'].forEach((t,i)=>ngTxt(c,t,L[i][0],L[i][1]+(i?24:-22),22,NG.navy,800));dots([L[0],P[0],P[1],L[1]])}
  if(e.title)ngTxt(c,e.title,cx,e.y+18,30,NG.navy,800)}
function ep10Kit(s,A,END){const K=ep09Kit(s,A,END),{ng}=K;
  const card=(x,y,w,h,text,win,o={})=>ng('card2',{x,y,w,h,text,...o},win);
  const bit=(x,y,w,h,name,sub,val,win)=>ng('bit2',{x,y,w,h,name,sub,val},win);
  const wipe=t=>ng('wipe2',{x:0,y:0,w:W,h:H,noPop:true},[t-.38,t+.38]);
  const actor=(look,beats,win,o={})=>{const st=addStick({scene:s,quiet:true,look,action:beats[0][1],size:o.size||460,x:o.x??40,y:o.y??(H-(o.size||460)-10),facing:o.facing||1,entrance:'pop',delay:0,withPrev:true,draw:.1,name:o.name||look});st.win=win;st.beats=beats.map(([t,pose])=>({t,pose,blend:.3}));st.speak=[];return st};
  const presenter=(win,o={})=>{const st=addStick({scene:s,quiet:true,look:'office',action:'idle_a',size:o.size||420,x:o.x??-30,y:o.y??(H-(o.size||420)-6),facing:1,entrance:'pop',delay:0,withPrev:true,draw:.1,name:'Presenter'});
    st.win=win;const bs=(o.poses||EP10_POSE).filter(b=>b[0]>=win[0]-.5&&b[0]<win[1]);st.beats=[{t:0,pose:bs.length?bs[0][1]:'idle_a',blend:.3},...bs.map(([t,p])=>({t:t-win[0],pose:p,blend:.3}))];st.speak=[[0,win[1]-win[0]]];return st};
  const RUNG=(x,y,w,items,win,o={})=>ng('rung',{x,y,w,h:70,items,drawOn:true,...o},win);
  return{...K,card,bit,wipe,actor,presenter,RUNG};
}
async function buildEp10(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('16:9');S.narrOff=0;S.art='sketch';
  try{await document.fonts.load('700 30px InkHand')}catch(_){}
  const A=EP10_A,END=309.6;
  const s=newScene({name:'EP10 – Star-Delta starter',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep10Kit(s,A,END),{ng,T,PS,card,bit,wipe,actor,presenter,RUNG}=K,RED=NG.red,GRN=NG.grn,BLU=NG.blue,PUR='#7c3aed',ORG='#f59e0b';
  const P=(a,b=a)=>[PS(a),b>=27?END:PS(b+1)],dark=(t0,t1)=>ng('flash',{x:0,y:0,w:W,h:H,noPop:true,color:'#111827'},[t0,t1]);
  /* k0 HOOK – Ravi starts a 30 HP motor direct, lights dim, trip */
  actor('worker',[[0,'op_press_start'],[T(0,5)-.2,'op_lights_dim'],[T(0,7),'op_cover_ears']],[0,PS(1)],{x:20,size:500});
  card(620,60,560,90,'Veetu motor = light dim',[0,T(0,2)]);
  card(620,60,560,90,'30 HP motor – DIRECT start',[T(0,3),PS(1)],{bg:'#fef3c7'});
  bit(620,190,330,130,'CURRENT','starting current',[[0,'1×'],[T(0,4)+.4,'7–8×']],[T(0,4),PS(1)]);
  for(let i=0;i<3;i++)dark(T(0,5)+i*.7,T(0,5)+i*.7+.45);
  card(620,360,330,90,'TRIP!',[T(0,6),PS(1)],{bg:RED,emoji:'⚡',size:40});
  /* k1 INTRO – Star Delta, Kumar, FX3U timer, quiz */
  wipe(PS(1));presenter(P(1));
  card(380,60,520,120,'STAR – DELTA',P(1),{bg:ORG,size:56});
  actor('tech',[[0,'tc_all_ok']],[T(1,1),PS(2)],{x:880,size:420,y:H-430});
  card(380,230,460,84,'Technician Kumar',[T(1,1),PS(2)]);
  card(380,340,460,84,'FX3U + Timer',[T(1,2),PS(2)]);
  card(380,450,460,84,'Quiz – answer kadaisila',[T(1,3),PS(2)],{bg:'#dbeafe',emoji:'🎯'});
  /* k2–k3 PANEL + TERMINAL BOX (Kumar) */
  wipe(PS(2));
  actor('tech',[[0,'tc_open_panel'],[T(2,1),'tc_point_contactors']],P(2),{x:20,size:520});
  [['KM1','MAIN'],['KM2','STAR'],['KM3','DELTA']].forEach(([a,b],i)=>card(760,70+i*110,440,90,a+' · '+b,[T(2,2+i),PS(3)],{bg:['#dbeafe','#fef3c7','#ede9fe'][i]}));
  card(760,410,440,90,'Overload relay',[T(2,5),PS(3)]);
  actor('tech',[[0,'tc_motor_box']],P(3),{x:20,size:520});
  ['U1','V1','W1'].forEach((t,i)=>card(760+i*150,140,130,90,t,[T(3,2)+i*.5,PS(4)],{size:40}));
  ['U2','V2','W2'].forEach((t,i)=>card(760+i*150,290,130,90,t,[T(3,3)+i*.5,PS(4)],{size:40,bg:'#fef3c7'}));
  card(760,440,430,84,'6 terminals',[T(3,1),PS(4)]);
  /* k4–k5 STAR vs DELTA (presenter) */
  wipe(PS(4));presenter(P(4,5));
  ng('sdiag',{x:380,y:60,w:440,h:440,mode:'star',title:'STAR',vlab:'≈240 V',live:[[T(4,4),1]]},P(4,5));
  card(380,540,440,80,'U2 V2 W2 = short',[T(4,0)+1,PS(5)]);
  card(860,120,380,90,'415 ÷ √3 ≈ 240 V',[T(4,2),PS(5)],{bg:'#fef3c7'});
  card(860,240,380,90,'Current, torque = ⅓',[T(4,3),PS(5)]);
  card(860,360,380,90,'Mella start',[T(4,4),PS(5)],{bg:'#dcfce7'});
  ng('sdiag',{x:820,y:60,w:440,h:440,mode:'delta',title:'DELTA',vlab:'415 V',live:[[T(5,0)+1,1]]},P(5));
  card(860,540,360,80,'Full power · full torque',[T(5,1),PS(6)],{bg:'#dcfce7'});
  /* k6 SEQUENCE (Ravi) */
  wipe(PS(6));
  actor('worker',[[0,'op_press_start'],[T(6,2),'op_wait_watch'],[T(6,8),'op_thumbs_motor']],P(6),{x:20,size:500});
  const sec=[];for(let i=0;i<=8;i++)sec.push([T(6,1)+i*(T(6,5)-T(6,1))/8,i+' s']);
  bit(600,60,300,110,'KM1 MAIN','',[[0,0],[T(6,1),1]],P(6));bit(920,60,300,110,'KM2 STAR','',[[0,0],[T(6,1),1],[T(6,5),0]],P(6));
  bit(600,200,300,110,'KM3 DELTA','',[[0,0],[T(6,7),1]],P(6));bit(920,200,300,110,'T0 timer','star time',[[0,'0 s'],...sec],[T(6,1),PS(7)]);
  card(600,350,620,84,'Light dim aagala ✓',[T(6,3),T(6,5)],{bg:'#dcfce7'});
  card(600,350,300,84,'Star OFF',[T(6,5),PS(7)]);card(920,350,300,84,'GAP 0.1 s',[T(6,6),PS(7)],{bg:'#fef3c7'});
  card(600,460,620,84,'Delta ON → full speed',[T(6,7),PS(7)],{bg:'#dcfce7'});
  /* k7 TIMER SETTING (Kumar) */
  wipe(PS(7));
  actor('tech',[[0,'tc_clamp_meter'],[T(7,2),'tc_set_timer']],P(7),{x:20,size:520});
  card(720,90,500,90,'Timer evlo?',[PS(7),T(7,1)],{emoji:'🤔'});
  card(720,90,500,90,'Measure start time',[T(7,1),PS(8)]);
  card(720,220,500,90,'Timer set',[T(7,2),PS(8)]);
  card(720,350,500,90,'Manual: 6 s+',[T(7,3),PS(8)],{bg:'#fef3c7'});
  /* k8 PLC I/O */
  wipe(PS(8));presenter(P(8,15));
  card(380,40,860,80,'FX3U  I/O',[PS(8),PS(9)],{bg:NG.navy});
  [['X0','Start'],['X1','Stop'],['X2','Overload']].forEach(([a,b],i)=>card(380,150+i*110,410,90,a+' · '+b,[T(8,2+i),PS(9)],{bg:'#dbeafe'}));
  [['Y0','Main'],['Y1','Star'],['Y2','Delta']].forEach(([a,b],i)=>card(830,150+i*110,410,90,a+' · '+b,[T(8,6+i),PS(9)],{bg:'#dcfce7'}));
  /* k9 RUNG 1 self-holding */
  wipe(PS(9));
  const st1=[[T(9,4),1],[T(9,5),0]],m0=[[T(9,4)+.2,1],[T(9,6)+1,0]];
  ng('rung',{drawOn:true,x:400,y:170,w:820,h:130,num:'1',items:[{k:'NO',label:'X0 START',on:st1,par:{label:'M0',on:m0}},{k:'NC',label:'X1 STOP',on:[[0,1],[T(9,6)+1,0]]},{k:'NC',label:'X2 OL',on:[[0,1]]},{k:'COIL',label:'M0 RUN',on:m0}],power:[[T(9,4),1],[T(9,6)+1,0]]},[PS(9),PS(10)]);
  card(400,40,420,80,'Rung 1 · Self-holding',[PS(9),PS(10)],{bg:'#ccfbf1'});
  card(420,400,380,84,'Button vittaalum ON',[T(9,5),PS(10)],{bg:'#dcfce7'});card(840,400,380,84,'Stop / OL → OFF',[T(9,6),PS(10)],{bg:'#fee2e2'});
  /* k10 why not SET/RESET */
  wipe(PS(10));
  card(400,120,380,150,'SET / RESET',[T(10,1),PS(11)],{sub:'inga thevai illa',strike:T(10,2)});
  card(840,120,380,150,'Self-holding',[T(10,2),PS(11)],{sub:'1 rung · trace easy',bg:'#ccfbf1',tick:T(10,3)});
  card(500,330,620,84,'Application-ku yetha method',[T(10,4),PS(11)],{bg:'#fef3c7'});
  /* k11–k15 RUNGS 2–6 + a live run */
  wipe(PS(11));
  const run0=T(15,1)+1.2,tD=run0+3,tG=tD+.6,M0=[[run0,1]],T0d=[[tD,1]],Y1=[[run0,1],[tD,0]],T1d=[[tG,1]],Y2=[[tG,1]];
  RUNG(400,70,820,[{k:'NO',label:'M0',on:M0},{k:'COIL',label:'Y0 MAIN',on:M0}],[PS(11),PS(16)],{num:'2',power:M0});
  RUNG(400,170,820,[{k:'NO',label:'M0',on:M0},{k:'COIL',label:'T0 K80 (8 s)',on:T0d}],[PS(12),PS(16)],{num:'3',power:M0});
  RUNG(400,270,820,[{k:'NO',label:'M0',on:M0},{k:'NC',label:'T0',on:[[0,1],[tD,0]]},{k:'NC',label:'Y2',on:[[0,1],[tG,0]]},{k:'COIL',label:'Y1 STAR',on:Y1}],[PS(13),PS(16)],{num:'4',power:Y1});
  RUNG(400,370,820,[{k:'NO',label:'T0',on:T0d},{k:'COIL',label:'T1 K1 (0.1 s)',on:T1d}],[PS(14),PS(16)],{num:'5',power:T0d});
  RUNG(400,470,820,[{k:'NO',label:'T1',on:T1d},{k:'NC',label:'Y1',on:[[0,1],[run0,0],[tD,1]]},{k:'COIL',label:'Y2 DELTA',on:Y2}],[PS(15),PS(16)],{num:'6',power:Y2});
  card(400,580,400,80,'T0: 100 ms timer',[T(12,3),PS(13)],{bg:'#fef3c7'});card(840,580,380,80,'K80 = 8 s',[T(12,4),PS(13)],{bg:'#fef3c7'});
  card(400,580,820,80,'Run!  Star → gap → Delta',[run0-.4,PS(16)],{bg:'#dcfce7'});
  /* k16–k20 QUIZ (Ravi asks) */
  wipe(PS(16));
  actor('worker',[[0,'op_ask']],P(16),{x:20,size:500});
  card(600,70,620,110,'QUIZ',[PS(16),PS(17)],{bg:ORG,size:52,emoji:'🎯'});
  card(600,220,620,100,'Gap timer illaama?',[T(16,2),PS(17)],{bg:'#fef3c7'});
  card(600,360,620,100,'Star OFF + Delta ON – same scan',[T(16,3),PS(17)]);
  presenter(P(17,21));
  card(380,60,860,90,'Enna aagum?',[PS(17),PS(21)],{bg:ORG});
  [['A','Smooth-aa Delta-ku',GRN],['B','Short circuit · flash, trip',RED],['C','Reverse-la odum',BLU]].forEach(([l,t,c],i)=>{card(380,180+i*120,110,100,l,[PS(17+i),PS(21)],{bg:c,size:52});card(510,180+i*120,730,100,t,[PS(17+i)+.3,PS(21)])});
  card(380,550,860,90,'Comment pannunga!',[PS(20),PS(21)],{bg:'#dbeafe',emoji:'💬'});
  /* k21 SOFTWARE INTERLOCK */
  wipe(PS(21));
  RUNG(400,150,820,[{k:'NO',label:'M0'},{k:'NC',label:'T0'},{k:'NC',label:'Y2 (interlock)'},{k:'COIL',label:'Y1 STAR'}],[T(21,2),PS(22)],{num:'4'});
  RUNG(400,300,820,[{k:'NO',label:'T1'},{k:'NC',label:'Y1 (interlock)'},{k:'COIL',label:'Y2 DELTA'}],[T(21,3),PS(22)],{num:'6'});
  card(400,40,520,84,'INTERLOCK',[T(21,1),PS(22)],{bg:PUR});
  card(400,450,820,84,'Rendum orey nerathula ON aagave koodaadhu',[T(21,4),PS(22)],{bg:'#fee2e2'});
  /* k22 HARDWARE INTERLOCK (Kumar) */
  wipe(PS(22));
  actor('tech',[[0,'tc_point_contactors'],[T(22,1),'tc_check_interlock']],P(22),{x:20,size:520});
  card(720,70,500,90,'PLC interlock mattum podhaadhu',[PS(22),PS(23)],{bg:'#fef3c7'});
  card(720,200,500,90,'Contact WELD → stuck',[T(22,2),PS(23)],{bg:'#fee2e2',emoji:'⚠️'});
  card(720,330,500,90,'PLC OFF… contactor ON!',[T(22,3),PS(23)]);
  card(720,460,500,90,'Aux NC = hardware interlock',[T(22,4),PS(23)],{bg:'#dcfce7',tick:T(22,4)+1.5});
  /* k23 POWER CUT (Ravi) */
  wipe(PS(23));dark(PS(23),PS(23)+1.2);
  actor('worker',[[0,'op_wait_watch'],[T(23,3),'op_press_start']],P(23),{x:20,size:500});
  card(620,70,580,90,'Power cut?',[PS(23),PS(24)],{emoji:'🔌'});
  bit(620,200,330,120,'M0','run memory',[[0,1],[T(23,1),0]],P(23));
  card(620,360,580,90,'No auto start',[T(23,2),PS(24)],{bg:'#dcfce7'});
  card(620,480,580,90,'Self-holding = safe',[T(23,4),PS(24)],{bg:'#ccfbf1',tick:T(23,4)+1});
  /* k24 COMMON MISTAKES */
  wipe(PS(24));presenter(P(24,27));
  card(380,50,860,90,'Common mistakes',[PS(24),PS(25)],{bg:'#fee2e2',emoji:'⚠️'});
  card(380,180,410,150,'Timer kammi',[T(24,1),PS(25)],{sub:'current spike',scol:RED});card(830,180,410,150,'Timer adhigam',[T(24,3),PS(25)],{sub:'motor heat',scol:RED});
  card(380,380,860,90,'Overload = motor FLC',[T(24,4),PS(25)],{bg:'#dbeafe'});
  /* k25 SUMMARY */
  wipe(PS(25));
  card(380,40,860,84,'Quick summary',[PS(25),PS(26)],{bg:NG.navy});
  ['Star = mella start','Timer → gap','Appuram Delta','Interlock: soft + hard','Power cut → no auto start'].forEach((t,i)=>card(380,140+i*96,860,80,t,[T(25,1+i),PS(26)],{tick:T(25,1+i)+.6}));
  /* k26 ANSWER */
  wipe(PS(26));
  card(380,40,860,100,'ANSWER',[PS(26),PS(27)],{bg:ORG,size:52,emoji:'🎯'});
  card(380,170,860,90,'Contactor release time irukku',[T(26,1),PS(27)]);
  bit(380,290,280,120,'KM2 STAR','releasing…',[[0,1]],[T(26,3),PS(27)]);bit(700,290,280,120,'KM3 DELTA','closed',[[0,0],[T(26,3)+.6,1]],[T(26,3),PS(27)]);
  ng('flash',{x:0,y:0,w:W,h:H,noPop:true,color:RED},[T(26,4),T(26,4)+.6]);
  card(1000,290,240,120,'SHORT!',[T(26,4),PS(27)],{bg:RED,emoji:'⚡',size:34});
  card(380,450,860,110,'Answer: B',[T(26,5),PS(27)],{bg:NG.navy,size:56});
  /* k27 CTA */
  wipe(PS(27));
  card(380,50,860,90,'Correct answer-ku shout-out!',[PS(27),END],{emoji:'💬'});
  card(380,170,860,90,'Next: Forward / Reverse + interlock',[T(27,1),END],{bg:PUR});
  card(380,300,410,100,'LIKE',[T(27,2),END],{bg:BLU,emoji:'👍',size:40});card(830,300,410,100,'SHARE',[T(27,3),END],{bg:NG.teal,emoji:'↗️',size:40});
  card(530,440,560,110,'SUBSCRIBE',[T(27,4),END],{bg:RED,emoji:'🔔',size:48});
  o2schedule(s);S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
async function buildEp10Short(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('9:16');S.narrOff=0;S.art='sketch';
  try{await document.fonts.load('700 30px InkHand')}catch(_){}
  const A=EP10_SA,END=42.4;
  const s=newScene({name:'EP10 Short – Star-Delta',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep10Kit(s,A,END),{ng,T,PS,card,bit,wipe,actor,presenter}=K,RED=NG.red,GRN=NG.grn,ORG='#f59e0b';
  const dark=(t0,t1)=>ng('flash',{x:0,y:0,w:W,h:H,noPop:true,color:'#111827'},[t0,t1]);
  actor('worker',[[0,'op_press_start'],[T(0,2),'op_lights_dim'],[T(0,3),'op_cover_ears']],[0,PS(1)],{x:20,size:620,y:620});
  card(60,80,600,110,'Light dim aagudhaa?',[0,T(0,1)],{emoji:'💡'});
  card(60,80,600,110,'Periya motor – direct!',[T(0,1),PS(1)],{bg:'#fef3c7'});
  bit(60,230,360,140,'CURRENT','',[[0,'1×'],[T(0,2),'7–8×']],[T(0,2),PS(1)]);
  for(let i=0;i<3;i++)dark(T(0,3)+i*.6,T(0,3)+i*.6+.4);
  card(440,230,220,140,'TRIP!',[T(0,3)+.5,PS(1)],{bg:RED,size:40});
  wipe(PS(1));
  card(60,80,600,130,'STAR – DELTA',[PS(1),PS(2)],{bg:ORG,size:56});
  ng('sdiag',{x:90,y:250,w:540,h:540,mode:'star',title:'STAR',vlab:'≈240 V',live:[[T(1,1),1]]},[T(1,1),T(1,2)]);
  ng('sdiag',{x:90,y:250,w:540,h:540,mode:'delta',title:'DELTA',vlab:'415 V',live:[[T(1,2),1]]},[T(1,2),PS(2)]);
  card(60,830,600,100,'Mella start → Full power',[T(1,1),PS(2)],{bg:'#dcfce7'});
  wipe(PS(2));
  actor('worker',[[0,'op_ask']],[PS(2),PS(3)],{x:20,size:600,y:640});
  card(60,80,600,110,'Gap illaama?',[PS(2),PS(3)],{bg:ORG,size:44,emoji:'🤔'});
  card(60,230,600,100,'Star OFF + Delta ON',[T(2,1),PS(3)]);
  card(60,360,290,110,'Smooth?',[T(2,2),PS(3)],{bg:GRN,size:36});card(370,360,290,110,'Flash, trip?',[T(2,3),PS(3)],{bg:RED,size:30});
  wipe(PS(3));presenter([PS(3),END],{poses:EP10_SPOSE,x:-20,y:850,size:430});
  card(60,100,600,120,'Guess-ai COMMENT!',[PS(3),END],{emoji:'💬',bg:'#dbeafe'});
  card(60,260,600,110,'Answer ↓ full video',[T(3,1),END]);
  card(60,410,290,100,'LIKE',[T(3,2),END],{bg:NG.blue,emoji:'👍',size:34});card(370,410,290,100,'SHARE',[T(3,3),END],{bg:NG.teal,emoji:'↗️',size:34});
  card(110,560,500,120,'SUBSCRIBE',[T(3,4),END],{bg:RED,emoji:'🔔',size:44});
  o2schedule(s);S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
