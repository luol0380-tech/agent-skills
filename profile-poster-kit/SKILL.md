---
name: profile-poster-kit
description: Create a coordinated profile poster and character model sheet from a portrait, verified identity text, and optional local brand assets. Use when producing, revising, batching, or standardizing person-introduction visuals while preserving identity, text accuracy, adult proportions, and cross-image consistency.
---

# Profile Poster Kit

## Prepare

1. Collect a clear portrait, display name, role, and verified biography lines.
2. Load `private/brand-style.md` and `private/subject-profile.md` when present.
3. Treat the portrait as the identity source and local private assets as optional style references.
4. Never infer a person's name, credential, family role, organization, or biography from the image.
5. Resolve the output template using the template-selection rules below.

## Workflow

1. Group supplied facts without changing their meaning; omit empty groups.
2. Lock face, age impression, hair, glasses, expression, body proportions, clothing system, palette, and stable accessories.
3. Generate or design the primary poster first and inspect text, anatomy, hierarchy, and identity.
4. Build the character sheet from the approved poster character, using the portrait as a secondary identity reference.
5. Compare both outputs side by side for face, proportions, clothing, colors, and accessories.
6. Correct one failing element at a time while preserving approved elements.
7. Deliver only after inspecting every visible name, biography line, hand, limb, and recurring design cue.

## Accuracy rules

- Render supplied identity text verbatim unless the user approves editing.
- Add no credential, slogan, translation, seal, logo, or organization mark that was not supplied.
- Keep adult proportions unless the requested style explicitly requires otherwise.
- Treat public templates as layout guidance; keep portraits and proprietary brand assets local.
- Do not claim identity or text accuracy without visual inspection.

## Template selection

1. If the user names a template, use that template.
2. Otherwise read the single template name from `config/current_template.txt`.
3. Load the matching Markdown file from `templates/`.
4. Use semantic filenames; do not use version labels such as `v1` or `new2`.
5. Move retired templates to `templates/archive/`; never delete them during normal maintenance.
6. Keep every prompt layout and filled example outside this file.
