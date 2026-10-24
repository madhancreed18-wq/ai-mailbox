import json,re,sys,time
from pocketsphinx import Decoder
key=sys.argv[1]
paras=json.load(open('scripts.json'))[key]
NUM={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
def norm(t):
    t=t.replace('—',' ').replace('/',' ').replace('-',' ').replace('“',' ').replace('”',' ')
    t=re.sub(r"[^A-Za-z0-9' ]"," ",t)
    w=[]
    for x in t.lower().split():
        if x.isdigit(): w+=[NUM.get(c,c) for c in x]
        else: w.append(x.strip("'"))
    return [x for x in w if x]
ADD={'plc':'P IY EH L S IY','ctu':'S IY T IY Y UW','ctd':'S IY T IY D IY','ctud':'S IY T IY Y UW D IY','hsc':'EY CH EH S S IY','subtracts':'S AH B T R AE K T S',"counter's":'K AW N T ER Z','encoder':'EH N K OW D ER','interlocks':'IH N T ER L AA K S',"conveyor's":'K AH N V EY ER Z','identically':'AY D EH N T IH K L IY',"plc's":'P IY EH L S IY Z','acc':'EY S IY S IY'}
DIG=[('ngk','NG K'),('nj','N JH'),('ng','NG'),('zh','L'),('sh','SH'),('ch','CH'),('th','T'),('dh','D'),('kh','K'),('ph','F'),('bh','B'),('gh','G'),('aa','AA'),('ee','IY'),('ii','IY'),('oo','UW'),('uu','UW'),('ai','AY'),('au','AW'),('ae','EY')]
ONE={'a':'AH','e':'EH','i':'IH','o':'OW','u':'UH','k':'K','g':'G','c':'K','j':'JH','t':'T','d':'D','n':'N','p':'P','b':'B','m':'M','y':'Y','r':'R','l':'L','v':'V','w':'W','s':'S','h':'HH','f':'F','z':'Z','x':'K S','q':'K'}
def g2p(w):
    out=[];i=0;prev=None
    while i<len(w):
        m=None
        for a,b in DIG:
            if w.startswith(a,i): m=(a,b);break
        if m: ph=m[1];i+=len(m[0])
        else:
            ch=w[i];i+=1
            if ch not in ONE: continue
            ph=ONE[ch]
            if ph==prev and ph not in('AH','EH','IH','OW','UH'): continue
        out.append(ph);prev=ph
    return ' '.join(out)
d=Decoder(samprate=16000,bestpath=False)
words=[];pidx=[]
for i,p in enumerate(paras):
    for x in norm(p): words.append(x);pidx.append(i)
for w in set(words):
    if w in ADD and d.lookup_word(w) is None: d.add_word(w,ADD[w],True)
    elif d.lookup_word(w) is None: d.add_word(w,g2p(w),True)
t0=time.time();d.set_align_text(' '.join(words))
d.start_utt();d.process_raw(open(key+'.raw','rb').read(),full_utt=True);d.end_utt()
segs=[(s.word,s.start_frame/100,s.end_frame/100) for s in d.seg()]
segs=[s for s in segs if not s[0].startswith('<') and not s[0].startswith('[') and not s[0].startswith('+')]
print('segs',len(segs),'words',len(words),'time',round(time.time()-t0,1))
W=[[re.sub(r'\(\d+\)$','',w),a,b,pidx[k]] for k,(w,a,b) in enumerate(segs)]
json.dump(W,open(key+'.wordtimes.json','w'))
P={}
for w,a,b,p in W:
    if p not in P: P[p]=[a,b]
    P[p][1]=b
json.dump([[P[i][0],P[i][1],paras[i]] for i in range(len(paras))],open(key+'.paras.json','w'),ensure_ascii=False)
for i in range(len(paras)): print(f"{i:02d} {P[i][0]:7.2f} {P[i][1]:7.2f} {paras[i][:60]}")
