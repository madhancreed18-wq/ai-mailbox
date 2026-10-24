import re,json,sys,subprocess
key=sys.argv[1];noise=sys.argv[2] if len(sys.argv)>2 else '-35dB'
lines=json.load(open('scripts.json'))[key]
W=[len(l) for l in lines]
o=subprocess.run(['ffmpeg','-i',key+'.wav','-af',f'silencedetect=noise={noise}:d=0.22','-f','null','-'],capture_output=True,text=True).stderr
TOT=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',key+'.wav'],capture_output=True,text=True).stdout)
sil=[];cur=None
for ln in o.split('\n'):
    m=re.search(r'silence_start: ([\d.]+)',ln)
    if m: cur=float(m.group(1))
    m=re.search(r'silence_end: ([\d.]+)',ln)
    if m and cur is not None: sil.append((cur,float(m.group(1))));cur=None
if cur is not None: sil.append((cur,TOT))
start=sil[0][1] if sil and sil[0][0]<0.05 else 0.0
end=TOT
if sil and sil[-1][1]>=TOT-0.05: end=sil[-1][0]
cands=[(a,b) for a,b in sil if a>start+0.3 and b<end-0.3]
C=len(cands);L=len(lines)
speech=end-start-sum(b-a for a,b in cands);r=speech/sum(W)
INF=1e18
def seg(ja,kb):
    s=start if ja<0 else cands[ja][1];e=end if kb>=C else cands[kb][0];return s,e
def inner(ja,kb): # pause time inside
    return sum(cands[q][1]-cands[q][0] for q in range(ja+1,kb))
lam=1.0
dp=[[INF]*(C+1) for _ in range(L)];bk=[[-1]*(C+1) for _ in range(L)]
for k in range(C+1):
    s,e=seg(-1,k);d=e-s-inner(-1,k);exp=W[0]*r
    if d>0: dp[0][k]=((d-exp)/(exp+1.0))**2-(lam*(cands[k][1]-cands[k][0]) if k<C else 0)
for i in range(1,L):
    exp=W[i]*r
    for k in range(C+1):
        best=INF;bj=-1
        for j in range(max(-1,k-25),k):
            if j<0 or dp[i-1][j]>=INF: continue
            s,e=seg(j,k);d=e-s-inner(j,k)
            if d<=0.25: continue
            c=dp[i-1][j]+((d-exp)/(exp+1.0))**2-(lam*(cands[k][1]-cands[k][0]) if k<C else 0)
            if c<best: best=c;bj=j
        dp[i][k]=best;bk[i][k]=bj
k=C;b=[]
for i in range(L-1,-1,-1): b.append(k);k=bk[i][k]
b=b[::-1];out=[];prev=-1
for i in range(L):
    s,e=seg(prev,b[i]);out.append([round(s,2),round(e,2),lines[i]]);prev=b[i]
json.dump({'total':TOT,'paras':out,'pauses':cands},open(key+'.align.json','w'),ensure_ascii=False)
print(key,'paras',L,'pauses',C,'s/char',round(r,4))
for i,(s,e,t) in enumerate(out): print(f"{i:02d} {s:7.2f} {e:7.2f} {(e-s)/len(t)/r:4.2f} {t[:70]}")
