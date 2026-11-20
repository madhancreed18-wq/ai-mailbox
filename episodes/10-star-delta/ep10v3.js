/* ---------- EP10 v3 – Star-Delta on the real 3D stage ----------
   Main visual = g3 'sdstage' (state + camera follow the narration). Ladder parts: rungs on the left, live 3D inset.
   Presenter small bottom-left, lip-synced all the time. Ravi / Kumar only at their action moments. Small state chip, no captions. */
async function buildEp10v3(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('16:9');S.narrOff=0;S.art='sketch';
  try{await document.fonts.load('700 30px InkHand')}catch(_){}
  const A=EP10_A,END=309.6;
  const s=newScene({name:'EP10 v3 – Star-Delta (3D)',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep10Kit(s,A,END),{ng,T,PS,card,bit,actor,presenter,RUNG}=K,RED=NG.red,GRN=NG.grn,BLU=NG.blue,PUR='#7c3aed',ORG='#f59e0b';
  const P=(a,b=a)=>[PS(a),b>=27?END:PS(b+1)];
  const chip=(t,win,bg=NG.navy)=>card(28,22,Math.min(520,60+t.length*17),62,t,win,{bg,size:28});
  /* ---- state sequence + camera for the main 3D stage ---- */
  const seq=[[0,'off'],[T(0,3)+.8,'dol'],[T(0,6),'trip'],[T(6,1),'star'],[T(6,5),'gap'],[T(6,7),'delta'],[T(23,0)+.6,'trip'],
    [PS(24),'star'],[PS(24)+4,'gap'],[PS(24)+4.12,'delta'],[T(26,3)+1,'short'],[T(26,4)+1.2,'trip'],[PS(27),'star'],[PS(27)+3,'gap'],[PS(27)+3.12,'delta']];
  const cams=[[0,'wide'],[T(0,3),'panel'],[T(0,4),'ammeter'],[T(0,5),'light'],[T(0,6),'wide'],[PS(1),'wide'],[PS(2),'panel'],[T(2,1),'km'],[PS(3),'motor'],[PS(4),'wide'],
    [PS(6),'panel'],[T(6,1),'km'],[T(6,2),'motor'],[T(6,3),'light'],[T(6,4),'ammeter'],[T(6,5),'km'],[T(6,8),'motor'],[PS(7),'km'],
    [PS(16),'wide'],[PS(22),'km'],[PS(23),'light'],[T(23,1),'wide'],[PS(24),'motor'],[T(24,1),'ammeter'],[T(24,3),'motor'],[PS(25),'wide'],
    [PS(26),'km'],[T(26,5),'wide'],[PS(27),'motor'],[T(27,2),'wide']];
  const stage=win=>ng('g3',{shot:'sdstage',x:0,y:0,w:W,h:H,noPop:true,seq,cams},win);
  stage([0,PS(8)]);stage([PS(16),PS(21)]);stage([PS(22),END]);
  /* ---- ladder section: live 3D inset (top-right) ---- */
  const run0=T(15,1)+1.2,tD=run0+3,tG=tD+.6;
  const iseq=[[0,'off'],[PS(8),'star'],[PS(8)+3,'gap'],[PS(8)+3.12,'delta'],[run0-1,'off'],[run0,'star'],[tD,'gap'],[tG,'delta']];
  ng('g3',{shot:'sdstage',x:930,y:90,w:330,h:186,rr:16,frame:'#1f2430',noPop:true,seq:iseq,cams:[[0,'wide']]},[PS(8),PS(16)]);
  ng('g3',{shot:'sdstage',x:930,y:90,w:330,h:186,rr:16,frame:'#1f2430',noPop:true,seq:[[0,'delta']],cams:[[0,'km']]},[PS(21),PS(22)]);
  /* k0 HOOK */
  presenter([0,END],{size:330,x:-20,y:H-336});
  chip('Veetu motor → light dim?',[0,T(0,2)]);chip('30 HP – DIRECT START',[T(0,3),T(0,6)],RED);chip('TRIP!',[T(0,6),PS(1)],RED);
  actor('worker',[[0,'op_press_start'],[T(0,5),'op_lights_dim'],[T(0,7),'op_cover_ears']],[T(0,2),PS(1)],{x:930,size:320,y:H-330});
  /* k1 INTRO */
  chip('STAR – DELTA STARTER',P(1),ORG);
  actor('tech',[[0,'tc_all_ok']],[T(1,1),PS(2)],{x:930,size:320,y:H-330});
  card(760,110,470,80,'FX3U + timer',[T(1,2),PS(2)]);card(760,210,470,80,'Quiz – answer kadaisila',[T(1,3),PS(2)],{bg:'#fef3c7'});
  /* k2–k3 PANEL / TERMINALS */
  chip('PANEL',[PS(2),T(2,1)]);chip('KM1 MAIN',[T(2,2),T(2,3)],BLU);chip('KM2 STAR',[T(2,3),T(2,4)],ORG);chip('KM3 DELTA',[T(2,4),T(2,5)],PUR);chip('OVERLOAD RELAY',[T(2,5),PS(3)]);
  chip('MOTOR TERMINALS',P(3));
  ['U1','V1','W1'].forEach((t,i)=>card(800+i*140,110,120,80,t,[T(3,2)+i*.4,PS(4)],{size:36}));['U2','V2','W2'].forEach((t,i)=>card(800+i*140,220,120,80,t,[T(3,3)+i*.4,PS(4)],{size:36,bg:'#fef3c7'}));
  /* k4–k5 STAR / DELTA diagram on a side board */
  card(740,40,510,560,'',P(4,5),{bg:'#ffffff'});
  ng('sdiag',{x:770,y:90,w:450,h:450,mode:'star',title:'STAR',vlab:'≈240 V',live:[[T(4,4),1]]},P(4));
  ng('sdiag',{x:770,y:90,w:450,h:450,mode:'delta',title:'DELTA',vlab:'415 V',live:[[T(5,0)+1,1]]},P(5));
  chip('STAR: ⅓ current, mella start',[T(4,3),PS(5)],ORG);chip('DELTA: full power',P(5),PUR);
  /* k6 SEQUENCE */
  actor('worker',[[0,'op_press_start'],[T(6,2),'op_wait_watch'],[T(6,8),'op_thumbs_motor']],P(6),{x:930,size:320,y:H-330});
  chip('START',[PS(6),T(6,1)],GRN);chip('MAIN + STAR ON',[T(6,1),T(6,5)],ORG);chip('STAR OFF',[T(6,5),T(6,6)]);chip('GAP 0.1 s',[T(6,6),T(6,7)],RED);chip('DELTA ON – FULL SPEED',[T(6,7),PS(7)],PUR);
  /* k7 TIMER */
  actor('tech',[[0,'tc_clamp_meter'],[T(7,2),'tc_set_timer']],P(7),{x:930,size:320,y:H-330});
  chip('TIMER = motor start time',P(7));card(760,110,470,80,'Manual: 6 s+',[T(7,3),PS(8)],{bg:'#fef3c7'});
  /* k8 PLC I/O */
  chip('FX3U  I/O',P(8));
  [['X0','Start'],['X1','Stop'],['X2','Overload']].forEach(([a,b],i)=>card(360,110+i*100,260,80,a+' · '+b,[T(8,2+i),PS(9)],{bg:'#dbeafe'}));
  [['Y0','Main'],['Y1','Star'],['Y2','Delta']].forEach(([a,b],i)=>card(650,110+i*100,260,80,a+' · '+b,[T(8,6+i),PS(9)],{bg:'#dcfce7'}));
  /* k9 RUNG 1 */
  chip('RUNG 1 · SELF-HOLDING',P(9),NG.teal);
  const st1=[[T(9,4),1],[T(9,5),0]],m0=[[T(9,4)+.2,1],[T(9,6)+1,0]];
  ng('rung',{drawOn:true,x:360,y:200,w:540,h:130,num:'1',items:[{k:'NO',label:'X0 START',on:st1,par:{label:'M0',on:m0}},{k:'NC',label:'X1 STOP',on:[[0,1],[T(9,6)+1,0]]},{k:'NC',label:'X2 OL',on:[[0,1]]},{k:'COIL',label:'M0 RUN',on:m0}],power:[[T(9,4),1],[T(9,6)+1,0]]},P(9));
  /* k10 why not SET/RESET */
  chip('SET/RESET? Inga thevai illa',P(10),PUR);
  card(360,140,260,140,'SET / RESET',[T(10,1),PS(11)],{strike:T(10,2)});card(650,140,260,140,'Self-holding',[T(10,2),PS(11)],{bg:'#ccfbf1',tick:T(10,3)});
  /* k11–k15 RUNGS 2–6 (with live run) */
  const M0=[[run0,1]],T0d=[[tD,1]],Y1=[[run0,1],[tD,0]],T1d=[[tG,1]],Y2=[[tG,1]];
  chip('RUNGS 2 – 6',[PS(11),run0-.4],NG.navy);chip('LIVE RUN: STAR → GAP → DELTA',[run0-.4,PS(16)],GRN);
  RUNG(360,70,540,[{k:'NO',label:'M0',on:M0},{k:'COIL',label:'Y0 MAIN',on:M0}],[PS(11),PS(16)],{num:'2',power:M0});
  RUNG(360,165,540,[{k:'NO',label:'M0',on:M0},{k:'COIL',label:'T0 K80 (8 s)',on:T0d}],[PS(12),PS(16)],{num:'3',power:M0});
  RUNG(360,260,540,[{k:'NO',label:'M0',on:M0},{k:'NC',label:'T0',on:[[0,1],[tD,0]]},{k:'NC',label:'Y2',on:[[0,1],[tG,0]]},{k:'COIL',label:'Y1 STAR',on:Y1}],[PS(13),PS(16)],{num:'4',power:Y1});
  RUNG(360,355,540,[{k:'NO',label:'T0',on:T0d},{k:'COIL',label:'T1 K1 (0.1 s)',on:T1d}],[PS(14),PS(16)],{num:'5',power:T0d});
  RUNG(360,450,540,[{k:'NO',label:'T1',on:T1d},{k:'NC',label:'Y1',on:[[0,1],[run0,0],[tD,1]]},{k:'COIL',label:'Y2 DELTA',on:Y2}],[PS(15),PS(16)],{num:'6',power:Y2});
  /* k16–k20 QUIZ */
  chip('QUIZ 🎯',[PS(16),PS(21)],ORG);
  actor('worker',[[0,'op_ask']],P(16),{x:930,size:320,y:H-330});
  card(760,110,470,90,'Gap timer illaama?',[T(16,2),PS(17)],{bg:'#fef3c7'});
  [['A','Smooth-aa Delta-ku',GRN],['B','Short circuit · flash, trip',RED],['C','Reverse-la odum',BLU]].forEach(([l,t,c],i)=>{card(700,110+i*110,90,90,l,[PS(17+i),PS(21)],{bg:c,size:44});card(800,110+i*110,450,90,t,[PS(17+i)+.3,PS(21)])});
  card(700,450,550,80,'Comment pannunga!',[PS(20),PS(21)],{bg:'#dbeafe'});
  /* k21 SOFTWARE INTERLOCK */
  chip('INTERLOCK',P(21),PUR);
  RUNG(360,150,540,[{k:'NO',label:'M0'},{k:'NC',label:'T0'},{k:'NC',label:'Y2 ◀'},{k:'COIL',label:'Y1 STAR'}],[T(21,2),PS(22)],{num:'4'});
  RUNG(360,300,540,[{k:'NO',label:'T1'},{k:'NC',label:'Y1 ◀'},{k:'COIL',label:'Y2 DELTA'}],[T(21,3),PS(22)],{num:'6'});
  /* k22 HARDWARE INTERLOCK */
  chip('HARDWARE INTERLOCK',P(22),RED);
  actor('tech',[[0,'tc_point_contactors'],[T(22,1),'tc_check_interlock']],P(22),{x:930,size:320,y:H-330});
  card(760,110,470,80,'Contact WELD → stuck',[T(22,2),PS(23)],{bg:'#fee2e2'});card(760,210,470,80,'Aux NC interlock',[T(22,4),PS(23)],{bg:'#dcfce7',tick:T(22,4)+1.2});
  /* k23 POWER CUT */
  chip('POWER CUT',[PS(23),T(23,2)],'#111827');chip('NO AUTO START ✓',[T(23,2),PS(24)],GRN);
  actor('worker',[[0,'op_wait_watch'],[T(23,3),'op_press_start']],P(23),{x:930,size:320,y:H-330});
  /* k24 MISTAKES */
  chip('TIMER kammi → current spike',[T(24,1),T(24,3)],RED);chip('TIMER adhigam → motor heat',[T(24,3),T(24,4)],RED);chip('OVERLOAD = motor FLC',[T(24,4),PS(25)],BLU);chip('COMMON MISTAKES',[PS(24),T(24,1)],RED);
  /* k25 SUMMARY */
  chip('SUMMARY',P(25));['Star → mella start','Timer → gap','Delta → full power','Interlock: soft + hard','Power cut → no auto start'].forEach((t,i)=>card(800,100+i*90,440,74,t,[T(25,1+i),PS(26)],{tick:T(25,1+i)+.6}));
  /* k26 ANSWER */
  chip('ANSWER',[PS(26),T(26,4)],ORG);chip('SHORT CIRCUIT!',[T(26,4),T(26,5)],RED);chip('ANSWER: B',[T(26,5),PS(27)],NG.navy);
  /* k27 CTA */
  chip('NEXT: FORWARD / REVERSE',[T(27,1),END],PUR);
  card(800,130,420,90,'LIKE',[T(27,2),END],{bg:BLU,emoji:'👍',size:40});card(800,240,420,90,'SHARE',[T(27,3),END],{bg:NG.teal,emoji:'↗️',size:40});card(800,350,420,100,'SUBSCRIBE',[T(27,4),END],{bg:RED,emoji:'🔔',size:44});
  S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
