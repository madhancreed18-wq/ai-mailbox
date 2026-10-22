# Inkstroke – whiteboard video maker

Inkstroke is a single-file web app (`app/inkstroke-whiteboard-animator.html`)
that makes lively, hand-drawn whiteboard explainer videos. Open it in Chrome or
Edge; no install, no server.

It was built by reverse engineering how tools like VideoScribe, Doodly,
Animaker, InstaDoodle and AnkonAI-style explainers look and move, using the
"see a feature → explain how it works → build your own" method from
[REA](https://github.com/morluto/rea).

## Features

### Drawing
- A hand draws every item stroke by stroke, then paints the color in
- Marker-ink lines: tapered, slightly wobbly, with gentle "living line" jitter
- Color styles: smooth brush or crayon scribble
- Doodles get cartoon shading (soft shadow bottom-right, highlight top-left)

### Images → drawing
- Upload PNG/JPG/WebP or SVG
- Line art and AI doodle images: the center of every ink line is traced, so the hand draws them like an artist
- Photos: outlines are found and traced
- Drawing styles: lines + cartoon color, lines then real photo, line art only, pencil shading
- Line detail: low, medium, high

### Characters
- **Doodle characters:** curved, tapered limbs, shaped torso, sleeves and collars, 3/4 head with ear, nose, eyes with lids, eyebrows, blush
  - Outfits: office, worker (hi-vis + hard hat), casual, doctor, student, chef
  - 4 skin tones; hair: short, long, curly, bun, spiky, bald; custom colors
  - Extras: hard hat, cap, tie, glasses
- **Stickmen:** smooth curved limbs, bold eyes and brows, round hands and shoes
- 14 actions: stand, wave, walk, run, point, talk, think, cheer, jump, press button, type, shrug, dance, surprised
- Walk/run a set distance, then switch to a second action (for example walk in, then wave)
- Faces: auto, smile, big grin, surprised, thinking, sad, neutral

### Lively elements
- Arrows: curve, curly loop, zig-zag lightning, right angle
- Arrow lines: marker ink, dashed signal (moving dashes), water flow
- Tank filling with rising level, waves and bubbles
- Looping motion after drawing: sway, bob, float, pulse, spin, shake, blink
- Entrances: draw, pop in, fade in, slide in; "start with previous" to draw items together

### Doodle library
- Ideas: light bulb, gear, rocket, bar chart, heart, cloud, star, pet bowl, factory, check badge, arrow, person, warning sign, wrench, clock, padlock, target, sun
- Industry: PLC, pump, tank, switch, level sensor, valve, worker, lightning, water drop

### Video
- Scenes with thumbnails; transitions: camera pan, eraser wipe, fade, zoom, cut
- Boards: whiteboard, paper, chalkboard, glassboard
- Captions per scene (split by sentence)
- Voice-over per scene (upload audio) and background music (dips under voice, fades at the end)
- Templates: Character explainer, How a PLC works, Product explainer, Safety training, Education lesson, Marketing promo
- Save / open project (.json)
- Export MP4 or WebM at 720p or 1080p, with audio

## How to use

1. Pick a template, or start with the empty scene.
2. Add doodles, characters, text, arrows or images from the left panel.
3. Drag items to move them; drag the corner square (or arrow end dots) to change them.
4. Select an item and set its timing, color, entrance, motion or action in the right panel.
5. Add scenes, captions, voice-over and music.
6. Press Play to preview, then Export video.

Tip: images with thick black outlines, a white background and flat colors trace best.

## How it works

| Part | Technique |
| --- | --- |
| SVG drawing | Shapes sampled with `getPointAtLength` into pen paths, split at sub-path jumps |
| Marker ink | Points pushed sideways by smooth noise, tapered width; noise re-seeded 8×/s |
| Color reveal | Pre-rendered color layer shown through a growing zig-zag brush or crayon hatch mask |
| Shading | SVG filter per colored shape: eroded alpha, offset → inner shadow + highlight |
| Line art images | Dark ink mask → Zhang-Suen thinning → centerline tracing |
| Photos | Canny edges (blur, Sobel, non-maximum suppression, hysteresis) |
| Stroke order | Douglas-Peucker + Chaikin smoothing, then nearest-end order from top-left |
| Characters | 2-bone limbs from joint angles, feet snapped to the ground, one pose function per action |
| Doodle bodies | Limbs curve through the joint and taper; outline drawn first, color on top |
| Scenes | Each scene rendered off-screen, then composited for pan, wipe, fade, zoom |
| Audio | Web Audio: voice-over per scene, looping music with ducking and fade |
| Export | `canvas.captureStream` + audio stream → `MediaRecorder` (MP4 or WebM) |

## Roadmap

- Type a prompt → Claude draws a doodle (vector) for the scene
- Images from ChatGPT through this mailbox repo → traced into scenes
- Joint-by-joint custom posing
- Sitting poses and props (desk, chair, laptop)
- More hand styles; GIF and 4K export
