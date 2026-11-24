# usage: musicmix.py IN.mp4 MUSIC.mp3 OUT.mp4 [music_db=-20] [fade_out=3]
# loops the music under the whole video, ducks it ~10 dB whenever the voice/SFX track is active, fades in/out
import sys,subprocess,json
inp,mus,out=sys.argv[1:4];mdb=float(sys.argv[4]) if len(sys.argv)>4 else -20;fo=float(sys.argv[5]) if len(sys.argv)>5 else 3
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',inp]).decode())
fc=(f"[1:a]aloop=loop=-1:size=2e9,atrim=0:{dur},volume={mdb}dB,afade=t=in:d=1.5,afade=t=out:st={dur-fo}:d={fo},aformat=sample_rates=48000:channel_layouts=stereo[m];"
    f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,asplit=2[v][sc];"
    f"[m][sc]sidechaincompress=threshold=0.02:ratio=6:attack=20:release=400:makeup=1[md];"
    f"[v][md]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]")
subprocess.run(['ffmpeg','-v','error','-y','-i',inp,'-stream_loop','-1','-i',mus,'-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k',out],check=True)
print('music mixed',dur)
