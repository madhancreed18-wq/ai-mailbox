"""Deterministic image export / fit / texture-repeat preparation using ffmpeg."""
import json,subprocess,sys
from pathlib import Path
out=Path(__file__).resolve().parent.parent
for j in json.loads(Path(sys.argv[1]).read_text()):
 n=j['name'];w,h=(1024,1024) if n.startswith('hand-') or 'texture' in n else (1536,1024)
 if n=='cardboard-box-texture':w=h=512
 vf=f'scale={w}:{h}:flags=lanczos,format=rgba'
 if n=='ceiling-fan':vf='scale=1382:922:flags=lanczos,format=rgba,pad=1536:1024:(ow-iw)/2:(oh-ih)/2:color=black@0'
 if n=='conveyor-belt-texture':
  # Mirrored 2x2 repeat: opposite boundary pixels are identical.
  filt='[0:v]scale=512:512:flags=lanczos,split=4[a][b][c][d];[b]hflip[b1];[c]vflip[c1];[d]hflip,vflip[d1];[a][b1]hstack[top];[c1][d1]hstack[bottom];[top][bottom]vstack,format=rgba[v]'
  args=['-filter_complex',filt,'-map','[v]']
 else:args=['-vf',vf+",lut=a='if(lte(val,8),0,if(gte(val,245),255,val))'"]
 subprocess.run(['ffmpeg','-v','error','-y','-i',j['path'],*args,'-frames:v','1',str(out/(n+'.png'))],check=True)
 print(n)
