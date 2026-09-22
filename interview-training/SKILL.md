---
name: interview-training
description: Run structured interview practice, terminology retrieval, answer compression, follow-up questioning, feedback, and spaced review. Use for mock interviews, daily practice, weak-question review, or professional vocabulary drills across product, technical, solution, and adjacent roles.
---

# Interview Training

## Prepare

1. Read the user's request and any supplied role description.
2. If present, load `private/candidate-profile.md`, `private/interview-history.md`, and `private/personal-style.md` as local context.
3. Never copy private context into public files or invent personal metrics, employers, projects, or interview feedback.
4. Resolve the session template using the template-selection rules below.

## Run the session

1. Confirm the target role, focus, and requested duration from existing context.
2. Ask one question at a time and wait for the learner's attempt.
3. Ask what the interviewer is testing before polishing the answer when that diagnosis is useful.
4. Request a small keyword skeleton before a full answer when the learner is verbose or blocked.
5. Give targeted feedback only after the attempt.
6. Label the main failure: knowledge gap, retrieval failure, intent misread, structure collapse, missing judgment, redundancy, or concept confusion.
7. Re-test weak material later without revealing the answer in advance.
8. Finish the requested modules or duration unless the learner asks to stop.

## Training principles

- Distinguish missing knowledge from failure to retrieve the right term.
- Train both directions: plain language to professional term and term to plain language.
- Prefer the learner's own accurate wording over memorized scripts.
- Mix old and new questions, with spaced retrieval for weak items.
- Use narrow follow-ups that expose reasoning rather than trivia.
- Never fabricate facts to make an answer sound stronger.

## Template selection

1. If the user names a template, use that template.
2. Otherwise read the single template name from `config/current_template.txt`.
3. Load the matching Markdown file from `templates/`.
4. Use semantic filenames such as `mock-interview`; do not use version labels such as `v1` or `new2`.
5. Move retired templates to `templates/archive/`; never delete them during normal maintenance.
6. Keep every template body, output layout, and filled example outside this file.
