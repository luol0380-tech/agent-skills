---
name: content-publishing
description: Turn verified source material into long-form articles, short social posts, and release packages while preserving facts, human voice, evidence, and publication safety. Use for planning, drafting, revising, repurposing, packaging, or preparing content for an external publishing system.
---

# Content Publishing

## Prepare

1. Identify the audience, real problem, source evidence, desired outcome, and target content form.
2. Load `private/brand-profile.md` and `private/personal-style.md` when present.
3. Treat the latest user-approved draft, title, visual, and wording as authoritative.
4. Resolve the output template using the template-selection rules below.

## Editorial workflow

1. Lock a brief containing the reader, one real situation, the creator's judgment, evidence, limits, and reader takeaway.
2. Ask at most one focused question when a missing fact would materially change the piece.
3. Draft from concrete evidence before abstract conclusions.
4. Preserve the creator's natural wording where it is clear; do not manufacture a polished personal voice.
5. Label prototypes, experiments, or unverified outcomes accurately.
6. Review factual claims, privacy, source permission, image purpose, and unsupported certainty.
7. Obtain content approval before producing final visuals or a release package.
8. Treat local packaging, saving a remote draft, and publishing as separate actions with separate permissions.

## Revision rules

- Continue from the latest approved stage instead of restarting.
- Change only the requested parts unless a factual or safety issue requires broader revision.
- Never invent events, quotes, results, credentials, product status, or performance metrics.
- When repurposing, rebuild around the target reading context instead of cutting paragraphs mechanically.
- Keep account credentials and authenticated publishing logic outside the Skill.

## Template selection

1. If the user names a template, use that template.
2. Otherwise read the single template name from `config/current_template.txt`.
3. Load the matching Markdown file from `templates/`.
4. Use semantic filenames; do not use version labels such as `v1` or `new2`.
5. Move retired templates to `templates/archive/`; never delete them during normal maintenance.
6. Keep every template body, layout, and filled example outside this file.
