/* ---- v21 engagement engine: karaoke captions (exact spoken words), always-moving camera, floating cards ---- */
function drawKcap(e,c,tl){const ws=e.words;if(!ws||!ws.length)return;const fs=e.size||30;c.save();c.font=`700 ${fs}px ${ngFam()}`;
  const gap=fs*.32,maxW=e.maxW||900,lines=[[]];let lw=0;ws.forEach(w=>{const ww=c.measureText(w.w).width;if(lw+ww>maxW&&lines[lines.length-1].length){lines.push([]);lw=0}lines[lines.length-1].push({...w,ww});lw+=ww+gap});
  const lh=fs*1.35,totH=lines.length*lh+18,bw=Math.min(maxW,Math.max(...lines.map(L=>L.reduce((a,w)=>a+w.ww+gap,-gap))))+40,bx=e.cx-bw/2,by=e.cy-totH;
  c.globalAlpha*=.96;ngRR(c,bx,by,bw,totH,18);c.fillStyle='rgba(255,255,255,.93)';c.fill();c.lineWidth=3;c.strokeStyle=O2;c.stroke();c.globalAlpha/=.96;
  lines.forEach((L,li)=>{const W_=L.reduce((a,w)=>a+w.ww+gap,-gap);let x=e.cx-W_/2;const y=by+9+lh*li+lh/2;
    L.forEach(w=>{const on=tl>=w.t,cur=on&&tl<w.e;if(cur){const k=Math.min(1,(tl-w.t)/.12);c.save();c.fillStyle='#fde047';ngRR(c,x-6,y-fs*.62,w.ww+12,fs*1.24,8);c.fill();c.restore()}
      c.fillStyle=on?O2:'#9aa3b2';c.textAlign='left';c.textBaseline='middle';const s=cur?1.08:1;c.save();c.translate(x+w.ww/2,y);c.scale(s,s);c.fillText(w.w,-w.ww/2,1);c.restore();x+=w.ww+gap})});c.restore()}
function o2captions(s,A,paras,o){const SP=paras.map(p=>(p.match(/[^.?!]+[.?!]*/g)||[]).map(x=>x.trim()).filter(Boolean));const k={};
  A.forEach(([a,b,p],idx)=>{const i=k[p]||0;k[p]=i+1;const txt=(SP[p]||[])[i];if(!txt)return;const ws=txt.split(/\s+/),L=ws.reduce((x,w)=>x+w.length+1,0);let t=a;
    const words=ws.map(w=>{const d=(b-a)*(w.length+1)/L,o_={w,t,e:t+d};t+=d;return o_});const nx=A[idx+1],end=nx?Math.min(nx[0],b+.6):b+.6;
    s.els.push({id:uid++,type:'ngd',kind:'kcap',x:0,y:0,w:W,h:H,cx:o.cx,cy:o.cy,maxW:o.maxW,size:o.size,words,noPop:true,draw:.1,delay:0,withPrev:true,entrance:'none',motion:'none',win:[a-.05,end]})})}
function o2camera(s,cuts,o={}){const ev=s.els.filter(e=>e.type==='ngd'&&e.win&&!['mg','wipe2','flash','kcap'].includes(e.kind)&&e.w<W*.9).map(e=>({t:e.win[0],x:e.x+e.w/2,y:e.y+e.h/2}));
  s.els.filter(e=>e.type==='stick'&&e.win).forEach(e=>ev.push({t:e.win[0]+.2,x:(e.x||0)+(e.size||400)/2,y:(e.y||0)+(e.size||400)/2}));
  ev.sort((a,b)=>a.t-b.t);const ks=[{t:0,x:W/2,y:H/2,z:1}];let n=0;
  ev.forEach(v=>{if(v.t-ks[ks.length-1].t<1.1)return;const z=1.035+(n++%3)*.022;ks.push({t:v.t,x:W/2+(v.x-W/2)*.28,y:H/2+(v.y-H/2)*.22,z})});
  (cuts||[]).forEach(t=>ks.push({t:t-.05,x:W/2,y:H/2,z:1,cut:1}));ks.sort((a,b)=>a.t-b.t);
  /* continuous motion: each move lasts until the next keyframe; long holds get a slow drift keyframe in between */
  const out=[];ks.forEach((k,i)=>{const nx=ks[i+1];out.push(k);if(nx&&nx.t-k.t>3){const m=(k.t+nx.t)/2;out.push({t:m,x:k.x+(i%2?14:-14),y:k.y+6,z:k.z+.02})}});
  out.forEach((k,i)=>{const nx=out[i+1];k.d=k.cut?.3:Math.max(.6,Math.min(3,nx?nx.t-k.t:1))});s.cam=out}
