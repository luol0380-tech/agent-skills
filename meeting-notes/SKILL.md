---
name: meeting-notes
description: Turn transcripts, recordings, rough notes, or chat logs into factual meeting notes with decisions, open questions, risks, owners, and action items. Use when creating concise, detailed, leadership-facing, or follow-up-ready meeting records.
---

# Meeting Notes

## Prepare

1. Identify the meeting purpose, date, participants or roles, and source material.
2. Load `private/personal-style.md` when it exists; treat it only as a style preference.
3. Separate explicit facts from reasonable inferences. Label uncertainty instead of filling gaps.
4. Resolve the output template using the template-selection rules below.

## Process

1. Extract topics, decisions, reasons, objections, risks, unanswered questions, and follow-up work.
2. Merge repeated statements without erasing disagreements.
3. Preserve the distinction between a proposal, a discussion, and a final decision.
4. Assign an owner or deadline only when the source provides one; otherwise write `TBD`.
5. Keep action items testable and begin them with a verb.
6. Check names, dates, numbers, and commitments against the source before delivery.
7. Surface sensitive or uncertain passages for review rather than presenting them as settled facts.

## Template selection

1. If the user names a template, use that template.
2. Otherwise read the single template name from `config/current_template.txt`.
3. Load the matching Markdown file from `templates/`.
4. Use semantic filenames such as `brief` or `for-boss`; do not use version labels such as `v1` or `new2`.
5. Move retired templates to `templates/archive/`; never delete them during normal maintenance.
6. Keep every template body and filled example outside this file.

## Privacy

Do not place raw transcripts, participant contact details, internal project names, or personal writing samples in public Skill files. Store reusable private preferences locally under `private/`.
