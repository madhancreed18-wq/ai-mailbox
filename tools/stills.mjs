// node stills.mjs TEMPLATE AUDIO '[[t,"name"],...]' [scale] [p|l]  -> PNG stills at global times
import { chromium } from 'playwright';import fs from 'fs';
const [TPL,NARR,LIST,SCs,PORT]=process.argv.slice(2);const SC=+(SCs||1),CW=PORT==='p'?720:1280,CH=PORT==='p'?1280:720;
const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.cwd()+'/test.html');await p.waitForTimeout(3000);
if(NARR&&NARR!=='-'){await p.setInputFiles('#narrIn',NARR);await p.waitForFunction(()=>window.__T.S.narr,null,{timeout:60000})}
await p.evaluate(t=>window.__T.loadTemplate(t),TPL);await p.waitForTimeout(500);
for(const [t,n] of JSON.parse(LIST)){const d=await p.evaluate(([t,sc,cw,ch])=>{const c=document.createElement('canvas');c.width=cw*sc;c.height=ch*sc;window.__R(c.getContext('2d'),t,sc);return c.toDataURL('image/png')},[t,SC,CW,CH]);fs.writeFileSync(n+'.png',Buffer.from(d.split(',')[1],'base64'))}
await b.close();
