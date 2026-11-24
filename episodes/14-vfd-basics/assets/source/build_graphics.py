"""Exact educational waveform assets. Requires numpy and cairosvg."""
from pathlib import Path
import numpy as np
import cairosvg
P=Path(__file__).resolve().parent;OUT=P.parent
blue='#1876ca';dark='#18334d'
def text(x,y,s,size=27):return f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="{size}" fill="{dark}">{s}</text>'
def path(x,y,c,w=3):return '<polyline fill="none" stroke="'+c+'" stroke-width="'+str(w)+'" stroke-linejoin="round" points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in zip(x,y))+'"/>'
def save(name,w,h,body):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'+body+'</svg>'
 (P/(name+'.svg')).write_text(s);cairosvg.svg2png(bytestring=s.encode(),write_to=str(OUT/(name+'.png')))
for f in [50,25]:
 t=np.linspace(0,.08,2401);x=85+t/.08*1360;y=250-140*np.sin(2*np.pi*f*t)
 body=text(85,48,f'{f} Hz',36)+text(1070,48,'Same 80 ms window',24)
 body+=path([85,1450],[250,250],'#8b9eae',2)+path([85,85],[78,422],'#8b9eae',2)+path(x,y,blue,5)
 for ms in [0,20,40,60,80]:body+=text(72+ms/80*1360,458,str(ms)+' ms',22)
 save('sine-'+str(f)+'hz',1536,480,body)
t=np.linspace(0,.08,24001);ref=.85*np.sin(2*np.pi*50*t);tri=4*np.abs((t*1000)%1-.5)-1;pw=np.where(ref>=tri,1,-1)
body=text(85,43,'PWM switching pulses + sine reference',31)+text(85,83,'Illustration: 50 Hz reference / 1 kHz carrier',23)
body+=path([85,1450],[310,310],'#8b9eae',2)+path(85+t/.08*1360,310-150*pw,'#26313c',1.8)+path(85+t/.08*1360,310-150*ref,blue,4)
body+=text(85,558,'Blue: sine reference   /   Dark: switched voltage (normalised)',24)
save('pwm-pulses',1536,600,body)
t=np.linspace(0,.04,2401);v=np.array([np.sin(2*np.pi*50*t+p) for p in [0,-2*np.pi/3,2*np.pi/3]]);r=v.max(axis=0)-v.min(axis=0);smooth=np.zeros_like(r);smooth[0]=1.73
for i in range(1,len(t)):smooth[i]=max(r[i],smooth[i-1]*np.exp(-(t[i]-t[i-1] )/.08))
body=text(45,48,'Three-phase AC → rectified DC → capacitor smoothing',31)
for i,label in enumerate(['3-phase AC','6-pulse rectifier','Capacitor-smoothed DC']):
 x0=50+i*510;body+=text(x0,114,label,26);body+=path([x0,x0+420],[465,465],'#8b9eae',2)
 if i==0:
  body+=path([x0,x0+420],[300,300],'#8b9eae',1)
  for k,c in enumerate(['#d64542','#bd8b16',blue]):body+=path(x0+t/.04*420,300-v[k]*130,c,3)
 else:body+=path(x0+t/.04*420,465-(r if i==1 else smooth)*170,blue,4)
 body+=text(x0,505,'0–40 ms',22)
body+=text(50,568,'Idealised voltage shapes; DC ripple depends on load and capacitance.',23)
save('rectifier-dc',1536,600,body)
body='<rect width="1024" height="640" fill="#bdc2c7"/><rect x="20" y="20" width="984" height="600" rx="14" fill="none" stroke="#34414c" stroke-width="4"/>'
for x in [45,979]:
 for y in [45,595]:body+=f'<circle cx="{x}" cy="{y}" r="11" fill="#626c74"/>'
body+=text(85,100,'3-PHASE INDUCTION MOTOR',39)
for y,left,right in [(185,'POWER','2.2 kW'),(260,'VOLTAGE / CURRENT','415 V / 4.7 A'),(335,'FREQUENCY','50 Hz'),(410,'SPEED / POLES','1440 RPM / 4 POLE'),(485,'CONNECTION','Δ / Y')]:
 body+=text(85,y,left,25)+text(490,y,right,31)+path([80,944],[y+23,y+23],'#73808a',1)
body+=text(85,568,'ILLUSTRATIVE NAMEPLATE',22)
save('motor-nameplate',1024,640,body)
print('5 graphics exported')
