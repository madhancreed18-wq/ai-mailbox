import { chromium } from 'playwright';
import { spawn } from 'child_process';
const [TPL,NARR,OUT,SCs,PORT]=process.argv.slice(2);const SC=+SCs,FPS=30,CW=PORT==='p'?720:1280,CH=PORT==='p'?1280:720;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1100}});
p.on('pageerror',e=>console.log('PAGEERR',e.message));
await p.goto('file://'+process.cwd()+'/test.html');await p.waitForTimeout(3000);
await p.setInputFiles('#narrIn',NARR);await p.waitForFunction(()=>window.__T.S.narr,null,{timeout:60000});
await p.evaluate(t=>window.__T.loadTemplate(t),TPL);await p.waitForTimeout(500);
const total=await p.evaluate(()=>window.__T.S.total);
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-i',NARR,'-c:v','libx264','-preset','medium','-crf','21','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',OUT],{stdio:['pipe','inherit','inherit']});
const n=Math.round(total*FPS);
for(let i=0;i<n;i+=30){const arr=await p.evaluate(([a,k,F,sc,cw,ch])=>{const c=document.createElement('canvas');c.width=cw*sc;c.height=ch*sc;const x=c.getContext('2d');const o=[];for(let j=0;j<k;j++){window.__R(x,a+j/F,sc);o.push(c.toDataURL('image/jpeg',.9).split(',')[1])}return o},[i/FPS,Math.min(30,n-i),FPS,SC,CW,CH]);
 for(const d of arr){if(!ff.stdin.write(Buffer.from(d,'base64')))await new Promise(r=>ff.stdin.once('drain',r))}}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('done',OUT,total);
