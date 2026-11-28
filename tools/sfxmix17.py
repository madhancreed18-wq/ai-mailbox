import json,sys,subprocess
from collections import defaultdict
vid,sent,narr,out,which=sys.argv[1:6]
A=json.load(open(sent));d=defaultdict(list)
for a,b,k in A:d[k].append(a)
T=lambda k,i:d[k][min(i,len(d[k])-1)];PS=lambda k:max(0,d[k][0]-.25)
X='/home/claude/work/sfx/';ev=[]
if which=='long':
  ev+=[(T(0,2)+.3,'ding',.3),(T(0,4),'buzz',.4),(T(0,4)+.4,'sizzle',.25),(T(0,5),'hum',.25),(T(1,2),'pop',.4)]
  ev+=[(PS(k)-.8,'whoosh2',.22) for k in (2,3,4,5,6,8,9,10,12,13)]
  ev+=[(T(2,1),'clunk',.4),(T(2,2),'clunk',.4),(T(3,3),'tick',.3),(T(3,6),'ding',.35)]
  ev+=[(T(4,2+i),'pop',.4) for i in range(3)]
  ev+=[(T(5,4),'clunk',.4),(T(5,5),'clunk',.4),(T(5,6),'buzz',.35)]
  ev+=[(T(6,2),'tick',.3),(T(6,4),'tick',.3),(T(6,6),'buzz',.4),(T(7,1)+1,'ding',.35)]
  ev+=[(T(8,3)+1.2,'buzz',.35),(T(8,5),'ding',.35)]+[(T(9,i),'tick',.3) for i in range(1,5)]
  ev+=[(T(10,1),'ding',.5),(T(10,4)+1.6,'sizzle',.25),(T(11,4),'clunk',.35),(T(11,5),'ding',.4),(T(12,2),'pop',.4),(PS(13)+.2,'pop',.4)]
else:
  ev+=[(T(0,4),'clunk',.45),(T(0,5)-.2,'clunk',.45),(PS(2),'clunk',.45),(T(2,2),'buzz',.35),(T(2,4),'sizzle',.3),(T(3,2),'pop',.4),(PS(4)-.7,'whoosh2',.25),(PS(4),'ding',.35),(PS(5),'pop',.4)]
ins=['-i',vid,'-i',narr];fl=[];lab=[]
for i,(t,n,v) in enumerate(ev):
  ins+=['-i',X+n+'.wav'];ms=int(max(0,t)*1000);fl.append(f'[{i+2}:a]aresample=24000,adelay={ms}|{ms},volume={v}[s{i}]');lab.append(f'[s{i}]')
fc=';'.join(fl)+';[1:a]'+''.join(lab)+f'amix=inputs={len(ev)+1}:normalize=0:duration=first,alimiter=limit=0.95[a]'
subprocess.run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',out],check=True)
print('mixed',len(ev),'sfx')
