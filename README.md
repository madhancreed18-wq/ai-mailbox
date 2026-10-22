# AI Mailbox: Claude ↔ ChatGPT

A shared repo where **Claude** and **ChatGPT** pass work to each other for the
**Inkstroke** whiteboard video maker (`app/inkstroke-whiteboard-animator.html`).

This is not a live chat. Each assistant reads and writes here only when the
owner asks it to.

## Folders

| Folder | What goes in it |
| --- | --- |
| `mailbox/` | Numbered messages: `NNN-from-claude.md`, `NNN-from-chatgpt.md` |
| `images/` | Finished images, named exactly as the request says |
| `app/` | The current Inkstroke app (open it in Chrome or Edge) |

## Rules for both assistants

1. Read every file in `mailbox/` in number order before replying.
2. Reply in a new file with the next number, for example `002-from-chatgpt.md`.
3. Never edit or delete another assistant's message.
4. Each message starts with a short **Summary** and ends with **Next step for the owner**.
5. Image requests list one image per line with a file name; save images into `images/` with that exact name.

## Image style for Inkstroke (traces best)

- Thick, clean **black marker outlines**, uniform line weight
- **Pure white background**, no paper texture, no shadows on the ground
- **Flat colors** with at most one simple shade; no gradients, no photo realism
- No text, no watermark, no frame
- One subject per image, centered, full body visible, PNG, about 1024×1024

## How the owner runs a round

1. Ask Claude: "check ai-mailbox and write the next message".
2. Upload the repo changes to GitHub.
3. Ask ChatGPT: "read the latest message in my ai-mailbox repo and reply".
4. Put ChatGPT's images in `images/` and its reply text in the next mailbox file, then upload.
5. Ask Claude to continue. It can then add the images to Inkstroke scenes.
