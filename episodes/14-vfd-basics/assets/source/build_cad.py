"""Original generic EP14 instructional CAD. Not an OEM internal construction drawing.
Blender4.3: blender -b --python build_cad.py -- [vfd|conveyor|extras|all]
Reuses project-native primitives and original motor model from EP13.
"""
import bpy,sys,math,json
from pathlib import Path
from mathutils import Vector
HERE=Path(__file__).resolve().parent;OUT=HERE.parent
HELPER=HERE.parents[2]/'13-mcb-vs-mpcb/assets/source/build_equipment.py'
scope={'__file__':str(HELPER)};argv=sys.argv;sys.argv=['blender','--','helpers'];exec(compile(HELPER.read_text(),str(HELPER),'exec'),scope);sys.argv=argv
for k,v in scope.items():
 if k not in ['__file__','__name__','MODE']:globals()[k]=v
OUT=HERE.parent
scope['OUT']=OUT
MODE=argv[argv.index('--')+1] if '--' in argv else 'all'

def reset():
 scope['setup']();globals().update({k:scope[k] for k in ['white','gray','dark','steel','copper','brass','blue','black','red','green','GROUPS','META']})
 bpy.context.scene.cycles.samples=48
 global pcb,aluminium,brown,tape,led
 pcb=material('Green solder-mask PCB',(.018,.19,.065),.15,.34);aluminium=material('Extruded aluminium',(.59,.64,.68),.85,.26);brown=material('Plain cardboard',(.43,.24,.105),0,.87);tape=material('Kraft carton tape',(.68,.43,.19),0,.6)
 led=material('Red seven segment emission',(.7,.015,.006));p=led.node_tree.nodes.get('Principled BSDF');p.inputs['Emission Color'].default_value=(1,.025,.005,1);p.inputs['Emission Strength'].default_value=3

def finish_fonts():
 p=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
 if p.exists():
  f=bpy.data.fonts.load(str(p));f.pack()
  for o in bpy.context.scene.objects:
   if o.type=='FONT':o.data.font=f

def screw_at(x,y,z,g,r=1.5):
 cyl('Steel screw',(x,y,z),r,.8,steel,g);box('Cross slot',(x,y-.5,z),(r*1.4,.12,.3),dark,g,.04);box('Cross slot',(x,y-.51,z),(.3,.12,r*1.4),dark,g,.04)

def segment_digit(ch,x,y,z,g):
 on={'5':'afgcd','0':'abcedf'}[ch]
 points={'a':(0,5,5.3,.8),'g':(0,0,5.3,.8),'d':(0,-5,5.3,.8),'f':(-3,2.6,.8,4),'b':(3,2.6,.8,4),'e':(-3,-2.6,.8,4),'c':(3,-2.6,.8,4)}
 for key,(dx,dz,w,h) in points.items():box('LED segment '+key,(x+dx,y,z+dz),(w,.18,h),led if key in on else dark,g,.25)

def vfd():
 reset();shell(70,169,136,'housing')
 # Finned rear thermal path, separate names retained for a true rear render.
 rear=[]
 rear.append(box('Heatsink base',(0,65,88),(67,5,154),aluminium,'igbt',.6))
 for x in range(-30,31,5):rear.append(box('Heatsink vertical fin',(x,76,88),(1.5,19,150),aluminium,'igbt',.25))
 for z in [5,164]:box('Mounting ear',(0,65,z),(60,8,8),gray,'housing',.5)
 # Front removable face and terminal cover; vents are discrete moulded openings.
 box('Removable front shell',(0,-65,117),(66,18,100),white,'cover',1.2)
 box('Lower terminal protective cover',(0,-63,32),(66,14,59),white,'cover',1)
 for x in [-31,31]:
  for z in range(25,151,9):box('Side louvre',(x,-73.1,z),(2,.3,4),dark,'cover',.25)
 for z in [157,160.5]:
  for x in [-24,-16,-8,0,8,16,24]:box('Front exhaust slot',(x,-74.15,z),(5,.3,1.2),dark,'cover',.4)
 # PCB, front operator panel and potentiometer share one group and one camera.
 box('Control PCB',(0,-43,120),(60,2,76),pcb,'control',.4)
 for x,z,w,h in [(-23,145,7,10),(24,131,8,12),(-23,109,7,7),(22,99,6,8)]:
  box('Control IC',(x,-45,z),(w,2.4,h),black,'control',.15)
  for dz in [-h/2-.5,h/2+.5]:
   for xx in range(5):box('SMD leg',(x-w*.35+xx*w*.175,-45.1,z+dz),(.35,.6,1),steel,'control',.02)
 box('Keypad front moulding',(0,-75,124),(55,3,62),gray,'control',1)
 box('Display dark lens',(0,-77,144),(48,1,15),dark,'control',.7)
 for ch,x in [('5',-17),('0',-7),('0',7),('0',17)]:segment_digit(ch,x,-77.65,144,'control')
 cyl('Display decimal',(-.8,-77.7,139),.7,.2,led,'control','Y',32,.02)
 for label,x,z,colour in [('RUN',-14,125,green),('STOP',14,125,red),('↑',-17,109,white),('↓',-4,109,white),('ENTER',14,109,white)]:
  box('Key '+label,(x,-78,z),(11 if label!='ENTER' else 16,2,8),colour,'control',.65);text(label,(x,-79.2,z),2.4 if len(label)>1 else 4,black,'control')
 cyl('Potentiometer socket',(0,-70,85),9,4,gray,'control','Y',64,.4)
 cyl('Speed potentiometer',(0,-76,85),7.4,8,black,'control','Y',64,.6)
 box('Pot white pointer',(0,-80.1,89),(1,.12,3.4),white,'control',.12);text('SPEED',(0,-75,72),3,black,'control')
 # Power electronics: intentionally illustrative, individually layered for fly-through.
 box('IGBT module',(3,48,114),(48,11,38),black,'igbt',.7)
 for x in [-17,-9,-1,7,15,23]:box('IGBT power pin',(x,40,91),(1.1,8,8),copper,'igbt',.15)
 for x in [-20,25]:screw_at(x,41.8,115,'igbt',1.8)
 box('Rectifier bridge module',(-17,19,47),(25,13,22),black,'rectifier',.7)
 for z in [40,54]:
  for x in [-25,-17,-9]:box('Rectifier tab',(x,10,z),(3,6,1.2),brass,'rectifier',.12)
 # Two electrolytic cans, viewed from their side with recognisable safety vents.
 for x in [-16,16]:
  cyl('DC bus electrolytic can',(x,-9,64),11,32,black,'dcbus','Z',64,.5)
  cyl('Capacitor aluminium top',(x,-9,80.3),10.2,.7,aluminium,'dcbus','Z',64,.2)
  box('Capacitor sleeve stripe',(x-7,-19,64),(2,.3,26),gray,'dcbus',.1)
  for dx in [-3,3]:cyl('Capacitor lead',(x+dx,-9,46),.6,5,steel,'dcbus','Z',24,.05)
 # DC choke below capacitors, distinct from bridge at different depth.
 cyl('DC choke core',(18,-12,34),10,11,gray,'dcbus','Y',64,.4)
 for i in range(18):
  a=i*2*math.pi/18;pts=[]
  for j in range(17):
   t=j*2*math.pi/16;r=10+2.7*math.cos(t);pts.append((18+r*math.cos(a),-12+6.8*math.sin(t),34+r*math.sin(a)))
  tube('Choke copper turns',pts,.6,copper,'dcbus')
 # Cooling fan under the power stage, no random propeller outside housing.
 box('Cooling fan square frame',(0,11,25),(31,5,31),black,'fan',1)
 cyl('Fan central hub',(0,7,25),4,3,gray,'fan','Y',64,.3)
 for i in range(7):
  a=i*2*math.pi/7;o=box('Fan blade',(7*math.cos(a),7,25+7*math.sin(a)),(10,1,4),gray,'fan',1);o.rotation_euler[1]=-a+.4
 # R/S/T on left, U/V/W on right. PE is additional, not one of the three phases.
 for x,label in zip([-25,-16,-7,7,16,25],['R','S','T','U','V','W']):
  box('Power terminal cage',(x,-37,12),(7,10,9),gray,'terminals',.35);cyl('Brass cable well',(x,-42.2,12),2.2,.4,brass,'terminals');screw_at(x,-42.8,13,'terminals',1.5);text(label,(x,-44,20),3.2,black,'terminals')
 text('PE',(0,-44,5),2.5,black,'terminals');screw_at(0,-43,9,'terminals',1.3)
 finish_fonts();camera((0,0,84.5),202,1536,1536)
 closed=['housing','cover','igbt','rectifier','dcbus','fan','terminals','control'];scope['render']('vfd-front.png',closed)
 closed_names=[o.name for g in closed for o in GROUPS[g]]
 # Housing-only depth holdout clips internals to the common enclosure envelope.
 specs=[('housing',147,(0,65,84.5)),('igbt',125,(3,48,114)),('rectifier',97,(-17,19,47)),('dcbus',69,(0,-9,58)),('fan',89,(0,11,25)),('terminals',41,(0,-37,12)),('control',25,(0,-53,120))]
 rows=[]
 for i,(g,depth,centre) in enumerate(specs):
  for gg,objs in GROUPS.items():
   for o in objs:o.hide_render=gg not in [g,'housing'];o.is_holdout=(gg=='housing' and g!='housing')
  fn=f'vfd-cut-{g}.png';bpy.context.scene.render.filepath=str(OUT/fn);bpy.ops.render.render(write_still=True)
  for o in GROUPS['housing']:o.is_holdout=False
  rows.append({'file':fn,'canvas':[1536,1536],'position_px':[0,0],'composite_order':i,'centre_px':scope['point'](centre),'depth_from_front_mm':depth,'depth_status':'approximate generic model, not OEM measurements','objects':[o.name for o in GROUPS[g]]})
 data={'schema_version':1,'canvas':[1536,1536],'coordinates':'full source pixels, top-left origin,+xright,+ydown','front_face_reference':'keypad face y=-78mm, depth grows toward rear','same_camera':'all front/cut canvases from one locked orthographic camera','layers':rows,'potentiometer_pivot_px':scope['point']((0,-80,85)),'fan_pivot_px':scope['point']((0,7,25)),'component_depths_mm':{'keypad':0,'control_board':35,'IGBT':126,'capacitors':69,'rectifier':97,'back_plate':147},'limits':'Educational internal arrangement; integrated DC choke included per brief, not universal to compact VFDs.'}
 (OUT/'vfd-layers.json').write_text(json.dumps(data,indent=2)+'\n')
 for g,objs in GROUPS.items():
  for o in objs:o.hide_render=False;o.is_holdout=False
 bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(HERE/'vfd.blend'),compress=True)
 # Three-quarter: same device meshes with a simple panel back plate added.
 for o in [o for o in bpy.context.scene.objects if o.type in ['CAMERA','LIGHT']]:bpy.data.objects.remove(o,do_unlink=True)
 box('Mounting panel back plate',(0,92,84.5),(110,3,205),steel,'panel',1)
 camera((0,10,84.5),285,1536,1536,'threeq');scope['render']('vfd-3q.png',closed+['panel'])
 # Rear heatsink straight view, with only thermal assembly shown.
 for o in [o for o in bpy.context.scene.objects if o.type in ['CAMERA','LIGHT']]:bpy.data.objects.remove(o,do_unlink=True)
 cam=camera((0,65,88),190,1536,1536);cam.location.y=850;cam.rotation_euler=(Vector((0,65,88))-cam.location).to_track_quat('-Z','Y').to_euler()
 for light in [o for o in bpy.context.scene.objects if o.type=='LIGHT']:
  light.location.y=abs(light.location.y);light.rotation_euler=(Vector((0,65,88))-light.location).to_track_quat('-Z','Y').to_euler()
 GROUPS['rear_only']=rear;scope['render']('vfd-heatsink-back.png',['rear_only'])
 print('DONE VFD',flush=True)

def conveyor():
 reset();scope['motor_geometry']()
 # Rotate original single-drive-end motor so its shaft points toward the gearbox.
 for g in ['motor','terminalbox']:
  for o in GROUPS[g]:o.location=Vector((-o.location.x+350,-o.location.y-230,o.location.z+380));o.rotation_euler.z+=math.pi
 for y in [-142,142]:
  box('Conveyor structural side rail',(0,y,465),(1250,22,55),steel,'machine',3)
  for x in [-500,450]:box('Conveyor support leg',(x,y,225),(38,38,450),steel,'machine',2);box('Foot plate',(x,y,8),(90,80,16),gray,'machine',2)
 for x in [-600,600]:cyl('Conveyor head roller' if x>0 else 'Conveyor tail roller',(x,0,480),40,278,gray,'machine','Y',96,1)
 belt=material('Black rubber conveyor belt',(.018,.022,.025),0,.8)
 box('Upper conveyor belt',(0,0,522),(1200,280,5),belt,'machine',.8);box('Return belt',(0,0,438),(1200,280,4),belt,'machine',.8)
 box('Motor mounting skid',(380,-230,374),(520,250,12),steel,'machine',2)
 box('Right-angle gearbox',(600,-230,480),(100,110,110),gray,'machine',3)
 for x in [558,642]:
  for z in [438,522]:screw_at(x,-286,z,'machine',4)
 cyl('Motor input coupling',(544,-230,480),22,24,steel,'machine','X',64,1)
 cyl('Gearbox output shaft',(600,-160,480),14,40,steel,'machine','Y',64,.5)
 cyl('Roller shaft coupling',(600,-155,480),22,22,steel,'machine','Y',64,1)
 for x in [565,635]:box('Gearbox mounting pedestal',(x,-230,405),(20,80,50),steel,'machine',2)
 boxes=[]
 for i,x in enumerate([-360,-40,360]):
  o=box('Cardboard carton',(x,0,605),(170,150,160),brown,'boxes',2);boxes.append(o)
  strip=box('Carton tape seam',(x,0,686),(170,25,1.2),tape,'boxes',.1);strip.parent=o;strip.matrix_parent_inverse=o.matrix_world.inverted()
 camera((100,-10,350),2100,1920,1080);cam=bpy.context.scene.camera;cam.location=Vector((100,-2600,1250));cam.rotation_euler=(Vector((100,-10,350))-cam.location).to_track_quat('-Z','Y').to_euler()
 scope['render']('motor-conveyor.png',['machine','motor','terminalbox','boxes'])
 # Only boxes move; camera, machine, shaft coupling and motor are invariant.
 boxes[-1].location=Vector((675,0,560));boxes[-1].rotation_euler.y=math.radians(42)
 o=box('Falling carton',(835,0,285),(170,150,160),brown,'boxes',2,rot=(0,math.radians(62),0));strip=box('Falling carton tape',(835,0,365),(170,25,1.2),tape,'boxes',.1);strip.parent=o;strip.matrix_parent_inverse=o.matrix_world.inverted()
 scope['render']('motor-conveyor-boxes-falling.png',['machine','motor','terminalbox','boxes'])
 bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(HERE/'conveyor.blend'),compress=True)
 (OUT/'conveyor-registration.json').write_text(json.dumps({'same_camera':True,'same_machine_geometry':True,'only_box_poses_change':True,'drive':'Single motor drive shaft -> input coupling -> right-angle gearbox -> coaxial output/head-roller coupling','motor_input_axis':'X','head_roller_output_axis':'Y','canvas':[1920,1080]},indent=2)+'\n')
 print('DONE CONVEYOR',flush=True)

def extras():
 reset();phase=[material('Phase U red',(.65,.025,.015),.65,.3),material('Phase V gold',(.8,.42,.015),.65,.3),material('Phase W blue',(.02,.17,.65),.65,.3)]
 # Stator ring with24slots, four-pole educational3phase winding grouping.
 bpy.ops.mesh.primitive_torus_add(major_segments=96,minor_segments=16,location=(0,0,0),rotation=(math.pi/2,0,0),major_radius=76,minor_radius=15);obj(bpy.context.object,'Laminated stator ring',steel,'stator',0)
 for i in range(24):
  a=i*2*math.pi/24;x,z=59*math.sin(a),59*math.cos(a);o=box('Stator tooth',(x,-2,z),(8,16,16),steel,'stator',.5);o.rotation_euler.y=a
  a2=a+2*math.pi/24;pts=[]
  for r,aa,y in [(67,a,-12),(58,a,-18),(58,a2,-18),(67,a2,-12),(67,a2,3),(67,a,3),(67,a,-12)]:pts.append((r*math.sin(aa),y,r*math.cos(aa)))
  tube('Coloured phase coil group',pts,2.6,phase[(i//2)%3],'stator')
 cyl('Laminated rotor',(0,-2,0),43,18,gray,'stator','Y',96,.5)
 for i in range(28):
  a=i*2*math.pi/28;box('Squirrel cage end ring bar',(39*math.sin(a),-12,39*math.cos(a)),(2,.5,4),aluminium,'stator',.2)
 cyl('Drive-end shaft',(0,-18,0),10,22,steel,'stator','Y',64,.5)
 for t,x,z in [('U',0,99),('V',86,-49),('W',-86,-49)]:text(t,(x,-20,z),10,phase[['U','V','W'].index(t)],'stator')
 finish_fonts();camera((0,0,0),230,1536,1536);scope['render']('stator-cutaway.png',['stator']);bpy.ops.wm.save_as_mainfile(filepath=str(HERE/'stator.blend'),compress=True)
 reset();cyl('Impeller back disc',(0,5,0),90,3,aluminium,'impeller','Y',128,.4);cyl('Impeller shaft hub',(0,-3,0),19,20,steel,'impeller','Y',64,.4);cyl('Hub bore',(0,-14,0),8,.3,dark,'impeller','Y',64,.1)
 for i in range(12):
  a=i*2*math.pi/12;pts=[]
  for j in range(13):
   r=28+j*5;ang=a-.48*j/12;pts.append((r*math.sin(ang),-8,r*math.cos(ang)))
  # Blade is a real curved sheet between front and back edges, not a propeller.
  vs=[(x,y,z) for x,_,z in pts for y in [-15,3]];fs=[(2*j,2*j+1,2*j+3,2*j+2) for j in range(12)];me=bpy.data.meshes.new('Backward curved blade');me.from_pydata(vs,[],fs);ob=bpy.data.objects.new('Backward curved radial blade',me);bpy.context.collection.objects.link(ob);obj(ob,ob.name,aluminium,'impeller',.25);sol=ob.modifiers.new('Blade sheet thickness','SOLIDIFY');sol.thickness=1
 camera((0,0,0),210,1536,1536);scope['render']('blower-impeller.png',['impeller']);bpy.ops.wm.save_as_mainfile(filepath=str(HERE/'impeller.blend'),compress=True)
 print('DONE EXTRAS',flush=True)
if MODE in ['all','vfd']:vfd()
if MODE in ['all','conveyor']:conveyor()
if MODE in ['all','extras']:extras()
