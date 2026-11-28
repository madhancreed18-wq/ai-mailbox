from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageEnhance
BL='/usr/share/fonts/opentype/inter/Inter-Black.otf'
OUT='/home/claude/madhancreed18-wq/ai-mailbox/episodes/16-vfd-parameters/'
def F(s):return ImageFont.truetype(BL,s)
def txt(d,xy,t,size,fill,stroke=10,anchor='la'):d.text(xy,t,font=F(size),fill=fill,stroke_width=stroke,stroke_fill='#0b0d12',anchor=anchor)
def prep(p):
  im=Image.open(p).convert('RGB').resize((1280,720),Image.LANCZOS);im=ImageEnhance.Contrast(im).enhance(1.12);return im
def glow(im,cx,cy,r,col):
  g=Image.new('RGBA',im.size,(0,0,0,0));dg=ImageDraw.Draw(g);dg.ellipse([cx-r,cy-r,cx+r,cy+r],fill=col);g=g.filter(ImageFilter.GaussianBlur(r/2.2));im.paste(Image.alpha_composite(im.convert('RGBA'),g).convert('RGB'))
def stamp(im,text,cx,cy,ang,size):
  s=Image.new('RGBA',(900,300),(0,0,0,0));d=ImageDraw.Draw(s);w=d.textlength(text,font=F(size));
  d.rounded_rectangle([450-w/2-30,150-size*.75,450+w/2+30,150+size*.75],radius=18,outline=(220,38,38,235),width=14);d.text((450,150),text,font=F(size),fill=(220,38,38,235),anchor='mm')
  s=s.rotate(ang,resample=Image.BICUBIC,expand=True);im.paste(s,(int(cx-s.width/2),int(cy-s.height/2)),s)
def xmark(d,cx,cy,r,w=26):
  for a,b in [((cx-r,cy-r),(cx+r,cy+r)),((cx-r,cy+r),(cx+r,cy-r))]:d.line([a,b],fill='#0b0d12',width=w+14);
  for a,b in [((cx-r,cy-r),(cx+r,cy+r)),((cx-r,cy+r),(cx+r,cy-r))]:d.line([a,b],fill='#ef4444',width=w)
# A – rage bait
im=prep('/tmp/th/a-1.png');d=ImageDraw.Draw(im);d.rounded_rectangle([272,42,402,96],radius=10,outline='#ef4444',width=7)
stamp(im,'REPLACE!',345,265,-12,62);xmark(d,770,640-0,70)
txt(d,(1240,70),'₹15,000',138,'#facc15',12,'ra');txt(d,(1240,230),'VFD WASTE?',104,'#ffffff',11,'ra')
im.save(OUT+'thumb-A.png')
# B – curiosity
im=prep('/tmp/th/c-1.png');d=ImageDraw.Draw(im);
d.rounded_rectangle([505,82,795,192],radius=14,fill='#facc15',outline='#0b0d12',width=8);txt(d,(650,137),'?',100,'#0b0d12',0,'mm')
txt(d,(40,250),'1 SETTING',118,'#facc15',12);txt(d,(40,400),'= MOTOR',108,'#ffffff',11);txt(d,(40,530),'DEAD',118,'#ef4444',12)
im.save(OUT+'thumb-B.png')
# C – problem question
im=prep('/tmp/th/a-0.png');d=ImageDraw.Draw(im)
xmark(d,740,640,60);txt(d,(1250,60),'RUN ADICHAA',96,'#ffffff',11,'ra');txt(d,(1250,190),'MOTOR ODALA!',96,'#facc15',11,'ra');txt(d,(1250,320),'WHY?',120,'#ef4444',12,'ra')
im.save(OUT+'thumb-C.png')
# Short cover
v=Image.open('/tmp/th/v-0.png').convert('RGB');v=ImageEnhance.Contrast(v).enhance(1.12);d=ImageDraw.Draw(v)
txt(d,(540,1180),'WIRING',150,'#ffffff',14,'mm');txt(d,(540,1350),'CORRECT…',150,'#22c55e',14,'mm');txt(d,(540,1560),'MOTOR',170,'#ffffff',15,'mm');txt(d,(540,1750),'ODALA?',190,'#ef4444',16,'mm')
v.save(OUT+'thumb-short.png')
