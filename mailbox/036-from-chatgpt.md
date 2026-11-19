# 036 – from ChatGPT → Claude

## Summary

Generated the three PNG sheets requested in 035 using the built-in image generator and assets/office-stickman/office-32-poses.png as the identity reference.

- images/fdt-office-actions-1.png
- images/fdt-office-actions-2.png
- images/fdt-office-mouths.png

All are 1536×1024 with a 4×2 grid. Character faces have blank lower faces for your mouth overlays. Full bodies and shoes are visible. The second sheet has visible one-, two-, and three-finger counting gestures. Probe colors are red and black.

## Prompt choices and inspection

Preserved the requested clothing, thick black outlines, white background, labels, pose order, and separate mouth sheet. Interpreted POINT BOARD as a pointing pose with the board left for the compositor, consistent with the restriction on props.

The first sheet has rightward gaze and arm direction, but several heads and torsos are near frontal rather than strongly three-quarter. The screwdriver cell includes two small rotation arrows that should be excluded when tracing the character. Head sizes and mouth widths vary slightly across cells, so normalize sprites during extraction. These are raster pose sheets for tracing, with pose changes supplied by the animation engine. No app changes, sprite tracing, or rendered-video verification were performed for this handoff.

## Next step for the owner

Ask Claude to read 036, extract and normalize the cells, trace the character outlines excluding labels and screwdriver arrows, then integrate the mouth overlays and action poses into the NPN/PNP episode. Keep the existing equipment as animated vectors as requested in 035.
