/* ================= Motion-graphics parts (v15, code-drawn vectors; no traced images) =================
   ngd kind 'mg', e.mg = sensor | box | conv | plc | lampb | bulb. Times are scene-local seconds. */
function mgEase(k){return k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2}
function drawMG(e,c,tl){
  const T=e.mg,ink=NG.ink;c.lineWidth=3.5;c.strokeStyle=ink;
  if(T==='sensor'){ // side view, detection face on the left, cable to the right
    const x=e.x,y=e.y,w=e.w,h=e.h,r=h/2,cy=y+r;
    // detection field (expanding arcs) while a target is present
    if(e.det!=null&&tl>=e.det&&(e.detEnd==null||tl<e.detEnd)){for(let i=0;i<3;i++){const f=((tl-e.det)*1.2+i/3)%1;c.save();c.globalAlpha*=(1-f)*.8;c.strokeStyle='#ffb020';c.lineWidth=4;c.beginPath();c.arc(x,cy,r*.6+f*r*1.6,Math.PI*.62,Math.PI*1.38);c.stroke();c.restore()}}
    c.fillStyle='#ff8a1f';ngRR(c,x,y+h*.08,w*.12,h*.84,6);c.fill();c.stroke();                 // face
    c.fillStyle='#cfd5dc';ngRR(c,x+w*.12,y,w*.62,h,4);c.fill();c.stroke();                     // threaded body
    c.save();c.strokeStyle='#9aa3af';c.lineWidth=2;for(let i=1;i<14;i++){const xx=x+w*.12+i*w*.62/14;c.beginPath();c.moveTo(xx,y+3);c.lineTo(xx-4,y+h-3);c.stroke()}c.restore();
    c.fillStyle='#8e98a3';[.3,.58].forEach(p=>{ngRR(c,x+w*p,y-h*.12,w*.07,h*1.24,4);c.fill();c.stroke()}); // nuts
    c.fillStyle='#5d6b7a';ngRR(c,x+w*.74,y+h*.12,w*.12,h*.76,5);c.fill();c.stroke();         // rear cap
    const led=e.led!=null&&tl>=e.led&&(e.ledEnd==null||tl<e.ledEnd);
    c.beginPath();c.arc(x+w*.8,y+h*.12,h*.13,0,7);c.fillStyle=led?'#ffb020':'#e3e6ea';c.fill();c.lineWidth=2.5;c.stroke();
    if(led){c.save();c.globalAlpha*=.3+.15*Math.sin(tl*8);c.beginPath();c.arc(x+w*.8,y+h*.12,h*.32,0,7);c.fillStyle='#ffb020';c.fill();c.restore()}
    c.lineWidth=7;c.strokeStyle='#2b2f36';c.beginPath();c.moveTo(x+w*.86,cy);c.lineTo(x+w,cy);c.stroke();
    if(e.wires){const ends=[['#8b5a2b',-1],['#2f6fd6',0],['#1d1d1f',1]];ends.forEach(([col,k])=>{c.strokeStyle=col;c.lineWidth=5;c.beginPath();c.moveTo(x+w,cy);c.quadraticCurveTo(x+w+18,cy+k*14,x+w+34,cy+k*16);c.stroke()})}
  }
  else if(T==='box'){ // cardboard box, slides from fromX to x between mv[0]..mv[1]
    let x=e.x;if(e.mv){const k=mgEase(clamp((tl-e.mv[0])/(e.mv[1]-e.mv[0])));x=e.fromX+(e.x-e.fromX)*k}
    const y=e.y,w=e.w,h=e.h;c.fillStyle='#d9a066';ngRR(c,x,y,w,h,4);c.fill();c.stroke();
    c.fillStyle='#c08850';c.beginPath();c.moveTo(x,y);c.lineTo(x+w,y);c.lineTo(x+w-6,y+h*.22);c.lineTo(x+6,y+h*.22);c.closePath();c.fill();c.stroke();
    c.fillStyle='#f3e2c4';c.fillRect(x+w*.42,y+1,w*.16,h*.5);c.strokeRect(x+w*.42,y+1,w*.16,h*.5);
  }
  else if(T==='conv'){ // side-view belt, rollers turn and belt dashes move while running (e.run=[[a,b],...])
    const x=e.x,y=e.y,w=e.w,h=e.h||40,run=(e.run||[]).some(q=>tl>=q[0]&&tl<q[1]);let ph=0;(e.run||[]).forEach(([a,b])=>{ph+=Math.max(0,Math.min(tl,b)-a)});
    c.fillStyle='#9aa3af';[x+30,x+w-30].forEach(lx=>{c.fillRect(lx-6,y+h,12,90);c.strokeRect(lx-6,y+h,12,90)});
    c.fillStyle='#2b2f36';ngRR(c,x,y,w,h,h/2);c.fill();c.stroke();
    c.save();c.strokeStyle='#5d6b7a';c.lineWidth=3;c.setLineDash([16,14]);c.lineDashOffset=-ph*120;c.beginPath();c.moveTo(x+h/2,y+4);c.lineTo(x+w-h/2,y+4);c.stroke();c.restore();
    [x+h/2,x+w-h/2].forEach(rx=>{c.fillStyle='#cfd5dc';c.beginPath();c.arc(rx,y+h/2,h/2-5,0,7);c.fill();c.stroke();const a=ph*6;c.beginPath();c.moveTo(rx,y+h/2);c.lineTo(rx+Math.cos(a)*(h/2-8),y+h/2+Math.sin(a)*(h/2-8));c.stroke()});
    if(run){c.save();c.strokeStyle=NG.teal;c.lineWidth=4;c.setLineDash([18,16]);c.lineDashOffset=-tl*90;c.beginPath();c.moveTo(x+40,y+h+24);c.lineTo(x+w-40,y+h+24);c.stroke();c.restore()}
  }
  else if(T==='plc'){ // compact PLC: terminals on top, input LEDs, label
    const x=e.x,y=e.y,w=e.w,h=e.h;c.fillStyle='#eef1f4';ngRR(c,x,y,w,h,10);c.fill();c.stroke();
    c.fillStyle='#d4d9df';ngRR(c,x+8,y+8,w-16,h*.22,6);c.fill();c.stroke();
    const n=8;for(let i=0;i<n;i++){const tx=x+20+i*(w-40)/(n-1);c.beginPath();c.arc(tx,y+8+h*.11,6,0,7);c.fillStyle='#fff';c.fill();c.lineWidth=2;c.stroke();c.beginPath();c.moveTo(tx-3,y+8+h*.11);c.lineTo(tx+3,y+8+h*.11);c.stroke()}
    c.lineWidth=3;ngTxt(c,e.label||'PLC',x+w*.3,y+h*.62,Math.round(h*.16),NG.navy,800);
    const on=e.on!=null&&tl>=e.on&&(e.onEnd==null||tl<e.onEnd);
    ['X0','X1','X2','X3'].forEach((l,i)=>{const lx=x+w*.58+i*w*.1,ly=y+h*.55;c.beginPath();c.arc(lx,ly,7,0,7);c.fillStyle=i===0&&on?NG.grn:'#d9dde3';c.fill();c.lineWidth=2;c.stroke();ngTxt(c,l,lx,ly+18,11,NG.navy,800)});
    if(on){c.save();c.globalAlpha*=.3;c.beginPath();c.arc(x+w*.58,y+h*.55,16,0,7);c.fillStyle=NG.grn;c.fill();c.restore()}
  }
  else if(T==='bulb'){ // 24 V lamp with base; rays when on
    const cx=e.x+e.w/2,cy=e.y+e.w/2,r=e.w/2,on=e.on!=null&&tl>=e.on&&(e.onEnd==null||tl<e.onEnd);
    if(on){c.save();c.strokeStyle='#ffb020';c.lineWidth=4;for(let i=0;i<8;i++){const a=i*Math.PI/4+.2,p=1+.08*Math.sin(tl*7);c.beginPath();c.moveTo(cx+Math.cos(a)*r*1.25,cy+Math.sin(a)*r*1.25);c.lineTo(cx+Math.cos(a)*r*1.6*p,cy+Math.sin(a)*r*1.6*p);c.stroke()}c.restore()}
    c.beginPath();c.arc(cx,cy,r,0,7);c.fillStyle=on?'#ffd23f':'#e3e6ea';c.fill();c.stroke();
    c.fillStyle='#8e98a3';ngRR(c,cx-r*.45,cy+r*.85,r*.9,r*.5,4);c.fill();c.stroke();
  }
}
