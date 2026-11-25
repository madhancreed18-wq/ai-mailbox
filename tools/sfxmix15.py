import json,sys,subprocess
from collections import defaultdict
vid,sent,narr,out,which=sys.argv[1:6]
A=json.load(open(sent));d=defaultdict(list)
for a,b,k in A:d[k].append(a)
T=lambda k,i:d[k][min(i,len(d[k])-1)];PS=lambda k:max(0,d[k][0]-.25)
X='/home/claude/work/sfx/';ev=[]
if which=='long':
  bl=T(0,3)+1.6
  ev+=[(T(0,1)+.4+.25*i,'click',.3) for i in range(6)]+[(T(0,2)+.45,'clunk',.6),(T(0,2)+.7,'hum',.25),(bl,'boom',.7),(bl,'spark',.5),(bl+.3,'sizzle',.5),(T(1,2),'buzz',.3)]
  ev+=[(PS(k)-.8,'whoosh2',.22) for k in (2,3,4,11,12,13,14,15,16,17,18,19,20)]
  ev+=[(T(2,2)+1.4,'sizzle',.4),(T(3,5),'spark',.55),(T(3,5),'boom',.35)]
  ev+=[(T(4,2)+.5+.25*i,'click',.3) for i in range(3)]+[(T(4,4)+.5+.25*i,'click',.3) for i in range(3)]+[(T(4,6)+.5,'click',.3)]
  fw=T(8,2)+1.2;pz=T(9,3)+.4;ft=T(10,1)+.8
  ev+=[(fw,'click',.5),(fw+.4,'hum',.25)]+[(pz+.6*i,'tick',.3) for i in range(5)]+[(ft,'buzz',.35),(ft+.1,'ding',.4)]
  ev+=[(T(11,2+i),'pop',.4) for i in range(3)]+[(PS(12)+.3,'pop',.4)]
  op=T(13,1)+1.4;cb=T(14,1)+1.2
  ev+=[(op-.1,'clunk',.55),(op,'spark',.6),(op+.3,'winddown',.35),(T(13,4),'ding',.5),(cb,'boom',.6),(cb,'spark',.45),(cb+.3,'winddown',.35)]
  ev+=[(PS(15)+.8+i*1.4,'clunk',.45) for i in range(4)]+[(T(15,2)+.3,'ding',.35)]
  ev+=[(T(16,1),'buzz',.3),(T(16,2)+1,'ding',.35),(T(17,1)+.3,'clunk',.5),(T(17,2),'buzz',.3),(T(17,4)+.6,'tick',.4)]
  ev+=[(T(18,i),'tick',.3) for i in range(1,7)]+[(T(19,1)+2.6,'pop',.4),(PS(20)+.2,'pop',.4)]
else:
  bl=T(1,1)+1.7
  ev+=[(T(0,1)+.4+.25*i,'click',.3) for i in range(6)]+[(PS(1)+.6,'clunk',.6),(PS(1)+.9,'hum',.25),(bl,'boom',.7),(bl,'spark',.5),(bl+.3,'sizzle',.5)]
  ev+=[(T(2,1)+.1+i,'tick',.35) for i in range(3)]+[(PS(3)+.2,'pop',.4),(T(3,1),'pop',.4),(PS(5)-.7,'whoosh2',.25),(PS(5),'ding',.35),(PS(6),'pop',.4)]
ins=['-i',vid,'-i',narr];fl=[];lab=[]
for i,(t,n,v) in enumerate(ev):
  ins+=['-i',X+n+'.wav'];ms=int(max(0,t)*1000);fl.append(f'[{i+2}:a]aresample=24000,adelay={ms}|{ms},volume={v}[s{i}]');lab.append(f'[s{i}]')
fc=';'.join(fl)+';[1:a]'+''.join(lab)+f'amix=inputs={len(ev)+1}:normalize=0:duration=first,alimiter=limit=0.95[a]'
subprocess.run(['ffmpeg','-v','error','-y',*ins,'-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',out],check=True)
print('mixed',len(ev),'sfx')
