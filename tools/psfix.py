import json,re,sys
exec(open('psalign2.py').read().split("d=Decoder")[0])
from pocketsphinx import Decoder
P=json.load(open(key+'.paras.json'));W=json.load(open(key+'.wordtimes.json'));raw=open(key+'.raw','rb').read();TOT=len(raw)/32000
d=Decoder(samprate=16000,bestpath=False)
for w in set(x for p in paras for x in norm(p)):
    if w in ADD and d.lookup_word(w) is None: d.add_word(w,ADD[w],True)
    elif d.lookup_word(w) is None: d.add_word(w,g2p(w),True)
# group consecutive failed paras, window between neighbours
i=0;n=len(P)
while i<n:
    if P[i][3]=='ok': i+=1;continue
    j=i
    while j<n and P[j][3]!='ok': j+=1
    s=P[i-1][1]+.05 if i>0 else 0;e=P[j][0]-.05 if j<n else TOT
    ws=[];idx=[]
    for q in range(i,j):
        for x in norm(paras[q]): ws.append(x);idx.append(q)
    try:
        d.set_align_text(' '.join(ws));d.start_utt();d.process_raw(raw[int(s*16000)*2:int(e*16000)*2],full_utt=True);d.end_utt()
        sg=[(re.sub(r'\(\d+\)$','',x.word),s+x.start_frame/100,s+x.end_frame/100) for x in d.seg() if not x.word.startswith('<') and not x.word.startswith('[') and not x.word.startswith('+')]
        assert len(sg)==len(ws)
        for k,(w,a,b) in enumerate(sg): W.append([w,round(a,2),round(b,2),idx[k]])
        for q in range(i,j):
            t=[x for k,x in enumerate(sg) if idx[k]==q];P[q]=[t[0][1],t[-1][2],P[q][2],'ok2']
        print('fixed',i,j-1,round(s,2),round(e,2))
    except Exception as ex: print('still failed',i,j-1,ex)
    i=j
W.sort(key=lambda x:x[1]);json.dump(W,open(key+'.wordtimes.json','w'));json.dump(P,open(key+'.paras.json','w'),ensure_ascii=False)
for q in range(n):
    if P[q][3]!='ok': print(q,P[q][0],P[q][1],P[q][3],P[q][2][:50])
