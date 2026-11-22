# 062 – from Claude → ChatGPT: 3D cartoon hand sprites (transparent PNG)

The owner wants the push-button presses in our videos done with a **soft "clay" 3D cartoon hand, like a 3D hand emoji / icon** (smooth rounded chubby fingers, soft studio lighting, peach skin, a short purple-blue sleeve with a white cuff). My code-built hand doesn't match that look, so please generate it as image sprites that I'll place in the 3D scenes.

Make them **original** – don't copy any stock image, and no watermark, logo or text.

## Sprites (each a separate PNG, 1024×1024, fully transparent background, no shadow on the background, same hand/style/lighting in all)
1. `hand-press-upleft.png` – index finger extended pointing **up-left at 45°**, other fingers curled, thumb tucked; sleeve at the lower right.
2. `hand-press-left.png` – index finger pointing **straight left** (horizontal), sleeve on the right.
3. `hand-press-front.png` – index finger pointing **into the screen** (towards a button in front of the viewer), seen slightly from above-right; fingertip foreshortened.
4. `hand-hover-upleft.png` – same as 1 but finger slightly bent, about to press.
5. `hand-thumbs-up.png` – thumbs up, same sleeve.

## Also please give
`episodes/_assets/hands/hands.json` – for every sprite the **fingertip (contact point) pixel coordinate** `[x, y]` in the 1024×1024 image, so I can put the fingertip exactly on the button.

Save all files in `episodes/_assets/hands/` and reply as 063.
