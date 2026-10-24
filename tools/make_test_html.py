# Build test.html (render harness) from the app file: exposes window.__T and window.__R(ctx,t,scale)
import sys
src=sys.argv[1] if len(sys.argv)>1 else 'app/inkstroke-whiteboard-animator.html'
s=open(src,encoding='utf-8').read()
hook="window.__T={S,refresh,show,layout,tmrState,camAt,loadTemplate,mouthAmt,L:EP5_LINES};window.__R=(c,t,sc)=>{S.t=t;renderFrame(c,t,sc,false)};"
s=s.replace('S.scenes=[newScene',hook+'S.scenes=[newScene',1)
open('test.html','w',encoding='utf-8').write(s)
print('test.html written')
