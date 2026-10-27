import json,numpy as np,wave,sys
d=json.load(open('sfx.json'))
sr=24000
w=wave.open('v1.wav');n=w.getnframes();nar=np.frombuffer(w.readframes(n),dtype=np.int16).astype(np.float32)/32768;w.close()
out=np.zeros(n+sr*2,np.float32);rng=np.random.default_rng(1)
def env(L,a=.002,dcy=.05):
    t=np.arange(L)/sr;return np.minimum(1,t/a)*np.exp(-t/dcy)
def tone(f,dur,dcy=.08,amp=1):
    L=int(dur*sr);t=np.arange(L)/sr;return np.sin(2*np.pi*f*t)*env(L,.003,dcy)*amp
def noise(dur,dcy=.03,amp=1):
    L=int(dur*sr);return rng.standard_normal(L)*env(L,.001,dcy)*amp
def lp(x,k=6):return np.convolve(x,np.ones(k)/k,'same')
def mixs(*xs):
    L=max(len(x) for x in xs);o=np.zeros(L)
    for x in xs:o[:len(x)]+=x
    return o
S={}
S['click']=mixs(lp(noise(.05,.008,.8),3),tone(2200,.04,.01,.4))
S['clack']=mixs(lp(noise(.12,.03,1.0),8),tone(130,.15,.05,.9),tone(1500,.05,.01,.3))
S['clack_off']=mixs(lp(noise(.1,.02,.7),8),tone(100,.12,.04,.6))
S['beep']=tone(1320,.11,.06,.5)
x=np.zeros(int(.25*sr));c1=lp(noise(.03,.006,.9),2);x[:len(c1)]+=c1;x[int(.08*sr):int(.08*sr)+len(c1)]+=c1*.8;S['shutter']=x
a=np.zeros(int(1.6*sr))
for i in range(4):
    b=tone(880 if i%2==0 else 660,.3,.25,.45);a[int(i*.38*sr):int(i*.38*sr)+len(b)]+=b
S['alarm']=a
L=int(.45*sr);t=np.arange(L)/sr;wh=np.convolve(rng.standard_normal(L),np.ones(24)/24,'same')*np.sin(np.pi*t/.45)**2*.5;S['whoosh']=wh
S['motor']=tone(80,.4,.2,.3)
lv={'click':.5,'clack':.45,'clack_off':.4,'beep':.35,'shutter':.5,'alarm':.35,'whoosh':.18,'motor':.3}
for t0,k in d['sfx']:
    i=int(t0*sr);x=S[k]*lv[k];m=min(len(x),len(out)-i);out[i:i+m]+=x[:m]
for a0,b0,v in d['run']:
    i0=int(a0*sr);i1=min(int(b0*sr),len(out));L=i1-i0
    if L<=0:continue
    t=np.arange(L)/sr;ramp=np.minimum(1,t/.6)*np.minimum(1,(L/sr-t)/.3)
    f=95+v*.08;out[i0:i1]+=(np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*2*f*t)+.2*np.sin(2*np.pi*3*f*t))*ramp*.035
mix=out[:n]+nar;pk=np.abs(mix).max();print('peak',pk)
if pk>.98:mix*=.98/pk
w=wave.open(sys.argv[1] if len(sys.argv)>1 else 'v1_mix.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(mix,-1,1)*32767).astype(np.int16).tobytes());w.close()
