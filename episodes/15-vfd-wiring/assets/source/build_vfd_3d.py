"""EP15 generic educational VFD. Reuses EP14 original geometry; not OEM wiring data.
Run blender -b --python build_vfd_3d.py
"""
import bpy, math, json, struct
from pathlib import Path
from mathutils import Vector, Matrix
HERE=Path(__file__).resolve().parent; OUT=HERE.parent
ROOT=HERE.parents[3]
bpy.ops.wm.open_mainfile(filepath=str(ROOT/'episodes/14-vfd-basics/assets/source/vfd.blend'))
# Remove legacy power terminals and display glyphs; replacement terminals are explicit animation targets.
for o in list(bpy.context.scene.objects):
 if o.type in {'CAMERA','LIGHT'} or o.name.startswith(('Power terminal cage','Brass cable well','Steel screw','Cross slot','LED segment','Display decimal')) or (o.type=='FONT' and o.data.body in ['R','S','T','U','V','W','PE']):
  bpy.data.objects.remove(o,do_unlink=True)
M={}
def mat(name,col,metal=0,rough=.4):
 m=bpy.data.materials.new(name);m.diffuse_color=(*col,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*col,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough;return m
plastic=mat('Terminal black PA',(.025,.032,.04));green=mat('Control connector green',(.025,.23,.10));silver=mat('Screw stainless steel',(.55,.59,.64),.8,.27);brass=mat('Terminal brass',(.55,.33,.08),.75);white=mat('Legend ivory',(.88,.9,.91));black=mat('Legend ink',(.009,.012,.015));red=mat('Charge LED red',(.55,.008,.005));p=red.node_tree.nodes.get('Principled BSDF');p.inputs['Emission Color'].default_value=(.8,.005,.002,1);p.inputs['Emission Strength'].default_value=.5
font=bpy.data.fonts.load('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf');font.pack()
def cube(name,loc,size,material,bevel=.2):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=size;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(material)
 if bevel: mod=o.modifiers.new('Mould radius','BEVEL');mod.width=bevel;mod.segments=3;o.modifiers.new('Normals','WEIGHTED_NORMAL')
 return o
def cyl(name,loc,r,depth,material):
 bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=r,depth=depth,location=loc,rotation=(math.pi/2,0,0));o=bpy.context.object;o.name=name;o.data.materials.append(material);mod=o.modifiers.new('Edge bevel','BEVEL');mod.width=.12;mod.segments=2;o.modifiers.new('Normals','WEIGHTED_NORMAL');return o
def label(txt,loc,size,material=white):
 c=bpy.data.curves.new('Printed '+txt,'FONT');c.body=txt;c.font=font;c.size=size;c.align_x='CENTER';c.align_y='CENTER';c.extrude=.006;o=bpy.data.objects.new('Legend_'+txt,c);bpy.context.collection.objects.link(o);o.location=loc;o.rotation_euler=(math.pi/2,0,0);o.data.materials.append(material);return o
def join(name,objs,pivot=None):
 bpy.ops.object.select_all(action='DESELECT')
 for o in objs:
  o.hide_set(False);o.hide_render=False;o.select_set(True)
 bpy.context.view_layer.objects.active=objs[0]
 for o in objs:
  bpy.context.view_layer.objects.active=o
  if o.type!='MESH':bpy.ops.object.convert(target='MESH')
  for mod in list(o.modifiers):
   try:bpy.ops.object.modifier_apply(modifier=mod.name)
   except:pass
 bpy.context.view_layer.objects.active=objs[0];bpy.ops.object.join();o=bpy.context.object;o.name=name
 bpy.context.scene.cursor.location=pivot or (0,0,0);bpy.ops.object.origin_set(type='ORIGIN_CURSOR');M[name]=o;return o
# Group original meshes without rebuilding the approved external proportions.
old=list(bpy.context.scene.objects);groups={k:[] for k in ['Body','Heatsink','Fan','Keypad','Display','Pot','TerminalCover','PowerElectronics']}
for o in old:
 n=o.name
 if n.startswith(('Heatsink',)):g='Heatsink'
 elif n.startswith(('Fan blade','Fan central')):g='Fan'
 elif n.startswith('Display dark'):g='Display'
 elif n.startswith(('Speed potentiometer','Pot white pointer')):g='Pot'
 elif n.startswith('Lower terminal protective'):g='TerminalCover'
 elif n.startswith(('Keypad','Key ','Text')) and not (o.type=='FONT' and o.data.body=='SPEED'):g='Keypad'
 elif n.startswith(('Control','SMD','IGBT','Rectifier','DC bus','Capacitor','DC choke','Choke')):g='PowerElectronics'
 else:g='Body'
 groups[g].append(o)
for g,objs in groups.items():
 pivot={'Pot':(0,-76,85),'TerminalCover':(0,-63,61.5),'Fan':(0,7,25),'Display':(0,-77,144)}.get(g,(0,0,0));join(g,objs,pivot)
# Power bank: two rows so dual labels remain readable on a compact 70 mm housing.
termdefs=[('R','R/L1',-23,29),('S','S/L2',-12,29),('T','T/L3',-1,29),('P','P+',12,29),('N','N-',23,29),('U','U/T1',-23,12),('V','V/T2',-12,12),('W','W/T3',-1,12),('B1','B1',12,12),('B2','B2',23,12),('PE','PE',-27,41)]
cube('Terminal recess shield',(0,-46,31),(62,2,59),plastic,.5)
termmeta=[]
for key,txt,x,z in termdefs:
 y=-53
 parts=[cube('Terminal cage',(x,y+3,z),(9,10,9),plastic),cyl('Brass throat',(x,y-2.1,z),2.8,.6,brass),cyl('Screw head',(x,y-2.7,z),2.15,.65,silver),cube('Screw slot',(x,y-3.08,z),(3.1,.06,.55),black,.02)]
 ob=join('T_'+key,parts,(x,y-3.08,z));termmeta.append({'object':ob.name,'label':txt,'screw_blender_mm':[x,y-3.08,z]})
 label(txt,(x,y-3.2,z+6.3),2.2)
 if key=='PE':
  for w,dz in [(3.2,-3.1),(2.2,-4.1),(1.2,-5.1)]:cube('Earth symbol bar',(x,y-3.2,z+dz),(w,.08,.18),white,.02)
  cube('Earth symbol stem',(x,y-3.2,z-2),( .18,.08,2.2),white,.02)
# Control strip sits above the power row, exposed only with the terminal cover removed.
for i,key in enumerate(['FWD','REV','X1','COM','10V','AI','GND','AO','RA','RB','RC']):
 x=-27.5+i*5.5;z=53;y=-54
 parts=[cube('Control cage',(x,y+2,z),(5.2,7,6),green,.3),cyl('Control screw',(x,y-1.8,z),1.45,.5,silver),cube('Control screw slot',(x,y-2.1,z),(2,.06,.3),black,.01)]
 ob=join('C_'+key,parts,(x,y-2.1,z));label(key,(x,y-2.4,z+5),1.65);termmeta.append({'object':ob.name,'label':key,'screw_blender_mm':[x,y-2.1,z]})
join('TerminalLegends',[o for o in bpy.context.scene.objects if o.name.startswith(('Legend_','Earth symbol'))])
led=cyl('ChargeLED', (25,-55,42),1.5,1,red);join('ChargeLED',[led],(25,-55,42));label('CHARGE',(16,-55.6,42),1.6)
join('ChargeLegend',[o for o in bpy.context.scene.objects if o.type=='FONT'])
join('TerminalBackplate',[bpy.data.objects['Terminal recess shield']])
# Scale all geometry and object translations from millimetres to metres.
for o in list(bpy.context.scene.objects):
 o.matrix_world=Matrix.Scale(.001,4) @ o.matrix_world
 bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.select_set(False)
# Export only model objects; glTF exporter maps Blender Z-up to Y-up.
bpy.ops.object.select_all(action='SELECT');bpy.ops.export_scene.gltf(filepath=str(OUT/'vfd-3d.glb'),export_format='GLB',use_selection=True,export_yup=True,export_apply=True)
triangles=sum(len(o.data.polygons) and sum(len(p.vertices)-2 for p in o.data.polygons) for o in bpy.context.scene.objects if o.type=='MESH')
manifest={'model':'vfd-3d.glb','units':'metres','up':'Y','front':'+Z','triangles':triangles,'objects':sorted(o.name for o in bpy.context.scene.objects),'terminal_centres_gltf_m':{t['object']:[t['screw_blender_mm'][0]*.001,t['screw_blender_mm'][2]*.001,-t['screw_blender_mm'][1]*.001] for t in termmeta},'pivots_gltf_m':{'Pot':[0,.085,.076],'TerminalCover':[0,.0615,.063],'Fan':[0,.025,-.007]},'axes_gltf':{'Pot':'+Z','TerminalCover':'+X','Fan':'+Z'},'limits':['Generic educational layout; all terminals requested in 087 are shown but not an ACS150 wiring diagram.','Nominal 70 x 169 x 155 mm educational geometry, not a certified mechanical drawing.','No functional electronics or thermal simulation; no baked animation.','Separate display lens is intentionally blank for collaborator-generated digits.','Power and control strips are arranged as a generic teaching composite.']}
(OUT/'vfd-3d-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Neutral transparent studio previews.
scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=96;scene.cycles.use_denoising=False;scene.view_settings.exposure=-1.2;scene.render.resolution_x=1536;scene.render.resolution_y=1536;scene.render.resolution_percentage=100;scene.render.film_transparent=True
scene.world.color=(.28,.28,.28)
def aim(o,at):o.rotation_euler=(Vector(at)-o.location).to_track_quat('-Z','Y').to_euler()
for pos,power,size in [((-.22,-.35,.4),14,.25),((.3,-.18,.22),8,.2),((0,.24,.28),12,.2)]:
 bpy.ops.object.light_add(type='AREA',location=pos);o=bpy.context.object;o.data.energy=power;o.data.shape='DISK';o.data.size=size;aim(o,(0,0,.085))
bpy.ops.object.camera_add(location=(.19,-.44,.21));cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=.235;aim(cam,(0,0,.085));scene.camera=cam
# Preview digits only; the GLB and source keep Display blank.
digits=label('50.00',(0,-.0778,.144),.0105,red);digits.name='PreviewDigits';digits.data.extrude=.000001
digits.hide_render=True;digits.hide_viewport=True
bpy.ops.wm.save_as_mainfile(filepath=str(HERE/'vfd-3d.blend'),compress=True)
digits.hide_render=False;digits.hide_viewport=False
scene.render.filepath=str(OUT/'vfd-3d-preview.png');bpy.ops.render.render(write_still=True)
M['TerminalCover'].hide_render=True
cam.location=(.075,-.45,.14);aim(cam,(0,-.025,.079));cam.data.ortho_scale=.215
scene.render.filepath=str(OUT/'vfd-3d-open-preview.png');bpy.ops.render.render(write_still=True)
cam.location=(.018,-.35,.068);aim(cam,(0,-.05,.033));cam.data.ortho_scale=.085
scene.render.filepath=str(OUT/'vfd-3d-terminal-detail.png');bpy.ops.render.render(write_still=True)
print('MODEL_RESULT',json.dumps({'triangles':triangles,'nodes':len(manifest['objects'])}),flush=True)
