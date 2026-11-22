# 063 – from ChatGPT → Claude: clay 3D hand sprite set

## Summary
Completed the five original generated hand sprites requested in 062. All PNGs are **1024 × 1024 RGBA with transparent background**, saved under:

`episodes/_assets/hands/`

## Files and contact points
Coordinates are integer pixel indices in the final exported PNG, **origin top-left**, x right / y down.

| PNG | Fingertip [x,y] | Contact digit |
| --- | --- | --- |
| hand-press-upleft.png | [91,125] | index |
| hand-press-left.png | [40,442] | index |
| hand-press-front.png | [391,133] | index |
| hand-hover-upleft.png | [107,181] | index |
| hand-thumbs-up.png | [521,83] | thumb |

`hands.json` contains the filename-keyed `sprites` map with `fingertip` arrays, contact digit, pose, alpha at each anchor, silhouette bounds, pixel-centre UVs and PNG SHA-256 identities. `README.md` documents placement and flip-Y conventions. `generation-prompts.json` preserves the exact prompt set.

## Style and pose interpretation
Soft smooth clay 3D, peach skin, rounded chubby fingers, short purple-blue sleeve and white cuff, upper-left studio light. The first generated up-left hand was used as identity/material/lighting reference for the other four; no stock image was used as an input. No button, backdrop, text, logo or visible watermark is part of the sprites.

The front pose is a foreshortened index pointing away into scene depth, viewed from above-right; its coordinate is a projected 2D visible-tip anchor, not a 3D depth coordinate. The hover index is bent with its own anchor. For thumbs-up the requested fingertip field refers to the **thumb tip**; it is a reaction pose, not an index pressing gesture.

## Export and checks actually performed
Generated with the built-in image tool, one call per sprite. Resized native outputs to exactly 1024 × 1024 with Lanczos while retaining RGBA. Near-zero 1/255 alpha noise was normalized to zero during export; no background fill or hand remodelling was applied.

Visually inspected the generated poses and exported front pose; calibrated anchors from the final alpha contour. Verified exact PNG dimensions/mode, fully transparent outer borders, one connected alpha≥128 hand silhouette per image, in-bounds anchors and alpha≥128 at each contact point. File hashes are recorded in the metadata. Slight perspective/scale differences remain between generated poses; use each pose's own anchor and preview transitions in the consuming scene.

These are bitmap sprites, not a rigged 3D model. No in-scene button animation, texture flip-Y behaviour or rendered-video integration has been tested here. This handoff delivers 062 and does not mark the separate EP12 thumbnail request in 060 complete.

## Next step for the owner
Ask Claude to read **063**, load the PNGs and `hands.json`, and align each per-pose fingertip to the button. Preserve the full transparent canvas, account for the consumer's texture flip-Y once, and preview hover-to-press transitions before replacing the existing hand animation.
