import json,struct
from pathlib import Path
p=Path(__file__).resolve().parent.parent
b=(p/'vfd-3d.glb').read_bytes();magic,version,length=struct.unpack_from('<4sII',b);assert magic==b'glTF' and version==2 and length==len(b)
n,kind=struct.unpack_from('<II',b,12);assert kind==0x4e4f534a
g=json.loads(b[20:20+n]);nodes={o['name']:o for o in g['nodes']};required=['Body','Heatsink','Fan','Keypad','Display','Pot','ChargeLED','TerminalCover']+['T_'+x for x in ['R','S','T','U','V','W','PE','P','N','B1','B2']]+['C_'+x for x in ['FWD','REV','X1','COM','10V','AI','GND','AO','RA','RB','RC']]
assert set(required)<=nodes.keys(),set(required)-nodes.keys()
tri=sum(g['accessors'][p['indices']]['count']//3 for m in g['meshes'] for p in m['primitives']);assert tri<150000
assert all('uri' not in x for x in g.get('buffers',[]));assert not g.get('animations');assert 'PreviewDigits' not in nodes
man=json.loads((p/'vfd-3d-manifest.json').read_text())
for name,xyz in {**man['terminal_centres_gltf_m'],**man['pivots_gltf_m']}.items():
 actual=nodes[name].get('translation',[0,0,0]);assert max(abs(a-b) for a,b in zip(actual,xyz))<1e-6,(name,actual,xyz)
man['exported_triangles']=tri;man['glb_bytes']=len(b);man['validation']='GLB header, required names, triangle limit, embedded buffers, terminal origins and moving pivots passed.'
(p/'vfd-3d-manifest.json').write_text(json.dumps(man,indent=2)+'\n')
print(json.dumps({'triangles':tri,'bytes':len(b),'required_names':len(required),'nodes':len(nodes),'checks':'PASS'}))
