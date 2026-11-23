"""074 panel scene: preserve original camera/backplate/rails/ducts/contactor;
replace left breaker with072front texture and middle device with registered MPCBv2mesh.
Run after build_mpcb_v2.py: blender -b --python build_panel_3p.py
"""
import bpy,sys,json,math
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parent;OUT=P.parent
scope={'__file__':str(P/'build_equipment.py')};saved=sys.argv;sys.argv=['blender','--','helpers'];exec(compile((P/'build_equipment.py').read_text(),str(P/'build_equipment.py'),'exec'),scope);sys.argv=saved
scope['OUT']=OUT;scope['setup']()
box=scope['box'];steel=scope['steel'];white=scope['white'];dark=scope['dark'];GROUPS=scope['GROUPS']
# These are the original069panel geometry positions and materials.
box('Panel back plate',(0,12,70),(240,3,140),steel,'panel',1)
for z in [25,55,85,115]:
 box('DIN rail channel',(0,5,z),(210,4,25),steel,'panel',.3)
 for zz in [z-17.5,z+17.5]:box('35mm DIN rail lip',(0,2,zz),(210,2,3),steel,'panel',.2)
for x in [-111,111]:
 box('Cable duct',(x,-4,70),(15,25,136),white,'panel',.5)
 for z in range(8,135,8):box('Duct slots',(x,-17,z),(11,.2,3),dark,'panel',.05)
# Match existing contactor construction/location exactly; no redraw or movement.
scope['contactor']((45,-3,33))
contactor_objects=[o.name for o in GROUPS['panel'] if o.name.startswith('Contactor')]
# 072 alpha sprite on an actual fixed front-facing plane. Its body retains85mmheight.
image=bpy.data.images.load(str(OUT/'mcb3p-front.png'));image.pack()
mat=bpy.data.materials.new('072 three-pole MCB exact front appearance');mat.use_nodes=True
nodes=mat.node_tree.nodes;nodes.clear();out=nodes.new('ShaderNodeOutputMaterial');mix=nodes.new('ShaderNodeMixShader');trans=nodes.new('ShaderNodeBsdfTransparent');emit=nodes.new('ShaderNodeEmission');tex=nodes.new('ShaderNodeTexImage');tex.image=image;tex.interpolation='Linear';emit.inputs['Strength'].default_value=1
links=mat.node_tree.links;links.new(tex.outputs['Color'],emit.inputs['Color']);links.new(tex.outputs['Alpha'],mix.inputs[0]);links.new(trans.outputs[0],mix.inputs[1]);links.new(emit.outputs[0],mix.inputs[2]);links.new(mix.outputs[0],out.inputs[0])
x=-75.4;y=-57;z=70.5;side=99.85
verts=[(x-side/2,y,z-side/2),(x+side/2,y,z-side/2),(x+side/2,y,z+side/2),(x-side/2,y,z+side/2)]
mesh=bpy.data.meshes.new('Locked 072 MCB sprite plane');mesh.from_pydata(verts,[],[(0,1,2,3)]);mesh.uv_layers.new()
for li,uv in enumerate([(0,0),(1,0),(1,1),(0,1)]):mesh.uv_layers.active.data[li].uv=uv
ob=bpy.data.objects.new('072 three-pole MCB front on rail',mesh);bpy.context.collection.objects.link(ob);ob.data.materials.append(mat);GROUPS['panel'].append(ob)
# A physical short rail behind the replacement MCB retains the rail appearance.
# Append only the registered closed-state MPCBv2 objects, at old middle-device origin.
names=json.loads((P/'mpcb-v2-closed-objects.json').read_text())
with bpy.data.libraries.load(str(P/'mpcb-v2.blend'),link=False) as (src,dst):dst.objects=names
for obj in dst.objects:
 if obj:bpy.context.collection.objects.link(obj);obj.location+=Vector((-25,-2,27));obj.hide_render=False;GROUPS['panel'].append(obj)
scope['camera']((0,0,70),285,1920,1080);s=bpy.context.scene;s.cycles.samples=80
scope['render']('factory-panel-3p.png',['panel'])
(P/'panel-074-layout.json').write_text(json.dumps({'camera':'identical069camera; orthographic285mm, centre0/0/70','MPCB_origin_mm':[-25,-2,27],'contactor_origin_mm':[45,-3,33],'MCB_centre_mm':[-75.4,-57,70.5],'MCB_change':'wider3Pbody; centre3.4mmleftofold1Pcentre to avoid collision; original85mmheight','optional_wiring':'not added; preserve original duct/rail/backplate layout','contactor_objects':contactor_objects},indent=2)+'\n')
bpy.ops.file.pack_all()
bpy.ops.wm.save_as_mainfile(filepath=str(P/'panel-3p.blend'),compress=True)
print('DONE PANEL074',flush=True)
