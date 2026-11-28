from PIL import Image,ImageDraw,ImageFont,ImageEnhance
BL='/usr/share/fonts/opentype/inter/Inter-Black.otf';OUT='/home/claude/madhancreed18-wq/ai-mailbox/episodes/17-tank-level-control/'
F=lambda s:ImageFont.truetype(BL,s)
def txt(d,xy,t,size,fill,stroke=10,anchor='la'):d.text(xy,t,font=F(size),fill=fill,stroke_width=stroke,stroke_fill='#0b0d12',anchor=anchor)
def prep(p):im=Image.open(p).convert('RGB').resize((1280,720),Image.LANCZOS);return ImageEnhance.Contrast(im).enhance(1.12)
# A
im=prep('/tmp/t17/a-0.png');d=ImageDraw.Draw(im)
txt(d,(1250,60),'0 ERRORS ✓',84,'#22c55e',10,'ra');txt(d,(1250,180),'TANK',140,'#ffffff',12,'ra');txt(d,(1250,330),'OVERFLOW?!',118,'#ef4444',12,'ra')
im.save(OUT+'thumb-A.png')
# B – the rung itself
im=prep('/tmp/t17/a-0.png');d=ImageDraw.Draw(im)
sh=Image.open('/tmp/L-00027.png').convert('RGB');w,h=sh.size;lad=sh.crop((int(w*.02),int(h*.105),int(w*.98),int(h*.415)));lad=lad.resize((700,int(700*lad.height/lad.width)))
im.paste(lad,(560,30));d=ImageDraw.Draw(im);cx,cy=560+int(700*.335),40+int(lad.height*.62);txt(d,(560+640,40+20),'?',130,'#facc15',11,'ra')
txt(d,(1240,440),'1 CONTACT',110,'#facc15',12,'ra');txt(d,(1240,580),'= FLOOD',120,'#ef4444',12,'ra')
im.save(OUT+'thumb-B.png')
# C
im=prep('/tmp/t17/a-0.png');d=ImageDraw.Draw(im)
txt(d,(1250,70),'PUMP',130,'#ffffff',12,'ra');txt(d,(1250,220),'NIKKAVE ILLA!',96,'#facc15',11,'ra');txt(d,(1250,360),'WHY?',150,'#ef4444',13,'ra')
im.save(OUT+'thumb-C.png')
# Short cover
v=Image.open('/tmp/t17/v-0.png').convert('RGB');v=ImageEnhance.Contrast(v).enhance(1.12);d=ImageDraw.Draw(v)
txt(d,(540,180),'PROGRAM OK',130,'#22c55e',13,'mm');txt(d,(540,1560),'TANK',190,'#ffffff',16,'mm');txt(d,(540,1760),'OVERFLOW?',150,'#ef4444',15,'mm')
v.save(OUT+'thumb-short.png')
