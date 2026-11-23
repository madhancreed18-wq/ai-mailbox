"""Original generic CAD visual models; external envelopes source-backed, internals illustrative.
Blender 4.3: blender -b --python build_equipment.py -- [mcb|mpcb|motor|panel|all]
"""
import bpy,math,json,sys
from pathlib import Path
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
OUT=Path(__file__).resolve().parent.parent
MODE=sys.argv[sys.argv.index('--')+1] if '--' in sys.argv else 'all'
GROUPS={}; META={}; DEVICE=''; W=H=0

def material(n,c,metal=0,rough=.34):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough;return m

def setup():
 global white,gray,dark,steel,copper,brass,blue,black,red,green
 bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False);GROUPS.clear();META.clear()
 s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=48;s.cycles.use_denoising=False;s.render.threads_mode='FIXED';s.render.threads=6;s.render.film_transparent=True;s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGBA';s.render.image_settings.color_depth='8';s.render.image_settings.compression=85;s.render.dither_intensity=0;s.view_settings.view_transform='AgX'
 s.world.use_nodes=True;s.world.node_tree.nodes.get('Background').inputs['Color'].default_value=(.65,.69,.75,1);s.world.node_tree.nodes.get('Background').inputs['Strength'].default_value=.45
 white=material('Unbranded moulded pale-grey polymer',(.70,.72,.73));gray=material('Graphite moulding',(.12,.14,.16));dark=material('Recesses',(.018,.022,.028));steel=material('Machined steel',(.42,.48,.53),.88,.24);copper=material('Copper winding',(.64,.25,.09),.86,.24);brass=material('Brass busbar',(.65,.47,.17),.8,.29);blue=material('Blue motor enamel',(.018,.13,.33),.48,.27);black=material('Black polymer',(.025,.03,.035));red=material('Red test button',(.6,.025,.018));green=material('Green ON mark',(.03,.34,.11))

def obj(o,n,m,g,bev=.3):
 o.name=n;o.data.materials.append(m);GROUPS.setdefault(g,[]).append(o)
 if bev:
  b=o.modifiers.new('Manufactured edge radii','BEVEL');b.width=bev;b.segments=3
  o.modifiers.new('Weighted face normals','WEIGHTED_NORMAL')
 return o

def box(n,p,d,m,g,bev=.3,rot=None):
 bpy.ops.mesh.primitive_cube_add(size=1,location=p);o=bpy.context.object;o.scale=d;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 if rot:o.rotation_euler=rot
 return obj(o,n,m,g,bev)

def cyl(n,p,r,h,m,g,axis='Y',verts=48,bev=.15):
 bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=h,location=p);o=bpy.context.object
 if axis=='Y':o.rotation_euler[0]=math.pi/2
 if axis=='X':o.rotation_euler[1]=math.pi/2
 for f in o.data.polygons:f.use_smooth=abs(f.normal.z)<.9
 return obj(o,n,m,g,bev)

def tube(n,pts,r,m,g):
 cu=bpy.data.curves.new(n,'CURVE');cu.dimensions='3D';cu.bevel_depth=r;cu.bevel_resolution=3;sp=cu.splines.new('POLY');sp.points.add(len(pts)-1)
 for p,co in zip(sp.points,pts):p.co=(*co,1)
 o=bpy.data.objects.new(n,cu);bpy.context.collection.objects.link(o);return obj(o,n,m,g,0)

def text(n,p,size,m,g):
 cu=bpy.data.curves.new(n,'FONT');cu.body=n;cu.align_x='CENTER';cu.align_y='CENTER';cu.size=size;cu.extrude=.018
 o=bpy.data.objects.new(n,cu);bpy.context.collection.objects.link(o);o.location=p;o.rotation_euler=(math.pi/2,0,0);return obj(o,n,m,g,0)

def screw(x,y,z,r,g):
 cyl('Terminal screw',(x,y,z),r,.7,steel,g);box('Screwdriver slot',(x,y-.4,z),(r*1.5,.1,.32),dark,g,.03)

def terminal(x,z,g,width=8,y=-22):
 box('Terminal brass cage',(x,y,z),(width,7,6),brass,g,.3);box('Cable aperture',(x,y-3.55,z-.3),(width*.6,.2,2.3),dark,g,.2);screw(x,y-4.2,z+1,1.6,g)

def coil(x,z,g,r=3.1,height=11,y=-25):
 box('Magnetic steel frame',(x,y+1,z),(r*2+1.2,5,height+2),steel,g,.15)
 pts=[]
 for i in range(481):
  t=i/480*2*math.pi*11;pts.append((x+r*math.cos(t),y-1+r*math.sin(t),z-height/2+height*i/480))
 tube('Copper solenoid winding',pts,.42,copper,g)

def shell(width,height,depth,g):
 box('Back housing shell',(0,depth/2-2,height/2),(width,4,height),white,g,.8)
 for x in [-width/2+.9,width/2-.9]:box('Housing side wall',(x,0,height/2),(1.8,depth,height),white,g,.5)
 for z in [1,height-1]:box('Housing end wall',(0,0,z),(width-2,depth,2),white,g,.4)
 # Actual rear attachment and lower release tab, visible in 3/4 views.
 box('DIN rear fixed hook',(0,depth/2+1,height*.66),(width*.65,3,5),gray,g,.3)
 box('DIN rear lower clip',(0,depth/2+1,height*.25),(width*.65,3,7),gray,g,.3)
 box('DIN bottom release pull tab',(0,depth/2+1,-2),(width*.48,4,4),gray,g,.2)

def camera(center,scale,w,h,view='front'):
 global W,H
 W=w;H=h;s=bpy.context.scene;s.render.resolution_x=w;s.render.resolution_y=h;s.render.resolution_percentage=100
 c=Vector(center);dist=max(scale*4,400);offset=Vector((0,-dist,0)) if view=='front' else Vector((-dist*.62,-dist,dist*.45))
 bpy.ops.object.camera_add(location=c+offset);cam=bpy.context.object;cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=scale;cam.data.clip_end=100000;cam.data.clip_start=.01;s.camera=cam
 for n,off,power,size in [('Upper-left key',(-.7,-1,1.2),125000,scale*1.4),('Front soft fill',(.9,-.8,.4),55000,scale),('Rear rim',(.3,.7,.9),85000,scale)]:
  bpy.ops.object.light_add(type='AREA',location=c+Vector(off)*scale);l=bpy.context.object;l.name=n;l.data.energy=power*(scale/100)**2;l.data.size=size;l.rotation_euler=(c-l.location).to_track_quat('-Z','Y').to_euler()
 bpy.context.view_layer.update();return cam

def point(p):
 v=world_to_camera_view(bpy.context.scene,bpy.context.scene.camera,Vector(p));return [round(v.x*W,2),round((1-v.y)*H,2)]

def hint(g,pivot=None,tip=None,travel=None):
 META[g]={'pivot_world_mm':pivot,'bimetal_tip_world_mm':tip,'travel_world_mm':travel}

def render(name,groups):
 allobjs=[o for a in GROUPS.values() for o in a]
 selected={o for g in groups for o in GROUPS.get(g,[])}
 for o in allobjs:o.hide_render=o not in selected
 s=bpy.context.scene;s.render.filepath=str(OUT/name);print('RENDER',name,flush=True);bpy.ops.render.render(write_still=True)

def export_layers(device,names):
 rows=[]
 for i,g in enumerate(names):
  filename=device+'-cut-'+g+'.png';render(filename,[g]);d={'file':filename,'canvas':[W,H],'composite_order':i,'position_px':[0,0],'illustrative_motion':True,'objects':[o.name for o in GROUPS[g]]}
  for k,p in META.get(g,{}).items():
   if p is None:continue
   if k=='travel_world_mm':
    anchor=META[g].get('pivot_world_mm') or (0,0,0);a=point(anchor);b=point(Vector(anchor)+Vector(p));d['travel_px']=[round(b[0]-a[0],2),round(b[1]-a[1],2)]
   else:d['pivot_px' if k.startswith('pivot') else 'bimetal_tip_px']=point(p)
  rows.append(d)
 (OUT/(device+'-layer-registration.json')).write_text(json.dumps({'canvas':[W,H],'camera':'fixed orthographic front','units':'pixels, top-left origin','internal_geometry_status':'generic educational mechanism, not an OEM manufacturing section','layers':rows},indent=2))
 # Composite is deliberately defined by the isolated layer stack, without cross-layer shadows.
 bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'source'/(device+'.blend')))

def fit_envelope(width,height,depth):
 from mathutils import Matrix
 objs=list({o for a in GROUPS.values() for o in a});bpy.context.view_layer.update()
 pts=[o.matrix_world@Vector(c) for o in objs for c in o.bound_box]
 lo=Vector([min(p[i] for p in pts) for i in range(3)]);hi=Vector([max(p[i] for p in pts) for i in range(3)])
 sc=Vector((width/(hi.x-lo.x),depth/(hi.y-lo.y),height/(hi.z-lo.z)))
 tr=Vector((-(lo.x+hi.x)*sc.x/2,-(lo.y+hi.y)*sc.y/2,-lo.z*sc.z))
 transform=Matrix.Translation(tr)@Matrix.Diagonal((*sc,1))
 for o in objs:o.matrix_world=transform@o.matrix_world
 for row in META.values():
  for k,v in row.items():
   if v is not None:row[k]=list(Vector((v[0]*sc.x,v[1]*sc.y,v[2]*sc.z))+(Vector((0,0,0)) if k=='travel_world_mm' else tr))
 bpy.context.view_layer.update()

def build_mcb():
 setup();shell(18,85,70,'housing');
 # stepped front: terminal areas recessed, centre nose forward.
 box('Front terminal cover top',(0,-23,75),(18,20,20),white,'cover',.7);box('Front terminal cover bottom',(0,-23,10),(18,20,20),white,'cover',.7);box('Central front cap',(0,-31.5,42.5),(18,16.5,45),white,'cover',.65)
 for z in [80,5]:
  box('Terminal recess',(0,-33.2,z),(9,.3,6.4),dark,'cover',.4);terminal(0,z,'terminals',9,-29)
 box('Toggle recess',(0,-40,56),(12,.25,10),dark,'cover',.4)
 box('Toggle grip ON',(0,-43,59),(11,6,5),black,'front-toggle',.65,rot=(math.radians(-18),0,0))
 text('C16',(0,-40.2,38),4.4,black,'cover');text('6000',(0,-40.2,29),3,black,'cover')
 for z in [18,68]:
  box('Moulded side step',(0,-15,z),(17,13,2),white,'housing',.3)
 # Internal electrical path, ordered top->coil->contacts->bimetal->bottom.
 coil(-3,66,'coil',2.8,10,-22)
 cyl('Plunger',(-3,-22,69),1.25,9,steel,'plunger','Z');cyl('Striker tip',(-3,-22,61),.7,7,steel,'plunger','Z')
 tube('Top terminal to solenoid',[(0,-24,77),(-3,-24,74),(-3,-24,71)],.75,copper,'coil')
 tube('Solenoid to moving pivot',[(-3,-24,61),(-5,-24,54),(-5,-24,42)],.6,copper,'coil')
 tube('Moving copper contact arm',[(-5,-26,42),(-1,-26,46),(2,-26,46)],.8,copper,'moving-contact');cyl('Silver moving contact',(2,-26.5,46),1.15,1.8,steel,'moving-contact')
 tube('Fixed contact to thermal strip',[(2,-25,47),(4,-25,47),(4,-25,35),(-4,-25,35)],.8,copper,'fixed-contact');cyl('Fixed silver contact',(2,-26.5,48),1.2,1.8,steel,'fixed-contact')
 box('Bimetal thermal strip',(-4,-23,24),(1.4,1.2,24),steel,'bimetal',.08);tube('Bimetal to bottom terminal',[(-4,-23,12),(-4,-23,6),(0,-23,5)],.7,copper,'bimetal')
 for j in range(9):box('Arc splitter plate %02d'%j,(5.2,-24,50+j*.9),(5.3,6,.35),steel,'arcchute',.06)
 for z in [50,59]:box('Arc chute insulating support',(5.2,-21,z),(6,1,1),gray,'arcchute',.1)
 box('Toggle internal rocker',(0,-27,55),(7,3,4),black,'toggle-latch',.3);cyl('Rocker axle',(0,-25,55),1.1,6,steel,'toggle-latch')
 tube('Toggle latch linkage',[(0,-27,55),(-2,-27,51),(-5,-27,42)],.5,steel,'toggle-latch');tube('Trip latch from bimetal',[(-4,-25,35),(-6,-25,39),(-2,-25,51)],.45,steel,'toggle-latch')
 for z in [51,57]:cyl('Mechanism rivet',(-2,-28,z),.65,.8,steel,'toggle-latch')
 hint('toggle-latch',(0,-25,55));hint('moving-contact',(-5,-26,42));hint('bimetal',(-4,-23,12),(-4,-23,36));hint('plunger',(-3,-22,69),travel=(0,0,-3))
 fit_envelope(18,85,78.5)
 cam=camera((0,-1,42.5),100,1024,1536)
 render('mcb-front.png',['housing','cover','front-toggle','terminals'])
 GROUPS['toggle-latch']+=GROUPS['front-toggle']
 export_layers('mcb',['housing','terminals','coil','bimetal','fixed-contact','arcchute','moving-contact','plunger','toggle-latch'])
 # Same pixels/mm as MPCB3q: fixed camera 120mm high on common1536 square.
 for o in [x for x in bpy.context.scene.objects if x.type in ['CAMERA','LIGHT']]:bpy.data.objects.remove(o,do_unlink=True)
 camera((0,0,42.5),125,1536,1536,'threeq');render('mcb-3q.png',['housing','cover','front-toggle','terminals'])

def build_mpcb():
 setup();shell(45,89,82,'housing')
 for x in [-14,0,14]:
  for z in [81,8]:terminal(x,z,'terminals',10,-24)
  for z,labeltxt in [(85.5,['1/L1','3/L2','5/L3'][[-14,0,14].index(x)]),(3.5,['2/T1','4/T2','6/T3'][[-14,0,14].index(x)])]:text(labeltxt,(x,-31,z),2.5,black,'terminals')
  box('Terminal cover',(x,-21,81),(13,10,14),white,'cover',.5);box('Terminal cover',(x,-21,8),(13,10,13),white,'cover',.5)
 for x in [0,14]:box('Unopened pole front',(x,-21,44),(13.8,8,60),white,'housing',.65)
 box('Removed pole face',(-14,-21,44),(13.8,8,60),white,'cover',.65)
 # Actuator lives above the internal pole plane, retained as a detachable layer.
 cyl('Rotary mechanism hub',(3,-29,47),9,5,gray,'knob-mechanism');box('ON rotary handle',(3,-34,50),(5,6,16),black,'knob-mechanism',1)
 text('I',(3,-38,60),3,black,'knob-mechanism');text('O',(-9,-34,48),3,black,'knob-mechanism')
 tube('Knob trip linkage',[(3,-23,47),(-7,-23,44),(-14,-23,43)],.7,steel,'knob-mechanism')
 cyl('Setting dial',(4,-28,68),6,3,white,'dial-cam')
 for val,ang in [('6',150),('8',90),('10',30)]:
  a=math.radians(ang);text(val,(4+8*math.cos(a),-30,68+8*math.sin(a)),2.6,black,'dial-cam')
 box('Setting screwdriver index',(4,-30,69),(1,1,5),black,'dial-cam',.1)
 cyl('Eccentric setting cam',(3,-21,67),3.5,2,brass,'dial-cam');tube('Cam shifts trip lever',[(3,-23,64),(-6,-23,56),(-10,-23,35),(-14,-23,33)],.5,steel,'dial-cam')
 box('TEST button',(17,-28,65),(4,4,4),red,'housing',.3);text('TEST',(17,-30.2,60),1.8,black,'housing')
 # Open left pole only. Other pole thermal elements are inside their closed covers.
 coil(-14,65,'coil',3,10,-15)
 cyl('Magnetic plunger',(-14,-15,68),1.2,10,steel,'plunger','Z');cyl('Trip striker',(-14,-15,60),.7,7,steel,'plunger','Z')
 tube('Top terminal to magnetic winding',[(-14,-20,78),(-14,-20,71)],.75,copper,'coil')
 box('Heated bimetal strip',(-14,-15,22),(1.4,1,24),steel,'bimetal-heater',.08)
 heater_pts=[]
 for j in range(45):
  dx,dy=[(-2,-1.5),(-2,1.5),(2,1.5),(2,-1.5)][j%4];heater_pts.append((-14+dx,-15+dy,12+j*.43))
 tube('Continuous wrapped heater winding',heater_pts,.32,copper,'bimetal-heater')
 tube('Thermal exit to lower terminal',[(-14,-15,10),(-14,-20,8)],.7,copper,'bimetal-heater')
 for x in [-17,-11]:
  cyl('Double break fixed silver contact',(x,-20,45),.95,1.7,steel,'fixed-contact');tube('Fixed pole conductor',[(x,-19,45),(x,-19,54 if x==-17 else 34),(-14,-19,60 if x==-17 else 34)],.65,copper,'fixed-contact')
 box('Double break moving bridge',(-14,-22,43.7),(8,2,1.3),copper,'moving-contact',.2)
 for x in [-17,-11]:cyl('Moving bridge silver tip',(x,-22,44.6),.9,1,steel,'moving-contact','Z')
 tube('Moving bridge actuator',[(-14,-22,43),(-14,-22,40),(-8,-22,40)],.6,steel,'moving-contact')
 for side in [-1,1]:
  for j in range(7):box('Arc chamber splitter',( -14+side*4.4,-17,43+j*.8),(2.4,6,.32),steel,'arcchamber',.04)
 box('Arc chamber separator',(-14,-13,46),(10,1,13),gray,'arcchamber',.2)
 box('Phase-loss differential slider',(0,-27,34),(39,2,2),steel,'phaseloss-slide',.2)
 for x in [-14,0,14]:
  box('Bimetal sensing tab',(x,-26,32),(2,3,4),brass,'phaseloss-slide',.12)
  if x!=-14:box('Other pole hidden bimetal tip',(x,-17,31),(1,1,5),steel,'housing',.05)
 hint('knob-mechanism',(3,-29,47));hint('dial-cam',(4,-28,68));hint('bimetal-heater',(-14,-15,10),(-14,-15,34));hint('moving-contact',(-14,-22,40),travel=(0,0,-3));hint('plunger',(-14,-15,68),travel=(0,0,-3));hint('phaseloss-slide',(0,-27,34),travel=(1.5,0,0))
 fit_envelope(45,89,97)
 camera((0,0,44.5),109,1536,1536)
 closed=['housing','cover','terminals','knob-mechanism','dial-cam'];render('mpcb-front.png',closed)
 export_layers('mpcb',['housing','terminals','coil','bimetal-heater','fixed-contact','arcchamber','moving-contact','plunger','knob-mechanism','dial-cam','phaseloss-slide'])
 for o in [x for x in bpy.context.scene.objects if x.type in ['CAMERA','LIGHT']]:bpy.data.objects.remove(o,do_unlink=True)
 camera((0,0,42.5),125,1536,1536,'threeq');render('mpcb-3q.png',closed)

def motor_geometry():
 cyl('Finned motor frame',(0,0,100),88,240,blue,'motor','X',96,1)
 for j in range(36):
  a=j*2*math.pi/36;o=box('Lengthwise cooling fin',(0,math.sin(a)*93,100+math.cos(a)*93),(224,3,16),blue,'motor',.65);o.rotation_euler[0]=-a
 for x,r,h in [(-124,96,13),(-135,42,12),(126,101,12),(157,102.5,62)]:cyl('Drive shield' if x<0 else 'Non-drive fan cowl',(x,0,100),r,h,blue,'motor','X',96,1)
 # NO shaft outside the fan cowl: only drive end extends toward -X.
 cyl('Drive shaft',(-158,0,100),14,60,steel,'motor','X',80,.6);box('Shaft key',(-161,0,114),(45,8,3),steel,'motor',.25)
 cyl('Drive bearing seal',(-141.5,0,100),21,2,dark,'motor','X')
 for i in range(12):
  a=i*math.pi/6;o=box('Rear fan grille slot',(188.4,math.sin(a)*60,100+math.cos(a)*60),(1,4,26),dark,'motor',.8);o.rotation_euler[0]=-a
 for y in [-80,80]:
  foot=box('Continuous foot',(5,y,7.5),(170,40,15),blue,'motor',1.5)
  for x in [-65,75]:
   box('Cast foot web',(x,math.copysign(62,y),35),(23,18,45),blue,'motor',1)
   bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=6,depth=40,location=(x,y,7.5));hole=bpy.context.object;mod=foot.modifiers.new('Through mounting hole','BOOLEAN');mod.operation='DIFFERENCE';mod.object=hole;bpy.context.view_layer.objects.active=foot;bpy.ops.object.modifier_apply(modifier=mod.name);bpy.data.objects.remove(hole,do_unlink=True)
 box('Top terminal enclosure',(-10,0,200),(122,100,70),blue,'terminalbox',2)
 box('Terminal lid gasket',(-10,0,236),(124,102,2),dark,'terminalbox',1);box('Terminal lid',(-10,0,239),(126,104,4),blue,'terminalbox',1.5)
 for x in [-60,40]:
  for y in [-38,38]:cyl('Terminal lid screw',(x,y,241.4),3,1.5,steel,'terminalbox','Z',48,.15)
 cyl('Cable gland',(-10,-57,203),11,16,gray,'terminalbox','Y',12,.4)
 box('Lifting eye base',(74,0,191),(25,23,8),blue,'motor',1)
 pts=[(74+13*math.sin(i*math.pi/24),0,215+13*math.cos(i*math.pi/24)) for i in range(49)];tube('Lifting eye',pts,3.5,steel,'motor')
 box('Blank side nameplate',(5,-95,113),(69,1.5,31),steel,'motor',.5)
 for x in [-25,35]:
  for z in [101,125]:cyl('Nameplate rivet',(x,-96,z),1.3,1,steel,'motor','Y',24,.1)
 for x in [-130,131]:
  for j in range(4):
   a=math.pi/4+j*math.pi/2;cyl('Shield hex bolt',(x,78*math.sin(a),100+78*math.cos(a)),4,5,steel,'motor','X',6,.2)

def build_motor():
 setup();motor_geometry();camera((0,0,121),535,1536,1024,'threeq');render('motor-3q.png',['motor','terminalbox'])
 # Soot material/state only. Geometry, lighting and camera do not change.
 soot=material('Burnt soot around terminal box',(.013,.009,.007),.05,.95)
 for o in GROUPS['terminalbox']:
  if o.type=='MESH':o.data.materials[0]=soot
 # Small neighbouring upper fins receive darkened paint without changing any meshes.
 for o in GROUPS['motor']:
  if o.name.startswith('Lengthwise') and o.location.z>170:o.data.materials[0]=material('Heat discoloured motor paint',(.025,.045,.065),.25,.55)
 render('motor-3q-burnt.png',['motor','terminalbox']);bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'source'/'motor.blend'))

def contactor(center,g='panel'):
 x0,y0,z0=center
 def b(n,x,y,z,w,d,h,m):return box(n,(x+x0,y+y0,z+z0),(w,d,h),m,g,.5)
 b('Contactor grey base',0,10,38,45,65,77,gray);b('Contactor front body',0,-20,38,44,20,40,white);b('Contactor actuator',0,-34,39,15,9,15,black)
 for x in [-14,0,14]:
  for z,t in [(70,['1/L1','3/L2','5/L3'][[-14,0,14].index(x)]),(7,['2/T1','4/T2','6/T3'][[-14,0,14].index(x)])]:
   b('Contactor terminal block',x,-18,z,12,18,14,white);terminal(x+x0,z+z0,g,8,-27+y0);text(t,(x+x0,-32+y0,z+z0+6),2.5,black,g)
 for x,z,t in [(-18,58,'A1'),(-18,20,'A2'),(17,54,'13'),(17,24,'14')]:
  screw(x+x0,-34+y0,z+z0,1.2,g);text(t,(x+x0,-35+y0,z+z0+4),2,black,g)

def build_panel():
 # Closed-device meshes are linked from the two editable scenes; no redraw drift.
 setup();box('Panel back plate',(0,12,70),(240,3,140),steel,'panel',1)
 for z in [25,55,85,115]:
  box('DIN rail channel',(0,5,z),(210,4,25),steel,'panel',.3)
  for zz in [z-17.5,z+17.5]:box('35mm DIN rail lip',(0,2,zz),(210,2,3),steel,'panel',.2)
 for x in [-111,111]:
  box('Cable duct',(x,-4,70),(15,25,136),white,'panel',.5)
  for z in range(8,135,8):box('Duct slots',(x,-17,z),(11,.2,3),dark,'panel',.05)
 def load_closed(filename,allowed,offset):
  with bpy.data.libraries.load(str(OUT/'source'/filename),link=False) as (data,loaded):loaded.objects=[n for n in data.objects if not n.startswith(('Camera','Upper-left','Front soft','Rear rim'))]
  # Stored objects include mechanism layers hidden. Select by saved groups via sidecar names.
  for o in loaded.objects:
   if o and o.type in ['MESH','FONT','CURVE']:
    bpy.context.collection.objects.link(o);o.location+=Vector(offset)
    if o.hide_render:continue
    GROUPS['panel'].append(o)
 # Instead of accidentally using the last isolated layer's visibility, select exact closed object names.
 def from_scene(filename,names,offset):
  with bpy.data.libraries.load(str(OUT/'source'/filename),link=False) as (src,dst):dst.objects=names
  for o in dst.objects:
   if o:bpy.context.collection.objects.link(o);o.location+=Vector(offset);o.hide_render=False;GROUPS['panel'].append(o)
 # JSON generated below lists exact closed-set identities, invariant across views.
 regs=json.loads((OUT/'source'/'closed-objects.json').read_text())
 from_scene('mcb.blend',regs['mcb'],(-72,-2,28))
 from_scene('mpcb.blend',regs['mpcb'],(-25,-2,27))
 contactor((45,-3,33));camera((0,0,70),285,1920,1080);render('din-panel.png',['panel']);bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'source'/'panel.blend'))

# Capture closed object sets before layer isolation overwrites object visibility.
_original_render=render
CLOSED={}
def render(name,groups):
 if name in ['mcb-front.png','mpcb-front.png']:CLOSED[name.split('-')[0]]=[o.name for g in groups for o in GROUPS.get(g,[])]
 _original_render(name,groups)
 if CLOSED:(OUT/'source'/'closed-objects.json').write_text(json.dumps(CLOSED,indent=2))

if MODE in ['all','mcb']:build_mcb()
if MODE in ['all','mpcb']:build_mpcb()
if MODE in ['all','motor']:build_motor()
if MODE in ['all','panel']:build_panel()
print('DONE',MODE,flush=True)
