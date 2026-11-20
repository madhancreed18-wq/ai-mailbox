/* ---- v22 Star-Delta motion graphic (kind 'sdmg'): animated power circuit driven by e.seq [[t,mode]] ----
   modes: off | dol | star | gap | delta | short | trip.  KM1 main, KM2 star, KM3 delta.
   Everything moves from one model: contact bridges, coils, current dots (speed ~ current), motor speed,
   ammeter needle, tube-light brightness/flicker, star-timer dial, arc sparks, short-circuit flash. */
const SDM={off:[0,0,0],dol:[1,0,1],star:[1,1,0],gap:[1,0,0],delta:[1,0,1],short:[1,1,1],trip:[0,0,0]};
function sdModel(seq,t){let s=0,I=0,mode='off',t0=0,prevMode='off';const segs=(seq||[[0,'off']]);
  for(let i=0;i<segs.length;i++){const[a,m]=segs[i],b=i+1<segs.length?segs[i+1][0]:1e9;if(t<a)break;const tt=Math.min(t,b)-a;
    const tgt=m==='dol'||m==='delta'?1:m==='star'?.8:0,tau=m==='dol'?1.4:m==='star'?2.6:m==='delta'?1.2:2.2;
    const s0=s;s=tgt+(s0-tgt)*Math.exp(-tt/tau);mode=m;t0=a;prevMode=i?segs[i-1][1]:'off'}
  const since=t-t0;
  if(mode==='dol')I=1+6.5*(1-s);else if(mode==='star')I=.6+1.9*(1-s/.8);else if(mode==='delta')I=1+1.4*Math.exp(-since/.5);else if(mode==='short')I=10;else I=0;
  return{s,I,mode,since,prevMode}}
function drawSDMG(e,c,tl){const{x,y,w,h}=e,M=sdModel(e.seq,tl),st=SDM[M.mode]||SDM.off,ink=O2,cu='#b45309';
  const close=k=>{const tc=(e.seq||[]).filter(([,m])=>(SDM[m]||[0,0,0])[k]!==undefined);let v=0,lt=-9,prev=0;tc.forEach(([a,m])=>{if(tl>=a){const nv=(SDM[m]||[0,0,0])[k];if(nv!==v){prev=v;v=nv;lt=a}}});const p=Math.min(1,(tl-lt)/.12);return{v:prev+(v-prev)*p,lt,opening:v===0&&tl-lt<.25&&prev===1}};
  const sx=v=>x+v*w,sy=v=>y+v*h,flow=M.I>0?(tl*(.6+M.I*.35))%1:0;
  // supply bus L1 L2 L3
  const busY=sy(.08),ph=['#e11d48','#f59e0b','#2563eb'];
  [0,1,2].forEach(i=>{const yy=busY+i*18;c.beginPath();c.moveTo(sx(.04),yy);c.lineTo(sx(.62),yy);c.lineWidth=4;c.strokeStyle=ph[i];c.stroke();ngTxt(c,'L'+(i+1),sx(.025),yy,18,ph[i],800)});
  // contactor drawer
  const kx=[.12,.30,.48],kl=['KM1 MAIN','KM3 DELTA','KM2 STAR'],kidx=[0,2,1],cw=w*.14,chh=h*.24,ky=sy(.2);
  const pole=(i,j)=>sx(kx[i])+cw*(.22+j*.28);
  const wire=(pts,live,col)=>{c.beginPath();pts.forEach((p,i)=>i?c.lineTo(p[0],p[1]):c.moveTo(p[0],p[1]));c.lineWidth=4;c.strokeStyle=col||ink;c.stroke();
    if(live&&M.I>0){let L=0;const seg=[];for(let i=1;i<pts.length;i++){const d=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);seg.push(d);L+=d}
      const n=Math.max(2,Math.round(L/36));for(let q=0;q<n;q++){let u=((q/n+flow)%1)*L,i=0;while(i<seg.length-1&&u>seg[i]){u-=seg[i];i++}const f=Math.min(1,u/seg[i]),px=pts[i][0]+(pts[i+1][0]-pts[i][0])*f,py=pts[i][1]+(pts[i+1][1]-pts[i][1])*f;
        c.beginPath();c.arc(px,py,M.I>4?7:5,0,7);c.fillStyle=M.I>4?'#ef4444':'#fbbf24';c.fill()}}};
  [0,1,2].forEach(i=>{const k=kidx[i],C=close(k),bx=sx(kx[i]),by=ky;
    o2box(c,bx,by,cw,chh,14,'#e5e7eb',4,false);ngTxt(c,kl[i],bx+cw/2,by+chh+20,17,ink,800);
    // coil
    c.beginPath();c.arc(bx+cw-16,by+16,9,0,7);c.fillStyle=C.v>.5?'#22c55e':'#9ca3af';c.fill();c.lineWidth=2;c.strokeStyle=ink;c.stroke();
    // poles: fixed contacts + moving bridge
    [0,1,2].forEach(j=>{const px=pole(i,j),top=by+chh*.28,bot=by+chh*.72,gap=(1-C.v)*14;
      c.fillStyle=ink;c.fillRect(px-6,top-4,12,6);c.fillRect(px-6,bot-2,12,6);
      c.save();c.translate(px,(top+bot)/2-gap);c.fillStyle=C.v>.5?'#16a34a':'#6b7280';c.fillRect(-9,-3,18,6);c.restore();
      c.beginPath();c.moveTo(px,top-4);c.lineTo(px,by-2);c.lineWidth=3;c.strokeStyle=ink;c.stroke();
      if(C.opening&&M.I>.3){c.save();c.strokeStyle='#60a5fa';c.lineWidth=3;c.beginPath();for(let z=0;z<5;z++){c.lineTo(px+(Math.random()-.5)*14,top+z*((bot-top)/4))}c.stroke();c.restore()}});
    // feed from bus (KM1, KM3)
    if(k!==1)[0,1,2].forEach(j=>wire([[pole(i,j),busY+j*18],[pole(i,j),by]],st[0]&&C.v>.5&&M.I>0,ph[j]))});
  // motor + terminals
  const mx=sx(.30),my=sy(.78),mr=Math.min(w,h)*.15,t1y=sy(.56),t2y=sy(.64),tx=j=>mx-60+j*60;
  ['U1','V1','W1'].forEach((t,j)=>{c.beginPath();c.arc(tx(j),t1y,8,0,7);c.fillStyle='#fde68a';c.fill();c.lineWidth=2;c.strokeStyle=ink;c.stroke();ngTxt(c,t,tx(j)-22,t1y-14,14,ink,800)});
  ['W2','U2','V2'].forEach((t,j)=>{c.beginPath();c.arc(tx(j),t2y,8,0,7);c.fillStyle='#fde68a';c.fill();c.lineWidth=2;c.strokeStyle=ink;c.stroke();ngTxt(c,t,tx(j)-22,t2y+16,14,ink,800)});
  const live=M.I>0;
  [0,1,2].forEach(j=>wire([[pole(0,j),ky+chh],[pole(0,j),ky+chh+30+j*10],[tx(j),ky+chh+30+j*10],[tx(j),t1y-8]],live,ph[j]));   // KM1 -> U1 V1 W1
  [0,1,2].forEach(j=>wire([[tx(j),t2y+8],[tx(j),t2y+26+j*8],[pole(1,j),t2y+26+j*8],[pole(1,j),ky+chh]],live&&st[2],null));     // W2 U2 V2 -> KM3
  [0,1,2].forEach(j=>wire([[pole(1,j),t2y+26+j*8],[pole(2,j),t2y+26+j*8],[pole(2,j),ky+chh]],live&&st[1],null));             // -> KM2
  // star point bar on KM2 top
  c.beginPath();c.moveTo(pole(2,0)-6,ky-8);c.lineTo(pole(2,2)+6,ky-8);c.lineWidth=6;c.strokeStyle=st[1]?'#16a34a':ink;c.stroke();ngTxt(c,'star point',pole(2,1),ky-24,14,'#6b7280',700);
  // motor body + spinning fan
  const ang=(tl*M.s*22)%(Math.PI*2);c.save();c.translate(mx,my+mr*.6);
  o2box(c,-mr*1.3,-mr*.9,mr*2.6,mr*1.8,20,'#94a3b8',4,false);for(let f=-3;f<=3;f++){c.beginPath();c.moveTo(-mr*1.1,f*mr*.22);c.lineTo(mr*1.1,f*mr*.22);c.lineWidth=2;c.strokeStyle='#64748b';c.stroke()}
  c.fillStyle='#475569';c.fillRect(mr*1.3,-8,mr*.6,16);
  c.save();c.translate(mr*1.9,0);c.rotate(ang);for(let b=0;b<4;b++){c.rotate(Math.PI/2);c.beginPath();c.ellipse(0,-mr*.32,mr*.11,mr*.32,0,0,7);c.fillStyle='#f59e0b';c.fill();c.lineWidth=2;c.strokeStyle=ink;c.stroke()}c.restore();
  ngTxt(c,'MOTOR',0,0,22,'#fff',800);if(M.s>.05){for(let q=0;q<3;q++){c.beginPath();c.arc(mr*1.9,0,mr*.55+q*8,-.6+ang,.2+ang);c.lineWidth=2;c.strokeStyle='rgba(31,36,48,.35)';c.stroke()}}c.restore();
  ngTxt(c,M.s>.02?Math.round(M.s*1440)+' rpm':'0 rpm',mx,my+mr*1.75,20,ink,800);
  // ammeter
  const ax=sx(.82),ay=sy(.30),ar=Math.min(w,h)*.15,Iv=Math.min(9,M.I),na=Math.PI*(1.1+.8*Iv/9)+(M.I>4?Math.sin(tl*40)*.02:0);
  o2box(c,ax-ar*1.15,ay-ar*1.1,ar*2.3,ar*1.6,16,'#fff',4,false);c.beginPath();c.arc(ax,ay+ar*.2,ar,Math.PI*1.1,Math.PI*1.9);c.lineWidth=3;c.strokeStyle=ink;c.stroke();
  [0,2,4,6,8].forEach(v=>{const a=Math.PI*(1.1+.8*v/9);c.beginPath();c.moveTo(ax+Math.cos(a)*ar*.85,ay+ar*.2+Math.sin(a)*ar*.85);c.lineTo(ax+Math.cos(a)*ar,ay+ar*.2+Math.sin(a)*ar);c.stroke();ngTxt(c,v+'×',ax+Math.cos(a)*ar*.68,ay+ar*.2+Math.sin(a)*ar*.68,14,ink,700)});
  c.beginPath();c.moveTo(ax,ay+ar*.2);c.lineTo(ax+Math.cos(na)*ar*.95,ay+ar*.2+Math.sin(na)*ar*.95);c.lineWidth=4;c.strokeStyle=M.I>4?'#ef4444':'#16a34a';c.stroke();
  ngTxt(c,'CURRENT '+(M.I>0?M.I.toFixed(1)+'×':'0'),ax,ay+ar*.48,18,M.I>4?'#ef4444':ink,800);
  // tube light (brightness drops with current)
  const lx=sx(.82),ly=sy(.66),br=M.mode==='trip'?0:Math.max(.15,1-Math.max(0,M.I-1.5)*.13)*(M.I>4?(.75+.25*Math.sin(tl*31)):1);
  const g=c.createRadialGradient(lx,ly,10,lx,ly,ar*1.4);g.addColorStop(0,`rgba(253,224,71,${.55*br})`);g.addColorStop(1,'rgba(253,224,71,0)');c.fillStyle=g;c.fillRect(lx-ar*1.5,ly-ar*1.2,ar*3,ar*2.4);
  o2box(c,lx-ar*1.1,ly-14,ar*2.2,28,14,`rgb(${Math.round(150+105*br)},${Math.round(150+100*br)},${Math.round(140+60*br)})`,4,false);ngTxt(c,'FACTORY LIGHT',lx,ly+36,16,ink,800);
  // star timer dial
  const starSeg=(e.seq||[]).find(([a,m])=>m==='star'&&tl>=a);if(starSeg&&e.tset){const el=Math.min(e.tset,tl-starSeg[0]),dx=sx(.82),dy=sy(.90),dr=ar*.55;
    c.beginPath();c.arc(dx,dy,dr,0,7);c.fillStyle='#fff';c.fill();c.lineWidth=4;c.strokeStyle=ink;c.stroke();c.beginPath();c.moveTo(dx,dy);c.arc(dx,dy,dr-4,-Math.PI/2,-Math.PI/2+Math.PI*2*el/e.tset);c.closePath();c.fillStyle='rgba(245,158,11,.55)';c.fill();
    ngTxt(c,'T0 '+el.toFixed(1)+' s',dx+dr+60,dy,20,ink,800)}
  // short circuit
  if(M.mode==='short'&&M.since<1.2){const k=M.since;c.save();c.globalAlpha=Math.max(0,1-k/1.2);c.fillStyle='#fff7ae';c.fillRect(x,y,w,h);c.globalAlpha=1;
    for(let z=0;z<6;z++){c.beginPath();c.moveTo(sx(.39),ky+chh/2);for(let q=1;q<8;q++)c.lineTo(sx(.39)+(Math.random()-.5)*90,ky+chh/2+(Math.random()-.5)*120);c.lineWidth=4;c.strokeStyle='#2563eb';c.stroke()}c.restore();ngTxt(c,'SHORT CIRCUIT!',sx(.39),ky-40,34,'#ef4444',800)}
  if(M.mode==='trip'){ngTxt(c,'TRIP!',sx(.39),ky-40,40,'#ef4444',800)}}
