import json,sys,subprocess
from collections import defaultdict
vid,sent,narr,out,which=sys.argv[1:6]
A=json.load(open(sent));d=defaultdict(list)
for a,b,k in A:d[k].append(a)
T=lambda k,i:d[k][min(i,len(d[k])-1)];PS=lambda k:max(0,d[k][0]-.25)
X='/home/claude/work/sfx/';ev=[]
if which=='long':
  ev+=[(T(0,1)+.3+.25*i,'click',.25) for i in range(6)]+[(T(0,5)+.6,'clunk',.6),(T(0,6)-.2,'ding',.25),(T(0,7)+.5,'click',.5),(T(0,9),'buzz',.3),(T(1,3),'pop',.4)]
  ev+=[(PS(k)-.8,'whoosh2',.22) for k in (2,3,7,8,9,10,12,13,14,15,16,17)]
  sel=T(2,5)+.9
  ev+=[(T(2,0)+1,'click',.3),(T(2,1),'buzz',.25),(T(2,4)+.5,'click',.35),(sel+.9,'click',.35),(sel+1.1,'ding',.4)]
  ev+=[(T(3,1),'tick',.3),(T(3,2)+.7,'click',.45),(T(3,3),'buzz',.3)]+[(T(4,1)+.8*i,'tick',.25) for i in range(3)]
  fix=T(5,5)+1.4
  ev+=[(T(5,2),'tick',.3),(T(5,3)+.4,'click',.4),(T(5,4),'tick',.3),(fix,'ding',.45),(fix+1.6,'click',.45),(fix+1.8,'hum',.25)]
  ev+=[(T(6,2),'tick',.3),(T(6,3)+.4,'tick',.3),(T(6,8)+.4,'click',.4),(T(6,9),'buzz',.3)]
  ev+=[(T(7,1)+.3+.8*i,'tick',.25) for i in range(5)]+[(T(7,6)+1,'sizzle',.35)]
  ev+=[(T(8,1)+.7,'boom',.25),(T(8,1)+.8,'pop',.3)]+[(T(8,5+i),'pop',.4) for i in range(3)]
  ev+=[(T(9,2)+.5,'hum',.3),(T(11,4),'ding',.5),(T(11,5)+.7,'pop',.3)]
  ev+=[(T(12,1)-.4,'buzz',.45),(T(12,4)-.3,'buzz',.45)]
  ev+=[(T(13,2)+.5,'clunk',.4),(T(14,4)+.7,'buzz',.45),(T(14,6)+.6,'tick',.3),(T(14,6)+2,'ding',.4)]
  ev+=[(T(15,i),'tick',.3) for i in range(1,8)]+[(T(16,3),'pop',.4),(PS(17)+.2,'pop',.4)]
else:
  ev+=[(T(0,2)-.2+.25*i,'click',.25) for i in range(6)]+[(T(1,1)+.45,'clunk',.6),(T(1,2)-.1,'ding',.25),(T(2,0)+.6,'click',.5),(T(2,2),'buzz',.3)]
  ev+=[(T(3,2),'pop',.4),(PS(4)-.7,'whoosh2',.25),(PS(4),'ding',.35),(PS(5),'pop',.4)]
ins=['-i',vid,'-i',narr];fl=[];lab=[]
for i,(t,n,v) in enumerate(ev):
  ins+=['-i',X+n+'.wav'];ms=int(max(0,t)*1000);fl.append(f'[{i+2}:a]aresample=24000,adelay={ms}|{ms},volume={v}[s{i}]');lab.append(f'[s{i}]')
fc=';'.join(fl)+';[1:a]'+''.join(lab)+f'amix=inputs={len(ev)+1}:normalize=0:duration=first,alimiter=limit=0.95[a]'
subprocess.run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',out],check=True)
print('mixed',len(ev),'sfx')
