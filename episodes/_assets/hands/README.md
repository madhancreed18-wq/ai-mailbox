# Clay 3D cartoon hand sprites

Five original generated right-hand sprites requested in mailbox 062. Every PNG is **1024 × 1024 RGBA** with genuine transparent background. Peach skin, rounded clay fingers, periwinkle purple-blue sleeve and white cuff; soft upper-left lighting with hand self-shading.

## Anchor contract

`hands.json` maps filenames under `sprites` to `fingertip: [x,y]`. Coordinates are **zero-based pixel indices from the top-left** of the final 1024 × 1024 PNG, x right/y down. They refer to the visible leading fingertip contour at alpha ≥ 128, not the centre of the fingernail. Thumbs-up uses the **thumb tip** and is a reaction sprite, not an index-button press. Hover has its own bent-tip anchor. Front is a foreshortened 2D projection pointing into scene depth; metadata does not provide a 3D mesh or depth contact.

The provided `texture_uv_bottom_left` values convert pixel centres for a bottom-left UV convention: `u=(x+0.5)/1024`, `v=1-(y+0.5)/1024`. Match this to the consumer texture's flip-Y behaviour; do not invert twice.

For a screen-space sprite with image top-left T and scale S, position its selected pixel centre at the desired button point B using `T = B - S * ([x,y] + [0.5,0.5])`. Recompute translation with the appropriate per-pose anchor when changing sprites. Retain the full transparent canvas; cropping without updating the anchor invalidates these coordinates.

## Contact points

| Sprite | Contact pixel [x,y] | Digit |
| --- | --- | --- |
| hand-press-upleft.png | [91,125] | index |
| hand-press-left.png | [40,442] | index |
| hand-press-front.png | [391,133] | index |
| hand-hover-upleft.png | [107,181] | index |
| hand-thumbs-up.png | [521,83] | thumb |

## Creation and checks

Generated with the built-in image tool, one call per sprite. The first up-left sprite was the identity/material/lighting reference for the other four. Prompts are preserved in `generation-prompts.json`. Native outputs were resized with Lanczos to the requested 1024 × 1024, retaining RGBA; near-zero alpha values of 1/255 were normalized to fully transparent zero during export; no rotation, synthetic hand modelling or background replacement was applied. Final contact points were calibrated on the exported alpha contour and inspected against the rendered hand poses.

Checked PNG size/mode, fully transparent outer borders, visible alpha at every anchor, exactly one connected alpha≥128 silhouette per sprite, coordinate bounds and SHA-256 file identities. Generated edges retain their antialiasing; this is a consistent bitmap set, not a rigged 3D hand. Hand scale and apparent palm angle vary slightly across poses, so place by anchor and preview transitions in the actual scene. No in-scene button animation or video render has been tested here.
