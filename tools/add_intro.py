"""Insert the channel intro (assets/brand/intro.mp4, 6 s, FD logo) into a finished long video.

usage: python3 tools/add_intro.py IN.mp4 OUT.mp4 [--at SECONDS]
  --at 0        intro at the very start
  --at 12.4     intro right after the hook (recommended: the end of the first paragraph)
The intro is scaled to the video's size/fps; its own sound plays, the narration resumes after it.
"""
import subprocess, sys, json
a = sys.argv; src, out = a[1], a[2]; at = float(a[a.index('--at') + 1]) if '--at' in a else 0.0
INTRO = __file__.rsplit('/tools/', 1)[0] + '/assets/brand/intro.mp4'
p = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate',
                               '-of', 'json', src], capture_output=True, text=True).stdout)['streams'][0]
W, H, fps = p['width'], p['height'], p['r_frame_rate']
v = f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,fps={fps},format=yuv420p,setsar=1'
au = 'aresample=48000,aformat=channel_layouts=stereo'
if at <= 0:
    fc = f'[1:v]{v}[iv];[1:a]{au}[ia];[0:v]{v}[mv];[0:a]{au}[ma];[iv][ia][mv][ma]concat=n=2:v=1:a=1[v][a]'
else:
    fc = (f'[0:v]{v},split[v0][v1];[0:a]{au},asplit[a0][a1];[v0]trim=0:{at},setpts=PTS-STARTPTS[va];[a0]atrim=0:{at},asetpts=PTS-STARTPTS[aa];'
          f'[v1]trim={at},setpts=PTS-STARTPTS[vb];[a1]atrim={at},asetpts=PTS-STARTPTS[ab];[1:v]{v}[iv];[1:a]{au}[ia];'
          f'[va][aa][iv][ia][vb][ab]concat=n=3:v=1:a=1[v][a]')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-i', INTRO, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', out], check=True)
print('wrote', out)
