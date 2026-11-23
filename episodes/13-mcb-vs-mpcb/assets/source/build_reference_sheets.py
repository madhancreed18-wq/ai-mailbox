"""Original line drawings; only listed envelope/mounting dimensions are source-backed."""
from pathlib import Path
import math
import cairosvg
OUT=Path(__file__).resolve().parent.parent
class Sheet:
 def __init__(self,title):
  self.s=['<svg xmlns="http://www.w3.org/2000/svg" width="2400" height="1600" viewBox="0 0 2400 1600"><defs><marker id="a" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto-start-reverse"><path d="M9,1 L1,5 L9,9" fill="none" stroke="black" stroke-width="1.3"/></marker></defs><rect width="2400" height="1600" fill="white"/><g stroke="black" stroke-width="2.8" fill="none" stroke-linejoin="round">']
  self.text(100,80,title,42);self.text(100,130,'ORTHOGRAPHIC REFERENCE • DIMENSIONS mm • GENERIC DETAIL OUTLINE',24)
  self.line(90,165,2310,165);self.text(110,235,'FRONT',28);self.text(1170,235,'SIDE',28);self.text(110,960,'TOP',28)
 def line(self,x1,y1,x2,y2,extra=''):self.s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {extra}/>')
 def rect(self,x,y,w,h,r=0):self.s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>')
 def circle(self,x,y,r):self.s.append(f'<circle cx="{x}" cy="{y}" r="{r}"/>')
 def path(self,d):self.s.append(f'<path d="{d}"/>')
 def text(self,x,y,t,size=24,anchor='start'):self.s.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans,sans-serif" font-size="{size}" stroke="none" fill="black" text-anchor="{anchor}">{t}</text>')
 def dimx(self,x1,x2,y,t):
  self.line(x1,y-18,x1,y+18);self.line(x2,y-18,x2,y+18);self.line(x1,y,x2,y,'marker-start="url(#a)" marker-end="url(#a)" stroke-width="1.8"');self.text((x1+x2)/2,y-13,t,24,'middle')
 def dimy(self,x,y1,y2,t):
  self.line(x-18,y1,x+18,y1);self.line(x-18,y2,x+18,y2);self.line(x,y1,x,y2,'marker-start="url(#a)" marker-end="url(#a)" stroke-width="1.8"');self.text(x+18,(y1+y2)/2,t,24)
 def notes(self,lines):
  self.rect(1170,1020,1110,400)
  for i,t in enumerate(lines):self.text(1200,1070+i*46,t,24)
 def save(self,name):
  self.text(100,1510,'Envelope dimensions sourced from manufacturer documentation; see SOURCES.md.',23);self.text(100,1550,'Detail contours are original generic modelling guides, not OEM production drawings.',23)
  self.s.append('</g></svg>');svg=''.join(self.s);(OUT/'source'/(name+'.svg')).write_text(svg);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(OUT/(name+'.png')),output_width=2400,output_height=1600)

def breaker(name,w,h,d,mp=False,cont=False):
 s=Sheet('THREE-POLE CONTACTOR' if cont else 'THREE-POLE MOTOR PROTECTION BREAKER' if mp else 'SINGLE-POLE MINIATURE CIRCUIT BREAKER')
 k=5.5;fx=500-w*k/2;fy=300;fw=w*k;fh=h*k
 s.rect(fx,fy,fw,fh,6);s.dimx(fx,fx+fw,fy-35,str(w));s.dimy(fx+fw+45,fy,fy+fh,str(h))
 poles=3 if mp or cont else 1
 for j in range(poles):
  x=fx+fw*(j+.5)/poles
  for y in [fy+40,fy+fh-40]:s.rect(x-22,y-18,44,36,3);s.circle(x,y,11);s.line(x-8,y,x+8,y)
  if poles==3:s.line(fx+fw*(j+1)/3,fy,fx+fw*(j+1)/3,fy+fh)
 if mp:
  cx=fx+fw*.55;cy=fy+fh*.42;s.circle(cx,cy,44);s.rect(cx-12,cy-40,24,80,4);s.circle(cx,cy-115,25);s.text(cx,cy-108,'8',18,'middle');s.text(cx-37,cy-112,'6',18,'middle');s.text(cx+37,cy-112,'10',18,'middle');s.rect(fx+fw-42,cy-115,20,20,3);s.text(fx+fw-32,cy-130,'TEST',12,'middle')
 elif cont:
  s.rect(fx+fw*.34,fy+fh*.39,fw*.32,fh*.23,5)
  for x,y,t in [(fx+20,fy+fh*.28,'A1'),(fx+20,fy+fh*.72,'A2'),(fx+fw-25,fy+fh*.3,'13'),(fx+fw-25,fy+fh*.7,'14')]:s.circle(x,y,7);s.text(x,y-15,t,17,'middle')
 else:
  s.rect(fx+fw*.18,fy+fh*.3,fw*.64,fh*.16,5);s.text(fx+fw/2,fy+fh*.6,'C16',25,'middle');s.text(fx+fw/2,fy+fh*.72,'6000',20,'middle')
 if poles==3:
  for j in range(3):
   x=fx+fw*(j+.5)/3;s.text(x,fy+15,['1/L1','3/L2','5/L3'][j],15,'middle');s.text(x,fy+fh-7,['2/T1','4/T2','6/T3'][j],15,'middle')
 # Side: source-backed depth/height envelope, generic stepped nose and DIN clip.
 sx=1290;sy=300;sw=d*k;sh=h*k
 s.path(f'M{sx+sw},{sy} H{sx+sw*.25} V{sy+sh*.22} H{sx} V{sy+sh*.78} H{sx+sw*.25} V{sy+sh} H{sx+sw} V{sy+sh*.65} H{sx+sw*.88} V{sy+sh*.35} H{sx+sw} Z')
 s.rect(sx+sw*.88,sy+sh*.37,sw*.08,sh*.26);s.dimx(sx,sx+sw,sy+sh+55,str(d));s.dimy(sx+sw+45,sy,sy+sh,str(h));s.text(sx+sw*.7,sy+sh*.52,'DIN',18,'middle')
 # Top: x=module width, y=depth. Its consistent scale is independent of the other views.
 tk=4.1;tx=500-w*tk/2;ty=1020;tw=w*tk;th=d*tk;s.rect(tx,ty,tw,th,5)
 for j in range(poles):
  x=tx+tw*(j+.5)/poles;s.rect(x-14,ty+28,28,45,3);s.circle(x,ty+50,8)
 s.dimx(tx,tx+tw,ty+th+45,str(w));s.dimy(tx+tw+45,ty,ty+th,str(d))
 s.notes(['VERIFIED ENVELOPE',f'Width {w}   Height {h}   Depth {d}', '1-pole/3-pole widths shown at true physical scale.', 'Terminal and control identifiers follow the brief.', 'DIN attachment outline is generic.', 'No installation clearances are implied.'])
 s.save(name)

def motor():
 s=Sheet('FOOT-MOUNTED TEFC MOTOR — SINGLE DRIVE-END SHAFT');k=2.35
 # front, 218 overall width / 240 overall height, shaft axis 100 above mounting plane
 x=500;y=300;cx=x;cy=y+(240-100)*k
 s.circle(cx,cy,100*k);s.circle(cx,cy,38*k);s.circle(cx,cy,14*k)
 for j in range(12):
  a=j*math.pi/6;s.line(cx+82*k*math.cos(a),cy+82*k*math.sin(a),cx+99*k*math.cos(a),cy+99*k*math.sin(a))
 s.rect(cx-61*k,y,122*k,65*k,4)
 for xx in [-80,80]:s.rect(cx+(xx-20)*k,y+225*k,40*k,15*k,2);s.circle(cx+xx*k,y+232*k,6*k)
 s.dimx(cx-109*k,cx+109*k,y-35,'218');s.dimy(cx+125*k,y,y+240*k,'240');s.dimy(cx-130*k,cy,y+240*k,'100');s.text(cx+45,cy-18,'Ø28',24)
 # side, drive end LEFT; fin direction is horizontal/axial
 sx=1230;sy=300;sk=2.3;axis=sy+140*sk
 s.rect(sx+60*sk,axis-92*sk,254*sk,184*sk,12);s.rect(sx+314*sk,axis-100*sk,62*sk,200*sk,12);s.rect(sx,axis-14*sk,60*sk,28*sk,2)
 for z in range(-75,76,15):s.line(sx+75*sk,axis+z*sk,sx+300*sk,axis+z*sk)
 s.rect(sx+115*sk,sy,122*sk,70*sk,4)
 s.rect(sx+108*sk,sy+225*sk,170*sk,15*sk,3)
 s.dimx(sx,sx+376*sk,sy-35,'376');s.dimx(sx,sx+60*sk,axis+55*sk,'60');s.dimy(sx+405*sk,sy,sy+240*sk,'240');s.dimx(sx+123*sk,sx+263*sk,sy+240*sk+45,'140 foot-hole pitch')
 # top, width 218, longitudinal footprint / four mounting holes 160 x140.
 tx=170;ty=1020;tk=1.75;s.rect(tx+60*tk,ty,316*tk,218*tk,18);s.rect(tx,ty+95*tk,60*tk,28*tk,2);s.rect(tx+115*tk,ty+48*tk,122*tk,122*tk,3)
 for xx in [123,263]:
  for yy in [29,189]:s.circle(tx+xx*tk,ty+yy*tk,6*tk)
 s.dimx(tx,tx+376*tk,ty+218*tk+45,'376');s.dimy(tx+400*tk,ty,ty+218*tk,'218');s.dimy(tx+300*tk,ty+29*tk,ty+189*tk,'160');s.text(tx+55,ty+85,'4 × Ø12',22)
 s.notes(['VERIFIED DIMENSIONS (mm)','L 376 • W 218 • HD 240 • shaft height 100','Drive shaft Ø28, extension 60','Mounting hole pitch 160 × 140; holes Ø12','Fan cowl is opposite drive end: NO rear shaft.','Fin direction is axial. Blank side nameplate.'])
 s.save('ref-motor-sheet')
if __name__=='__main__':
 motor();breaker('ref-mcb-sheet',18,85,78.5);breaker('ref-mpcb-sheet',45,89,97,mp=True);breaker('ref-contactor-sheet',45,77,86,cont=True)
 print('Reference sheets complete')
