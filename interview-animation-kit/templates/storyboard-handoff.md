# Storyboard Handoff

## Format

```markdown
# [Project] — Production handoff

## Asset manifest
- C01 — [character card and source]
- S01 — [scene description] — Time: [range]
- P01 — [identity-critical prop] — Used in: [scenes]

## Global continuity
- [identity, clothing, environment, medium, palette, aspect ratio]

## Shot instructions
### S01 — [filename]
- Motion: [motion]
- Expression: [expression]
- Camera: [camera]
- Dialogue/Narration: [line or none]
- Preserve: [invariants]
- Avoid: [negative constraints]

## Reference upload order
1. [primary character reference]
2. [environment reference]
3. [preceding scene]
```

Every asset must have one code, one purpose, and a time mapping. Use separate downloadable frames; do not rely on conversation order.

## Example

Input: `Prepare a handoff for one character card, three scenes, and one branded notebook that must remain exact.`

Expected manifest: `C01`, `S01`–`S03`, and `P01`, followed by global continuity, per-shot motion/camera notes, negative constraints, and upload order.
