"""Original generic IEC90L teaching motor. All construction coordinates below in mm.
Reference: SIVO IE4 B3 dimensional catalogue p7: H90 A140 B125 D24 E50 AC175.
Internal geometry is educational, not an OEM production winding/rotor drawing.
Run: blender -b --python build_motor_3ph.py
"""
import bpy,math,json
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parent;OUT=P.parent
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
for d in list(bpy.data.materials):bpy.data.materials.remove(d)
G={}
def mat(n,c,metal=0,rough=.4):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough;return m
blue=mat('Blue cast aluminium paint',(.035,.16,.30),.5,.31);steel=mat('Machined steel',(.46,.53,.59),.85,.24);iron=mat('Laminated electrical steel',(.22,.26,.29),.72,.38);black=mat('Black cooling fan',(.025,.029,.035),.15,.48);alu=mat('Cast aluminium rotor cage',(.63,.67,.69),.8,.3);brass=mat('Brass terminals',(.64,.43,.12),.8,.25);ceramic=mat('Terminal insulator',(.15,.12,.09),0,.6);dark=mat('Lamination etch',(.06,.075,.085),.5,.5)
phases=[mat('Phase U red',(.7,.025,.018),.25,.3),mat('Phase V yellow',(.95,.56,.025),.25,.3),mat('Phase W blue',(.018,.15,.85),.25,.3)]
def add(o,g,m):
 o.data.materials.append(m);G.setdefault(g,[]).append(o);return o

def mesh(n,vs,fs,g,m):
 d=bpy.data.meshes.new(n);d.from_pydata(vs,[],fs);d.update();o=bpy.data.objects.new(n,d);bpy.context.collection.objects.link(o);return add(o,g,m)
def box(n,pos,size,g,m,bevel=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=pos);o=bpy.context.object;o.name=n;o.dimensions=size;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 if bevel:
  mod=o.modifiers.new('Cast edge radius','BEVEL');mod.width=bevel;mod.segments=2;bpy.context.view_layer.objects.active=o;bpy.ops.object.modifier_apply(modifier=mod.name)
 return add(o,g,m)
def cyl(n,pos,r,h,g,m,axis='X',verts=48):
 bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=h,location=pos);o=bpy.context.object;o.name=n
 if axis=='X':o.rotation_euler[1]=math.pi/2
 if axis=='Y':o.rotation_euler[0]=math.pi/2
 return add(o,g,m)
def ring(n,x,ro,ri,length,g,m,N=72):
 vs=[]
 for xx,r in [(x-length/2,ro),(x+length/2,ro),(x-length/2,ri),(x+length/2,ri)]:vs.extend((xx,r*math.cos(i*2*math.pi/N),r*math.sin(i*2*math.pi/N)) for i in range(N))
 fs=[]
 for i in range(N):
  j=(i+1)%N
  for a,b in [(0,N),(2*N,3*N),(0,2*N),(N,3*N)]:fs.append((a+i,a+j,b+j,b+i))
 return mesh(n,vs,fs,g,m)
def tube(n,pts,r,g,m,sides=8,closed=False):
 vs=[];fs=[]
 for i,p in enumerate(pts):
  t=Vector(pts[(i+1)%len(pts)])-Vector(pts[(i-1)%len(pts)]) if closed or (i>0 and i<len(pts)-1) else Vector(pts[min(i+1,len(pts)-1)])-Vector(pts[max(0,i-1)])
  t.normalize();a=t.cross(Vector((0,0,1)))
  if a.length<.01:a=t.cross(Vector((0,1,0)))
  a.normalize();b=t.cross(a);p=Vector(p)
  vs.extend(tuple(p+r*(math.cos(k*2*math.pi/sides)*a+math.sin(k*2*math.pi/sides)*b)) for k in range(sides))
 for i in range(len(pts) if closed else len(pts)-1):
  j=(i+1)%len(pts)
  for k in range(sides):fs.append((i*sides+k,i*sides+(k+1)%sides,j*sides+(k+1)%sides,j*sides+k))
 return mesh(n,vs,fs,g,m)
def arcpts(x,r,N=72):return [(x,r*math.cos(i*2*math.pi/N),r*math.sin(i*2*math.pi/N)) for i in range(N)]
# Housing is a hollow casting, no hidden solid cylinder through stator.
ring('Casting shell',0,78,70,165,'Housing',blue)
for i in range(32):
 a=2*math.pi*i/32
 if abs(math.cos(a))<.30 and math.sin(a)>.5:continue
 o=box('Axial cooling fin',(0,82.5*math.cos(a),82.5*math.sin(a)),(158,10,2.2),'Housing',blue,.45);o.rotation_euler[0]=a
for x in [-80,80]:ring('Casting end rim',x,80,70,6,'Housing',blue)
# End shields and bearing bosses.
for side,x in [('DE',101),('NDE',-101)]:
 g='EndShield_'+side;ring('End shield skirt',88 if x>0 else -88,77,70,20,g,blue);ring('Cast end shield',x,77,24,14,g,blue);ring('Bearing boss',x+(4 if x>0 else -4),30,17,15,g,blue)
 for a in [math.pi/4+i*math.pi/2 for i in range(4)]:cyl('End shield bolt',(x+(9 if x>0 else -9),65*math.cos(a),65*math.sin(a)),4,4,g,steel,verts=12)
# Through shaft: drive extension24x50 from +110 to+160; rear extension enclosed.
cyl('Internal rotor shaft',(2.5,0,0),12,215,'Shaft',steel)
shaft=cyl('DE shaft extension',(135,0,0),12,50,'Shaft',steel,verts=64)
cut=box('Keyway cutter',(134,0,11.6),(42,8,5),'CUT',dark)
mod=shaft.modifiers.new('Milled keyway','BOOLEAN');mod.object=cut;bpy.context.view_layer.objects.active=shaft;bpy.ops.object.modifier_apply(modifier=mod.name);bpy.data.objects.remove(cut,do_unlink=True);G.pop('CUT')
box('Parallel shaft key',(134,0,11.7),(40,8,6),'Key',steel,.4)
cyl('NDE internal fan shaft',(-125,0,0),10,44,'Shaft',steel)
# Four real mounting holes. Base plane is z=-90, shaft is at z=0.
for y in [-70,70]:
 foot=box('B3 mounting foot',(0,y,-85),(154,30,10),'Feet',blue,1)
 for x in [-62.5,62.5]:
  h=cyl('Foot hole cutter',(x,y,-85),5,25,'CUT',dark,axis='Z',verts=24);mo=foot.modifiers.new('Through bolt hole','BOOLEAN');mo.object=h;bpy.context.view_layer.objects.active=foot;bpy.ops.object.modifier_apply(modifier=mo.name);bpy.data.objects.remove(h,do_unlink=True)
 for x in [-55,55]:box('Foot web',(x,y*.84,-62),(17,13,42),'Feet',blue,1)
G.pop('CUT',None)
# Top terminal box: walls with open interior, removable lid, one gland.
box('Terminal box saddle',(0,0,80),(70,66,12),'TerminalBox',blue,2)
for pos,size in [((0,-43,104),(88,5,42)),((0,43,104),(88,5,42)),((-44,0,104),(5,86,42)),((44,0,104),(5,86,42))]:box('Terminal box wall',pos,size,'TerminalBox',blue,1)
box('Terminal box floor',(0,0,85),(88,86,5),'TerminalBox',blue,1)
box('Terminal box lid',(0,0,128),(94,94,7),'TerminalBoxCover',blue,2)
for x in [-36,36]:
 for y in [-36,36]:cyl('Lid screw',(x,y,132),2.5,2,'TerminalBoxCover',steel,axis='Z',verts=12)
cyl('Single cable gland',(0,-52,104),10,17,'TerminalBox',black,axis='Y',verts=12);cyl('Gland entry bore',(0,-61,104),6,1,'TerminalBox',dark,axis='Y')
box('Six stud terminal block',(0,0,92),(64,59,7),'TerminalBlock',ceramic,1)
for y in [-17,17]:
 for x in [-22,0,22]:
  cyl('Terminal stud',(x,y,102),2.5,15,'TerminalBlock',brass,axis='Z',verts=12);cyl('Terminal hex nut',(x,y,108),4.5,3,'TerminalBlock',brass,axis='Z',verts=6)
for x in [-22,0,22]:box('Delta vertical link',(x,0,105),(7,40,2),'TerminalBlock',brass,.5)
# Embedded text labels, read from +Z with DE to the right.
for y,labs in [(27,['U1','V1','W1']),(-29,['W2','U2','V2'])]:
 for x,lab in zip([-22,0,22],labs):
  cu=bpy.data.curves.new(lab,'FONT');cu.body=lab;cu.size=5;cu.align_x='CENTER';cu.extrude=.12;o=bpy.data.objects.new(lab,cu);bpy.context.collection.objects.link(o);o.location=(x,y,96.1);o.data.materials.append(brass);G['TerminalBlock'].append(o)
# Lifting eye clear of terminal box.
tube('Lifting eye',[(65+9*math.cos(i*2*math.pi/32),0,83+9*math.sin(i*2*math.pi/32)) for i in range(32)],2.8,'Housing',steel,8,True)
# Exact 36-slot stator bore profile extruded axially.
profile=[];pitch=2*math.pi/36
for s in range(36):
 a=s*pitch
 for da,r in [(-pitch/2,45),(-.035,45),(-.035,61),(.035,61),(.035,45),(pitch/2,45)]:profile.append((r*math.cos(a+da),r*math.sin(a+da)))
N=len(profile);vs=[]
for x in [-60,60]:
 vs.extend((x,y,z) for y,z in profile);vs.extend((x,68*math.cos(2*math.pi*i/N),68*math.sin(2*math.pi*i/N)) for i in range(N))
fs=[]
for i in range(N):
 j=(i+1)%N
 fs.extend([(i,j,2*N+j,2*N+i),(N+i,3*N+i,3*N+j,N+j),(i,N+i,N+j,j),(2*N+i,2*N+j,3*N+j,3*N+i)])
mesh('36 slotted stator stack',vs,fs,'StatorCore',iron)
for x in range(-58,60,4):ring('Stator lamination line',x,68.12,67.85,.22,'StatorCore',dark,N=72)
# Double-layer full-pitch coil geometry: 36 coils,9-slot pitch,3 coils/group.
# Phase colour belts satisfy requested U/V/W 30degree offsets and four groups90degree apart.
# This is visual geometry, not a validated electrical connection schedule.
for s in range(36):
 phase=(s//3)%3;g=['Winding_U','Winding_V','Winding_W'][phase];a=s*pitch;b=a+9*pitch;r1=50.2;r2=55.5;pts=[];extension=13+(s%3)*4
 for x in [-60,-30,0,30,60]:pts.append((x,r1*math.cos(a),r1*math.sin(a)))
 for k in range(1,19):
  t=k/18;r=r1+(r2-r1)*t;th=a+(b-a)*t;pts.append((60+extension*math.sin(math.pi*t),r*math.cos(th),r*math.sin(th)))
 for x in [30,0,-30,-60]:pts.append((x,r2*math.cos(b),r2*math.sin(b)))
 for k in range(1,19):
  t=k/18;r=r2+(r1-r2)*t;th=b+(a-b)*t;pts.append((-60-extension*math.sin(math.pi*t),r*math.cos(th),r*math.sin(th)))
 tube('Insulated winding coil',pts,1.35,g,phases[phase],8,True)
# Rotor body + skewed aluminium bars, two cast end rings.
cyl('Rotor laminated core',(0,0,0),44.15,116,'Rotor',iron,verts=96)
for x in range(-55,57,4):ring('Rotor lamination line',x,44.22,44,.18,'Rotor',dark,N=64)
for i in range(28):
 pts=[]
 for k in range(11):
  x=-59+118*k/10;a=i*2*math.pi/28+.11*(k/10-.5);pts.append((x,43.2*math.cos(a),43.2*math.sin(a)))
 tube('Skewed cage bar',pts,1.4,'Rotor',alu,8)
for x in [-61,61]:
 ring('Cage short circuit end ring',x,45,36,5,'Rotor',alu)
 for i in range(14):
  a=i*2*math.pi/14;o=box('Rotor cast cooling rib',(x+(4 if x>0 else -4),38*math.cos(a),38*math.sin(a)),(5,12,2),'Rotor',alu,.3);o.rotation_euler[0]=a
# Visible races and balls, separately animatable inner races.
for suffix,x in [('DE',88),('NDE',-88)]:
 root=bpy.data.objects.new('Bearing_'+suffix,None);bpy.context.collection.objects.link(root);root.empty_display_type='PLAIN_AXES'
 ring('Outer race',x,26,22,14,'Bearing_'+suffix+'_OuterRace',steel,N=64)
 ring('Inner race',x,17,12,14,'Bearing_'+suffix+'_InnerRace',steel,N=64)
 for i in range(9):
  a=i*2*math.pi/9;bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=8,radius=3.8,location=(x,19.5*math.cos(a),19.5*math.sin(a)));add(bpy.context.object,'Bearing_'+suffix+'_Balls',steel)
# Shaft-mounted NDE fan inside closed cowl; no exposed NDE shaft.
cyl('Fan hub',(-137,0,0),17,13,'Fan',black)
for i in range(10):
 a=i*2*math.pi/10;pts=[(-137+7*t, (18+45*t)*math.cos(a+.35*t),(18+45*t)*math.sin(a+.35*t)) for t in [0,.25,.5,.75,1]]
 # broad swept blade surface, thickness via two nearby strips
 vs=[]
 for x,y,z in pts:
  for dx in [-2,2]:vs.append((x+dx,y,z))
 fs=[(2*k,2*k+1,2*k+3,2*k+2) for k in range(4)];o=mesh('Swept fan blade',vs,fs,'Fan',black);mo=o.modifiers.new('Fan blade thickness','SOLIDIFY');mo.thickness=2;bpy.context.view_layer.objects.active=o;bpy.ops.object.modifier_apply(modifier=mo.name)
ring('Fan cowl shell',-139,80,77,62,'FanCowl',blue)
# Rear grille made of real open concentric rings and radial spokes.
for r in [12,23,34,45,56,67,77]:tube('Rear grille ring',arcpts(-174,r,64),1.6,'FanCowl',blue,6,True)
for i in range(12):
 a=i*2*math.pi/12;tube('Rear grille spoke',[(-174,8*math.cos(a),8*math.sin(a)),(-174,77*math.cos(a),77*math.sin(a))],1.5,'FanCowl',blue,6)
# Join named groups; apply transforms and set every rotating pivot on motor axis.
parts=[]
for name,objs in G.items():
 bpy.ops.object.select_all(action='DESELECT')
 for o in objs:o.select_set(True)
 bpy.context.view_layer.objects.active=objs[0];bpy.ops.object.convert(target='MESH');bpy.ops.object.join();o=bpy.context.object;o.name=name
 bpy.context.scene.cursor.location=(0,0,0);bpy.ops.object.origin_set(type='ORIGIN_CURSOR');bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
 for v in o.data.vertices:v.co*=.001
 if name.startswith('Bearing_'):o.parent=bpy.data.objects['Bearing_'+name.split('_')[1]]
 parts.append(o)
 for f in o.data.polygons:f.use_smooth=len(f.vertices)==4 and name not in ['Feet','TerminalBox','TerminalBoxCover','TerminalBlock']
scene=bpy.context.scene;scene.unit_settings.system='METRIC';scene.unit_settings.scale_length=1
# GLB mesh-only selection includes bearing parent nodes; no cameras/lights exported.
bpy.ops.object.select_all(action='DESELECT')
for o in bpy.context.scene.objects:o.select_set(True)
bpy.ops.export_scene.gltf(filepath=str(OUT/'motor-3ph.glb'),export_format='GLB',use_selection=True,export_yup=True,export_apply=True,export_cameras=False,export_lights=False,export_extras=True)
tris=sum(sum(len(p.vertices)-2 for p in o.data.polygons) for o in parts);assert tris<150000,tris
required=['Housing','EndShield_DE','EndShield_NDE','FanCowl','TerminalBox','TerminalBoxCover','TerminalBlock','StatorCore','Winding_U','Winding_V','Winding_W','Rotor','Shaft','Key','Bearing_DE','Bearing_NDE','Fan','Feet']
assert all(n in bpy.data.objects for n in required)
info={'triangle_count':tris,'units':'metres','gltf_up':'+Y','shaft_axis':'+X','DE_direction':'+X','shaft_centre_gltf':[0,0,0],'floor_gltf_y':-.09,'required_nodes':required,'mesh_nodes':[o.name for o in parts],'rotating_nodes':['Rotor','Shaft','Key','Fan','Bearing_DE_InnerRace','Bearing_NDE_InnerRace'],'dimensions_mm':{'shaft_height':90,'foot_holes_A_B':[140,125],'drive_shaft_D_E':[24,50],'fin_diameter':175,'overall_length':335.6},'winding_geometry':{'slots':36,'poles':4,'coils':36,'coils_per_group':3,'coil_pitch_slots':9,'phase_groups_each':4,'group_spacing_deg':90,'phase_colour_group_offset_deg':30},'limits':['Generic educational internal assembly; no electromagnetic or thermal rating validation.','Requested 2.2kW/415V is a narrative rating, not verified against this exact90L casting.','Phase-colour group positions follow083, not a complete validated winding connection schedule.','Lamination lines are sampled visual grooves, not every physical sheet.','Bearings have visible simplified races/balls, no cage or seals.','No hidden exposed rear shaft; NDE shaft terminates within fan cowl.']}
(OUT/'motor-3ph-manifest.json').write_text(json.dumps(info,indent=2))
# Preview lighting and camera.
scene.render.engine='CYCLES';scene.cycles.samples=40;scene.cycles.use_denoising=False;scene.render.resolution_x=1536;scene.render.resolution_y=1024;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG';scene.render.image_settings.color_mode='RGBA';scene.render.film_transparent=True
world=bpy.data.worlds.new('Studio') if not bpy.data.worlds else bpy.data.worlds[0];scene.world=world;world.use_nodes=True;world.node_tree.nodes['Background'].inputs[0].default_value=(.5,.58,.68,1);world.node_tree.nodes['Background'].inputs[1].default_value=.4
for pos,power,size in [((.35,-.4,.65),55,.5),((-.3,.2,.35),35,.4),((.15,.3,.15),18,.3)]:
 bpy.ops.object.light_add(type='AREA',location=pos);o=bpy.context.object;o.data.energy=power*.45;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,.02))-o.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.camera_add(location=(.49,-.64,.34));cam=bpy.context.object;cam.rotation_euler=(Vector((-.015,0,.02))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=.48;scene.camera=cam
scene.view_settings.view_transform='AgX'
scene.render.filepath=str(OUT/'motor-3ph-preview.png');bpy.ops.render.render(write_still=True)
for n in ['Housing','EndShield_DE','EndShield_NDE','FanCowl','TerminalBox','TerminalBoxCover','TerminalBlock','Feet']:bpy.data.objects[n].hide_render=True
# Core ghosting is preview-only: show real coil/rotor geometry within the core.
core=bpy.data.objects['StatorCore'];core.hide_render=True
import bmesh
cutcore=core.copy();cutcore.data=core.data.copy();bpy.context.collection.objects.link(cutcore);cutcore.name='PreviewOnly_CoreSection';cutcore.hide_render=False
bm=bmesh.new();bm.from_mesh(cutcore.data);bmesh.ops.delete(bm,geom=[v for v in bm.verts if v.co.y<0],context='VERTS');bm.to_mesh(cutcore.data);bm.free()
scene.render.filepath=str(OUT/'motor-3ph-xray-preview.png');bpy.ops.render.render(write_still=True)
bpy.data.objects.remove(cutcore,do_unlink=True)
for o in parts:o.hide_render=False
scene.render.filepath='//../motor-3ph-preview.png';bpy.context.preferences.filepaths.save_version=0;bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(P/'motor-3ph.blend'),compress=True)
print('MOTOR_DONE',tris,flush=True)
