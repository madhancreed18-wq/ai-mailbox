import wave,numpy as np,sys,json
w=wave.open(sys.argv[1]);sr=w.getframerate();x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768
hop=int(sr*.01);e=np.array([np.sqrt(np.mean(x[i:i+hop]**2)) for i in range(0,len(x)-hop,hop)])
db=20*np.log10(e+1e-9);thr=float(sys.argv[2]) if len(sys.argv)>2 else -38;mind=float(sys.argv[3]) if len(sys.argv)>3 else .3
sp=db>thr;segs=[];i=0;n=len(sp)
while i<n:
  if sp[i]:
    j=i
    while j<n and (sp[j] or (j+int(mind*100)<n and sp[j:j+int(mind*100)].any())):j+=1
    segs.append([round(i/100,2),round(j/100,2)]);i=j
  else:i+=1
segs=[s for s in segs if s[1]-s[0]>.12]
print(len(segs));json.dump(segs,open(sys.argv[1]+'.segs.json','w'))
print(segs[:8],segs[-3:])
