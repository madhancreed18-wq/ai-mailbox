#!/usr/bin/env node
'use strict';
// Offline deterministic Canvas-frame export; no account/session/browser UI access.
const fs = require('node:fs');
const path = require('node:path');
const { spawn, spawnSync } = require('node:child_process');
const { once } = require('node:events');
const { chromium } = require('playwright');

async function main() {
  const argv = process.argv.slice(2), opts = {};
  for (let i = 0; i < argv.length; i += 2) {
    if (!argv[i].startsWith('--') || argv[i + 1] == null) throw Error('Use --name value pairs.');
    opts[argv[i].slice(2)] = argv[i + 1];
  }
  const template = opts.template || 'ep6sen';
  if (!['ep6en', 'ep6ta', 'ep6sen', 'ep6sta', 'mixfull', 'promo05'].includes(template)) throw Error('Unsupported template.');
  const source = path.resolve(opts.app || path.join(__dirname, '../app/inkstroke-whiteboard-animator.html'));
  const output = path.resolve(opts.out || 'render.mp4');
  const fps = Number(opts.fps || 30), start = Number(opts.start || 0), scale = Number(opts.scale || 1);
  if (![fps, start, scale].every(Number.isFinite) || fps < 1 || fps > 60 || start < 0 || scale <= 0 || scale > 3) throw Error('Invalid fps/start/scale.');
  if (fs.existsSync(output)) throw Error('Output exists; choose a new filename.');
  let html = fs.readFileSync(source, 'utf8');
  const marker = '/* ---------- Start ---------- */';
  if (!html.includes(marker)) throw Error('Unrecognized app version: start marker missing.');
  const bridge = `
window.__inkstrokeRender = {
  ready: false,
  async build(key) { await loadTemplate(key); S.playing=false; S.pin=false; S.sel=null; return {width:W,height:H,duration:S.total,aspect:S.aspect,scenes:S.scenes.length,captions:S.captions}; },
  frame(t,scale) { const c=document.createElement('canvas'); c.width=Math.round(W*scale); c.height=Math.round(H*scale); renderFrame(c.getContext('2d'),t,scale,false); return c.toDataURL('image/png').split(',')[1]; }
};
`;
  html = html.replace(marker, bridge + marker);
  const boot = "await guard(()=>loadTemplate('ep6en'));S.cur=0;S.pin=false;S.t=0;refresh();";
  if (!html.includes(boot)) throw Error('Unrecognized app startup; inspect source before adapting.');
  html = html.replace(boot, boot + 'window.__inkstrokeRender.ready=true;');
  const browser = await chromium.launch({ ...(opts.browser ? { executablePath: path.resolve(opts.browser) } : {}), headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  let encoder, encoderError = '', errors = [];
  try {
    const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
    page.on('pageerror', e => errors.push(String(e)));
    // Render locally supplied app data only. System font fallbacks are explicit in the report.
    await page.route(/^https?:/, route => route.abort());
    await page.setContent(html, { waitUntil: 'load', timeout: 30000 });
    await page.waitForFunction(() => window.__inkstrokeRender?.ready, { timeout: 60000 });
    const info = await page.evaluate(key => window.__inkstrokeRender.build(key), template);
    const duration = opts.duration == null ? info.duration - start : Number(opts.duration);
    if (!Number.isFinite(duration) || duration <= 0 || start + duration > info.duration + .001) throw Error('Requested interval exceeds the template.');
    const frames = Math.round(duration * fps);
    if (!frames) throw Error('Interval has no frames.');
    fs.mkdirSync(path.dirname(output), { recursive: true });
    const ff = ['-v', 'error', '-n', '-f', 'image2pipe', '-framerate', String(fps), '-vcodec', 'png', '-i', 'pipe:0'];
    if (opts.audio) ff.push('-ss', String(start), '-i', path.resolve(opts.audio), '-map', '0:v:0', '-map', '1:a:0', '-c:a', 'aac', '-b:a', '128k');
    else ff.push('-an');
    ff.push('-t', String(frames / fps), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', output);
    encoder = spawn('ffmpeg', ff, { stdio: ['pipe', 'ignore', 'pipe'] });
    const finished = new Promise((resolve, reject) => { encoder.on('error', reject); encoder.on('close', code => code === 0 ? resolve() : reject(Error('FFmpeg failed: ' + encoderError))); });
    encoder.stderr.on('data', b => { encoderError = (encoderError + b).slice(-4000); });
    encoder.stdin.on('error', () => {});
    for (let i = 0; i < frames; i++) {
      const data = await page.evaluate(({ t, scale }) => window.__inkstrokeRender.frame(t, scale), { t: start + i / fps, scale });
      if (!encoder.stdin.write(Buffer.from(data, 'base64'))) await once(encoder.stdin, 'drain');
      if (i && i % (fps * 5) === 0) process.stdout.write(JSON.stringify({ renderedSeconds: i / fps, totalSeconds: frames / fps }) + '\n');
    }
    encoder.stdin.end();
    await finished;
    if (errors.length) throw Error('Browser errors: ' + errors.join('\n'));
    const probe = spawnSync('ffprobe', ['-v', 'error', '-show_entries', 'stream=codec_type,width,height,avg_frame_rate:format=duration', '-of', 'json', output], { encoding: 'utf8' });
    if (probe.status !== 0) throw Error(probe.stderr);
    const report = { source, template, start, duration: frames / fps, frames, fps, scale, templateInfo: info, audio: opts.audio ? 'supplied track muxed; existing template timings unchanged' : 'silent',
      caveats: ['System font fallbacks used; remote font requests disabled.', 'Reproduction test is not style approval or word-level audio alignment verification.'], output: JSON.parse(probe.stdout) };
    fs.writeFileSync(output + '.json', JSON.stringify(report, null, 2) + '\n');
    process.stdout.write(JSON.stringify(report) + '\n');
  } finally {
    if (encoder && encoder.exitCode === null) encoder.kill();
    await browser.close();
  }
}
main().catch(error => { console.error(error.stack || error); process.exitCode = 1; });
