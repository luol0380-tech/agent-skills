# Detailed Meeting Notes

## Format

```markdown
# [Meeting title]

## Context
- Date: [date or TBD]
- Participants: [names or roles supplied by the source]
- Objective: [objective]

## Discussion by topic
### [Topic]
- Evidence or background: [facts]
- Views raised: [agreements and disagreements]
- Outcome: [decision / proposal / unresolved]

## Decisions and rationale
- [decision] — Why: [supported reason]

## Risks and dependencies
- [risk] — Impact: [impact] — Mitigation: [if stated]

## Action items
- [ ] [task] — Owner: [owner or TBD] — Due: [date or TBD]

## Open questions
- [question] — Next check: [step or TBD]
```

Mark inferred links as `Inference:` and preserve unresolved disagreement.

## Example

Input: `Support reports that setup questions doubled after the new flow. Product proposed restoring one explanation step. Engineering said the change is small but needs analytics verification. The group approved a two-week experiment; analytics ownership is still open.`

Output:

```markdown
# Setup flow review

## Context
- Date: TBD
- Participants: Support, Product, Engineering
- Objective: Reduce setup-related questions.

## Discussion by topic
### Explanation step
- Evidence or background: Setup questions doubled after the new flow.
- Views raised: Product proposed restoring one explanation step; Engineering requested analytics verification.
- Outcome: A two-week experiment was approved.

## Decisions and rationale
- Run a two-week experiment with one explanation step restored — Why: Support volume indicates a comprehension problem.

## Risks and dependencies
- Analytics verification is required before interpreting results.

## Action items
- [ ] Implement the experiment — Owner: Engineering — Due: TBD
- [ ] Confirm analytics ownership — Owner: TBD — Due: TBD

## Open questions
- Who owns experiment analysis? — Next check: assign an owner.
```
