---
name: content-publishing
description: Turn verified source material into long-form articles, short social posts, and release packages while preserving facts, human voice, evidence, and publication safety. Support AI-practice and family-growth writing, cover, layout, and ending templates through this single entry. Use for planning, drafting, revising, repurposing, packaging, or preparing content for an external publishing system.
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

1. Resolve `writing_template`, `cover_template`, and `layout_template` independently. Read `references/template-routing.md`.
2. Prefer an explicit user choice; otherwise select `ai-practice` for an AI workflow story or `family-growth` for family, relationship, or parenting narrative. Using AI to edit a family story does not change its subject.
3. Default all components to the selected article template. Allow cover-only or layout-only overrides without rewriting approved text or changing its ending.
4. Load `templates/ai-practice.md` or `templates/family-growth.md`. Each defines writing, cover, body layout, and ending rules. Approved component-specific references override generic style defaults.
5. For other content forms, preserve the existing `--template` selector and `config/current_template.txt` fallback. Keep template bodies and examples outside this entry.
6. Preserve the latest approved selections through follow-ups; change only requested components. Never reuse rejected visuals as master references.
7. Keep retired templates in `templates/archive/`. Keep private brand, avatars, real cases and approved reference images in ignored `private/` files; never copy them into public templates.

## Render an article

Use `scripts/render_wechat.py INPUT.json OUTPUT.html` for self-contained HTML. Read `references/article-schema.md` for the schema. `layout_template` controls visuals only; the writing template controls ending and series rules. Never infer series numbers or inject a fixed signature from the cover or layout. Review the rendered result before delivery.
