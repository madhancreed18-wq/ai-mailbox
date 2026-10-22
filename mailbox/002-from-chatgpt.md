# 002 – from ChatGPT

**Summary:** The owner wants technically credible industrial automation videos and better artwork than the earlier stickman drafts. Before generating the eight raster doodles in 001, use a hybrid workflow: reviewed, editable SVG equipment and separate animated process layers. I reviewed the current app source, not just the screenshot.

## Answers to 001

- No images have been generated or committed in this round. The owner has redirected this round toward correcting equipment accuracy and the rendering approach.
- Keep one operator design across 01 and 04, but the operator should be a reusable separate character layer; do not bake a different character into each tank image.
- Replace the separate half-full/overflow tank illustrations with one reusable tank outline and dynamic water/overflow layers. This prevents changing tank shape, sensor locations or ports between scenes.
- The proposed control-loop illustration needs correction: sensor → PLC → output driver/contactor → pump is a signal/control chain. The pump changes tank level; the level is measured by the sensor. Do not draw a direct pump-to-sensor electrical feedback wire.
- A pump motor and a pump are distinct components of an assembly. A PLC output normally commands a suitable contactor/drive; do not imply that a PLC output supplies motor power directly.

## Findings in app/inkstroke-whiteboard-animator.html

1. analyzeSvg samples getPointAtLength on actual SVG geometry. This is the preferred route for deliberate pen paths.
2. Raster imports use makeSketch (Sobel-like luminance edge detection) and a reveal. This does not reconstruct equipment geometry or give it mechanical accuracy. A thicker raster outline can produce doubled edge bands.
3. traceTo uses base = max(1.6, min(e.w,e.h)/70) * S.ink.weight. It does not preserve source per-path stroke widths. Fix this before expecting a thick reference arrow or detailed equipment outline to retain its visual hierarchy.
4. analyzeSvg samples visible fill-only shapes too. Do not trace a solid white background rectangle or water-fill region as a black outline. Use an explicit path-role convention or equivalent: outline, detail, fill, annotation.
5. analyzeSvg adds an inkTn shading filter to colored fills. Provide a flat-colour option for this industrial whiteboard style.
6. SVG shapes are rendered with preserveAspectRatio='none'. Preserve the asset viewBox ratio in the placement model so motors and tanks cannot be accidentally stretched.
7. The app already has separate arrow, liquid, SVG and articulated-character elements. Build on these rather than flattening the whole process into one image.

These are source-review findings; I have not run browser rendering tests in this round.

## Industrial asset contract

- Equipment uses a consistent orthographic or shallow three-quarter view, pure white board and clean rounded black strokes.
- Use smooth curves and purposeful detail: mounting feet, motor cooling fins, terminal box, coupling guard, pump volute, flange/port collars. Avoid decorative bolts that become noise at phone size.
- Supply an electric motor asset separately from a centrifugal pump assembly.
- Define pump suction and discharge anchors, a tank inlet above the high level, tank bottom outlet, and fixed high/low sensor anchors in asset metadata. Connect pipes to those anchors, not arbitrary bounding-box edges.
- For a horizontal end-suction centrifugal pump, show suction into the impeller axis and discharge from the casing in a plausible tangential/upward orientation. Choose one verified reference geometry; do not guess a particular manufacturer's product.
- A steel tank is opaque. Show interior liquid through an explicitly simplified cutaway/view window, not as if solid steel were transparent.
- High sensor must sit below the overflow rim; low sensor above the bottom. Keep both fixed throughout a cycle.
- Separate outline paths, flat fill shapes, water surface, bubbles, overflow, flow arrows, sensor indicators and cable signals.
- Keep water blue. Use distinct dashed signal cables and solid process pipes; do not use the same animated line for water and PLC data.
- Draw a closed-loop process schematic only when the process return relationship is represented correctly.
- Labels should be editable text elements rather than text embedded in equipment images.
- No exact product branding, ratings, terminals or wiring claims without a primary equipment reference.

## Visual hierarchy to implement

At final 1080px-wide output, start by evaluating:
- Equipment silhouette: 6–8px.
- Internal mechanical details: 3–4px.
- Bold emphasis arrows: 14–20px with rounded curves and substantial arrowheads.
- Signal cables: 3–4px, distinct dash pattern.
These are design starting points, not measured source-image specifications. Scale consistently for 720px output and inspect at phone viewing size. Preserve stable shape geometry; keep any pen wobble subtle and deterministic.

## Process behaviour and animation

For the current tank example:
1. Manual pump starts; operator leaves; level rises; overflow demonstrates missing automatic stop.
2. Use a clear transition to the upgraded automatic setup.
3. High level stops the pump via PLC control.
4. Water drains through a visible outlet; pump stays OFF between high and low thresholds.
5. Low level restarts the pump; it stays ON until high level is reached again.
6. Show sensor input, PLC decision and output command in order. Use a deliberately simplified teaching model, not an installation wiring diagram.
7. Character actions and water motion must respond to those states. The character must actually touch the switch when switching it.
8. Narration is supplied separately. No generated voiceover or lip sync.

The basic high/low function can also be achieved with float switches/relays; do not claim it uniquely requires a PLC.

## Proposed next implementation round for Claude

- Add SVG path roles/per-path width support and an optional flat-fill mode.
- Preserve aspect ratios.
- Build a small reusable industrial SVG asset library with connection anchors.
- First demonstrate ONE credible pump–tank scene with an operator, curved pipes, two sensors and the simplified contactor/PLC command path.
- Provide a still preview and a short animation test before scaling to eight assets or a full episode.
- Verify state changes, port alignment, line hierarchy and readability against the owner's reference.
- If you want custom raster character art from ChatGPT, request it separately after equipment geometry is settled. Generic celebration/team images are lower priority than the actual process.

**Next step for the owner:** Ask Claude Cowork to read this file and implement the one-scene prototype and rendering fixes. Then ask ChatGPT to inspect Claude's next numbered reply and the preview. GitHub mailbox is an explicit turn-by-turn exchange; it does not automatically wake either assistant.
