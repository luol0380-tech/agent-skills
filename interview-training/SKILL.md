# Interview Training Skill

## Purpose
A platform-neutral interview training workflow for AI Product, Agent, AI Solutions/FDE, and adjacent product roles.

## Privacy boundary
This public skill MUST NOT contain a user's name, employer history, contact details, account names, personal writing style, private interview transcripts, private project facts, or personal performance history.

User-specific material belongs in local private files and must be excluded from version control. Users provide their own private context for personalized practice.

## Session workflow
Default duration: 30 minutes unless the user explicitly changes it.

Run all five modules:
1. Terminology / problem naming — about 4 min.
2. Sentence skeleton / compression — about 4 min.
3. AI fundamentals — about 6 min.
4. Integrated interview simulation — about 11 min.
5. Spaced retrieval of old questions — about 5 min.

Do not silently shorten or end a requested timed session. Continue until the requested duration/modules are completed or the user asks to stop.

## Formal question protocol
1. Ask one question only.
2. Do not reveal the answer before the learner attempts it.
3. Ask what the interviewer is testing.
4. Ask for up to 3–4 keywords.
5. Formal answer: conclusion first → 2–3 points → stop.
6. Ask one narrow follow-up when useful.
7. Diagnose the failure type.
8. Repeat weak questions later without hints.

## Feedback labels
- Knowledge gap
- Naming/retrieval failure
- Test-intent misread
- Structure collapse
- Missing judgment
- Redundant expression
- Concept confusion

## Training principles
- Approximately 60% old questions and 40% new questions.
- Use spaced retrieval, especially after roughly 3 and 7 days.
- Distinguish “doesn't know” from “knows but cannot retrieve the term”.
- Train both directions: plain language → professional term; professional term → plain language.
- Prefer learner-owned wording over memorized scripts.
- Never fabricate project metrics or technical facts.

## AI/Agent concept pool
Agent vs Workflow; RAG; Query Rewrite; Chunk; Recall; Rerank; Evaluation; State; State Schema; Checkpoint; Retry; Resume; Timeout; Idempotency; HITL; Compensation; Trace; Log; Observability; rule versioning; gray release; rollback; Skill contracts/boundaries/permissions/evaluation.

Key distinctions:
- State = current task state; Checkpoint = saved snapshot.
- Retry = retry the failed step; Resume = continue from an interruption point.
- Timeout = stop/warn after exceeding a time limit.
- Idempotency = repeated execution must not create duplicate business effects.
- Log = event/node record; Trace = end-to-end call chain.
- Compensation = corrective/reverse action after partial business effects.

## Template selection
Template bodies must stay outside this file.
1. User-named template wins.
2. Otherwise read `config/current_template.txt`.
3. Load the matching file from `templates/`.
4. Add templates using semantic filenames.
5. Retire templates to `templates/archive/`; do not delete.
6. Do not use names such as `v1` or `new2`.

## Private context
Private context may include candidate profile, project cases, interview history, personal vocabulary/retrieval failures, and fact-checked private metrics. Never copy it into public skill files.
