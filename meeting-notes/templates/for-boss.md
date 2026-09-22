# Leadership Meeting Brief

## Format

```markdown
# [Meeting title] — Leadership brief

## One-line status
[current status and direction]

## Decisions
- [decision and business effect]

## Risks
- [risk] — Impact: [impact] — Response: [response or TBD]

## Support needed
- [specific decision, resource, or escalation]

## Next milestones
- [date or TBD] — [milestone] — Owner: [owner or TBD]
```

Prioritize business impact, uncertainty, and requests for leadership. Exclude conversational detail that does not change a decision.

## Example

Input: `The pilot met its adoption target but response time is above the agreed limit. The team wants one more week to optimize. A temporary infrastructure budget increase needs approval by Wednesday.`

Output:

```markdown
# Pilot review — Leadership brief

## One-line status
Adoption is on target; performance must improve before expansion.

## Decisions
- Extend optimization for one week before making the rollout decision.

## Risks
- Response time exceeds the agreed limit — Impact: poor user experience at scale — Response: one-week optimization.

## Support needed
- Approve the temporary infrastructure budget increase by Wednesday.

## Next milestones
- Wednesday — Budget decision — Owner: TBD
- Next week — Performance recheck — Owner: Technical lead
```
