"""074: edit the existing CAD source to reproduce 072 control layout in one registered scene.
Run: blender -b --python build_mpcb_v2.py -- [preview|all|panel]
Generic educational internals, not OEM construction or protection settings.
"""
import bpy,sys,json,math
from pathlib import Path
from mathutils import Vector
SOURCE=Path(__file__).resolve().parent
# Reuse original project-native geometry/camera helpers without executing their exports.
scope={'__file__':str(SOURCE/'build_equipment.py')};saved=sys.argv;sys.argv=['blender','--','helpers'];exec(compile((SOURCE/'build_equipment.py').read_text(),str(SOURCE/'build_equipment.py'),'exec'),scope);sys.argv=saved
globals().update({k:v for k,v in scope.items() if k not in ['__name__','__file__','MODE']})
# Helpers retain their own globals in scope, so all geometry calls share these objects.
OUT=SOURCE.parent;scope['OUT']=OUT
MODE=saved[saved.index('--')+1] if '--' in saved else 'all'

def configure():
 scope['setup']();globals().update({k:scope[k] for k in ['white','gray','dark','steel','copper','brass','black','red','GROUPS','META']})
 s=bpy.context.scene;s.cycles.samples=80
 # Product plastic texture, subtle enough to stay clean at panel scale.
 for mat in [white,black]:
  nd=mat.node_tree.nodes;links=mat.node_tree.links;n=nd.new('ShaderNodeTexNoise');n.inputs['Scale'].default_value=90;n.inputs['Roughness'].default_value=.6;b=nd.new('ShaderNodeBump');b.inputs['Strength'].default_value=.055;b.inputs['Distance'].default_value=.025;links.new(n.outputs['Fac'],b.inputs['Height']);links.new(b.outputs['Normal'],nd.get('Principled BSDF').inputs['Normal'])

def capsule(n,x,y,z,w,h,mat,g):
 return box(n,(x,y,z),(w,.3,h),mat,g,min(w,h)*.4)

def screw_front(n,x,y,z,r,g):
 cyl(n,(x,y,z),r,.85,steel,g,'Y',64,.1)
 box(n+' horizontal recess',(x,y-.5,z),(r*1.45,.12,.32),dark,g,.06)
 box(n+' vertical recess',(x,y-.51,z),(.32,.12,r*1.45),dark,g,.06)

def terminal_v2(x,z,label,g):
 # Cage/pole stays a single layer including its external screw cap and identity.
 box('Screw clamp enclosure',(x,-30,z),(13,16,12),white,g,.5)
 cyl('Round terminal well',(x,-38.2,z),3.1,.35,dark,g,'Y',64,.08)
 cyl('Brass clamp rim',(x,-38.45,z),2.65,.35,brass,g,'Y',64,.08)
 screw_front('Recessed clamping screw',x,-38.8,z,2.15,g)
 box('Cable entry from top',(x,-31,z+6.1),(6,8,.18),dark,g,.5)
 text(label,(x,-39.4,z+3.2),2.05,black,g)

def ringtext(txt,x,z,size,g='cover',y=-50.6):return text(txt,(x,y,z),size,black,g)

def build_device():
 configure()
 # Original stepped shell:95mm depth,45mm width,90mm height.
 shell(45,90,91,'housing')
 # White rear and front shoulders, no flat three-column box facade.
 for x in [-21.8,21.8]:
  box('Stepped outer white cheek',(x,-32,45),(1.4,28,88),white,'housing',.55)
 for z in [15,76]:box('Stepped cross shoulder',(0,-32,z),(44,20,7),white,'housing',.6)
 # Visible body moulding ribs/locator recesses, subtle front edge screws.
 for x in [-20,20]:
  for z in [18,74]:screw_front('Housing fastener',x,-42,z,1.05,'housing')
 for x in [-14,0,14]:
  terminal_v2(x,83.5,['1/L1','3/L2','5/L3'][[-14,0,14].index(x)],'terminals')
  terminal_v2(x,6.5,['2/T1','4/T2','6/T3'][[-14,0,14].index(x)],'terminals')
 # 072 distinctive wide upper louvres are common to closed/cut shell.
 box('Upper louvred nose',(0,-40,74),(44,18,8),white,'housing',.5)
 for z in [71.6,74,76.4]:
  for x in [-18,-12,-6,0,6,12,18]:capsule('Horizontal ventilation aperture',x,-49.13,z,3.7,.85,dark,'housing')
 # Front removable plate; split cover to expose one pole while keeping other two closed.
 box('Single-piece removable control facade',(0,-44.5,43.2),(44,10,53.5),white,'cover',.55)
 for x in [0,14.7]:box('Other poles retained cover',(x,-39.1,43.2),(14.6,1.3,53),white,'housing',.4)
 # Bottom design strip and exact 072 lettering are on removable cover.
 ringtext('MOTOR PROTECTION',0,23.4,2.8);ringtext('BREAKER',0,19.5,2.8)
 # Rotary control: black round disk, raised vertical handle ON.
 cyl('Rotary detent plate',(7,-50,44),12.7,1.8,gray,'knob-mechanism','Y',96,.35)
 cyl('Rotary black knob',(7,-51.5,44),12.25,2.4,black,'knob-mechanism','Y',96,.4)
 box('Vertical ON paddle',(7,-54.2,44.8),(4.7,4.2,23),black,'knob-mechanism',.8)
 box('White ON index',(7,-56.4,54.1),(.8,.15,4),white,'knob-mechanism',.05)
 # Markings stay with the mechanism layer and are never repositioned for cutaway.
 for txt,x,z,sz in [('I/ON',15,59.8,2.8),('TRIP',-1,58.8,2.1),('O/OFF',-12,33.5,2.15)]:ringtext(txt,x,z,sz,'knob-mechanism',-50.7)
 # Test button and dial are deliberately in different visible locations as072.
 cyl('Red TEST bezel',(-14,-50.2,44),2.9,1.1,white,'knob-mechanism','Y',64,.16)
 cyl('Red TEST pushbutton',(-14,-51.4,44),2.35,1.8,red,'knob-mechanism','Y',64,.3);ringtext('TEST',-8.0,44,1.65,'knob-mechanism',-50.7)
 tube('TEST trip pushrod',[(-14,-47,44),(-14,-27,44),(-11,-27,46)],.45,steel,'knob-mechanism')
 cyl('Rotary internal spindle',(7,-31,44),2.2,28,steel,'knob-mechanism','Y',48,.12)
 tube('Common trip linkage',[(7,-29,44),(2,-29,47),(-6,-29,47),(-12,-29,46)],.7,steel,'knob-mechanism')
 # Screwdriver-slot overload adjustment.
 cyl('Small overload dial',(-14,-50.5,57),3.1,1.5,gray,'dial-cam','Y',64,.25)
 o=box('Overload screwdriver slot',(-14,-51.3,57),(4.7,.2,.65),dark,'dial-cam',.08);o.rotation_euler[1]=math.radians(-45)
 for val,ang in [('6',220),('7',180),('8',140),('9',100),('10',55)]:
  a=math.radians(ang);x=-14+5.1*math.cos(a);z=57+5.1*math.sin(a);ringtext(val,x,z,1.9,'dial-cam',-50.7)
  xx=-14+3.9*math.cos(a);zz=57+3.9*math.sin(a);o=box('Dial calibration tick',(xx,-50.8,zz),(.13,.15,.7),black,'dial-cam',.01);o.rotation_euler[1]=-a
 ringtext('A',-9.2,54.6,1.9,'dial-cam',-50.7)
 cyl('Eccentric setting cam',(-14,-24,57),3.8,2.2,brass,'dial-cam','Y',64,.1)
 tube('Cam trip lever',[(-14,-26,54),(-10,-26,52),(-11,-26,40),(-14,-26,38)],.5,steel,'dial-cam')
 # Educational single open pole, all components inside common shell envelope.
 coil(-14,66,'coil',3.2,9,-24)
 cyl('Steel magnetic plunger',(-14,-24,65),1.25,10,steel,'plunger','Z',64,.1)
 cyl('Lower trip striker',(-14,-24,58),.7,5,steel,'plunger','Z',48,.1)
 tube('Top terminal to winding',[(-14,-25,80),(-14,-25,73),(-14,-25,70)],.8,copper,'coil')
 # Heater wraps directly around strip; all3thermal strips connect to common slider.
 for x in [-14,0,14]:
  box('Bimetal strip',(x,-24,28),(1.25,1.1,20),steel,'bimetal-heater',.07)
  pts=[]
  for i in range(80):
   t=i/79*2*math.pi*11;pts.append((x+2.1*math.cos(t),-24+1.8*math.sin(t),19+i/79*17))
  tube('Continuous heater around bimetal',pts,.35,copper,'bimetal-heater')
  tube('Lower terminal thermal conductor',[(x,-24,18),(x,-25,10)],.8,copper,'bimetal-heater')
 for x in [-17.4,-10.6]:
  tube('Fixed copper contact conductor',[(x,-24,50.3),(x,-24,55),(-14,-24,60 if x<-14 else 39)],.65,copper,'fixed-contact')
  cyl('Fixed silver contact',(x,-26,50.2),1.15,.8,steel,'fixed-contact','Z',48,.08)
 box('Double-break moving contact bridge',(-14,-27,48.7),(9,2,1.1),copper,'moving-contact',.18)
 for x in [-17.4,-10.6]:cyl('Moving silver contact',(x,-27,49.4),1.1,.6,steel,'moving-contact','Z',48,.08)
 tube('Contact bridge actuator',[(-14,-27,48.3),(-14,-27,46),(-7,-27,46)],.55,steel,'moving-contact')
 for side in [-1,1]:
  for j in range(8):box('Parallel steel arc splitter',(-14+side*5,-22,49+j*.8),(2.5,7,.32),steel,'arcchamber',.035)
 box('Arc chamber insulating backing',(-14,-16,51.5),(13,1,12),gray,'arcchamber',.2)
 box('Phase-loss differential slider',(0,-42,38.2),(39,1.8,1.8),steel,'phaseloss-slide',.2)
 for x in [-14,0,14]:box('Differential thermal sensing finger',(x,-38,37.3),(1.8,9,2),brass,'phaseloss-slide',.1)
 hint('knob-mechanism',(7,-50,44));hint('dial-cam',(-14,-50.5,57));hint('bimetal-heater',(-14,-24,18),(-14,-24,38));hint('moving-contact',(-14,-27,48.7),travel=(0,0,-3));hint('plunger',(-14,-24,65),travel=(0,0,-3));hint('phaseloss-slide',(0,-42,38.2),travel=(1.2,0,0))
 
 fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
 if Path(fontpath).exists():
  font=bpy.data.fonts.load(fontpath)
  for o in bpy.context.scene.objects:
   if o.type=='FONT':o.data.font=font
 camera((0,0,44),108.6,1536,1536)
 # Closed renders hide extra interior metal via physically opaque cover geometry.
 return ['housing','cover','terminals','knob-mechanism','dial-cam']

LAYERS=['housing','terminals','coil','bimetal-heater','fixed-contact','arcchamber','moving-contact','plunger','phaseloss-slide','knob-mechanism','dial-cam']
def render_registered_layer(filename,group):
 # Static housing is a depth holdout: hidden-pole internals must not float over covers.
 # Movable parts remain separately animatable on the visible open pole.
 occluders=['housing']+(['terminals'] if group!='terminals' else [])
 for g,objs in GROUPS.items():
  for obj in objs:
   obj.hide_render=g not in [group]+occluders
   obj.is_holdout=(g in occluders and g!=group)
 bpy.context.scene.render.filepath=str(OUT/filename)
 print('REGISTERED LAYER',filename,flush=True)
 bpy.ops.render.render(write_still=True)
 for gg in ['housing','terminals']:
  for obj in GROUPS[gg]:obj.is_holdout=False

def run():
 closed=build_device()
 closed_names=[o.name for g in closed for o in GROUPS[g]]
 
 if MODE not in ['layers','fixedges']:scope['render']('mpcb-front-v2.png',closed)
 if MODE=='preview':return
 rows=[]
 for i,g in enumerate(LAYERS):
  fn='mpcb-cut-'+g+'-v2.png'
  if not ((MODE=='layers' and g=='housing') or (MODE=='fixedges' and g not in ['coil','bimetal-heater'])):render_registered_layer(fn,g)
  row={'file':fn,'canvas':[1536,1536],'position_px':[0,0],'composite_order':i,'motion':'none','objects':[o.name for o in GROUPS[g]]}
  for key,p in META.get(g,{}).items():
   if p is None:continue
   if key=='travel_world_mm':
    anc=META[g]['pivot_world_mm'];a=scope['point'](anc);b=scope['point'](Vector(anc)+Vector(p));row['travel_px']=[round(b[j]-a[j],2) for j in [0,1]];row['motion']='translate'
   else:row['pivot_px' if key.startswith('pivot') else 'bimetal_tip_px']=scope['point'](p);row['motion']='bend' if 'bimetal' in g else 'rotate'
  # Bend all3 strips around individual fixed ends rather than rotate whole layer.
  if g=='bimetal-heater':row['bimetals']=[{'fixed_end_px':scope['point']((x,-24,18)),'tip_px':scope['point']((x,-24,38))} for x in [-14,0,14]]
  rows.append(row)
 data={'schema_version':1,'canvas':[1536,1536],'units':'full source pixels; top-left origin, +x right, +y down','camera':'one locked orthographic camera for front and all layers','closed_controls_identical_objects':True,'static_occlusion':'Housing and terminal depth holdouts baked into isolated part layers; motion past retained covers should be masked by the housing. Two other pole heaters are hidden behind retained covers.','knob_pivot_px':scope['point']((7,-50,44)),'dial_pivot_px':scope['point']((-14,-50.5,57)),'test_centre_px':scope['point']((-14,-51.4,44)),'outline':'common shell geometry, same silhouette envelope; front cover intentionally removed','internal_geometry_status':'generic illustrative mechanism, not an OEM internal construction drawing','layers':rows,'closed_objects':closed_names}
 (OUT/'assets-074.json').write_text(json.dumps(data,indent=2)+'\n')
 (SOURCE/'mpcb-v2-closed-objects.json').write_text(json.dumps(closed_names,indent=2)+'\n')
 # Save with the closed state visible, so append scripts can directly use it.
 for g,objs in GROUPS.items():
  for o in objs:o.hide_render=g not in closed
 bpy.ops.file.pack_all()
 bpy.ops.wm.save_as_mainfile(filepath=str(SOURCE/'mpcb-v2.blend'),compress=True)
 print('DONE074',flush=True)
if MODE!='panel':run()
