---
name: ugs-prompt
description: Use when the user wants to write image or video generation prompts in UGS (Universal Generation Specification) style — world-simulation-first, not picture-description. Also use when the user asks for "realistic", "cinematic", "game-style", "meme", "horror", or "anime" prompts that should feel causally coherent rather than decorative. Load when asked to "write a prompt", "make a UGS prompt", or when a generation request risks being picture-centric.
---

# UGS Prompt Skill

You write generation prompts (image/video) in **UGS v2** style: specify a *world*, let the *image emerge*. Never describe the picture; describe the causes.

## Core law (never violate)

> Do not describe the picture. Describe the world. The picture emerges on its own.

Priority order (non-negotiable):
```
Reality → Simulation → Observation → Rendering
```
Never the inverted decorative pipeline `Prompt → Composition → Beautiful Image`.

## When to load this skill
- User asks for a prompt for image/video generation.
- User says "UGS", "world-sim", "make it real", "not a pretty picture".
- Any request where coherence matters more than a single pretty frame.

## Operating procedure (follow every time)

1. **Detect language.** If the user writes Russian, emit Russian (cite `spec/ru/UGS-v2.md`). If English, emit English (cite `spec/en/UGS-v2.md`). Bilingual sessions: match the user's sentence.
2. **Classify the domain** using the playbooks (spec §25): photography, product, architecture, portrait, landscape, urban, historical, sci-fi, fantasy, underwater, macro, still-life, video, game, meme, horror.
3. **Fill the standard template** (field by field — empty field = failure):

```yaml
ontology:        # what kinds of things exist
world_rules:     # >=1 invariant law (physics/society/magic)
history:         # origin, age, owner of key objects
simulation:      # current state, INCLUDING off-frame
physics:
  light:        # power, temp(K), scattering, reflections, falloff, atmosphere
  material:     # behavior, wear, history, physics
environment:     # off-frame causes for on-frame content
characters:      # purpose + biography, NO posing
camera:         # observer by chance, hyperfocal default, DOF only if caused
observation:     # witnessed slice, not composed
```
   For video add `temporal` (accel/inertia/mass/begin/end) + `audio` (diegetic).
   For meme use `axiom_change: <exactly ONE>` + `everything_else: normal`.
   For game-frame use the `engine:` block (renderer/gpu/materials/lod/shadows/lighting/textures/hardware_era).
4. **Apply the verb-tense rule:** prefer past/present-perfect-continuous for states ("has been walking"), causal clauses over attributive ("lit because the plant runs"). Avoid bare appearance labels.
5. **Run the emergence test:** could the image be predicted without describing it directly? If you named colors/angles/mood to get the look → you described a picture. Rewrite.
6. **Run the checklist (spec §21):** all 10 levels must pass. If any fails, return to that level. Never patch at rendering.
7. **Scan failure taxonomy (spec §23):** refuse to emit if any F-code applies (floating subject F1, anachronism F2, inconsistent light F3, director camera F4, uncaused DOF F5, pastiche F6, identity loss F7, dead detail F8, teleport cut F9, acting F10, non-diegetic audio F11, decoration F12, noise meme F13, monster-shock F14, painterly game F15, slideshow video F16, skipped level F17).
8. **Emit** the filled template as the prompt. Optionally prefix with a one-line intent. Do NOT add "beautiful", "cinematic", "epic", "dramatic" as goals — they are byproducts of structure.

## Hard constraints (treat as non-negotiable)
- Hyperfocal focus by default. Artificial DOF / bokeh / portrait blur ONLY if caused by the observer's equipment and part of the story (spec §8.3).
- Camera is an observer, never a director. Give it a biography if it is a character.
- No random surrealism, decorative details, beautiful poses, random effects, chaos, visual noise (spec §15).
- Memes: change EXACTLY ONE axiom, keep everything else maximal-normal (spec §16).
- Horror: fear from understanding the world, monsters optional and rule-bound (spec §17).
- Games: simulate the engine's actual constraints, don't paint a screenshot (spec §18).

## Anti-patterns to refuse
- "Cinematic shot of X, dramatic lighting, shallow DOF" → rewrite via world.
- "Futuristic city" (style label) → specify the history that produced the form.
- "Mysterious glow" → give the physical source.
- "Epic dragon" with undefined magic → define the world rule first.

## Output format
Return the prompt as a fenced code block (yaml or markdown) plus a 1–2 sentence note on which UGS levels you emphasized and any assumption you made. If the user gave a picture-centric draft, first show the failure codes, then the UGS rewrite.

## References
- Full spec EN: `spec/en/UGS-v2.md` (and `spec/en/UGS-v2.pdf`)
- Full spec RU: `spec/ru/UGS-v2.md` (and `spec/ru/UGS-v2.pdf`)
- Templates: spec §26. Playbooks: spec §25. Exemplars: spec §31. Critique workshop: spec §32.
