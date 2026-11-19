/* ================= Motion-graphics parts, 2.5D (v16, code-drawn vectors with shading; no traced images) =================
   ngd kind 'mg', e.mg = sensor | box | conv | plc | bulb | floor. Times are scene-local seconds. */
function mgEase(k){return k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2}
function ngShade(hex,k){if(!/^#[0-9a-f]{6}$/i.test(hex))return hex;const n=parseInt(hex.slice(1),16),f=v=>Math.max(0,Math.min(255,Math.round(k<1?v*k:v+(255-v)*(k-1))));return'#'+[n>>16,(n>>8)&255,n&255].map(f).map(v=>v.toString(16).padStart(2,'0')).join('')}
function mgShadow(c,cx,cy,rx,ry,a=.16){c.save();const g=c.createRadialGradient(cx,cy,0,cx,cy,rx);g.addColorStop(0,`rgba(20,30,45,${a})`);g.addColorStop(1,'rgba(20,30,45,0)');c.fillStyle=g;c.beginPath();c.ellipse(cx,cy,rx,ry,0,0,7);c.fill();c.restore()}
function mgCyl(c,x,y,w,h,base,r=4){const g=c.createLinearGradient(0,y,0,y+h);g.addColorStop(0,ngShade(base,.78));g.addColorStop(.22,ngShade(base,1.55));g.addColorStop(.42,base);g.addColorStop(1,ngShade(base,.55));ngRR(c,x,y,w,h,r);c.fillStyle=g;c.fill();c.stroke()}
function drawMG(e,c,tl){
  const T=e.mg,ink=NG.ink;c.lineWidth=3;c.strokeStyle=ink;c.lineJoin='round';
  if(T==='floor'){ // soft studio floor: gradient + perspective lines, gives the scene depth
    c.save();c.translate(e.x,e.y);const W_=e.w,H_=e.h,hz=e.hz??H_*.62;const g=c.createLinearGradient(0,0,0,H_);g.addColorStop(0,'#ffffff');g.addColorStop(hz/H_,'#f6f8fb');g.addColorStop(1,'#e6ebf2');c.fillStyle=g;c.fillRect(0,0,W_,H_);
    c.save();c.strokeStyle='rgba(120,140,165,.13)';c.lineWidth=2;const vx=W_*(e.vx??.55);for(let i=-12;i<=12;i++){c.beginPath();c.moveTo(vx+i*14,hz);c.lineTo(vx+i*190,H_+20);c.stroke()}
    for(let j=1;j<7;j++){const y=hz+(H_-hz)*Math.pow(j/7,1.8);c.beginPath();c.moveTo(0,y);c.lineTo(W_,y);c.stroke()}c.restore();c.restore();return}
  if(T==='sensor'){ // side view, detection face on the left, cable to the right
    const x=e.x,y=e.y,w=e.w,h=e.h,cy=y+h/2;
    mgShadow(c,x+w*.48,y+h*1.55,w*.55,h*.22);
    if(e.det!=null&&tl>=e.det&&(e.detEnd==null||tl<e.detEnd)){for(let i=0;i<3;i++){const f=((tl-e.det)*1.2+i/3)%1;c.save();c.globalAlpha*=(1-f)*.85;c.strokeStyle='#ffb020';c.lineWidth=4;c.beginPath();c.arc(x,cy,h*.35+f*h*1.1,Math.PI*.62,Math.PI*1.38);c.stroke();c.restore()}}
    mgCyl(c,x,y+h*.08,w*.12,h*.84,'#ff8a1f',6);                                   // face
    mgCyl(c,x+w*.12,y,w*.62,h,'#c3cad3',4);                                       // threaded body
    c.save();c.strokeStyle='rgba(60,70,85,.35)';c.lineWidth=1.6;for(let i=1;i<16;i++){const xx=x+w*.12+i*w*.62/16;c.beginPath();c.moveTo(xx,y+3);c.lineTo(xx-4,y+h-3);c.stroke()}c.restore();
    [.3,.58].forEach(p=>mgCyl(c,x+w*p,y-h*.12,w*.07,h*1.24,'#8e98a3',4));            // nuts
    mgCyl(c,x+w*.74,y+h*.12,w*.12,h*.76,'#4f5b69',5);                             // rear cap
    const led=e.led!=null&&tl>=e.led&&(e.ledEnd==null||tl<e.ledEnd),lx=x+w*.8,ly=y+h*.12;
    if(led){c.save();const g=c.createRadialGradient(lx,ly,0,lx,ly,h*.6);g.addColorStop(0,'rgba(255,176,32,.55)');g.addColorStop(1,'rgba(255,176,32,0)');c.fillStyle=g;c.beginPath();c.arc(lx,ly,h*.6,0,7);c.fill();c.restore()}
    c.beginPath();c.arc(lx,ly,h*.13,0,7);c.fillStyle=led?'#ffb020':'#dfe3e8';c.fill();c.lineWidth=2.5;c.stroke();
    c.save();c.lineCap='round';c.lineWidth=8;c.strokeStyle='#22262c';c.beginPath();c.moveTo(x+w*.86,cy);c.lineTo(x+w,cy);c.stroke();c.lineWidth=2;c.strokeStyle='rgba(255,255,255,.35)';c.beginPath();c.moveTo(x+w*.86,cy-2);c.lineTo(x+w,cy-2);c.stroke();c.restore();
    if(e.wires){[['#8b5a2b',-1],['#2f6fd6',0],['#1d1d1f',1]].forEach(([col,k])=>{c.strokeStyle=col;c.lineWidth=5;c.lineCap='round';c.beginPath();c.moveTo(x+w,cy);c.quadraticCurveTo(x+w+18,cy+k*14,x+w+34,cy+k*16);c.stroke()})}
  }
  else if(T==='box'){ // isometric cardboard box, slides from fromX to x between mv[0]..mv[1]
    let x=e.x;if(e.mv){const k=mgEase(clamp((tl-e.mv[0])/(e.mv[1]-e.mv[0])));x=e.fromX+(e.x-e.fromX)*k}
    const y=e.y,w=e.w,h=e.h,d=w*.28;mgShadow(c,x+w*.55,y+h+4,w*.75,10,.22);
    c.fillStyle='#e7b479';c.beginPath();c.moveTo(x,y);c.lineTo(x+d,y-d*.55);c.lineTo(x+w+d,y-d*.55);c.lineTo(x+w,y);c.closePath();c.fill();c.stroke();   // top
    c.fillStyle='#b98049';c.beginPath();c.moveTo(x+w,y);c.lineTo(x+w+d,y-d*.55);c.lineTo(x+w+d,y+h-d*.55);c.lineTo(x+w,y+h);c.closePath();c.fill();c.stroke(); // side
    const g=c.createLinearGradient(x,y,x,y+h);g.addColorStop(0,'#dca266');g.addColorStop(1,'#c88a4f');c.fillStyle=g;ngRR(c,x,y,w,h,2);c.fill();c.stroke(); // front
    c.fillStyle='#f3e2c4';c.beginPath();c.moveTo(x+w*.42,y);c.lineTo(x+w*.42+d,y-d*.55);c.lineTo(x+w*.58+d,y-d*.55);c.lineTo(x+w*.58,y);c.closePath();c.fill();c.stroke();
  }
  else if(T==='conv'){ // 2.5D belt: top surface in depth, side frame, rollers turn and belt texture moves while running (e.run=[[a,b],...])
    const x=e.x,y=e.y,w=e.w,h=e.h||40,d=h*.9;let ph=0;(e.run||[]).forEach(([a,b])=>{ph+=Math.max(0,Math.min(tl,b)-a)});
    mgShadow(c,x+w/2+d*.4,y+h+96,w*.62,16,.18);
    c.fillStyle='#8e98a3';[x+30,x+w-30].forEach(lx=>{mgCyl(c,lx-7,y+h,14,92,'#9aa3af',3);mgCyl(c,lx-7+d,y+h-d*.5,14,92,'#7b8592',3)});
    c.fillStyle='#2b2f36';c.beginPath();c.moveTo(x+h/2,y);c.lineTo(x+h/2+d,y-d*.5);c.lineTo(x+w-h/2+d,y-d*.5);c.lineTo(x+w-h/2,y);c.closePath();c.fill();c.stroke(); // belt top
    c.save();c.beginPath();c.moveTo(x+h/2,y);c.lineTo(x+h/2+d,y-d*.5);c.lineTo(x+w-h/2+d,y-d*.5);c.lineTo(x+w-h/2,y);c.closePath();c.clip();c.strokeStyle='rgba(255,255,255,.14)';c.lineWidth=3;
      const sp=34,off=(ph*120)%sp;for(let xx=x-d+off;xx<x+w+d;xx+=sp){c.beginPath();c.moveTo(xx,y+2);c.lineTo(xx+d,y-d*.5);c.stroke()}c.restore();
    const g=c.createLinearGradient(0,y,0,y+h);g.addColorStop(0,'#b9c2cc');g.addColorStop(.5,'#8e98a3');g.addColorStop(1,'#5d6b7a');ngRR(c,x,y,w,h,h/2);c.fillStyle=g;c.fill();c.stroke(); // side frame
    [x+h/2,x+w-h/2].forEach(rx=>{const rg=c.createRadialGradient(rx-4,y+h/2-4,2,rx,y+h/2,h/2);rg.addColorStop(0,'#eef1f4');rg.addColorStop(1,'#8e98a3');c.fillStyle=rg;c.beginPath();c.arc(rx,y+h/2,h/2-5,0,7);c.fill();c.stroke();const a=ph*6;c.beginPath();c.moveTo(rx,y+h/2);c.lineTo(rx+Math.cos(a)*(h/2-8),y+h/2+Math.sin(a)*(h/2-8));c.stroke()});
  }
  else if(T==='plc'){ // 2.5D compact PLC: top + side faces, terminals, input LEDs
    const x=e.x,y=e.y,w=e.w,h=e.h,d=Math.min(30,w*.12);mgShadow(c,x+w/2+d/2,y+h+8,w*.62,12,.2);
    c.fillStyle='#c9d0d8';c.beginPath();c.moveTo(x,y);c.lineTo(x+d,y-d*.6);c.lineTo(x+w+d,y-d*.6);c.lineTo(x+w,y);c.closePath();c.fill();c.stroke();
    c.fillStyle='#a9b2bd';c.beginPath();c.moveTo(x+w,y);c.lineTo(x+w+d,y-d*.6);c.lineTo(x+w+d,y+h-d*.6);c.lineTo(x+w,y+h);c.closePath();c.fill();c.stroke();
    const g=c.createLinearGradient(0,y,0,y+h);g.addColorStop(0,'#fbfcfd');g.addColorStop(1,'#dde2e8');c.fillStyle=g;ngRR(c,x,y,w,h,8);c.fill();c.stroke();
    c.fillStyle='#cfd5dc';ngRR(c,x+8,y+8,w-16,h*.22,6);c.fill();c.stroke();
    const n=8;for(let i=0;i<n;i++){const tx=x+20+i*(w-40)/(n-1),ty=y+8+h*.11;const rg=c.createRadialGradient(tx-2,ty-2,1,tx,ty,6);rg.addColorStop(0,'#fff');rg.addColorStop(1,'#9aa3af');c.beginPath();c.arc(tx,ty,6,0,7);c.fillStyle=rg;c.fill();c.lineWidth=2;c.stroke()}
    c.lineWidth=3;ngTxt(c,e.label||'PLC',x+w*.28,y+h*.62,Math.round(h*.16),NG.navy,800);
    const on=e.on!=null&&tl>=e.on&&(e.onEnd==null||tl<e.onEnd);
    ['X0','X1','X2','X3'].forEach((l,i)=>{const lx=x+w*.56+i*w*.11,ly=y+h*.55;if(i===0&&on){c.save();const gg=c.createRadialGradient(lx,ly,0,lx,ly,22);gg.addColorStop(0,'rgba(34,179,94,.55)');gg.addColorStop(1,'rgba(34,179,94,0)');c.fillStyle=gg;c.beginPath();c.arc(lx,ly,22,0,7);c.fill();c.restore()}
      c.beginPath();c.arc(lx,ly,7,0,7);c.fillStyle=i===0&&on?NG.grn:'#d9dde3';c.fill();c.lineWidth=2;c.stroke();ngTxt(c,l,lx,ly+18,11,NG.navy,800)});
  }
  else if(T==='bulb'){ // 24 V lamp: glass sphere with highlight, glow + rays when on
    const cx=e.x+e.w/2,cy=e.y+e.w/2,r=e.w/2,on=e.on!=null&&tl>=e.on&&(e.onEnd==null||tl<e.onEnd);
    if(on){c.save();const gl=c.createRadialGradient(cx,cy,r*.4,cx,cy,r*2.6);gl.addColorStop(0,'rgba(255,210,63,.55)');gl.addColorStop(1,'rgba(255,210,63,0)');c.fillStyle=gl;c.beginPath();c.arc(cx,cy,r*2.6,0,7);c.fill();
      c.strokeStyle='#ffb020';c.lineWidth=4;c.lineCap='round';for(let i=0;i<8;i++){const a=i*Math.PI/4+.2,p=1+.08*Math.sin(tl*7);c.beginPath();c.moveTo(cx+Math.cos(a)*r*1.3,cy+Math.sin(a)*r*1.3);c.lineTo(cx+Math.cos(a)*r*1.65*p,cy+Math.sin(a)*r*1.65*p);c.stroke()}c.restore()}
    const g=c.createRadialGradient(cx-r*.35,cy-r*.35,r*.1,cx,cy,r);g.addColorStop(0,on?'#fffbe6':'#ffffff');g.addColorStop(1,on?'#ffc21f':'#cfd5dc');c.beginPath();c.arc(cx,cy,r,0,7);c.fillStyle=g;c.fill();c.stroke();
    c.save();c.globalAlpha*=.7;c.fillStyle='#fff';c.beginPath();c.ellipse(cx-r*.35,cy-r*.4,r*.22,r*.12,-.6,0,7);c.fill();c.restore();
    mgCyl(c,cx-r*.45,cy+r*.85,r*.9,r*.5,'#8e98a3',4);
  }
}
