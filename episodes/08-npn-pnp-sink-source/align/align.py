import json,re,sys,numpy as np
txt=open(sys.argv[1]).read();segs=json.load(open(sys.argv[2]))
paras=[p.strip() for p in txt.split('\n\n') if p.strip()]
S=[];P=[]
for pi,p in enumerate(paras):
  for s in re.findall(r'[^.?!]+[.?!]*',p.replace('\n',' ')):
    s=s.strip()
    if s:S.append(s);P.append(pi)
L=np.array([len(re.sub(r'[^A-Za-z0-9]','',s)) for s in S],float)
n,m=len(S),len(segs);d=np.array([b-a for a,b in segs])
rate=L.sum()/d.sum()
INF=1e18;C=np.full((n+1,m+1),INF);B=np.zeros((n+1,m+1),int);C[0,0]=0
cum=np.concatenate([[0],np.cumsum(d)])
for i in range(1,n+1):
  for j in range(1,m+1):
    for k in range(max(0,j-6),j):
      if C[i-1,k]>=INF:continue
      dur=cum[j]-cum[k];exp=L[i-1]/rate
      c=C[i-1,k]+((dur-exp)/ (exp+.6))**2
      gap=segs[k][0]-segs[k-1][1] if k>0 else 1.0
      if i-1>0 and P[i-1]!=P[i-2]: c-=1.2*min(gap,1.1)
      elif i-1>0: c+=0.6*max(0,gap-.75)
      if c<C[i,j]:C[i,j]=c;B[i,j]=k
# allow skipping nothing: must end at m
j=m;out=[]
for i in range(n,0,-1):
  k=B[i,j];out.append((segs[k][0],segs[j-1][1]));j=k
out=out[::-1]
res=[{'t':round(a,2),'end':round(b,2),'p':P[i],'s':S[i]} for i,(a,b) in enumerate(out)]
json.dump(res,open(sys.argv[3],'w'),ensure_ascii=False,indent=0)
print(n,'sentences',m,'segs','rate',round(rate,2),'cost',round(C[n,m],2))
for r in res:
  ex=L[res.index(r)]/rate
  if True: print(f"{r['t']:7.2f}-{r['end']:7.2f} ({r['end']-r['t']:4.1f} vs {ex:4.1f}) p{r['p']:2d} {r['s'][:70]}")
