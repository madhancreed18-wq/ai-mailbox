/* ================= EP09 v2 – SET / RESET (2D card design, v18) =================
   Flat 2D look (thick dark outline, soft shading, big outlined UI cards, emoji), one stage per topic,
   colour-stripe wipe transitions between topics, pop-in / pop-out on every card. */
const O2='#1f2430';
const o2t=(tl,t)=>{let v=0;(t||[]).forEach(([a,x])=>{if(tl>=a)v=x});return v},o2last=(tl,t)=>{let a=-1e9;(t||[]).forEach(([s])=>{if(tl>=s)a=s});return a},o2in=(w,t)=>(w||[]).some(([a,b])=>t>=a&&t<b);
const o2ease=k=>1-Math.pow(1-Math.max(0,Math.min(1,k)),3),o2back=k=>{k=Math.max(0,Math.min(1,k));const s=1.7;return 1+(s+1)*Math.pow(k-1,3)+s*Math.pow(k-1,2)};
function o2box(c,x,y,w,h,r,fill,lw=5,sh=true){c.save();if(sh){c.shadowColor='rgba(15,23,42,.18)';c.shadowBlur=18*curScale;c.shadowOffsetY=8*curScale}ngRR(c,x,y,w,h,r);c.fillStyle=fill;c.fill();c.restore();ngRR(c,x,y,w,h,r);c.lineWidth=lw;c.strokeStyle=O2;c.stroke()}
function o2emo(c,t,x,y,sz){c.save();c.font=`${sz}px "Noto Color Emoji","Apple Color Emoji",sans-serif`;c.textAlign='center';c.textBaseline='middle';c.fillText(t,x,y);c.restore()}
function drawCard2(e,c,tl){const{x,y,w,h}=e,bg=e.bg||'#fff',fg=e.fg||(bg==='#fff'?O2:'#fff');
  o2box(c,x,y,w,h,e.r??Math.min(26,h/3),bg,e.lw??5);
  if(e.band){ngRR(c,x,y,w,e.band.h||40,[e.r??22,e.r??22,0,0]);c.fillStyle=e.band.bg;c.fill();c.lineWidth=e.lw??5;c.strokeStyle=O2;c.beginPath();c.moveTo(x,y+(e.band.h||40));c.lineTo(x+w,y+(e.band.h||40));c.stroke();ngTxt(c,e.band.t,x+w/2,y+(e.band.h||40)/2+1,e.band.size||20,'#fff',800)}
  const by=e.band?(e.band.h||40):0,cy=y+by+(h-by)/2;
  if(e.emoji&&e.layout!=='col'){const es=e.esize||Math.min(h-by-14,64);o2emo(c,e.emoji,x+16+es/2,cy+2,es);ngTxt(c,e.text||'',x+32+es+(w-48-es)/2,cy+(e.sub?-12:1),e.size||Math.min(38,(h-by)*.45),fg,800);if(e.sub)ngTxt(c,e.sub,x+32+es+(w-48-es)/2,cy+20,e.ssize||18,e.scol||'#5b6475',700)}
  else if(e.emoji){const es=e.esize||64;o2emo(c,e.emoji,x+w/2,y+by+es/2+12,es);ngTxt(c,e.text||'',x+w/2,y+by+es+38,e.size||32,fg,800);if(e.sub)ngTxt(c,e.sub,x+w/2,y+by+es+70,e.ssize||18,e.scol||'#5b6475',700)}
  else{ngTxt(c,e.text||'',x+w/2,cy+(e.sub?-12:1),e.size||Math.min(44,(h-by)*.5),fg,800);if(e.sub)ngTxt(c,e.sub,x+w/2,cy+22,e.ssize||18,e.scol||'#5b6475',700)}
  if(e.strike!=null&&tl>=e.strike){const k=o2ease((tl-e.strike)/.35);c.save();c.lineWidth=9;c.strokeStyle=NG.red;c.lineCap='round';c.beginPath();c.moveTo(x+10,y+h-10);c.lineTo(x+10+(w-20)*k,y+h-10-(h-20)*k);c.stroke();c.restore()}
  if(e.tick!=null&&tl>=e.tick){const k=o2back((tl-e.tick)/.4);c.save();c.translate(x+w-6,y+6);c.scale(k,k);c.beginPath();c.arc(0,0,22,0,7);c.fillStyle=NG.grn;c.fill();c.lineWidth=4;c.strokeStyle=O2;c.stroke();c.strokeStyle='#fff';c.lineWidth=5;c.beginPath();c.moveTo(-9,0);c.lineTo(-2,8);c.lineTo(11,-8);c.stroke();c.restore()}}
function drawEmo2(e,c,tl){const a=tl-(e.win?e.win[0]:0),wob=Math.sin(a*9)*Math.exp(-a*2.2)*.25,s=1+Math.sin(a*5)*.04;c.save();c.translate(e.x+e.w/2,e.y+e.h/2);c.rotate(wob+(e.tilt||0));c.scale(s,s);o2emo(c,e.emoji,0,0,e.w*.9);c.restore()}
function drawWipe2(e,c,tl){const[a,b]=e.win,p=(tl-a)/(b-a),cols=e.cols||[NG.org,NG.navy,'#14b8a6'];c.save();
  cols.forEach((col,i)=>{const off=(i-1)*.09,x0=-W*1.3+(p+off)*W*2.9;c.beginPath();c.moveTo(x0,0);c.lineTo(x0+W*.9,0);c.lineTo(x0+W*.9-H*.35,H);c.lineTo(x0-H*.35,H);c.closePath();c.fillStyle=col;c.fill()});c.restore()}
function drawPhone2(e,c,tl){const{x,y,w,h}=e;o2box(c,x,y,w,h,42,'#2b3040',6);ngRR(c,x+16,y+40,w-32,h-80,24);const g=c.createLinearGradient(0,y,0,y+h);g.addColorStop(0,'#e0f2fe');g.addColorStop(1,'#f8fafc');c.fillStyle=g;c.fill();
  ngRR(c,x+w/2-40,y+16,80,12,6);c.fillStyle='#11141b';c.fill();ngTxt(c,'10:42',x+w/2,y+110,46,O2,800);
  // home icons
  const ic=[['💬','#22c55e'],['📷','#f59e0b'],['🎵','#ec4899'],['⚙️','#94a3b8']];ic.forEach(([em,col],i)=>{const ix=x+40+i*((w-80)/4)+((w-80)/8),iy=y+h-110;ngRR(c,ix-28,iy-28,56,56,14);c.fillStyle=col;c.fill();c.lineWidth=3;c.strokeStyle=O2;c.stroke();o2emo(c,em,ix,iy+1,30);
    if(i===0&&o2t(tl,e.notif)){c.beginPath();c.arc(ix+24,iy-24,13,0,7);c.fillStyle=NG.red;c.fill();c.lineWidth=3;c.strokeStyle='#fff';c.stroke();ngTxt(c,String(e.count?o2t(tl,e.count)||1:1),ix+24,iy-23,15,'#fff',800)}});
  // message envelope flying in
  (e.msg||[]).forEach(t0=>{const k=(tl-t0)/.7;if(k<0||k>1)return;const px=x-160+(w/2+160)*o2ease(k),py=y+160-Math.sin(k*Math.PI)*90;c.save();c.globalAlpha*=k<.85?1:(1-k)/.15;o2emo(c,'📩',px,py,64);c.restore()});
  // notification card
  const on=o2t(tl,e.notif),ts=o2last(tl,e.notif);let dx=0,dy=0,al=1;if(on){const k=o2back((tl-ts)/.45);dy=(1-k)*-140;al=Math.min(1,(tl-ts)/.15)}else{const k=(tl-ts)/.45;if(ts<-1e8||k>1)al=0;else{dx=o2ease(k)*w;al=1-k}}
  if(al>0){c.save();c.globalAlpha*=al;c.beginPath();ngRR(c,x+16,y+40,w-32,h-80,24);c.clip();const nx=x+26+dx,ny=y+170+dy,nw=w-52;o2box(c,nx,ny,nw,92,18,'#fff',4);ngRR(c,nx+12,ny+16,44,44,12);c.fillStyle='#22c55e';c.fill();o2emo(c,'💬',nx+34,ny+39,26);
    ngTxt(c,e.ntitle||'New message',nx+66,ny+30,19,O2,800,'left');ngTxt(c,e.ntext||'Hi! 👋 Call me',nx+66,ny+58,17,'#5b6475',700,'left');c.restore()}
  // finger swipe (clear)
  (e.swipe||[]).forEach(t0=>{const k=(tl-t0+.25)/.8;if(k<0||k>1)return;o2emo(c,'👆',x+60+o2ease(k)*(w-40),y+230,58)});
  // glow pulse when notification lands
  if(on&&tl-ts<.6){c.save();c.globalAlpha*=1-(tl-ts)/.6;c.lineWidth=8;c.strokeStyle='#38bdf8';ngRR(c,x-6,y-6,w+12,h+12,46);c.stroke();c.restore()}}
function drawPanel2(e,c,tl){const{x,y,w,h}=e,lamp=o2t(tl,e.lamp),flt=o2in(e.fault,tl),pr=o2in(e.press,tl);
  // tower lamp
  const tx=x+w*.78,ty=y-10;c.fillStyle='#9aa3b2';c.fillRect(tx-6,ty-40,12,40);c.lineWidth=4;c.strokeStyle=O2;c.strokeRect(tx-6,ty-40,12,40);
  if(lamp){const rg=c.createRadialGradient(tx,ty-80,10,tx,ty-80,120);rg.addColorStop(0,'rgba(255,70,70,.55)');rg.addColorStop(1,'rgba(255,70,70,0)');c.fillStyle=rg;c.beginPath();c.arc(tx,ty-80,120*(1+.06*Math.sin(tl*12)),0,7);c.fill()}
  ngRR(c,tx-26,ty-118,52,78,12);c.fillStyle=lamp?'#ff4545':'#7f1d1d';c.fill();c.lineWidth=4;c.strokeStyle=O2;c.stroke();ngRR(c,tx-30,ty-126,60,12,6);c.fillStyle='#cbd5e1';c.fill();c.stroke();
  // cabinet
  const g=c.createLinearGradient(x,0,x+w,0);g.addColorStop(0,'#e5e9f0');g.addColorStop(1,'#c9d1dc');o2box(c,x,y,w,h,18,g,5);
  ngRR(c,x+24,y+24,w*.52,h*.42,10);c.fillStyle='#1e293b';c.fill();c.lineWidth=4;c.strokeStyle=O2;c.stroke();
  ngTxt(c,e.screen||'MACHINE 1',x+24+w*.26,y+24+h*.21,22,'#7dd3fc',800);
  // fault spark
  if(flt){const k=(tl*6)%1;o2emo(c,'⚡',x+w*.3,y+h*.72,56+k*10);ngRR(c,x+w*.3+34,y+h*.72-18,110,36,18);c.fillStyle=NG.red;c.fill();c.lineWidth=3;c.strokeStyle=O2;c.stroke();ngTxt(c,'FAULT',x+w*.3+89,y+h*.72,18,'#fff',800)}
  // reset pushbutton
  const bx=x+w*.78,by=y+h*.62;c.beginPath();c.arc(bx,by,40,0,7);c.fillStyle='#e2e8f0';c.fill();c.lineWidth=4;c.strokeStyle=O2;c.stroke();
  c.beginPath();c.arc(bx,by+(pr?4:0),pr?27:30,0,7);c.fillStyle=pr?'#1d4ed8':'#3b82f6';c.fill();c.stroke();ngTxt(c,'RESET',bx,by+58,17,O2,800);
  if(pr){o2emo(c,'👇',bx+6,by-58,50)}
  if(lamp){ngRR(c,tx-70,ty-170,140,36,18);c.fillStyle=NG.red;c.fill();c.lineWidth=3;c.strokeStyle=O2;c.stroke();ngTxt(c,'🚨 ALARM',tx,ty-152,18,'#fff',800)}}
function drawBit2(e,c,tl){const{x,y,w,h}=e,v=o2t(tl,e.val),ts=o2last(tl,e.val);o2box(c,x,y,w,h,22,'#fff',5);
  ngTxt(c,e.name||'M0',x+24,y+30,22,'#5b6475',800,'left');ngTxt(c,e.sub||'',x+24,y+58,16,'#8a93a3',700,'left');
  const pk=tl-ts<.4?1+.25*Math.sin((tl-ts)/.4*Math.PI):1;c.save();c.translate(x+w-70,y+h/2+6);c.scale(pk,pk);ngTxt(c,String(v),0,0,h*.62,v?NG.blue:'#9aa3b2',900);c.restore();
  c.beginPath();c.arc(x+w-18,y+18,9,0,7);c.fillStyle=v?'#22c55e':'#cbd5e1';c.fill();c.lineWidth=3;c.strokeStyle=O2;c.stroke();
  if(v&&tl-ts<.5){c.save();c.globalAlpha*=1-(tl-ts)/.5;c.lineWidth=6;c.strokeStyle=NG.blue;ngRR(c,x-6,y-6,w+12,h+12,26);c.stroke();c.restore()}}
function drawLamp2(e,c,tl){const on=o2t(tl,e.val),cx=e.x+e.w/2,cy=e.y+e.w/2,r=e.w/2;if(on){const rg=c.createRadialGradient(cx,cy,r*.4,cx,cy,r*2);rg.addColorStop(0,'rgba(255,80,80,.5)');rg.addColorStop(1,'rgba(255,80,80,0)');c.fillStyle=rg;c.beginPath();c.arc(cx,cy,r*2,0,7);c.fill()}
  c.beginPath();c.arc(cx,cy,r,0,7);c.fillStyle=on?'#ff4d4d':'#e5e7eb';c.fill();c.lineWidth=5;c.strokeStyle=O2;c.stroke();ngRR(c,cx-r*.5,cy+r-2,r,r*.5,6);c.fillStyle='#94a3b8';c.fill();c.stroke();ngTxt(c,e.label||'Y0',cx,cy+r*1.75,20,O2,800)}

function ep2Kit(s,A,END){const K=ep09Kit(s,A,END),{ng}=K;
  const card=(x,y,w,h,text,win,o={})=>ng('card2',{x,y,w,h,text,...o},win);
  const emo=(emoji,cx,cy,sz,win,o={})=>ng('emo2',{x:cx-sz/2,y:cy-sz/2,w:sz,h:sz,emoji,...o},win);
  const wipe=t=>ng('wipe2',{x:0,y:0,w:W,h:H,noPop:true},[t-.38,t+.38]);
  const bit=(x,y,w,h,name,sub,val,win)=>ng('bit2',{x,y,w,h,name,sub,val},win);
  const lamp=(x,y,d,val,win,o={})=>ng('lamp2',{x,y,w:d,h:d,val,...o},win);
  return{...K,card,emo,wipe,bit,lamp};
}
async function buildEp09v2(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('16:9');S.narrOff=0;
  const A=EP09V2_A,END=431.2;
  const s=newScene({name:'EP09 – SET RESET in PLC (notification → alarm)',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep2Kit(s,A,END),{ng,T,PS,card,emo,wipe,bit,lamp,host}=K;
  const Pk=(a,b=a)=>[PS(a),b>=42?END:PS(b+1)],RED=NG.red,GRN=NG.grn,BLU=NG.blue,PUR='#7c3aed';
  s.els.push({id:uid++,type:'ngd',kind:'mg',mg:'floor',name:'floor',x:-200,y:0,w:1680,h:720,hz:470,vx:.5,draw:.1,delay:0,withPrev:true,entrance:'none',motion:'none',noPop:true,win:[0,END]});
  const RUNG=(x,y,w,items,win,o={})=>ng('rung',{x,y,w,h:80,items,...o},win);
  const Pon=(a,b)=>[[a,1],[b,0]];
  /* SC1 PHONE (k0–k2) */
  const notifT=[[T(0,1),1],[T(2,4),0],[T(2,4)+1.2,1],[T(2,5),0]];
  ng('phone2',{x:110,y:40,w:330,h:640,notif:notifT,msg:[T(0,0)+.2,T(2,4)+.5],swipe:[T(2,4),T(2,5)]},[0,PS(3)]);
  card(560,120,280,90,'Message',[T(0,0),T(0,4)],{emoji:'📩',sub:'1 second event'});
  card(560,240,300,90,'10 min later…',[T(0,3),PS(1)],{emoji:'⏰'});
  card(880,240,300,90,'Innum irukku!',[T(0,3)+1.2,PS(1)],{emoji:'👀',bg:'#fef3c7'});
  card(560,120,280,90,'Event mudinjiduchu',[T(0,4),PS(1)],{emoji:'✅',size:24});
  emo('🤔',740,470,150,[T(0,5),PS(1)]);host([T(0,5),PS(1)],[[0,'question']],{x:880,y:380,size:300});
  // k1 – SET / RESET intro
  card(560,110,300,120,'SET',Pk(1),{bg:GRN,size:60,emoji:'✅',esize:56});card(890,110,300,120,'RESET',[T(1,0)+.6,PS(2)],{bg:RED,size:52,emoji:'🧹',esize:52});
  card(560,270,630,84,'FX3U  ·  GX Works2 Ladder',[T(1,2),PS(2)],{emoji:'💻',size:30});
  card(560,390,630,84,'Challenge kadaisila!',[T(1,3),PS(2)],{emoji:'🎯',bg:'#fef3c7',size:30});
  // k2 – notification = SET, clear = RESET
  card(560,150,330,110,'Notification ON',Pk(2),{emoji:'🔔',sub:'= SET',scol:GRN,size:30});
  card(560,300,330,110,'Clear pannaa OFF',[T(2,4),PS(3)],{emoji:'👆',sub:'= RESET',scol:RED,size:30});
  card(930,150,250,110,'SET',[T(2,0)+.4,PS(3)],{bg:GRN,size:56});card(930,300,250,110,'RESET',[T(2,4)+.4,PS(3)],{bg:RED,size:48});
  /* SC2 PLC BIT (k3–k4) */
  wipe(PS(3));
  const M0a=[[T(3,1),1],[T(3,3),0]];
  RUNG(80,170,640,[{k:'NO',label:'X0',on:[[T(3,0),1],[T(3,1)+1.2,0]]},{k:'SET',label:'M0',on:M0a}],Pk(3,4),{num:'1',power:[[T(3,0),1],[T(3,1)+1.2,0]]});
  RUNG(80,330,640,[{k:'NO',label:'X1',on:[[T(3,3),1],[T(3,3)+1,0]]},{k:'RST',label:'M0',on:[[T(3,3),1],[T(3,3)+1,0]]}],[T(3,2),PS(5)],{num:'2',power:[[T(3,3),1],[T(3,3)+1,0]]});
  bit(860,150,320,130,'M0','memory bit 🧠',[[0,0],...M0a,[PS(4),1]],Pk(3,4));
  card(860,320,320,80,'Input OFF… M0 ON!',[T(3,1)+1.3,T(3,3)],{emoji:'😮',size:24,bg:'#fef3c7'});
  card(860,320,320,80,'RST = RESET',[T(3,4),PS(4)],{emoji:'🧹',size:26});
  card(860,320,320,80,'Internal bit',[PS(4),PS(5)],{emoji:'🧠',sub:'terminal illa',size:26});
  RUNG(80,470,640,[{k:'NO',label:'M0',on:[[PS(4),1]]},{k:'COIL',label:'Y0 LAMP',on:[[T(4,2),1]]}],[T(4,1),PS(5)],{num:'3',power:[[T(4,2),1]]});
  lamp(960,440,110,[[T(4,2),1]],[T(4,1),PS(5)],{label:'Y0 ALARM LAMP'});
  /* SC3 OUT COIL (k5–k6) */
  wipe(PS(5));
  card(340,60,600,96,'Normal OUT coil?',Pk(5,6),{emoji:'🤔',size:40});
  const xo=[[T(6,1),1],[T(6,2),0],[T(6,2)+1.6,1],[T(6,2)+2.4,0]];
  RUNG(120,260,700,[{k:'NO',label:'X0',on:xo},{k:'COIL',label:'Y0',on:xo}],Pk(6),{num:'1',power:xo});
  lamp(960,230,120,xo,Pk(6),{label:'Y0'});
  card(140,440,320,84,'X0 ON → Y0 ON',[T(6,1),PS(7)],{emoji:'✅',size:26});card(500,440,320,84,'X0 OFF → Y0 OFF',[T(6,2),PS(7)],{emoji:'❌',size:26});
  card(860,440,300,84,'Nyaabagam illa',[T(6,3),PS(7)],{emoji:'🙅',size:26,bg:'#fee2e2'});
  /* SC4 SELF-HOLDING vs SET (k7–k11) */
  wipe(PS(7));
  card(240,50,800,96,'Self-holding = SET?',Pk(7,8),{emoji:'🤔',size:40});
  card(200,220,380,130,'Self-holding',[T(7,1),PS(9)],{emoji:'🔁',sub:'hold pannum ✅',size:34});card(700,220,380,130,'SET',[T(7,1)+.4,PS(9)],{emoji:'📌',sub:'hold pannum ✅',size:40});
  card(380,420,520,90,'Aana method different!',[PS(8),PS(9)],{emoji:'⚠️',bg:'#fef3c7',size:32});
  const sh=[[T(9,0),1],[T(9,1),0]],shY=[[T(9,0)+.2,1],[T(9,2),0]];
  card(60,40,520,80,'Self-holding',Pk(9,11),{emoji:'🔁',size:32,bg:'#ccfbf1'});
  ng('rung',{x:40,y:200,w:620,h:120,num:'1',items:[{k:'NO',label:'START',on:sh,par:{label:'M0',on:shY}},{k:'NC',label:'STOP',on:[[0,1],[T(9,2),0],[T(9,2)+1,1]]},{k:'COIL',label:'M0',on:shY}],power:[[T(9,0),1],[T(9,2),0]]},Pk(9,11));
  card(700,40,520,80,'SET method',[PS(10),PS(12)],{emoji:'📌',size:32,bg:'#dbeafe'});
  RUNG(680,220,560,[{k:'NO',label:'START',on:[[T(10,1),1],[T(10,1)+1,0]]},{k:'SET',label:'M0',on:[[T(10,1)+.1,1]]}],[PS(10),PS(12)],{num:'1',power:[[T(10,1),1],[T(10,1)+1,0]]});
  RUNG(680,370,560,[{k:'NO',label:'STOP',on:[[T(10,3),1]]},{k:'RST',label:'M0',on:[[T(10,3),1]]}],[T(10,2),PS(12)],{num:'2',power:[[T(10,3),1]]});
  card(700,500,520,74,'Holding branch thevai illa',[T(10,0),PS(11)],{emoji:'✂️',size:24});
  card(60,500,560,90,'Holding PATH hold pannum',[PS(11),PS(12)],{emoji:'🔁',size:26});card(680,500,560,90,'INSTRUCTION hold pannum',[T(11,1),PS(12)],{emoji:'📌',size:26});
  /* SC5 FACTORY (k12–k19) */
  wipe(PS(12));
  card(380,40,520,96,'Factory-ku vaanga',Pk(12),{emoji:'🏭',size:40});
  const FL=[[T(13,0)+.5,T(13,0)+1.6]],FL2=[[T(15,0),T(16,0)]],FL3=[[T(18,0)+.3,PS(20)]];
  const lampT=[[T(13,0)+.5,1],[T(13,0)+1.6,0],[T(15,0)+.4,1],[T(17,4),0],[T(18,0)+.3,1]];
  ng('panel2',{x:80,y:250,w:420,h:380,fault:[...FL,...FL2,...FL3],lamp:lampT,press:[[T(16,4),T(16,4)+.8],[T(17,4),T(17,4)+.8],[T(18,0)+1.2,T(18,0)+2.2]]},[PS(12),PS(20)]);
  card(580,150,560,90,'Fault vandhu poyiduchu',[T(13,0),T(13,3)],{emoji:'⚡',size:28});
  card(580,270,560,90,'Operator illa',[T(13,1),T(13,3)],{emoji:'🙈',size:28});
  card(580,390,560,90,'Fault MISS!',[T(13,3),PS(14)],{emoji:'😱',bg:'#fee2e2',size:34});
  // k14 mapping
  [['X0','Fault input','⚡'],['X1','Reset button','🔵'],['M0','Alarm memory','🧠'],['Y0','Alarm lamp','🚨']].forEach(([a,b,em],i)=>card(580,130+i*105,560,88,a+'  ·  '+b,[T(14,1+Math.min(i,3)),PS(15)],{emoji:em,size:28}));
  // k15–k17 logic
  const m0=[[0,0],[T(15,0)+.2,1],[T(17,4),0],[T(18,0)+.3,1]];
  bit(580,110,300,110,'M0','alarm memory',m0,[PS(15),PS(20)]);
  RUNG(580,270,640,[{k:'NO',label:'X0 FAULT',on:[[T(15,0),1],[T(16,0),0],[T(18,0)+.3,1]]},{k:'SET',label:'M0',on:m0}],[PS(15),PS(20)],{num:'1',power:[[T(15,0),1],[T(16,0),0],[T(18,0)+.3,1]]});
  RUNG(580,420,640,[{k:'NO',label:'X1 RESET',on:[[T(17,4),1],[T(17,4)+.8,0],[T(18,0)+1.2,1],[T(18,0)+2.2,0]]},{k:'NC',label:'X0 FAULT',on:[[0,1],[T(15,0),0],[T(16,0),1],[T(18,0)+.3,0]]},{k:'RST',label:'M0',on:[[T(17,4),1],[T(17,4)+.8,0]]}],[PS(17),PS(20)],{num:'2',power:[[T(17,4),1],[T(17,4)+.8,0]]});
  card(920,110,300,110,'Fault OFF… lamp ON',[PS(16),PS(17)],{emoji:'🚨',size:22,bg:'#fef3c7'});
  host([T(16,2),PS(17)],[[0,'pointboard'],[T(16,4),'thumbsup']],{x:470,y:430,size:260});
  card(920,110,300,110,'Fault clear + Reset',[T(17,1),PS(18)],{emoji:'✅',size:22});
  // k18 question / k19 answer
  card(920,110,300,110,'Fault + Reset?',[PS(18),PS(19)],{emoji:'🤔',size:24,bg:'#fef3c7'});
  card(600,560,240,90,'ON?',[T(18,0)+.6,PS(19)],{emoji:'💡',size:40});card(880,560,240,90,'OFF?',[T(18,0)+.9,PS(19)],{emoji:'🌑',size:40});
  card(920,110,300,110,'Lamp ON-laye!',[PS(19),PS(20)],{emoji:'🔒',size:24,bg:'#dcfce7'});
  card(600,570,620,84,'Reset press ≠ fault sari',[T(19,2),PS(20)],{emoji:'⚠️',size:26,bg:'#fef3c7'});
  /* SC6 ORDER / DECODE (k20–k22) */
  wipe(PS(20));
  card(300,40,680,96,'Instruction ORDER mukkiyam',Pk(20,22),{emoji:'🔢',size:36});
  card(470,150,340,70,'⚡ DECODE',[T(21,0),T(21,0)+2.4],{bg:'#0ea5e9',size:34});
  const both=[[T(21,0),1]];
  RUNG(80,250,520,[{k:'NO',label:'X0',on:both},{k:'SET',label:'M0',on:both}],[T(21,0),PS(23)],{num:'1',power:both,sweep:[T(21,1),T(21,1)+1.4]});
  RUNG(80,380,520,[{k:'NO',label:'X1',on:both},{k:'RST',label:'M0',on:both}],[T(21,0),PS(23)],{num:'2',power:both,sweep:[T(21,1)+1.4,T(21,1)+2.8]});
  card(80,510,520,80,'Kadaisi = RST → OFF',[T(21,1)+2.8,PS(23)],{emoji:'🌑',size:28});
  RUNG(680,250,520,[{k:'NO',label:'X1',on:both},{k:'RST',label:'M0',on:both}],[T(21,2),PS(23)],{num:'1',power:both,sweep:[T(21,2)+.2,T(21,2)+1.4]});
  RUNG(680,380,520,[{k:'NO',label:'X0',on:both},{k:'SET',label:'M0',on:both}],[T(21,2),PS(23)],{num:'2',power:both,sweep:[T(21,2)+1.4,T(21,2)+2.6]});
  card(680,510,520,80,'Kadaisi = SET → ON',[T(21,2)+2.6,PS(23)],{emoji:'💡',size:28});
  card(300,610,680,80,'"RESET eppovum jeyikkum"',[PS(22),PS(23)],{emoji:'❌',size:28,bg:'#fee2e2',strike:T(22,0)+.8});
  /* SC7 CHALLENGE (k23–k26) */
  wipe(PS(23));
  card(380,40,520,110,'CHALLENGE',Pk(23,26),{emoji:'🎯',bg:'#f59e0b',size:52});
  ['SET M0','SET M0','SET M0'].forEach((t,i)=>card(140,200+i*95,300,80,t,[T(24,0)+i*.7,PS(27)],{bg:GRN,size:32,emoji:['1️⃣','2️⃣','3️⃣'][i]}));
  card(140,500,300,80,'RST M0',[T(24,1),PS(27)],{bg:RED,size:32,emoji:'🧹'});
  bit(560,230,300,140,'M0','final value?',[[0,0]],[T(24,2),PS(27)]);
  card(560,230,300,140,'?',[T(24,2)+.5,PS(27)],{size:90,bg:'#fef3c7'});
  card(560,430,240,90,'ON?',[PS(25),PS(27)],{emoji:'💡',size:40});card(830,430,240,90,'OFF?',[PS(25)+.3,PS(27)],{emoji:'🌑',size:40});
  card(900,200,320,90,'Count pannaadheenga',[T(26,1),PS(27)],{emoji:'🧠',size:24});
  card(560,560,560,90,'Comment pannunga! Answer kadaisila',[T(26,2),PS(27)],{emoji:'💬',size:24,bg:'#dbeafe'});
  /* SC8 ADVANTAGES (k27–k29) */
  wipe(PS(27));
  card(340,40,600,100,'SET RESET advantage',Pk(27,29),{emoji:'🚀',size:38});
  [['Alarm memory','🚨'],['Batch active','📦'],['Sequence step','🔢']].forEach(([t,em],i)=>card(80+i*385,200,355,200,t,[T(28,1)+i*.6,PS(29)],{emoji:em,layout:'col',esize:80,size:30}));
  card(300,460,680,90,'START & CLEAR thani-thaniyaa',[T(28,2),PS(29)],{emoji:'✂️',size:28});
  card(80,200,540,200,'Self-holding',[PS(29),PS(30)],{emoji:'🔁',layout:'col',esize:80,sub:'Simple Start / Stop · 1 rung',size:34});
  card(660,200,540,200,'SET RESET',[T(29,1),PS(30)],{emoji:'📌',layout:'col',esize:80,sub:'Start event / Clear event thani',size:34});
  card(340,460,600,90,'Application-ku yetha method',[T(29,2),PS(30)],{emoji:'🎯',size:28});
  /* SC9 MISTAKES (k30–k31) */
  wipe(PS(30));
  card(340,40,600,100,'Common mistake',Pk(30,31),{emoji:'⚠️',bg:'#fee2e2',size:40});
  RUNG(100,220,640,[{k:'NO',label:'X0',on:[[T(30,1),1],[T(30,3),0]]},{k:'SET',label:'M0',on:[[T(30,1)+.2,1]]}],Pk(30),{num:'1',power:[[T(30,1),1],[T(30,3),0]]});
  card(100,360,640,90,'RESET rung… illa!',[T(30,2),PS(31)],{emoji:'🤦',size:30,strike:null,bg:'#fef3c7'});
  bit(860,200,320,130,'M0','stuck ON',[[0,0],[T(30,1)+.2,1]],Pk(30));card(860,370,320,90,'ON-la nikkum',[T(30,3),PS(31)],{emoji:'🔒',size:28});
  card(240,490,800,90,'"Indha state eppo clear aaganum?"',[T(30,4),PS(31)],{emoji:'💡',size:28,bg:'#dcfce7'});
  [['Page 1','SET M0'],['Page 4','RST M0'],['Page 7','SET M0'],['Page 9','RST M0']].forEach(([p,t],i)=>card(80+i*290,200,260,140,t,[T(31,0)+i*.35,PS(32)],{band:{t:p,bg:i%2?RED:GRN},size:30}));
  card(380,400,520,90,'Yaar ON? Yaar OFF?',[T(31,1),PS(32)],{emoji:'🔍',size:30});
  card(380,520,520,90,'Clear comments',[T(31,2),PS(32)],{emoji:'📝',size:30,bg:'#dcfce7'});
  /* SC10 POWER CUT (k32–k35) */
  wipe(PS(32));
  ng('flash',{x:0,y:0,w:W,h:H,noPop:true,color:'#111827'},[PS(32),PS(32)+.7]);
  card(340,40,600,100,'Power cut-ku appuram?',Pk(32,35),{emoji:'🔌',size:36});
  card(380,220,520,110,'SET nyaabagam irukkumaa?',Pk(32),{emoji:'🤔',size:30,bg:'#fef3c7'});
  card(380,200,520,90,'Guarantee illa!',[PS(33),PS(34)],{emoji:'❌',size:34});
  [['Device','💾'],['Retained memory?','🔋'],['PLC settings','⚙️']].forEach(([t,em],i)=>card(80+i*385,330,355,120,t,[T(33,1)+i*.5,PS(34)],{emoji:em,size:26}));
  card(100,220,500,170,'Input OFF → ON-la',Pk(34),{emoji:'📌',layout:'col',esize:64,size:28,sub:'SET behaviour'});card(680,220,500,170,'Power cut → retain',[T(34,0)+1,PS(35)],{emoji:'🔋',layout:'col',esize:64,size:28,sub:'memory setting'});
  card(440,430,400,80,'2 different!',[T(34,0)+2,PS(35)],{emoji:'⚠️',size:30});
  card(180,200,920,110,'Retained bit = motor run?',[PS(35),PS(36)],{emoji:'⚙️',size:34});
  card(180,350,920,110,'Power return → unwanted restart',[T(35,0)+2.5,PS(36)],{emoji:'😱',bg:'#fee2e2',size:32});
  card(180,500,920,90,'Startup behaviour check pannunga',[T(35,1),PS(36)],{emoji:'✅',size:28,bg:'#dcfce7'});
  /* SC11 ANSWER (k36–k38) */
  wipe(PS(36));
  card(380,40,520,110,'ANSWER',Pk(36,38),{emoji:'🎯',bg:'#f59e0b',size:52});
  const av=[[0,0],[T(37,0),1],[T(38,0)+.4,0]];
  ['SET M0','SET M0','SET M0'].forEach((t,i)=>card(140,200+i*95,300,80,t,[T(37,0)+i*.6,PS(39)],{bg:GRN,size:32,emoji:'✅',tick:T(37,0)+i*.6+.4}));
  card(140,500,300,80,'RST M0',[PS(38),PS(39)],{bg:RED,size:32,emoji:'🧹'});
  bit(560,230,300,140,'M0','final value',av,Pk(36,38));
  card(900,230,320,90,'SET count pannaadhu',[T(37,1),PS(39)],{emoji:'🧠',size:24});
  card(560,430,560,130,'Answer: OFF',[T(38,2),PS(39)],{emoji:'🌑',bg:NG.navy,size:52});
  emo('🤯',1080,560,120,[T(38,2)+.4,PS(39)]);
  /* SC12 RECAP (k39–k41) */
  wipe(PS(39));
  card(240,40,800,100,'Latching = hold behaviour',Pk(39),{emoji:'💡',size:36});
  card(120,220,480,160,'Self-holding',[T(39,1),PS(40)],{emoji:'🔁',layout:'col',esize:64,size:32});card(680,220,480,160,'SET RESET',[T(39,1)+.4,PS(40)],{emoji:'📌',layout:'col',esize:64,size:32});
  card(340,40,600,100,'Troubleshoot checklist',[PS(40),PS(42)],{emoji:'🔍',size:34});
  [['Holding path enga?','🔁'],['Edhu SET pannudhu?','✅'],['Edhu RESET pannudhu?','🧹'],['Endha order?','🔢']].forEach(([t,em],i)=>card(240,180+i*110,800,92,t,[T(40,Math.min(i,4))+(i?0:0),PS(42)],{emoji:em,size:32,tick:PS(41)+i*.5}));
  /* SC13 CTA (k42) */
  wipe(PS(42));
  card(240,50,800,100,'Correct answer sonneengalaa?',[PS(42),END],{emoji:'💬',size:34});
  card(140,210,300,110,'LIKE',[T(42,1),END],{emoji:'👍',bg:BLU,size:44});card(490,210,300,110,'SHARE',[T(42,2),END],{emoji:'↗️',bg:NG.teal,size:44});
  card(840,210,300,110,'NEXT: ⏱ TIMER',[T(42,3),END],{bg:PUR,size:30});
  card(390,370,500,130,'SUBSCRIBE',[T(42,5),END],{emoji:'🔔',bg:RED,size:54});
  card(390,540,500,90,'Factory Decode Tamil · EP 09',[T(42,5)+.5,END],{size:28});
  host([T(42,1),END],[[0,'thumbsup'],[T(42,5),'wavebye']],{x:20,y:400,size:300});
  S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
async function buildEp09v2Short(){
  stopAudio();S.playing=false;S.scenes=[];S.sel=null;S.music=null;setAspect('9:16');S.narrOff=0;
  const A=EP09V2_SA,END=49.6;
  const s=newScene({name:'EP09 Short – SET RESET notification',style:'white',transition:'cut',trans:0,hold:0});s.minDur=END;S.scenes.push(s);
  const K=ep2Kit(s,A,END),{ng,T,PS,card,emo,wipe,bit,host}=K,RED=NG.red,GRN=NG.grn;
  s.els.push({id:uid++,type:'ngd',kind:'mg',mg:'floor',name:'floor',x:0,y:0,w:720,h:1280,hz:900,vx:.5,draw:.1,delay:0,withPrev:true,entrance:'none',motion:'none',noPop:true,win:[0,END]});
  const nt=[[T(0,1),1],[T(0,4),0]];
  ng('phone2',{x:180,y:300,w:360,h:700,notif:nt,msg:[T(0,0)+.1],swipe:[T(0,4)]},[0,PS(1)+.1]);
  card(110,80,500,110,'1 second message',[T(0,0),T(0,2)],{emoji:'📩',size:30});
  card(110,80,500,110,'Innum irukku!',[T(0,2),T(0,4)],{emoji:'👀',size:34,bg:'#fef3c7'});
  card(110,80,500,110,'Clear → OFF',[T(0,4),PS(1)],{emoji:'👆',size:34});
  wipe(PS(1));
  card(110,260,500,150,'SET',Pk1=[PS(1),PS(2)],{emoji:'✅',bg:GRN,size:70});card(110,450,500,150,'RESET',[PS(1)+.6,PS(2)],{emoji:'🧹',bg:RED,size:60});
  card(110,650,500,100,'PLC-layum idhe!',[PS(1)+1,PS(2)],{emoji:'💻',size:32});
  wipe(PS(2));
  card(60,120,600,110,'TWIST',[PS(2),PS(3)],{emoji:'🌀',bg:'#f59e0b',size:56});
  card(60,300,600,130,'Self-holding podhume?',[T(2,1),PS(3)],{emoji:'🔁',size:34});
  card(60,470,600,130,'Appo SET RESET edhukku?',[T(2,2),PS(3)],{emoji:'🤔',size:32,bg:'#fef3c7'});
  wipe(PS(3));
  ['SET M0','SET M0','SET M0'].forEach((t,i)=>card(110,140+i*120,500,100,t,[T(3,1)+i*.6,PS(4)],{bg:GRN,size:40,emoji:['1️⃣','2️⃣','3️⃣'][i]}));
  card(110,520,500,100,'RST M0',[T(3,1)+2,PS(4)],{bg:RED,size:40,emoji:'🧹'});
  card(60,680,290,120,'ON?',[T(3,2),PS(4)],{emoji:'💡',size:46});card(370,680,290,120,'OFF?',[T(3,2)+.3,PS(4)],{emoji:'🌑',size:46});
  card(60,850,600,110,'3 SET = 3 RESET?',[T(3,3),PS(4)],{emoji:'🤯',size:40,bg:'#fef3c7'});
  wipe(PS(4));
  card(60,120,600,130,'Guess-ai COMMENT!',[PS(4),END],{emoji:'💬',size:40,bg:'#dbeafe'});
  card(60,300,600,130,'Answer ⬇ Full video',[T(4,1),END],{emoji:'👇',size:38});
  card(60,480,280,110,'LIKE',[T(4,2),END],{emoji:'👍',bg:NG.blue,size:36});card(380,480,280,110,'SHARE',[T(4,3),END],{emoji:'↗️',bg:NG.teal,size:36});
  card(110,650,500,140,'SUBSCRIBE',[T(4,4),END],{emoji:'🔔',bg:RED,size:52});
  host([PS(4),END],[[0,'askviewer'],[T(4,4),'wavebye']],{x:-10,y:860,size:400});
  host([T(0,4),PS(1)],[[0,'question']],{x:-20,y:900,size:380});
  S.captions=false;S.showHand=false;S.cur=0;S.pin=false;S.t=1;refresh();
}
