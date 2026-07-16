# UGS v2 — Universal Generation Specification

UGS is not a prompt. UGS is a **specification of a virtual reality**. Any image or video is a *consequence* of a simulation, never its goal.

> **Do not describe the picture. Describe the world. The picture emerges on its own.**

Priority order (non-negotiable):

```
Reality → Simulation → Observation → Rendering
```

## Repository layout

| Path | Contents |
|---|---|
| `spec/en/UGS-v2.md` | Full English specification (source of truth) |
| `spec/en/UGS-v2.pdf` | Rendered English PDF |
| `spec/ru/UGS-v2.md` | Full Russian specification (same depth) |
| `spec/ru/UGS-v2.pdf` | Rendered Russian PDF |
| `skill/SKILL.md` | OpenCode skill: write prompts in UGS style |
| `skill/refs/template.md` | Fill-in prompt templates (standard / video / meme / game) |
| `build_pdf.py` | Markdown → PDF builder (reportlab, Cyrillic-aware) |

## Quick start

1. Read the spec for your language (`spec/en` or `spec/ru`).
2. To author a prompt, load the `ugs-prompt` skill, or use `skill/refs/template.md`.
3. Fill the template field by field. Empty field = failure.
4. Run the checklist (spec §21) and the failure taxonomy (spec §23).

## Build the PDFs

```powershell
python build_pdf.py spec/en/UGS-v2.md spec/en/UGS-v2.pdf
python build_pdf.py spec/ru/UGS-v2.md spec/ru/UGS-v2.pdf
```

## License

MIT — do what you want, but the world must stay consistent.
