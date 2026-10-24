import json,re,sys
exec(open('psalign2.py').read().split("d=Decoder")[0])
from pocketsphinx import Decoder
al=json.load(open(key+'.align.json'))['paras'];raw=open(key+'.raw','rb').read();TOT=len(raw)/32000
d=Decoder(samprate=16000,bestpath=False)
allw=set(x for p in paras for x in norm(p))
for w in allw:
    if w in ADD and d.lookup_word(w) is None: d.add_word(w,ADD[w],True)
    elif d.lookup_word(w) is None: d.add_word(w,g2p(w),True)
W=[];res=[];bad=0
for i,p in enumerate(paras):
    s=max(0,al[i][0]-.45);e=min(TOT,al[i][1]+.45);ws=norm(p)
    try:
        d.set_align_text(' '.join(ws));d.start_utt();d.process_raw(raw[int(s*16000)*2:int(e*16000)*2],full_utt=True);d.end_utt()
        sg=[(re.sub(r'\(\d+\)$','',x.word),s+x.start_frame/100,s+x.end_frame/100) for x in d.seg() if not x.word.startswith('<') and not x.word.startswith('[') and not x.word.startswith('+')]
        if len(sg)!=len(ws): raise Exception('n')
        for w,a,b in sg: W.append([w,round(a,2),round(b,2),i])
        res.append([sg[0][1],sg[-1][2],'ok'])
    except Exception as ex:
        bad+=1;res.append([al[i][0],al[i][1],'pause'])
json.dump(W,open(key+'.wordtimes.json','w'));json.dump([[r[0],r[1],paras[i],r[2]] for i,r in enumerate(res)],open(key+'.paras.json','w'),ensure_ascii=False)
print('failed paras',bad)
for i,r in enumerate(res): print(f"{i:02d} {r[0]:7.2f} {r[1]:7.2f} {r[2]:5s} | {al[i][0]:7.2f} {al[i][1]:7.2f} {paras[i][:40]}")
