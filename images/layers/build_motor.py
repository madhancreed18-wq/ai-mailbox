"""Reproducible, logo-free motor layer source. Run with Blender 4.3+."""
import bpy, math, json, sys
from pathlib import Path
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view

OUT=Path(__file__).parent/'motor'
OUT.mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=64
scene.cycles.use_denoising=False
scene.render.resolution_x=2048; scene.render.resolution_y=1024
scene.render.resolution_percentage=100
scene.render.dither_intensity=0
scene.render.film_transparent=True
scene.render.image_settings.file_format='PNG'
scene.render.image_settings.color_mode='RGBA'
scene.render.image_settings.color_depth='8'
scene.render.image_settings.compression=100
scene.view_settings.view_transform='AgX'
scene.world.color=(.28,.28,.28)
scene.render.threads_mode='FIXED';scene.render.threads=6

def mat(name,color,metal=0,rough=.35,cast=False):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    bs=m.node_tree.nodes.get('Principled BSDF')
    bs.inputs['Base Color'].default_value=(*color,1)
    bs.inputs['Metallic'].default_value=metal;bs.inputs['Roughness'].default_value=rough
    if cast:
        noise=m.node_tree.nodes.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=95
        bump=m.node_tree.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.11;bump.inputs['Distance'].default_value=.014
        m.node_tree.links.new(noise.outputs['Fac'],bump.inputs['Height']);m.node_tree.links.new(bump.outputs['Normal'],bs.inputs['Normal'])
    return m
blue=mat('Blue enamel cast iron',(.025,.13,.245),.45,.32,True)
darkblue=mat('Deep blue cowl',(.018,.085,.15),.45,.34,True)
steel=mat('Machined steel',(.47,.53,.59),.88,.23)
silver=mat('Brushed plate',(.55,.6,.64),.8,.34)
dark=mat('Dark sockets and rubber',(.012,.017,.023),.28,.34)
white=mat('White rotation index',(.9,.92,.95),.05,.38)
groups={n:[] for n in ['00_feet','01_body','02_terminal_box','03_shaft','04_coupling_face','05_nameplate']}

def finish(o,name,m,g,bevel=.025):
    o.name=name;o.data.materials.append(m);groups[g].append(o)
    if bevel:
        mod=o.modifiers.new('Cast edge radius','BEVEL');mod.width=bevel;mod.segments=3
        mod=o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
    return o

def box(name,loc,scale,m,g,bevel=.025,rot=None):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object
    o.scale=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if rot:o.rotation_euler=rot
    return finish(o,name,m,g,bevel)

def cyl(name,loc,r,depth,m,g,axis='X',vertices=80,bevel=.018):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=r,depth=depth,location=loc)
    o=bpy.context.object
    if axis=='X':o.rotation_euler[1]=math.pi/2
    if axis=='Y':o.rotation_euler[0]=math.pi/2
    for p in o.data.polygons:p.use_smooth=abs(p.normal.z)<.9
    return finish(o,name,m,g,bevel)

def torus(name,loc,major,minor,m,g,rot=(0,0,0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=major,minor_radius=minor,major_segments=64,minor_segments=12,location=loc,rotation=rot)
    return finish(bpy.context.object,name,m,g,0)

# Complete feet: under-body structure remains intact if body is removed.
for y in [-.78,.78]:
    box('Continuous mounting foot',(0,y,-1.14),(3.35,.47,.20),blue,'00_feet',.065)
    for x in [-1.12,1.12]:
        box('Cast foot web',(x,y,-.83),(.40,.27,.55),blue,'00_feet',.045)
        cyl('Foot washer',(x,y,-1.025),.105,.025,steel,'00_feet','Z',48,.008)
        cyl('Mounting bolt',(x,y,-.987),.067,.055,steel,'00_feet','Z',6,.005)

# Axial finned stator housing, complete front and rear bearing closures.
cyl('Stator cast housing',(0,0,0),.89,2.95,blue,'01_body')
for i in range(34):
    a=2*math.pi*i/34
    o=box('Longitudinal cooling fin %02d'%i,(0,math.sin(a)*.97,math.cos(a)*.97),(2.80,.045,.21),blue,'01_body',.012)
    o.rotation_euler[0]=-a
cyl('Drive end shield',(1.52,0,0),1.035,.22,blue,'01_body')
cyl('Front bearing boss',(1.68,0,0),.39,.17,blue,'01_body')
cyl('Bearing seal',(1.775,0,0),.235,.026,dark,'01_body')
for i in range(18):
    a=i*2*math.pi/18
    o=box('End shield radial rib %02d'%i,(1.65,math.sin(a)*.69,math.cos(a)*.69),(.075,.04,.46),blue,'01_body',.009)
    o.rotation_euler[0]=-a
for i in range(4):
    a=math.pi/4+i*math.pi/2
    cyl('End shield hex bolt',(1.675,math.sin(a)*.91,math.cos(a)*.91),.075,.085,steel,'01_body','X',6,.006)
cyl('Rear fan cowl',(-1.66,0,0),1.025,.48,darkblue,'01_body')
cyl('Rear cowl end',(-1.92,0,0),.96,.055,darkblue,'01_body')
for i in range(12):
    a=i*2*math.pi/12
    o=box('Fan cowl ventilation slot %02d'%i,(-1.938,math.sin(a)*.64,math.cos(a)*.64),(.012,.05,.36),dark,'01_body',.01)
    o.rotation_euler[0]=-a

# Near-side terminal box has a complete lid and closed interior behind it.
box('Terminal box pedestal',(-.45,-.90,.25),(1.04,.30,.80),blue,'02_terminal_box',.06)
box('Terminal enclosure',(-.45,-1.14,.35),(1.15,.48,.94),blue,'02_terminal_box',.07)
box('Terminal lid gasket',(-.45,-1.397,.35),(1.07,.03,.87),dark,'02_terminal_box',.045)
box('Terminal lid',(-.45,-1.43,.35),(1.12,.075,.91),blue,'02_terminal_box',.055)
for x in [-.9,0]:
    for z in [-.005,.705]:
        cyl('Terminal lid screw',(x,-1.481,z),.047,.028,steel,'02_terminal_box','Y',40,.004)
cyl('Cable gland threaded boss',(-.45,-1.18,-.21),.14,.22,dark,'02_terminal_box','Z',12,.009)
cyl('Cable gland nut',(-.45,-1.18,-.34),.16,.13,dark,'02_terminal_box','Z',6,.01)
torus('Cable gland lip',(-.45,-1.18,-.419),.106,.023,steel,'02_terminal_box')
box('Lifting eye plinth',(.42,0,1.08),(.35,.34,.22),blue,'02_terminal_box',.025)
cyl('Eye threaded stem',(.42,0,1.23),.10,.20,steel,'02_terminal_box','Z',32,.006)
torus('Lifting eye',(.42,0,1.48),.23,.067,blue,'02_terminal_box',(math.pi/2,0,0))

# Continuous machined shaft extends inside the bearing; no cut-out behind coupling.
cyl('Drive shaft',(2.10,0,0),.175,.82,steel,'03_shaft')
box('Shaft key',(2.12,0,.171),(.48,.075,.04),steel,'03_shaft',.009)

# Coupling is real complete geometry, origin on its rotation axis.
pivot=Vector((2.705,0,0))
cyl('Coupling hub',(2.49,0,0),.24,.28,steel,'04_coupling_face')
cyl('Coupling disk',(2.62,0,0),.43,.14,steel,'04_coupling_face')
cyl('Coupling central bore',(2.696,0,0),.065,.009,dark,'04_coupling_face','X',64,.003)
for i in range(4):
    a=math.pi/4+i*math.pi/2;y=math.sin(a)*.29;z=math.cos(a)*.29
    cyl('Coupling recessed bolt socket',(2.697,y,z),.043,.012,dark,'04_coupling_face','X',32,.004)
    cyl('Coupling socket steel rim',(2.700,y,z),.025,.017,steel,'04_coupling_face','X',6,.002)
box('Rotation index',(2.705,0,.365),(.009,.022,.065),white,'04_coupling_face',.002)
bpy.ops.object.empty_add(type='PLAIN_AXES',location=pivot)
rotor=bpy.context.object;rotor.name='Coupling rotation pivot'
for o in groups['03_shaft']+groups['04_coupling_face']:
    mw=o.matrix_world.copy();o.parent=rotor;o.matrix_world=mw

# Blank nameplate sits above the terminal box, on a fully modelled surface.
plate=box('Blank motor nameplate',(-.60,-.63,.87),(.85,.37,.025),silver,'05_nameplate',.018,(math.radians(42),0,0))
for x in [-.95,-.25]:
    for y,z in [(-.75,.78),(-.51,.99)]:
        screw=cyl('Nameplate rivet',(x,y,z),.023,.025,steel,'05_nameplate','Z',32,.004)
        screw.rotation_euler[0]=math.radians(42)

def area(name,loc,energy,size,target):
    bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.name=name
    o.data.energy=energy;o.data.shape='DISK';o.data.size=size
    o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler()
area('Top-left softbox',(-3,-6,7),1100,5,(0,0,0))
area('Gentle front fill',(6,-3,3),650,4,(0,0,0))
area('Rear rim',(0,5,5),950,4,(0,0,0))
bpy.ops.object.camera_add(location=pivot+Vector((8,-12,7)))
camera=bpy.context.object;camera.name='Fixed layer registration camera'
camera.rotation_euler=(pivot-camera.location).to_track_quat('-Z','Y').to_euler()
camera.data.type='ORTHO';camera.data.ortho_scale=5.4
scene.camera=camera
camera.data.lens=60
bpy.context.view_layer.update()
for _ in range(5):
    uvbounds=[world_to_camera_view(scene,camera,o.matrix_world@Vector(c)) for a in groups.values() for o in a for c in o.bound_box]
    factor=max(max(abs(v.x-.5)/.45,abs(v.y-.5)/.43) for v in uvbounds)
    if factor<=1:break
    camera.data.ortho_scale*=factor*1.025
    bpy.context.view_layer.update()
uv=world_to_camera_view(scene,camera,pivot)
assert abs(uv.x-.5)<1e-6 and abs(uv.y-.5)<1e-6,(uv.x,uv.y)

allparts=[o for a in groups.values() for o in a]
parts=[]
for group,objs in groups.items():
    filename='motor_'+group+'.png'
    parts.append({'file':filename,'order':int(group[:2]),'objects':[o.name for o in objs],'canvas':[2048,1024],'pivot_px':[1024,512] if group=='04_coupling_face' else None})
manifest={'asset':'motor','status':'first item of EP10 batch, source/render delivery; app integration pending','canvas':[2048,1024],'alpha':'straight RGBA','camera':'orthographic three-quarter side, key light top-left','stack':'alpha-over in ascending order, all layers positioned at (0,0)','rotation':{'part':'motor_04_coupling_face.png','pivot_px':[1024,512],'axis_world':'X','warning':'A three-quarter disk is an ellipse: 2D image rotation is stylized, not a physically correct shaft rotation. Use the supplied Blender rotor for correct 3D motion.'},'parts':parts,'full':'motor_full.png','source':'../build_motor.py','editable_scene':'motor.blend','sources':[{'url':'https://www.weg.net/institutional/CA/es/news/productos-y-soluciones/new-weg-w22','image':'https://static.weg.net/news/notice-CA-0157/03_noticia_detalhe_w.jpg','use':'drive-end fins, machined shaft and keyway photo reference'},{'url':'https://www.meritocomercial.com.br/motor-eletrico-weg-w22-125-cv-4-polos-ip55-trifasico-220v380v440v-4001001008932-p1032875','use':'full housing, feet, terminal box, fan cowl and lifting-eye reference'}],'limitations':['Generic visual model, not a dimensioned manufacturer replica.','Blank nameplate and no branding or ratings.','No motor internals, cables or driven load are implied.','Coupling front face is intentionally canvas-centred, so the full motor is left of canvas centre.','Independent layers have self-shading but no inter-layer cast shadows, preserving clean removal.']}
(OUT/'motor_manifest.json').write_text(json.dumps(manifest,indent=2))
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'motor.blend'))
for group,objs in groups.items():
    for o in allparts:o.hide_render=o not in objs
    scene.render.filepath=str(OUT/('motor_'+group+'.png'))
    print('RENDER',group,flush=True)
    bpy.ops.render.render(write_still=True)
# Full check image is the exact prescribed layer stack, generated by Blender's compositor.
for o in allparts:o.hide_render=True
scene.use_nodes=True
nodes=scene.node_tree.nodes;links=scene.node_tree.links;nodes.clear()
previous=None
for group in groups:
    n=nodes.new('CompositorNodeImage');n.image=bpy.data.images.load(str(OUT/('motor_'+group+'.png')),check_existing=False)
    if previous is None:previous=n.outputs['Image']
    else:
        over=nodes.new('CompositorNodeAlphaOver');over.inputs[0].default_value=1
        links.new(previous,over.inputs[1]);links.new(n.outputs['Image'],over.inputs[2]);previous=over.outputs['Image']
comp=nodes.new('CompositorNodeComposite');links.new(previous,comp.inputs['Image'])
scene.view_settings.view_transform='Standard'
scene.render.filepath=str(OUT/'motor_full.png');bpy.ops.render.render(write_still=True)
# Restore editable scene with all parts visible; compositor disabled for ordinary source rendering.
scene.use_nodes=False
scene.view_settings.view_transform='AgX'
scene.node_tree.nodes.clear()
for o in allparts:o.hide_render=False
scene.render.filepath=str(OUT/'motor_beauty.png')
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'motor.blend'))
print('MOTOR COMPLETE',flush=True)
