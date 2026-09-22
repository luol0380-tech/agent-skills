# Interview Training

A reusable, platform-neutral skill for AI Product / Agent / AI Solutions/FDE interview practice.

## What it does
Runs structured training with terminology retrieval, sentence compression, AI fundamentals, realistic interview questions, and spaced repetition.

## User configuration
Create local private files when personalized training is needed, for example:
- `private/candidate-profile.md`
- `private/interview-history.md`
- `private/personal-vocabulary.md`

These files are ignored by Git.

The default session template is selected by `config/current_template.txt`.

## Structure
```text
interview-training/
├── SKILL.md
├── README.md
├── config/current_template.txt
├── templates/
│   ├── daily-30min.md
│   ├── mock-interview.md
│   ├── vocabulary-drill.md
│   └── archive/
├── scripts/select_template.py
└── private/README.md
```

## Template rules
User-specified template wins. Otherwise use `current_template.txt`. Add templates with semantic names; move retired templates to `templates/archive/`.
