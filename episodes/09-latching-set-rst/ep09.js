/* ---------- EP09 – What is Latching in PLC? SET/RST vs Holding (Factory Decode Tamil) ----------
   Hybrid: real 3D shots (g3: lift, switches, FX3U-32MR/ES, mixie) + 2.5D ladder graphics + office stickman at key moments.
   5 guess beats with a 3-second ring, DECODE MOMENT (FX3U X-ray + scan), comment challenge mid-video, answer at the end.
   Timing: sentences placed inside ChatGPT's measured paragraph times (mailbox 039) – EP09_A / EP09_SA. */
const EP09_A=__EP09_A__;
const EP09_SA=__EP09_SA__;
function ep09Kit(s,A,END){const K=fdtKit(s,A),{ng}=K;
  const g3=(shot,o,win)=>ng('g3',{shot,x:0,y:0,w:W,h:H,noPop:true,...o},win);
  const ring=(t0,t1,o={})=>ng('count3',{x:(o.cx??1150)-60,y:(o.cy??120)-60,w:120,h:120,t0,t1,noPop:true,label:o.label||'3 SEC GUESS'},[t0-.15,t1+.9]);
  const host=(win,beats,o={})=>{const h=addStick({scene:s,quiet:true,look:'office',action:beats[0][1],size:o.size||300,x:o.x??10,y:o.y??(H-(o.size||300)-6),facing:1,entrance:'pop',delay:0,withPrev:true,draw:.3,name:'Host'});h.win=win;h.beats=beats.map(([t,pose])=>({t,pose,blend:.35}));h.speak=[[0,END]];return h};
  const card=(x,y,w,h,head,lines,col,win,o={})=>ng('box',{x,y,w,h,head,color:col,lines,lh:o.lh||40,align:o.align||'center',d3:true},win);
  const big=(text,cx,cy,win,o={})=>ng('label',{x:cx-(o.w??900)/2,y:cy-30,w:o.w??900,h:60,text,size:o.size||64,color:o.color||NG.navy},win);
  return{...K,g3,ring,host,card,big};
}
async function buildEp09(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('16:9');S.narrOff=0;
  const A=EP09_A,END=354.2;
  const s=newScene({name:'EP09 – What is Latching in PLC? SET/RST vs Holding',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep09Kit(s,A,END),{ng,T,PS,pill,label,box,g3,ring,host,card,big,seg,lamp}=K;
  const RED='#e5484d',PUR='#7c3aed',W_=(p,q=p)=>[PS(p),q>=27?END:PS(q+1)],P=W_,E=p=>A.filter(a=>a[2]===p).slice(-1)[0][1];
  s.els.push({id:uid++,type:'ngd',kind:'mg',mg:'floor',name:'floor',x:-200,y:0,w:1680,h:720,hz:430,vx:.5,draw:.1,delay:0,withPrev:true,entrance:'none',motion:'none',noPop:true,win:[0,END]});
  const flash=t=>ng('flash',{x:0,y:0,w:W,h:H,noPop:true},[t,t+.45]);

  /* 1 HOOK – 3D lift (0 – P2) */
  g3('lift',{press:.55,arrive:T(0,3)+.3,zoom:[T(0,4),T(0,4)+1.4]},P(0));
  pill('BUTTON-AI VITTAACHU… LIGHT ON?',640,24,[T(0,4),PS(1)],{w:620,bg:RED,size:26});
  /* 2 TITLE – latching + "3 sec guess" promise */
  flash(PS(1));big('LATCHING',640,250,P(1),{size:110});label('PLC-la "NYAABAGAM VECHUKKURA" VELAI',640,340,[T(1,1),PS(2)],{w:900,size:30,color:NG.org});
  ng('count3',{x:580,y:420,w:120,h:120,t0:T(1,2),t1:T(1,2)+3,noPop:true,label:'3 SEC-LA GUESS!'},[T(1,2)-.1,PS(2)]);
  /* 3–4 DOORBELL vs FAN – 3D switches */
  g3('switches',{bell:[[T(3,1)+.2,T(3,1)+2.2]],fan:[[T(3,4)+.3,1e9]],focus:[[PS(2),0],[T(3,1),-1],[T(3,4),1],[T(3,5)+.8,0]]},[PS(2),PS(4)]);
  pill('ENDHA SWITCH ON-LA IRUKKUM?',640,24,P(2),{w:560,bg:NG.navy,size:26});ring(T(2,3),E(2));
  pill('MOMENTARY',380,24,[T(3,3),PS(4)],{w:300,bg:NG.org});pill('MAINTAINED',900,24,[T(3,5),PS(4)],{w:300,bg:NG.teal});
  /* 5 FACTORY BUTTONS → PLC = FAN SWITCH */
  flash(PS(4));pill('FACTORY BUTTONS = DOORBELL MAADHIRI',640,24,P(4),{w:640,bg:NG.navy,size:26});
  ng('title',{x:90,y:200,w:220,h:90,text:'▶ START',size:34,bg:NG.grn},[T(4,0),PS(5)]);ng('title',{x:90,y:330,w:220,h:90,text:'■ STOP',size:34,bg:RED},[T(4,0)+.3,PS(5)]);
  seg(330,290,560,290,[T(4,1),PS(5)],{color:NG.ink,lw:6,head:true});
  g3('fx3u',{x:580,y:120,w:660,h:372,rr:18,frame:'#cbd5e1',leds:{X0:[[T(4,1),1],[T(4,1)+.6,0]],Y0:[[T(4,1)+.1,1]]},cam:[[0,'front']]},[T(4,1),PS(5)]);
  ng('title',{x:640,y:520,w:540,h:60,text:'PLC = "FAN SWITCH" VELAI',size:28,bg:NG.teal},[T(4,2),PS(5)]);ng('title',{x:740,y:600,w:340,h:52,text:'2 VAZHI',size:28,bg:NG.org},[T(4,3),PS(5)]);
  /* 6 HOLDING LOGIC rung */
  flash(PS(5));pill('VAZHI 1 · HOLDING LOGIC (SEAL-IN)',640,24,P(5),{w:620,bg:NG.teal,size:26});
  const X0p=[[T(5,1),1],[T(5,3)+.3,0]],Y0h=[[T(5,1)+.25,1]];
  ng('rung',{x:300,y:230,w:760,h:120,num:'1',items:[{k:'NO',label:'START X0',on:X0p,par:{label:'Y0',on:Y0h}},{k:'NC',label:'STOP',on:[[0,1]]},{k:'COIL',label:'Y0',on:Y0h}],power:[[T(5,1),1]],sweep:[T(5,1),T(5,1)+1]},[T(5,0),PS(6)]);
  ng('title',{x:380,y:470,w:580,h:56,text:'X0 VITTAALUM · Y0 THANNAIYE PIDICHUKKUDHU',size:22,bg:NG.grn},[T(5,3),PS(6)]);
  ng('title',{x:440,y:560,w:460,h:50,text:'DOL STARTER SEAL-IN = IDHE DHAAN',size:22,bg:NG.navy},[T(5,5),PS(6)]);
  /* 7 SET / RST rungs */
  flash(PS(6));pill('VAZHI 2 · SET / RST',640,24,P(6),{w:420,bg:PUR});
  const Y0s=[[T(6,1)+.2,1],[T(6,4)+.4,0]];
  ng('rung',{x:300,y:200,w:700,h:80,num:'1',items:[{k:'NO',label:'X0',on:[[T(6,1),1],[T(6,2),0]]},{k:'SET',label:'Y0',on:Y0s}],power:[[T(6,1),1],[T(6,2),0]]},[T(6,0),PS(7)]);
  ng('rung',{x:300,y:380,w:700,h:80,num:'2',items:[{k:'NO',label:'X1',on:[[T(6,4),1],[T(6,4)+1.2,0]]},{k:'RST',label:'Y0',on:[[T(6,4),1],[T(6,4)+1.2,0]]}],power:[[T(6,4),1],[T(6,4)+1.2,0]]},[T(6,3),PS(7)]);
  lamp(1130,300,90,Y0s[0][0],[T(6,0),PS(7)],{color:NG.grn,text:'Y0',onEnd:Y0s[1][0]});
  ng('title',{x:380,y:540,w:520,h:52,text:'X0 VITTAALUM Y0 ON · RST VARUM VARAIKKUM',size:21,bg:PUR},[T(6,2),PS(7)]);
  /* 8 GUESS – lift: SET or RST? */
  flash(PS(7));g3('lift',{x:40,y:110,w:620,h:349,rr:18,frame:'#cbd5e1',press:T(7,1),arrive:T(7,2)+.6},P(7));
  ng('title',{x:700,y:170,w:520,h:70,text:'BUTTON PRESS = SET? RST?',size:26,bg:NG.navy},[T(7,1),PS(8)]);ng('title',{x:700,y:270,w:520,h:70,text:'LIFT VANDHADHU = SET? RST?',size:26,bg:NG.navy},[T(7,2),PS(8)]);
  ring(T(7,3),E(7),{cx:960,cy:450});
  /* 9 REVEAL */
  g3('lift',{x:40,y:110,w:620,h:349,rr:18,frame:'#86efac',press:T(8,0),arrive:T(8,1)+.4},P(8));
  ng('title',{x:700,y:170,w:520,h:70,text:'PRESS = SET ✓',size:30,bg:NG.grn},[T(8,0),PS(9)]);ng('title',{x:700,y:270,w:520,h:70,text:'LIFT VANDHADHU = RST ✓',size:30,bg:PUR},[T(8,1),PS(9)]);
  /* 10 SAME…BUT 2 DIFFERENCES */
  flash(PS(9));card(140,170,440,260,'HOLDING',[{t:'button vittaalum ON'}],NG.teal,P(9));card(700,170,440,260,'SET / RST',[{t:'button vittaalum ON'}],PUR,P(9));
  big('≠',640,300,[T(9,1),PS(10)],{w:120,size:96,color:RED});ng('title',{x:420,y:520,w:440,h:60,text:'2 MUKKIYA DIFFERENCE',size:28,bg:RED},[T(9,2),PS(10)]);
  /* 11 DIFFERENCE 1 – where is the RST? */
  flash(PS(10));pill('DIFFERENCE 1 · RST ENGA?',640,24,P(10),{w:480,bg:NG.navy});
  card(90,120,500,300,'HOLDING · 1 RUNG',[{t:'Start · Stop · Coil',size:24},{t:'orey idathula ✓',size:24,color:NG.grn}],NG.teal,[T(10,1),PS(11)]);
  card(690,120,240,170,'PAGE 1',[{t:'SET Y0',size:26}],PUR,[T(10,3),PS(11)]);card(980,250,240,170,'PAGE 7',[{t:'RST Y0',size:26}],PUR,[T(10,3)+.5,PS(11)]);
  ng('title',{x:700,y:480,w:520,h:56,text:'🔍 FAULT FIND: RST-AI THEDANUM',size:22,bg:RED},[T(10,4),PS(11)]);
  /* 12 GUESS – SET + RST together */
  flash(PS(11));pill('SET + RST ORE NERATHULA TRUE?',640,24,P(11),{w:560,bg:NG.navy,size:26});
  const both=[[T(11,0),1]];
  ng('rung',{x:240,y:200,w:640,h:80,num:'1',items:[{k:'NO',label:'X0',on:both},{k:'SET',label:'Y0',on:both}],power:both},P(11));
  ng('rung',{x:240,y:380,w:640,h:80,num:'2',items:[{k:'NO',label:'X1',on:both},{k:'RST',label:'Y0',on:both}],power:both},P(11));
  ng('title',{x:960,y:250,w:240,h:70,text:'Y0 = ?',size:36,bg:RED},[T(11,1),PS(12)]);ring(T(11,2),E(11),{cx:1080,cy:470});
  /* 13 DECODE MOMENT – FX3U X-ray + scan, then the program scan */
  flash(PS(12));g3('fx3u',{x:0,y:80,w:700,h:394,rr:0,leds:{X0:both,X1:both,Y0:[[0,0]]},xray:[T(12,0),T(12,4)+1],cam:[[0,'front']]},P(12));
  ng('title',{x:380,y:16,w:520,h:64,text:'⚡ DECODE MOMENT',size:34,bg:'#0ea5e9'},[T(12,0),T(12,0)+4]);
  pill('PROGRAM: MELA → KEEZHA SCAN',640,24,[T(12,0)+4,PS(13)],{w:560,bg:'#0ea5e9',size:26});
  ng('rung',{x:760,y:200,w:440,h:80,num:'1',items:[{k:'NO',label:'X0',on:both},{k:'SET',label:'Y0',on:both}],power:both,sweep:[T(12,2),T(12,2)+1.6]},[T(12,1),PS(13)]);
  ng('rung',{x:760,y:360,w:440,h:80,num:'2',items:[{k:'NO',label:'X1',on:both},{k:'RST',label:'Y0',on:both}],power:both,sweep:[T(12,3),T(12,3)+1.6]},[T(12,1),PS(13)]);
  ng('title',{x:780,y:480,w:400,h:56,text:'Y0 IMAGE = 1',size:26,bg:NG.grn},[T(12,2)+1.2,T(12,3)+1.2]);ng('title',{x:780,y:480,w:400,h:56,text:'Y0 IMAGE = 0',size:26,bg:RED},[T(12,3)+1.2,PS(13)]);
  ng('title',{x:760,y:570,w:440,h:56,text:'SCAN END → OUTPUT UPDATE',size:22,bg:NG.navy},[T(12,4),PS(13)]);
  ng('title',{x:120,y:560,w:480,h:60,text:'KEEZHA IRUKKURADHU JEYIKKUM',size:24,bg:RED},[T(12,5),PS(13)]);ng('title',{x:150,y:640,w:420,h:52,text:'STOP PRIORITY → RST KEEZHA',size:22,bg:NG.teal},[T(12,7),PS(13)]);
  /* 14–18 COMMENT CHALLENGE (answer at the end) */
  flash(PS(13));pill('💬 CHALLENGE · ANSWER VIDEO KADAISILA',640,24,[PS(13),PS(18)],{w:700,bg:NG.org,size:26});
  const sw=[[T(13,3),1]];
  ng('rung',{x:330,y:170,w:600,h:70,num:'1',items:[{k:'NO',label:'X1',on:sw},{k:'RST',label:'Y0',on:sw}],power:sw},[T(13,3),PS(18)]);
  ng('rung',{x:330,y:310,w:600,h:70,num:'2',items:[{k:'NO',label:'X0',on:sw},{k:'SET',label:'Y0',on:sw}],power:sw},[T(13,3)+.3,PS(18)]);
  ng('title',{x:960,y:220,w:250,h:64,text:'RST MELA ↑',size:24,bg:RED},[T(13,4),PS(18)]);ng('title',{x:960,y:330,w:250,h:64,text:'SET KEEZHA ↓',size:24,bg:NG.grn},[T(13,4)+.3,PS(18)]);
  [['A','Y0 ON aagum',NG.grn],['B','Y0 OFF-la irukkum',RED],['C','ON / OFF maarum',NG.blue]].forEach(([l,t,c],i)=>{ng('title',{x:330+i*300,y:470,w:70,h:70,text:l,size:40,bg:c},[PS(14+i),PS(18)]);ng('box',{x:405+i*300,y:470,w:205,h:70,color:c,lines:[{t,size:20}],d3:true},[PS(14+i),PS(18)])});
  ng('title',{x:380,y:580,w:520,h:64,text:'💬 IPPOVE COMMENT: A/B/C + REASON',size:24,bg:NG.navy},[PS(17),PS(18)]);
  /* 19–20 MIXIE – power cut, restarts by itself */
  flash(PS(18));g3('mixie',{run:[[T(18,1)-1,1e9]],cut:[[T(18,2),T(19,0)]],knobOn:[[0,1e9]]},[PS(18),PS(20)]);
  pill('POWER CUT!',640,24,[T(18,2),T(19,0)],{w:300,bg:'#111827'});ring(T(18,4),E(18),{cx:1120,cy:130});
  flash(T(19,0));pill('⚠ MIXIE THAANAA ODUDHU!',640,24,[T(19,0),PS(20)],{w:520,bg:RED,size:28});
  /* 21 FX3U memory – general vs latched, BATT */
  flash(PS(20));pill('FX3U MEMORY',640,24,P(20),{w:340,bg:NG.navy});
  g3('fx3u',{x:620,y:110,w:640,h:360,rr:18,frame:'#cbd5e1',cam:[[0,'front'],[T(20,4),'batt']],xray:[T(20,4)+.6,PS(21)],leds:{}},P(20));
  card(60,130,500,150,'M0 – M499 · GENERAL',[{t:'Power pona → CLEAR',size:24}],'#64748b',[T(20,0),PS(21)]);
  card(60,320,500,150,'M500 – M1023 · LATCHED',[{t:'Battery → NYAABAGAM ✓',size:24,color:PUR}],PUR,[T(20,2),PS(21)]);
  ng('title',{x:120,y:540,w:400,h:56,text:'🔋 BATT LIGHT + BATTERY',size:24,bg:PUR},[T(20,4),PS(21)]);
  /* 22 GUESS – SET M500 → motor, after power cut? */
  flash(PS(21));pill('SET M500 → MOTOR Y0',640,24,P(21),{w:420,bg:PUR});
  const m5=[[T(21,1),1]];
  ng('rung',{x:200,y:190,w:600,h:80,num:'1',items:[{k:'NO',label:'X0',on:[[T(21,1),1],[T(21,1)+1,0]]},{k:'SET',label:'M500',on:m5}],power:[[T(21,1),1],[T(21,1)+1,0]]},P(21));
  ng('rung',{x:200,y:360,w:600,h:80,num:'2',items:[{k:'NO',label:'M500',on:m5},{k:'COIL',label:'Y0 MOTOR',on:[[T(21,1),1],[T(21,2),0]]}],power:[[T(21,1),1],[T(21,2),0]]},[T(21,1)+.5,PS(22)]);
  ng('title',{x:860,y:200,w:360,h:64,text:'⚡ POWER CUT → BACK',size:24,bg:'#111827'},[T(21,2),PS(22)]);ng('title',{x:860,y:300,w:360,h:64,text:'MOTOR ODUMAA?',size:28,bg:RED},[T(21,4),PS(22)]);
  ring(T(21,5),E(21),{cx:1040,cy:480});
  /* 23 DANGER – restarts by itself */
  g3('fx3u',{leds:{POWER:[[0,1],[PS(22),0],[T(22,0)+.6,1]],RUN:[[0,1],[PS(22),0],[T(22,1),1]],Y0:[[T(22,1)+.4,1]]},dim:[[0,0],[PS(22),1],[T(22,0)+.6,0]],cam:[[0,'front'],[T(22,1),'leds']]},P(22));
  ng('flash',{x:0,y:0,w:W,h:H,noPop:true,color:RED},[T(22,3),T(22,3)+.6]);pill('⚠ DANGER · YAARUM START PRESS PANNALA',640,24,[T(22,3),PS(23)],{w:720,bg:RED,size:26});
  /* 24 HOLDING is safe */
  flash(PS(23));pill('HOLDING LOGIC · POWER CUT-LA SAFE',640,24,P(23),{w:640,bg:NG.teal,size:26});
  const hy=[[0,1],[T(23,1),0]];
  ng('rung',{x:300,y:230,w:760,h:120,num:'1',items:[{k:'NO',label:'START X0',on:[[0,0]],par:{label:'Y0',on:hy}},{k:'NC',label:'STOP',on:[[0,1]]},{k:'COIL',label:'Y0',on:hy}],power:hy},P(23));
  ng('title',{x:380,y:470,w:580,h:56,text:'POWER CUT → Y0 OFF · SEAL BREAK',size:24,bg:'#111827'},[T(23,1),PS(24)]);
  ng('title',{x:380,y:550,w:580,h:56,text:'START PRESS PANNA DHAAN ODUM ✓',size:24,bg:NG.grn},[T(23,2),PS(24)]);
  ng('title',{x:380,y:630,w:580,h:52,text:'MOTOR · CONVEYOR · PUMP = HOLDING',size:22,bg:NG.teal},[T(23,4),PS(24)]);
  /* 25 when SET/RST is right */
  flash(PS(24));pill('SET / RST THAPPA? ILLA!',640,24,P(24),{w:460,bg:PUR});
  [['🔔 ALARM LATCH',T(24,3)],['📦 BATCH RUNNING',T(24,3)+.6],['⚠ FAULT MESSAGE (ACK)',T(24,3)+1.2]].forEach(([t,a],i)=>ng('title',{x:120+i*360,y:160,w:330,h:70,text:t,size:22,bg:PUR},[a,PS(25)]));
  ng('title',{x:240,y:320,w:800,h:72,text:'✗ MOTOR-AI LATCHED BIT-LA SET PANNAADHEENGA',size:26,bg:RED},[T(24,4),PS(25)]);
  ng('title',{x:340,y:440,w:600,h:60,text:'POWER RETURN-LA ENNA AAGUM? CHECK ✓',size:22,bg:NG.navy},[T(24,5),PS(25)]);
  /* 26 SUMMARY */
  flash(PS(25));pill('QUICK SUMMARY',640,24,P(25),{w:340,bg:NG.navy});
  card(70,140,360,300,'HOLDING',[{t:'Power cut → OFF'},{t:'Motor-ku SAFE ✓',color:NG.grn}],NG.teal,[T(25,1),PS(26)]);
  card(460,140,360,300,'SET / RST',[{t:'Thani RST venum'},{t:'Keezha jeyikkum'}],PUR,[T(25,2),PS(26)]);
  card(850,140,360,300,'LATCHED M500',[{t:'Power cut-ku'},{t:'appuram-um ON',color:RED}],RED,[T(25,3),PS(26)]);
  /* 27 ANSWER REVEAL */
  flash(PS(26));pill('CHALLENGE ANSWER',640,24,P(26),{w:400,bg:NG.org});
  const sw2=[[T(26,2),1]];
  ng('rung',{x:280,y:180,w:640,h:80,num:'1',items:[{k:'NO',label:'X1',on:sw2},{k:'RST',label:'Y0',on:sw2}],power:sw2,sweep:[T(26,3),T(26,3)+1.6]},P(26));
  ng('rung',{x:280,y:350,w:640,h:80,num:'2',items:[{k:'NO',label:'X0',on:sw2},{k:'SET',label:'Y0',on:sw2}],power:sw2,sweep:[T(26,3)+1.8,T(26,3)+3.4]},P(26));
  ng('title',{x:980,y:180,w:240,h:70,text:'A ✓ Y0 ON',size:32,bg:NG.grn},[T(26,5),PS(27)]);
  ng('title',{x:300,y:500,w:680,h:64,text:'"RST EPPOVUM JEYIKKUM" ✗  ORDER DHAAN RULE ✓',size:24,bg:NG.navy},[T(26,7),PS(27)]);
  /* 28 END */
  flash(PS(27));big('🎉 CORRECT-AA SONNAVANGALUKKU SHOUT-OUT',700,170,P(27),{size:34,w:1000});
  ng('title',{x:420,y:260,w:560,h:70,text:'NEXT: TIMER + LATCH = MACHINE',size:28,bg:NG.teal},[T(27,1),END]);
  ng('title',{x:420,y:380,w:270,h:70,text:'👍 LIKE',size:30,bg:NG.blue},[T(27,2),END]);ng('title',{x:710,y:380,w:270,h:70,text:'↗ SHARE',size:30,bg:NG.teal},[T(27,2)+.3,END]);
  ng('title',{x:530,y:480,w:340,h:76,text:'▶ SUBSCRIBE',size:34,bg:RED},[T(27,3),END]);
  /* office stickman – key moments only */
  host([0,PS(2)],[[0,'question'],[T(0,4),'scratchhead']]);
  host([T(7,3)-.3,PS(8)],[[0,'chinthink']],{x:1040,y:440,size:260});
  host([T(11,2)-.3,PS(12)],[[0,'chinthink']],{x:30,y:470,size:240});
  host([PS(13),PS(18)],[[0,'askviewer'],[PS(17),'count1']],{x:20,y:400,size:300});
  host([T(19,0),PS(20)],[[0,'worriedlook']],{x:20,y:420,size:280});
  host([T(21,5)-.3,PS(22)],[[0,'chinthink']],{x:1050,y:440,size:260});
  host([PS(27),END],[[0,'thumbsup'],[T(27,3),'wavebye']],{x:30,y:400,size:300});
  fdt25(s);S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
async function buildEp09Short(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('9:16');S.narrOff=0;
  const A=EP09_SA,END=37.6;
  const s=newScene({name:'EP09 Short – Lift button latching',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep09Kit(s,A,END),{ng,T,PS,pill,g3,ring,host,big}=K,RED='#e5484d',PUR='#7c3aed';
  s.els.push({id:uid++,type:'ngd',kind:'mg',mg:'floor',name:'floor',x:0,y:0,w:720,h:1280,hz:640,vx:.5,draw:.1,delay:0,withPrev:true,entrance:'none',motion:'none',noPop:true,win:[0,END]});
  g3('lift',{x:0,y:150,w:720,h:720,press:.4,arrive:9e9,zoom:[T(0,1),T(0,1)+1.2]},[0,PS(2)]);
  pill('BUTTON VITTAACHU… LIGHT ON?',360,40,[0,PS(1)],{w:620,h:70,bg:RED,size:30});ring(T(0,3),PS(1)-.2,{cx:360,cy:980,label:'3 SEC GUESS'});
  ng('flash',{x:0,y:0,w:720,h:1280,noPop:true},[PS(1),PS(1)+.45]);ng('title',{x:110,y:40,w:500,h:76,text:'⚡ DECODE MOMENT',size:36,bg:'#0ea5e9'},[T(1,0),T(1,0)+2.4]);
  g3('lift',{x:0,y:150,w:720,h:720,press:T(1,2),arrive:T(1,3)+.3},[PS(1),PS(2)]);
  ng('title',{x:110,y:900,w:500,h:76,text:'PRESS = SET',size:36,bg:NG.grn},[T(1,2),PS(2)]);ng('title',{x:110,y:1000,w:500,h:76,text:'LIFT VANDHADHU = RESET',size:30,bg:PUR},[T(1,3),PS(2)]);
  ng('title',{x:60,y:40,w:600,h:76,text:'PLC-LA IDHU LATCHING',size:34,bg:NG.navy},[T(1,1),PS(2)]);
  g3('fx3u',{x:0,y:200,w:720,h:540,leds:{POWER:[[0,1],[T(2,1),0],[T(2,1)+1.2,1]],RUN:[[0,1],[T(2,1),0],[T(2,1)+1.4,1]],Y0:[[T(2,1)+1.8,1]]},dim:[[0,0],[T(2,1),1],[T(2,1)+1.2,0]],cam:[[0,'leds']]},P2=[PS(2),PS(3)]);
  pill('⚠ POWER CUT-KU APPURAM?',360,40,P2,{w:620,h:76,bg:RED,size:32});ng('title',{x:80,y:800,w:560,h:80,text:'MACHINE THAANAA START!',size:32,bg:RED},[T(2,1)+1.8,PS(3)]);
  ng('title',{x:80,y:910,w:560,h:76,text:'FULL VIDEO ↓ LINKED',size:32,bg:NG.navy},[T(2,2),PS(3)]);
  ng('flash',{x:0,y:0,w:720,h:1280,noPop:true},[PS(3),PS(3)+.45]);big('FACTORY DECODE TAMIL',360,200,[PS(3),END],{w:660,size:42});
  ng('title',{x:200,y:330,w:320,h:84,text:'👍 LIKE',size:36,bg:NG.blue},[T(3,0),END]);ng('title',{x:200,y:450,w:320,h:84,text:'↗ SHARE',size:36,bg:NG.teal},[T(3,0)+.6,END]);ng('title',{x:200,y:570,w:320,h:90,text:'▶ SUBSCRIBE',size:38,bg:RED},[T(3,1),END]);
  host([0,PS(1)],[[0,'question'],[T(0,3),'chinthink']],{x:-10,y:860,size:400});host([PS(3),END],[[0,'thumbsup'],[T(3,1),'wavebye']],{x:-10,y:860,size:400});
  fdt25(s);S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
