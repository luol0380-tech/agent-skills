---
name: interview-animation-kit
description: Turn a truthful interview moment or personal story into a short animation insert with a timed script, consistent characters, separate storyboard frames, asset codes, motion instructions, and a production handoff. Use for interview videos, school or camp stories, documentary inserts, and image-to-video preparation.
---

# Interview Animation Kit

## Prepare

1. Identify one observable event, the emotional turn, and what the speaker understood afterward.
2. Load `private/project-context.md` and `private/personal-style.md` when present.
3. Require identity-critical photos, setting references, and exact branded props before generating them.
4. Resolve the output template using the template-selection rules below.

## Workflow

1. Design only the number of visual beats that can be read in the requested duration.
2. Write the timed script before creating images.
3. Lock character identity, clothing, height relationships, environment, time of day, visual medium, palette, aspect ratio, and recurring props.
4. Use stable asset codes: `C` for character, `S` for scene, `P` for prop, and `B` for background.
5. Approve the primary character reference before the first scene.
6. Generate storyboard frames separately and use the approved character plus the preceding scene to preserve continuity.
7. Inspect each frame before continuing; correct one error at a time while preserving approved elements.
8. Deliver a timed script, separate assets, an asset-to-time mapping, continuity rules, per-shot motion notes, negative constraints, and reference order.

## Truth and continuity rules

- Show observable behavior instead of abstract transformation claims.
- Do not add dialogue, relationships, places, logos, signs, or props unsupported by the source.
- Treat a brand or event name as context, not as a visual instruction.
- Keep asset codes in filenames and handoff notes, not inside the artwork.
- Do not combine storyboard frames into a grid unless explicitly requested.
- Do not accept an attractive frame when it changes the story's meaning.

## Template selection

1. If the user names a template, use that template.
2. Otherwise read the single template name from `config/current_template.txt`.
3. Load the matching Markdown file from `templates/`.
4. Use semantic filenames; do not use version labels such as `v1` or `new2`.
5. Move retired templates to `templates/archive/`; never delete them during normal maintenance.
6. Keep every output layout and filled example outside this file.
