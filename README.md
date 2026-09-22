# Reusable Agent Skills

Platform-neutral reusable agent skills.

## Design principles
- Separate public workflows from private user context.
- Each skill uses `SKILL.md + README.md + templates/ + scripts/`.
- Templates are external, semantic-named, and swappable.
- Public skills do not contain personal identity, employer history, contact information, private writing samples, or private interview history.
- Private context stays local and is excluded from Git.

## Skills
- `interview-training/` — structured AI Product / Agent / AI Solutions/FDE interview training.

## Local private configuration
Users should provide their own private profile/context files when personalization is required. Do not commit private context.
