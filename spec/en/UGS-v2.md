# UGS v2 — Universal Generation Specification

> **Version:** 2.0 (full specification)
> **Language:** English (primary)
> **Origin:** Derived from the design note *"UGS v2 — Design Goals"* by Konstantin Parashchuk.
> **Companion:** A Russian-language edition (`spec/ru/UGS-v2.md`) carries the same structure and depth.
> **Purpose:** A model-agnostic specification for generating images and video from *world simulation* rather than *picture description*. This document is intended to be **operated upon** — quoted, checked against, and enforced — by prompt-authoring agents and humans alike.

---

## 0. What UGS Is — and Is Not

UGS is **not a prompt**.

UGS is a **specification of a virtual reality**.

This distinction is not semantic hair-splitting; it is the entire foundation. A prompt says *"make this."* A specification says *"here is how a world works; now observe it."* The difference determines what the generator is allowed to invent, what it must deduce, and what it must refuse to do.

Any image or video produced under UGS is a *consequence* of a simulation, never its goal. The generator must never ask itself:

> "How do I make a beautiful shot?"

It must ask:

> "What frame would naturally arise in this world, given everything that has happened in it up to this moment?"

This single inversion — goal becomes byproduct — is the defining property of UGS and the reason it differs from "cinematic prompt" collections that merely accumulate visual tricks. Those collections are lists of effects. UGS is a **decision hierarchy**: first the construction of the world and its causality, then the modeling of its state, and only at the very end the selection of the observed image or video.

### 0.1 Why "specification" and not "prompt"

A prompt is addressed to a model as a command. It is evaluated by the model as an instruction to maximize the probability of producing something matching the words. The model has no obligation to be *consistent* — only to be *matchable*. This is why prompt-based generation produces beautiful-but-impossible images: a lake that violates its own shoreline, a character whose handedness flips between cuts, a room whose door opens onto a wall.

A specification is addressed to a world. It is evaluated by the generator (human or model) as a set of constraints that a simulated reality must satisfy. Consistency is no longer optional; it is the *definition* of compliance. When you specify the world, the image cannot contradict it, because the image is downstream of the world.

### 0.2 The role of the generator

Under UGS the generator is not an artist taking creative liberties. It is a **rendering process** — the final, mechanical stage of a pipeline that begins with ontology and ends with observation. The creative act happens *earlier*, in world design, where it belongs. By the time the generator runs, the only freedom left is the accidental freedom of "where the camera happened to be."

This reframing solves the oldest problem in generative art: the tension between control and surprise. In prompt-based work you either over-constrain (and get sterile results) or under-constrain (and get chaos). In UGS you constrain the *world* richly and let the *observation* be loose. Control lives upstream; surprise lives downstream. They no longer fight.

### 0.3 Scope of this document

This specification covers:

- The non-negotiable priority order (Section 1).
- The master principle and its operational consequences (Section 2).
- The ten structural layers of a UGS world: past (3), off-frame existence (4), causality (5), materials (6), light (7), camera (8), reference synthesis (9), identity (10), environment (11), temporality (12).
- Domain extensions: animation (13), audio (14), negative constraints (15), memes (16), horror (17), games (18), video (19).
- The master formula and how to apply it (20).
- An operational authoring checklist (21).
- Worked examples and counter-examples (22).
- A reference taxonomy of failure modes (23).
- Guidance for machine-readable use (24).

---

## 1. Priority Order (Non-Negotiable)

Always respect the following order. It is the spine of the entire system.

```
Reality
   ↓
Simulation
   ↓
Observation
   ↓
Rendering
```

**Never** the inverted, decorative pipeline:

```
Prompt
   ↓
Composition
   ↓
Beautiful Image
```

### 1.1 What each level means

- **Reality** — the ontological substrate. What *is*. The physical, social, and material facts that obtain in the world before any observer exists.
- **Simulation** — the temporal process. Reality evolving through time according to its rules. State at moment *t* is a function of state at *t-1* and the world's laws.
- **Observation** — a bounded slice of the simulated reality captured by an observer (camera, witness, sensor) that happens to be present.
- **Rendering** — the mechanical translation of that observation into pixels or frames.

### 1.2 Why the order cannot be reversed

If you start from "Beautiful Image" you have already committed to a goal that the world must serve. The world then becomes a prop. Every inconsistency is hidden or rationalized to protect the pretty picture. The result is *decorative realism* — it looks right in isolation and collapses under scrutiny.

If you start from "Reality" you have committed to truth. The image that emerges may not be beautiful by conventional standards, but it will be *inevitable*. Inevitability reads as realism even when the subject is ugly, mundane, or frightening.

### 1.3 Enforcement

This order is not advice. A UGS-compliant request that reaches the rendering stage having skipped an earlier level is **non-compliant** and must be sent back to the missing level. Skipping levels is the single most common cause of artificial output. The checklist in Section 21 exists to catch exactly this.

---

## 2. The Master Principle

> **Do not describe the picture. Describe the world. The picture emerges on its own.**

This is the sentence that, if internalized, makes most "prompt engineering" obsolete. Everything else in this document is an elaboration of it.

### 2.1 The mechanism

When you describe a picture, you enumerate *surface features*: a man stands, a house is destroyed, it rains. These are labels applied to a frozen frame. They carry no information about why the frame looks that way, so the generator fills the gaps with the statistically most likely clichés.

When you describe a world, you enumerate *processes*: a man has walked for hours, a house was destroyed by artillery three days ago, an atmospheric front passed in the night. These are causes. The generator, given causes, can reconstruct the surface features *and* all the unstated consequences (the man's damp boots, the house's specific collapse geometry, the wet road).

### 2.2 The verb-tense rule

A practical operational rule follows directly:

- Prefer **past perfect and present perfect continuous** for states: "has been walking," "was shelled," "has stood."
- Prefer **causal clauses** over attributive ones: "the lamp is lit because the plant is running" beats "a lit lamp."
- Avoid **bare present-tense labels** of appearance: "a destroyed house" is a label; "a house destroyed three days ago" is a cause.

### 2.3 The emergence test

After writing a UGS description, apply the **emergence test**: *Could the image be predicted from what I wrote, without me having described the image directly?* If yes, you described a world. If you had to name colors, angles, or "mood" to get the picture, you described a picture. Rewrite.

### 2.4 Examples

| Do not write | Write instead |
|---|---|
| A man stands. | A man has been walking through the forest for several hours. The camera happened to see him just now. |
| A destroyed house. | A house destroyed by artillery three days ago. |
| Rain. | An atmospheric front passed during the night. |
| A sad woman. | A woman who learned an hour ago that the shipment she depended on will not arrive. |
| A futuristic city. | A city whose energy economy collapsed in 2041, after which construction shifted to modular salvage. |

The last example is important: "futuristic city" is a style label. The UGS version specifies the *history* that produced the visible form. The form is then a deduction, not a costume.

---

## 3. Everything Has a Past

Every object in a UGS world carries a biography. Not a backstory invented for charm — a biography required by causality.

### 3.1 The six attributes

- **origin** — where it came from, who made or naturalized it.
- **history** — the sequence of events that brought it to its current state.
- **age** — how long it has existed in this state, measured against its expected lifespan.
- **owner** — who is responsible for it, who uses it, who abandoned it.
- **state** — its current condition, including wear, damage, modification.
- **future** — what will become of it (will it decay, be used, be replaced?).

### 3.2 Why biography is mandatory

An object without a biography is an object without a cause, and an object without a cause is a causality violation (Section 5). The generator will fill the gap with a generic default, and generic defaults are how worlds become *theme parks* — places that look designed rather than lived-in.

### 3.3 Depth of biography scales with prominence

Not every pebble needs a full origin story. The rule is *proportional*: the more visually or narratively prominent an object is, the more complete its biography must be. A background brick may need only "laid in the 1970s, weathered." A foreground vehicle needs origin, owner, last journey, reason for stopping.

### 3.4 Worked biography

Consider a rifle leaning against a wall in frame.

- *Label version:* "an old rifle."
- *UGS version:* "A 7.62mm battle rifle, issued to the district militia in 1998, re-stocked by a local carpenter after the original cracked, last fired two winters ago, leaned here by its owner who stepped outside to smoke and has not returned. The sling is frayed where the bayonet scabbard rubbed it for years."

The second version dictates dozens of visible details the generator can now render correctly: the mismatched stock, the fray point, the dust pattern. None of these were "described as a picture"; they *emerged* from the biography.

---

## 4. The World Exists Outside the Frame

> A frame shows less than 1% of the world. Everything else keeps living.

This is the most important rule in UGS. It is also the most violated, because generators and prompters are both biased toward what is *seen*.

### 4.1 The off-frame implication

For every element visible in frame, ask: *What must be true outside the frame for this element to be here, like this, now?*

- If there is a train — it is going **somewhere**, from **somewhere**, on a schedule set by an operator who is elsewhere.
- If there is a soldier — he has **received an order**, from a chain of command that extends beyond the frame.
- If a hatch is open — **someone** opened it, and that person's absence is itself informative.
- If a lamp is lit — the **power plant is running**, with fuel, staff, and a grid.

### 4.2 The continuity requirement

The off-frame world is not decoration. It is the *cause* of the on-frame content. Cutting the world at the frame edge and pretending the rest is void produces the "studio" look: a subject floating in authored space. UGS demands that the space beyond the frame be *populated with causes*.

### 4.3 Operational technique: the outward question

When stuck, use the **outward question**: pick any on-frame element and ask "what is the rest of its situation?" Then write one sentence answering it. Repeat until the frame feels like a window rather than a stage.

### 4.4 Counter-example

A prompt: "A lone knight on a hill, dramatic sky." The hill is a pedestal; the sky is a backdrop. UGS: "A knight who deserted at the ford three days east, climbing toward the pass before snow closes it, unaware that the column he fled is already disbanded. The wind from the north means the storm reaches him by nightfall." Now the hill, the sky, and the figure are *causally linked*. The dramatic sky is no longer decoration — it is weather with a schedule.

---

## 5. Causality

Nothing exists without a reason. For every object the agent must mentally answer:

- Why did it appear?
- Who made it?
- When?
- Why **here** specifically?
- What will happen in one minute?

### 5.1 Causality as a filter

Causality is the filter that removes decoration. Any element that cannot survive the five questions is a candidate for deletion or for being given a cause. A randomly placed crate, a conveniently placed puddle, a "mysterious light" with no source — all fail.

### 5.2 The five questions in detail

1. **Why did it appear?** Distinguish necessity from accident. Necessary objects belong to the world's function (a control panel in a plant). Accidental objects belong to its history (a dropped glove). Both are legitimate; *unexplained* objects are not.
2. **Who made it?** Even natural objects have agents in their past (a river made the valley; a road crew made the road). Assigning the agent prevents the "appeared from nowhere" failure.
3. **When?** Temporal placement anchors the object in the simulation timeline. "Recently" vs "generations ago" changes its visible state.
4. **Why here?** Location is never arbitrary in a simulated world. A thing is where its因果 chain deposited it.
5. **What in one minute?** Forces the object to have a future. Static props that will "do nothing" are acceptable only if their future is "continue as is" — which is itself an answer.

### 5.3 Causal chains, not causal dots

A single object may satisfy the five questions and still be孤立 if its causal chain does not connect to others. UGS worlds are **networks** of causes. The knight's weather connects to the column's disbanding connects to the ford. Trace connections; do not stop at per-object answers.

### 5.4 Contradiction detection

If two elements imply incompatible pasts, that is a causality contradiction. Example: a "brand-new" object in a ruin dated centuries older, with no explanation of preservation. Either date the object to the ruin's era (and show appropriate wear) or explain the anachronism (a recent dig, a time traveler — but then the rest of the world must accommodate that axiom; see Section 16).

---

## 6. Materials

Every material has behavior, wear, history, and physics. Material is not a texture swatch; it is a *predictive model* of how a substance responds to time, force, and environment.

### 6.1 The four material dimensions

- **behavior** — how the material acts under stress, heat, moisture, load.
- **wear** — the characteristic pattern of degradation (uniform, localized, catastrophic).
- **history** — the use-cycle that produced the current surface.
- **physics** — measurable response: thermal expansion, corrosion rate, acoustic signature, refractive index.

### 6.2 Contrastive examples

- **Wood** ages by checking, graying, rotting at the base, insect colonization. It holds dents and tool marks. It is anisotropic.
- **Concrete** ages by spalling, rebar stain-bleed, efflorescence, crack propagation from stress points. It is massive and slow to change.
- **Plastic** ages by UV chalking, embrittlement, deformation under load, color shift. It does not patinate like metal.
- **Steel** ages by rust front propagation, galvanic attack at joints, fatigue at welds.
- **Copper** ages by oxidation to verdigris, a chemically distinct process from steel rust.

### 6.3 Material mismatch as causality violation

A "new" object in an ancient ruin is a mismatch unless explained. A plastic part in a pre-petroleum setting is a violation. Material anachronism is the fastest tell of a non-simulated world. UGS requires that material, era, and wear form a consistent triangle.

### 6.4 Specifying material correctly

Do not write "metal wall." Write "a corrugated steel wall, galvanized in the 1980s, now rusted through at every fastener, with a vertical streak of orange where a leaking joint ran for a season." The generator now knows: corrugation profile, fastener pattern, rust loci, streak cause. All emergent.

### 6.5 Multi-material assemblies

Real objects are assemblies. Specify the join: welded, bolted, glued, riveted, grown. The join is where failure and wear concentrate, and thus where realism is won or lost.

---

## 7. Light

Light is not painted. It **propagates**. Every source has power, temperature, scattering, reflections, falloff, and atmosphere.

### 7.1 Light as transport, not tone

Prompt language says "warm cinematic lighting." UGS says "a 3000K tungsten source, 60W equivalent, at 1.8m height, scattering through dust-laden air, reflecting off a linoleum floor at 0.3 albedo." The first is a mood word; the second is a physical emission-and-transport description from which the visible tone *emerges*.

### 7.2 The six light attributes

- **power** — luminous flux / radiant intensity. Determines absolute brightness.
- **temperature** — correlated color temperature in kelvin. Determines hue (warm/cool).
- **scattering** — interaction with particulates (dust, fog, smoke, rain).
- **reflections** — specular and diffuse response of surfaces.
- **falloff** — inverse-square or engineered attenuation with distance.
- **atmosphere** — the medium the light travels through, which tints and diffuses it.

### 7.3 Shadows as geometry

Shadows are not added; they are *occlusion of a propagating field*. Specify the source geometry and the occluder, and the shadow is determined. Soft shadows imply an area source or scattering medium; hard shadows imply a point source in clear air.

### 7.4 Time-of-day as a world property

Light is tied to the simulation clock. "Overcast, 15:00, latitude 50°N, late autumn" fully determines the sun's elevation and the sky's character. Do not separate lighting from the world's time and place.

### 7.5 Counter-example

Prompt: "mysterious blue glow." UGS: "a failed neon sign, one tube segment shorted, leaking a 420nm-dominated discharge into the wet alley, illuminating the puddle below at grazing angle." The "glow" is now caused, located, and physically bounded.

---

## 8. Camera

The camera is an **observer**, not a director. It emphasizes nothing. It happened to be here by chance.

### 8.1 The observer stance

In prompt-based work the camera is a god: it chooses the perfect angle, the perfect focus, the perfect moment. In UGS the camera is a **recording device that would exist regardless of the subject**. A surveillance mount, a tourist's phone left on a wall, a helmet cam of someone who happened to walk by. Its presence is explained by the world, not by the desire for a good shot.

### 8.2 Optics — Hyperfocal Focus (default)

By default:

> The whole world is equally worthy of attention.

There is no "main subject." There is a **main idea** (the world's situation). Therefore:

- Default to **hyperfocal** focus: everything from near to far is acceptably sharp.
- **Never** apply, unless the story itself demands it:
  - bokeh
  - portrait blur
  - artificial depth of field
  - selective focus that "directs the eye"

### 8.3 When DOF is allowed

Artificial DOF is permitted *only* when it is part of the world's own logic — e.g., a photograph taken by a person using a 50mm f/1.8 lens for a reason (portraiture within the story), or a macro shot made by a character with a macro rig. The DOF must be *caused by the observer's equipment*, not by the generator's urge to flatter.

### 8.4 Composition

Composition arises by itself. It cannot be "drawn." Beauty is a *consequence of the world's structure*. A pile of salvaged beams composes itself through gravity and storage logic; you do not arrange it for the frame.

### 8.5 Camera as a character (optional)

In some UGS works the camera *is* a character (a person filming). Then the camera has a biography (Section 3): who holds it, why, how steady their hands are, what they are trying to capture. Even then, the camera does not *direct* — it *witnesses with intent*, which is different from directing the world.

---

## 9. Reference Synthesis

If references are given:

> Never copy frames. Extract only the *language*.

### 9.1 The language extraction list

From a reference, extract and recombine:

- language of form (silhouette vocabulary, proportion logic)
- language of material (how surfaces are treated)
- language of light (the reference's characteristic illumination logic)
- language of camera (its optical defaults)
- language of architecture (spatial grammar)
- language of color (palette logic, not swatches)
- language of editing (for video: cut rhythm, transition logic)
- language of animation (for motion: weight, timing)

### 9.2 Why copying fails

Copying a frame imports its *composition* — which was tuned for that reference's specific world, not yours. The result is pastiche: your world wearing someone else's clothes. Extracting the language lets you **build a new world that speaks the same dialect**.

### 9.3 Method

1. Describe the reference in UGS terms (what world produced that frame?).
2. Identify which languages it speaks.
3. Apply those languages to *your* ontology and history.
4. Produce a frame that is unmistakably in the reference's family but could not be mistaken for the reference.

---

## 10. Identity Preservation

If a photograph of a person is given:

1. Preserve the person first.
2. Then change the style.
3. Never the reverse.

### 10.1 The invariant

Only the **visual language** changes. Never the **personality / identity**. The face structure, age markers, distinguishing features, and the *sense of who this is* must survive any stylistic translation.

### 10.2 Order matters

Changing style first and then "fitting the person in" destroys identity, because the style's composition will have already dictated pose, proportion, and expression. Preserve the person as a constraint, then translate the world around them.

### 10.3 Application to non-face identity

Identity extends to any specific entity with a fixed referent: a building, a vehicle, a logo. Preserve the referent's defining structure; translate only the surrounding visual language.

---

## 11. Environmental Storytelling

Every corner of the frame tells a story. Even trash. Even a scratch. Even an open door.

### 11.1 The principle

The environment is not a set dressed for the shot; it is the *residue of lived time*. A scratch is where something was dragged. An open door is where someone passed and did not return. Trash is where someone ate, repaired, or abandoned.

### 11.2 Density without clutter

Environmental storytelling is not maximalism. It is *legibility*: each detail, however small, is readable as the outcome of an event. A clean minimal room can tell a story (recent departure, careful inhabitation) as strongly as a cluttered one.

### 11.3 The detail question

For any detail, ask: "What event does this record?" If the honest answer is "none, it's just there for texture," reconsider. Texture must itself be caused (weather, use, manufacture).

---

## 12. Temporal Continuity

Video is **not a sequence of frames**. It is a continuous physical process.

### 12.1 The physical basis

Every motion has:

- **acceleration** — change of velocity, not instant velocity.
- **inertia** — tendency to continue; mass resists change.
- **mass** — determines how forces translate to motion.
- **a beginning moment** — when the force started.
- **an ending moment** — when it ceased or will cease.

### 12.2 Consequences for video

- No teleporting between cuts; position is continuous unless the cut is a new observation (and then the new observer's position is explained).
- No impossible acceleration (a heavy object snapping to speed with no wind-up).
- Recoil, follow-through, settle: motions have tails.

### 12.3 Simulation clock

Video is sampled from the simulation clock. Frame *t+1* is determined by frame *t* plus the world's laws. This is what makes video feel continuous rather than edited.

---

## 13. Animation

Characters never *act*. They **live**. All movement must have a purpose. No "beautiful gestures" caused by nothing.

### 13.1 Purpose-driven motion

Every movement answers: *what is the character trying to accomplish?* Walking to a door, reaching for a tool, steadying against a lurch. Motion without a goal is the hallmark of "acting for the camera."

### 13.2 Weight and intention

A movement's quality (hesitant, decisive, exhausted) is a function of the character's state (fear, urgency, fatigue), which itself comes from their biography and current situation. The generator should derive the *quality* from the *state*, not be told "make it look tired."

### 13.3 Micro-behavior

Real life is full of non-goal micro-behaviors: fidgeting, glances, weight shifts. These are permitted *only* when caused (nervousness, waiting, cold). Random micro-behavior is decoration.

---

## 14. Audio (for video)

Sound is part of physics, not an ornament.

- If an engine exists — it makes noise, with a spectrum set by its type and load.
- If wind is strong — it shapes the sound field (turbulence, whipping, attenuation of distant sources).
- If a room is large — there is reverberation, with decay set by geometry and materials.

### 14.1 Audio as a physical field

Treat audio like light: a propagating field with sources, media, and reflections. Specify the source's physics and the space's acoustics; the soundtrack emerges.

### 14.2 Diegetic vs non-diegetic

UGS audio is **diegetic** by default — occurring within the world. Non-diegetic music (scored over the top) is a directorial choice and contradicts the observer stance unless the observer is explicitly a filmmaker within the story.

---

## 15. Negative Constraints

Never produce:

- random surrealism
- decorative details
- beautiful poses
- random effects
- meaningless chaos
- visual noise

### 15.1 The common root

All six failures share one root: **decoration without cause**. They are added to please the eye, not to record the world. UGS forbids adding anything that fails the causality and emergence tests.

### 15.2 Enforcement as subtraction

Negative constraints are easier to apply as subtraction than as rules. After drafting, scan for elements that exist only to look good. Delete or cause them.

---

## 16. Memes

Absurdity is born not from randomness, but from **one single altered axiom of the world**. After that, the entire world develops logically around it.

### 16.1 The mechanism

A meme (in the UGS sense — a comedic or absurd world-concept) is a *controlled causality break*. You change exactly one axiom: "gravity points outward from surfaces," "everyone believes Tuesday does not exist," "water is socially anxious." Then you run the *normal* causal engine on the modified axiom. The humor comes from consistency, not from chaos.

### 16.2 The one-axiom rule

Changing more than one axiom produces noise (Section 15). The discipline is: alter one thing, then let everything else be *maximally normal* relative to it. A world where gravity is inward AND time runs backward AND people are fish is surreal sludge. A world where only "objects are loyal to their owner and follow them" is a sharp, legible joke.

### 16.3 Worked meme

Axiom change: *electrical devices are afraid of the dark and huddle together.* Everything else normal. Result: lamps clustered, appliances migrated to the brightest room, a toaster found in the fridge because the fridge light was on. The world is absurd yet fully因果-consistent. That is the UGS meme.

---

## 17. Horror

Monsters may not exist at all. Fear must arise from **understanding the world**.

### 17.1 Horror from causality

The scary thing in UGS is not a monster; it is a *realization*. A room whose layout implies someone has been living in the walls. A schedule of disappearances that matches the tide table. The dread is produced by the viewer inferring the world's hidden rules.

### 17.2 If monsters exist

They must obey the same causality as everything else: origin, biology, motive, limitation. A monster that violates physics for shock value is a decoration (15), not horror.

### 17.3 The forbidden-knowledge structure

Horror in UGS often takes the form: the world is normal, but one inferred fact makes it terrible. The generator's job is to render the *normal* world so completely that the inference is unavoidable.

---

## 18. Games

Do not draw a screenshot. **Simulate an existing game engine.** Define:

- renderer (deferred/forward, API era)
- GPU limits (VRAM, fillrate, shader model)
- materials (how the engine represents them)
- LOD (level-of-detail rules)
- shadows (shadow map size, cascade count)
- lighting (baked vs dynamic)
- textures (resolution, compression)
- hardware era (what silicon this ran on)

### 18.1 Why simulate the engine

A "game screenshot" drawn as a picture looks like a render *trying to be a painting*. A frame produced by simulating the engine's actual constraints (pop-in at LOD distance, compression artifacts, fixed shadow resolution) looks like it *was* captured from a running build.

### 18.2 The engine as a world rule

The engine's limitations are world rules (Section 20). They dictate what can and cannot be represented, and thus shape the visible frame causally.

---

## 19. Video (general)

Video must feel like a **continuous simulation**, not a sequence of beautiful frames.

### 19.1 The sequence trap

Prompt-based video generation optimizes each frame for beauty, producing a slideshow of gorgeous but disconnected moments. UGS video samples one continuous simulation; beauty, if present, is incidental to the world's structure.

### 19.2 Observer continuity

If the observer moves, the motion is caused (walking, panning from a tripod, a vehicle). The camera's trajectory is part of the simulation, not a directorial whip-pan.

---

## 20. The Master Formula of UGS

The most important rule reduces to one chain:

```
Ontology
   ↓
World Rules
   ↓
History
   ↓
Simulation
   ↓
Physics
   ↓
Environment
   ↓
Characters
   ↓
Camera
   ↓
Observation
   ↓
Image / Video
```

### 20.1 Reading the chain

Each level is a prerequisite for the next. You cannot specify History before Ontology, because history is about the kinds of things that exist. You cannot specify Physics before World Rules, because physics *is* a world rule. The chain is a compile order: upstream levels must be resolved before downstream levels are even meaningful.

### 20.2 The chain as a validation tool

Given a finished request, walk the chain bottom-up. At each arrow, ask: *does the lower level fully determine the conditions the upper level assumed?* If Observation assumes a camera that History never placed, that is a break. The chain localizes errors.

### 20.3 Why this distinguishes UGS

Picture-centric prompting is a flat list: "cinematic, 35mm, shallow DOF, teal-orange, dramatic." UGS is a *dependency graph* with a mandated topological order. The structure, not the vocabulary, is the innovation.

---

## 21. Operational Authoring Checklist

Before emitting a generation request in UGS style, confirm each level. If any is missing or contradicts an earlier one, return to that level.

1. **Ontology** — what kinds of things exist in this world? (entities, categories, what is possible)
2. **World Rules** — what are the invariant laws (physics, society, tech, magic if any)?
3. **History** — what happened before the frame? (origin, age, owner of key objects)
4. **Simulation** — what state is the world in *right now*, off-screen included?
5. **Physics** — light, material, mass, inertia modeled as real, propagating fields?
6. **Environment** — does the off-frame world have a cause for the on-frame content?
7. **Characters** — do they have purposes and biographies, not poses?
8. **Camera** — observer by chance, hyperfocal, no artificial DOF unless caused?
9. **Observation** — is the frame a *witnessed* slice, not a composed one?
10. **Image/Video** — does the output *emerge* rather than *decorate*?

### 21.1 The regression rule

Never patch at the rendering stage. If the image is wrong, the error is almost never in rendering — it is upstream, in a world assumption. Fix the world; re-render.

### 21.2 Minimum viable specification

For a quick generation you may compress, but you may not *skip*. A minimal UGS request still names: ontology, one world rule, a piece of history, and the observer. The compression is in depth, not in omitted levels.

---

## 22. Worked Examples and Counter-Examples

### 22.1 Example A — the soldier

**Bad (picture-centric):** "Cinematic shot of a tired soldier standing in a ruined city, dramatic lighting, shallow depth of field."

**UGS (world-centric):**

> *Ontology:* A mid-20th-century continental war. Humans, machinery, municipalities.
> *World Rules:* Artillery outranges infantry movement; supply lines determine where units halt.
> *History:* The district was shelled on the third of the month; the building behind the figure lost its eastern wall then.
> *Simulation:* A conscript's platoon received a hold order at dawn. He has been stationary near the intersection for four hours awaiting relief.
> *Physics:* Overcast diffuse light, no sun; concrete dust settled on wool; a brass casing oxidized where it landed.
> *Environment:* A supply truck is overdue from the west — its absence is why he is still here.
> *Characters:* He is not posing. He is waiting, weight on one leg, ration cold.
> *Camera:* A fixed surveillance mount on the intact water tower, recording regardless of interest.
> *Observation:* The frame is one of 14,400 recorded that day. Nothing was staged.

The image that emerges is automatically coherent. The "beauty" is a side effect of structure.

### 22.2 Example B — the meme

**Bad:** "A weird funny world where everything is random and silly."

**UGS:**

> *Axiom change:* Objects are loyal to their owners and follow them when called.
> *Everything else normal.* A chair trails its owner to the kitchen. A forgotten umbrella waits by the door it was last used at. A library book, returned late, sulks on the shelf.

The humor is in the consistency, not the chaos.

### 22.3 Example C — the game frame

**Bad:** "A screenshot from a fantasy RPG, epic."

**UGS:**

> *Engine:* Forward renderer, shader model 3.0, 256MB VRAM, 2006-era GPU.
> *LOD:* Distant ruins use the 1/8 mesh; pop-in begins at 80m.
> *Shadows:* 1024px single cascade, baked for static geometry.
> *Lighting:* One dynamic directional sun, ambient occlusion baked.
> *Result:* A frame where the hero's sword has the engine's characteristic 512px normal map and the far cliff shows LOD simplification at the horizon.

---

## 23. Failure-Mode Taxonomy

A reference list of how UGS requests go wrong, for use during review.

| # | Failure | Root cause | Detection |
|---|---|---|---|
| F1 | Floating subject | Off-frame world undefined | Outward question (4.3) fails |
| F2 | Anachronism | Material/era triangle broken | Material check (6.3) |
| F3 | Inconsistent light | Light not modeled as field | Six attributes (7.2) incomplete |
| F4 | Director camera | Observer stance violated | Camera has no biography (8.1) |
| F5 | Artificial DOF | DOF not caused | 8.3 violated |
| F6 | Pastiche | Reference copied, not extracted | 9.2 |
| F7 | Identity loss | Style changed before person | 10.2 |
| F8 | Dead detail | Detail has no event | 11.3 |
| F9 | Teleport cut | Temporal continuity broken | 12.2 |
| F10 | Acting | Motion without purpose | 13.1 |
| F11 | Scored audio | Non-diegetic added | 14.2 |
| F12 | Decoration | Negative constraint hit | 15.1 |
| F13 | Noise meme | >1 axiom changed | 16.2 |
| F14 | Monster shock | Physics violated for scare | 17.2 |
| F15 | Painterly game | Engine not simulated | 18.1 |
| F16 | Slideshow video | Not continuous sim | 19.1 |
| F17 | Skipped level | Chain broken | 20.2 / 21 |

---

## 24. Machine-Readable Use

This specification is designed to be **operated upon by agents**, not just read.

### 24.1 As an enforcement contract

A prompt-authoring agent should treat Sections 1, 2, 5, 15, 20, 21, and 23 as **hard constraints** and the remaining sections as **guidance**. On producing a draft, the agent runs the checklist (21) and the failure taxonomy (23) and refuses to emit a request that fails a hard constraint.

### 24.2 As a structured template

The chain (20) can be emitted as a structured record:

```
ontology: ...
world_rules: [...]
history: [...]
simulation: ...
physics: ...
environment: ...
characters: [...]
camera: ...
observation: ...
```

A skill (see the companion `skill/` directory) can fill this template field by field, guaranteeing level coverage.

### 24.3 Bilingual note

The Russian edition is not a paraphrase; it is the same specification. Agents operating in Russian should cite `spec/ru/UGS-v2.md`; English agents cite this file. The chain and checklist are language-independent.

---

---

## 25. Extended Field Guide — Per-Domain Playbooks

The master chain (Section 20) is domain-agnostic. This section gives concrete playbooks that instantiate it for recurring generation targets. Each playbook names the level that usually breaks for that domain and the specific discipline that fixes it.

### 25.1 Photography (documentary / reportage)

- **Typical break:** director camera (F4). The prompter reaches for "rule of thirds," "leading lines."
- **Fix:** Specify the photographer as a character (8.5) with a biography: assignment, deadline, exhausted hands, one roll left. The frame is their witness, not their composition.
- **Discipline:** replace every compositional instruction with a causal one. "Leading lines" → "the fence row was planted to mark the property line in 1962; the path follows it."

### 25.2 Product / object render

- **Typical break:** object without biography (F2) and material mismatch (F2/F3).
- **Fix:** give the product an origin (manufacture date, factory, batch), a use history (who owned it, how it was handled), and a material spec exact enough to predict wear.
- **Discipline:** the scuff is not "added detail"; it is the record of a specific contact event. Name the event.

### 25.3 Architecture / interior

- **Typical break:** environment as set (F8), no off-frame cause (F1).
- **Fix:** the room was built for a purpose by someone, modified by later occupants, and is currently in a state caused by who left last. The door is open because a specific person passed.
- **Discipline:** for each opening (door, window, hatch) answer "who moved it and why," else close it.

### 25.4 Portrait

- **Typical break:** identity loss on style change (F7), posing (F10).
- **Fix:** preserve the referent (10); give the subject a current situation that explains expression and posture (they are not posing — they are mid-activity). The camera is a chance encounter.
- **Discipline:** expression must be caused by inner state, not chosen for attractiveness.

### 25.5 Landscape / nature

- **Typical break:** pretty-postcard lighting (F3), no process.
- **Fix:** specify the geological and meteorological history. The valley was carved by the river; the mist is the overnight front (Section 2.4). Light is a function of the simulation clock (7.4).
- **Discipline:** a landscape is the *current frame of a slow simulation*. Describe the slow simulation.

### 25.6 Urban scene

- **Typical break:** floating subject (F1), decoration (F12).
- **Fix:** every building has a developer, an era, a current use; the street has a traffic regime; the lone figure has a destination. The city is a network of causes (5.3).
- **Discipline:** apply the outward question (4.3) to at least three on-frame elements.

### 25.7 Historical reconstruction

- **Typical break:** anachronism (F2), material mismatch (F2).
- **Fix:** lock the era; specify each object's manufacture date and wear consistent with elapsed time. Cross-check the material/era triangle (6.3).
- **Discipline:** build a dated inventory; reject any object whose date falls outside the window unless explained.

### 25.8 Sci-fi / future

- **Typical break:** style label "futuristic" (Section 2.4), inconsistent tech.
- **Fix:** derive the visible form from a specified history (e.g., energy collapse → salvage modularity, Example 22). Tech must have a development lineage and physical limits.
- **Discipline:** every device answers "what problem did it solve, and with what physics?"

### 25.9 Fantasy

- **Typical break:** magic without rules (world-rule gap).
- **Fix:** magic is a world rule (20). Specify its source, cost, limits, and social effect. A glowing sword obeys the six light attributes (7.2) plus a mana budget.
- **Discipline:** treat the supernatural as physics with different constants, not as exemption.

### 25.10 Underwater / extreme environment

- **Typical break:** light not modeled as medium (F3).
- **Fix:** water is an attenuating, scattering, wavelength-selective medium. Specify depth, turbidity, surface light. Color falls off by wavelength (red first).
- **Discipline:** the medium is a world rule; the look is its consequence.

### 25.11 Macro / microscopic

- **Typical break:** scale unspecified, physics wrong.
- **Fix:** at small scale, surface tension, capillary action, and diffraction dominate. Specify the scale; the visible physics change accordingly.
- **Discipline:** do not carry macro physics into a human-scale frame or vice versa.

### 25.12 Still life

- **Typical break:** arranged-for-beauty (F12).
- **Fix:** the objects co-occur because of a real activity (a repair mid-task, a meal half-eaten). The arrangement is the residue of that activity (11).
- **Discipline:** ask "what was the person doing when they left?" and render that.

---

## 26. Template Library

Fill these templates field by field. Empty fields are failures (Section 21).

### 26.1 Minimal (quick) template

```yaml
ontology: <kinds of things>
world_rules: <1 invariant law>
history: <1 past event causally linked to frame>
camera: <observer, by chance, hyperfocal>
observation: <witnessed slice, not composed>
```

### 26.2 Standard template

```yaml
ontology:
world_rules:
history:
  - origin
  - age
  - owner
simulation: <current state, off-frame included>
physics:
  light: <power, temp, scattering, reflections, falloff, atmosphere>
  material: <behavior, wear, history, physics>
environment: <off-frame causes>
characters:
  - purpose
  - biography
camera:
  - observer stance
  - hyperfocal (default)
observation: <witnessed, not composed>
```

### 26.3 Video template (adds temporality)

```yaml
# inherits standard template, then:
temporal:
  acceleration:
  inertia:
  mass:
  begin_moment:
  end_moment:
continuity: <position continuous across cuts unless new observer explained>
audio:
  sources: <physical, diegetic>
  acoustics: <space, reverb, medium>
```

### 26.4 Meme template

```yaml
axiom_change: <exactly ONE altered axiom>
everything_else: normal
result: <world develops logically around the axiom>
```

### 26.5 Game-frame template

```yaml
engine:
  renderer:
  gpu_limits:
  materials:
  lod:
  shadows:
  lighting:
  textures:
  hardware_era:
result: <frame shows engine's characteristic artifacts>
```

### 26.6 Horror template

```yaml
world: <normal>
hidden_rule: <one inferred fact that makes it terrible>
render: <normal world so completely the inference is unavoidable>
```

### 26.7 Reference-synthesis template

```yaml
reference_world: <what world produced the reference frame>
languages_extracted:
  - form
  - material
  - light
  - camera
  - architecture
  - color
  - editing (if video)
  - animation (if motion)
apply_to: <your ontology + history>
output: <new world in the family, not a copy>
```

### 26.8 Identity-preservation template

```yaml
referent: <person/entity to preserve — invariant>
visual_language: <what may change>
order: preserve first, then translate
```

### 26.9 Environmental-storytelling template

```yaml
for each detail:
  event_recorded: <what happened to leave this mark>
  if none: remove or cause it
```

### 26.10 Checklist-as-template

Use Section 21 verbatim as a gate: emit only if all ten levels pass.

---

## 27. Failure Autopsies

Eight real-world-shaped failure cases, diagnosed with the taxonomy (23).

### 27.1 "The floating knight"

*Symptom:* dramatic lone figure on a hill, sky as backdrop.
*Diagnosis:* F1 (floating subject) + F4 (director camera).
*Root:* off-frame world undefined; camera is god.
*Fix:* give the knight a desertion history, a destination, a weather schedule; make the camera a chance witness (4.4).

### 27.2 "The brand-new ruin"

*Symptom:* ancient ruin with a pristine object in frame.
*Diagnosis:* F2 (anachronism) + material/era triangle broken (6.3).
*Root:* object dated outside window, unexplained.
*Fix:* date the object to the era with appropriate wear, or explain a recent intrusion (a dig, a looter).

### 27.3 "The noon-night"

*Symptom:* shadows say noon, sky says dusk.
*Diagnosis:* F3 (inconsistent light).
*Root:* light not modeled as a field with one source and one clock (7.4).
*Fix:* lock time-of-day and a single dominant source; derive shadows from it.

### 27.4 "The bokeh portrait"

*Symptom:* subject razor-sharp, everything else melted.
*Diagnosis:* F5 (artificial DOF) unless caused (8.3).
*Root:* DOF added to flatter, not caused by observer equipment.
*Fix:* either remove DOF (default hyperfocal) or specify the observer's fast lens and reason.

### 27.5 "The pastiche"

*Symptom:* frame that looks like the reference but is hollow.
*Diagnosis:* F6 (pastiche) — reference copied, not extracted (9.2).
*Root:* imported the reference's composition.
*Fix:* re-extract languages (9.1) and build a new world (9.3).

### 27.6 "The swapped face"

*Symptom:* stylized version where the person is unrecognizable.
*Diagnosis:* F7 (identity loss) — style changed before person (10.2).
*Root:* composition dictated by style.
*Fix:* preserve referent as invariant; translate only surrounding language (10.3).

### 27.7 "The teleport cut"

*Symptom:* video where the subject jumps between shots.
*Diagnosis:* F9 (teleport cut) — temporal continuity broken (12.2).
*Root:* frames optimized independently.
*Fix:* sample one continuous simulation; explain any new observer (12.3).

### 27.8 "The random funny"

*Symptom:* "weird silly world," reads as noise.
*Diagnosis:* F13 (noise meme) — more than one axiom changed (16.2).
*Root:* chaos mistaken for absurdity.
*Fix:* change exactly one axiom; keep everything else maximal-normal (16.3).

---

## 28. Glossary

- **Ontology** — the catalog of what kinds of things exist in the world.
- **World Rule** — an invariant law (physical, social, magical) the simulation obeys.
- **Simulation** — the world evolving through time under its rules.
- **Observation** — a bounded slice captured by a chance observer.
- **Rendering** — mechanical translation of observation to pixels/frames.
- **Hyperfocal** — focus setting keeping near-to-far acceptably sharp; UGS default.
- **Diegetic** — occurring within the world (sound, light source).
- **Biography** (of an object) — its origin, history, age, owner, state, future.
- **Emergence test** — can the image be predicted without describing it directly?
- **Outward question** — what must be true off-frame for this element to be here?
- **Axiom change** — the single altered rule that defines a UGS meme.
- **Observer stance** — camera as chance witness, not director.
- **Material triangle** — material, era, and wear must form a consistent set.
- **Causal chain** — the network of causes linking elements, not isolated causes.

---

## 29. Frequently Asked Questions

**Q1. Is UGS only for realistic subjects?**
No. Fantasy, sci-fi, and horror are covered; the supernatural is treated as physics with different constants (25.9, 17).

**Q2. Can I still ask for a beautiful image?**
Beauty is permitted as a *byproduct* of structure. You may not pursue it as the goal (Section 2).

**Q3. Do I need all ten checklist levels for a quick gen?**
You may compress depth but never skip a level (21.2). Minimal template in 26.1.

**Q4. What if the model ignores my world spec?**
Then the model is non-compliant. Re-state the world; the image is downstream. Do not patch at rendering (21.1).

**Q5. How long should the biography be?**
Proportional to prominence (3.3). Background objects need a line; foreground needs a paragraph.

**Q6. Is hyperfocal always required?**
Default yes; DOF allowed only when caused by the observer's equipment (8.3).

**Q7. How do I handle multiple characters?**
Each gets a purpose and biography; their causal chains interconnect (5.3).

**Q8. Can the camera move?**
Yes, if the motion is caused (walking, vehicle, tripod pan) — not a directorial whip-pan (19.2).

**Q9. What about stylization (anime, painterly)?**
Translate only the visual language; preserve ontology, history, causality (10).

**Q10. How is UGS different from "show, don't tell"?**
"Show don't tell" is about narrative prose. UGS is about *causal priority*: the world is specified, the image is witnessed (0.1).

**Q11. Does UGS apply to text-to-3D?**
Yes — the same chain produces a consistent 3D scene; rendering is just a different final stage.

**Q12. Can I use references?**
Yes, by extracting language, never copying frames (9).

**Q13. What makes a good meme?**
Exactly one altered axiom, maximal normality elsewhere (16).

**Q14. Why forbid random surrealism?**
It is decoration without cause (15); the opposite of UGS.

**Q15. How do I verify a generated image against the spec?**
Run the checklist (21) and taxonomy (23) on the request, then inspect the output for the predicted consequences.

**Q16. Is the priority order a hard rule?**
Yes (1.3). Skipping levels is the top cause of artificial output.

**Q17. Can audio be non-diegetic?**
Only if the observer is explicitly a filmmaker within the story (14.2).

**Q18. How detailed must physics be?**
Enough that light, mass, and wear are *determined*, not chosen (7, 6, 12).

**Q19. Does the Russian edition differ?**
No — same specification, different language (24.3).

**Q20. Where do I start as a beginner?**
Use the minimal template (26.1); expand level by level as needed.

---

## 30. Quick-Reference Card

```
UGS in ten lines
1. Worlds, not pictures.
2. Reality -> Simulation -> Observation -> Rendering.
3. Describe causes; let images emerge.
4. Every object has a biography.
5. The world lives outside the frame.
6. Nothing without a cause.
7. Materials age by physical law.
8. Light propagates; camera observes by chance.
9. Hyperfocal default; no uncaused DOF.
10. Run the checklist; fix the world, not the render.
```

---

---

## 31. Part III — Worked Specifications (Exemplars)

These are complete, ready-to-use UGS specifications. Each is written to pass the checklist (21) and the failure taxonomy (23). Use them as templates you adapt, not as fixed prompts.

### 31.1 Abandoned railway station, dawn, winter

```
ontology:
  - a regional railway terminus, closed 1994
  - humans: a single signalman who stayed on as caretaker
  - machinery: mechanical interlocking, oil-heated office
world_rules:
  - once a train stops running, maintenance decays by weather, not by use
  - the caretaker keeps only the office warm; the rest is at ambient
history:
  - origin: station opened 1928, standard-gauge branch line
  - age: 66 years of service, 30 years of abandonment
  - owner: transferred to the municipality in 1994, unstaffed since
simulation:
  - current state: pre-dawn, -9C, the caretaker lighting the office stove
  - off-frame: the branch line is buried in snow 400m east; a snowplow
    is overdue from the junction
physics:
  light: pre-dawn diffuse, 4500K sky, no direct sun for 90 min; the
    office window glows at 2200K leaking onto the platform
  material: oak bench split along grain from freeze-thaw; cast-iron
    pillars oxidized at the base where meltwater pooled each spring
environment:
  - the open door to the office explains the only warm pool of light
  - a forgotten lantern on the bench records the last night shift
characters:
  - caretaker: purpose = stay until the plow confirms the line is cut;
    biography = hired 1988, chose to remain
camera:
  - observer stance: a fixed CCTV housing on the canopy, ice-fogged lens
  - hyperfocal, no artificial DOF
observation:
  - one of 8,640 frames recorded that night; the caretaker is unaware
```

### 31.2 Street market, overheating city, late afternoon

```
ontology:
  - a mediterranean market square, 11:00 on a 39C July day
  - vendors, shoppers, a malfunctioning fountain
world_rules:
  - at this heat, shade is the only traded commodity; commerce clusters
    under awnings and the one working tree
  - the municipal water main lost pressure at 10:40; the fountain died
history:
  - origin: square paved 1952 over a roman fill; the tree planted 1971
  - age: the awning canvas replaced every 3 years, sun-rotted early
simulation:
  - current state: trade slowed, people drift to the tree, a child
    cups hands under the dead fountain
  - off-frame: a water truck is rerouted from the west depot, 12 min out
physics:
  light: 5800K harsh sun at 58deg elevation, hard shadows, heat shimmer
    lifting off the stone (a scattering medium of hot air)
  material: canvas bleached and brittle; stone hot to touch, no dew
environment:
  - the dead fountain is the cause of the crowd shift toward the tree
  - dropped produce records the moment trade paused
characters:
  - vendor: purpose = sell before the truck restores water and trade
    resumes; biography = fourth generation on this pitch
camera:
  - observer stance: a tourist's phone left on a crate, recording
  - hyperfocal
observation:
  - witnessed slice; the heat is a physical fact, not a mood
```

### 31.3 Deep-sea vent, no human present

```
ontology:
  - a hydrothermal vent field at 2400m, mid-ocean ridge
  - tube worms, squat lobsters, particulate plumes
world_rules:
  - no sunlight; all light is bioluminescent or from the vent's own glow
  - pressure is 240 atm; buoyancy and slow motion dominate
history:
  - origin: the vent ignited 14 years ago after a tectonic shift
  - age: the mineral spire grows ~3cm/year
simulation:
  - current state: a slurry of sulfide particles rising; a worm colony
    pulsing in response to a passing current
  - off-frame: a whale fall lies 200m north, drawing the lobsters away
physics:
  light: zero solar; 470nm bioluminescence from bacterial symbiotes;
    the vent mouth glows dull red (black-body ~600K rock)
  material: chitin tubes brittle under pressure cycles; sulfide crust
    ac cretion layers record annual vent output
environment:
  - the absent lobsters are explained by the northern whale fall
  - the rising plume explains the particulate backscatter on any light
camera:
  - observer stance: an ROV's floodlight, aimed by a pilot on a ship
  - note: the ROV light is the only non-biological source; its cone
    defines the visible volume
observation:
  - a lit volume in darkness; everything outside the cone is inferred
```

### 31.4 Suburban kitchen, ordinary morning

```
ontology:
  - a 1990s suburb kitchen, occupied family of four
  - appliances, a half-packed lunch, a cat
world_rules:
  - a working family compresses activity into a 25-min window before
    school; surfaces record the rush
history:
  - origin: house built 1994, laminate counters, oak cabinets
  - age: the toaster bought 2009, the magnet collection since 2015
simulation:
  - current state: 07:41, the parent at the counter, the cat on the
    stool watching the lunch being packed
  - off-frame: the school bus is 4 min out; the dog is in the yard
physics:
  light: 5200K north window, overcast; the fridge lamp 2700K spills
    when opened
  material: laminate scratched near the stool where the cat claws;
    the cabinet paint touched up once, mismatched sheen
environment:
  - the open fridge explains the cold draft and the spill of light
  - a toppled cereal box records the rushed grab
characters:
  - parent: purpose = get the child fed and out; biography = same
    routine 6 years running
  - cat: purpose = wait for dropped crumbs; not posing
camera:
  - observer stance: a nest cam above the door, always recording
  - hyperfocal
observation:
  - mundane, legible, fully caused
```

### 31.5 Battlefield triage, night, rain

```
ontology:
  - a forward aid post in a 20th-c war, 02:10, heavy rain
  - medics, wounded, a tent, a generator
world_rules:
  - triage sorts by survivability; the post is where the line holds
history:
  - origin: the post established at dusk when the advance stalled
  - age: the generator borrowed from a supply column, low on fuel
simulation:
  - current state: a medic suturing by lantern; the generator falters
  - off-frame: the next wave is 20 min out; the lamp oil is nearly gone
physics:
  light: 1900K lantern, rain-scattered, low power; puddles reflect it
  material: wool saturated, medic's apron stiff with dried blood;
    the tent canvas sagging under water weight
environment:
  - the faltering generator explains the dimming lantern and the
    medic's haste
  - boot prints in the mud record the last evacuation
characters:
  - medic: purpose = stabilize the wounded before the wave; biography =
    trained 3 years, first posting
camera:
  - observer stance: a wounded soldier's discarded camera on a crate
  - hyperfocal, rain on the lens
observation:
  - witnessed; the horror is in the world's logic, not a monster
```

### 31.6 Orbital station, failure, silence

```
ontology:
  - a crewed station in low orbit, 40 min into a power fault
  - two crew, failing modules, a docked capsule
world_rules:
  - without solar tracking, batteries drain; systems shed in sequence
history:
  - origin: station assembled over 6 launches, 2019-2023
  - age: the gyro that failed was flagged 8 months ago, deferred
simulation:
  - current state: emergency lights only; one crew sealing a hatch,
    the other at the faulty panel
  - off-frame: the supply capsule awaits docking; ground is 9 min away
physics:
  light: 3000K emergency strips, no window sun (station in earth shadow)
  material: aluminum scuffed at handholds from years of ingress; the
    hatch seal cracked at one corner, the cause of the fault
environment:
  - the cracked seal explains the fault and the crew's location
  - a drifting clip records the moment power shed
characters:
  - crew A: purpose = isolate the leak; biography = commander, 2 flights
  - crew B: purpose = diagnose the bus; not posing, moving with urgency
camera:
  - observer stance: an internal cabin cam, one of many, looping
  - hyperfocal
observation:
  - cold, causal, the silence is a system state
```

### 31.7 Child's bedroom, decades later

```
ontology:
  - a child's room abandoned in 1987, undisturbed since
  - toys, wallpaper, a bed, dust
world_rules:
  - an unheated room preserves paper and fabric by stasis, not by care
history:
  - origin: room decorated 1979 for a daughter born that year
  - age: 37 years sealed; the family moved, the house sold, left as is
simulation:
  - current state: a 2010s estate-sale viewer opening the door; dust
    disturbed for the first time in decades
  - off-frame: the daughter is now 45, lives abroad, does not know
physics:
  light: 5500K daylight from the once-curtained window, now bare;
    motes lit in the beam
  material: wallpaper yellowed uniformly; the teddy bear's fur matted
    where it lay; the bedsprings rusted at the feet
environment:
  - the opened door explains the disturbed dust and the single shaft
  - a toppled block tower records a game interrupted in 1987
characters:
  - viewer: purpose = assess the estate; not the child, not posing
camera:
  - observer stance: the viewer's phone, held at chest height
  - hyperfocal
observation:
  - the story is entirely in the residue of one interrupted moment
```

### 31.8 Factory floor, shift change

```
ontology:
  - a metalworks, 06:00, the day shift arriving as night leaves
  - machines, a foreman, lockers, a time-clock
world_rules:
  - a foundry never fully cools; the night's heat is the day's starting
    state; the clock governs everything
history:
  - origin: plant opened 1961, expanded 1985
  - age: the time-clock installed 1990, the locker bank repainted 2003
simulation:
  - current state: the night foreman handing over, the first day worker
    already at the panel; the pour scheduled 06:20
  - off-frame: the ladle is preheating; the crane is being tested
physics:
  light: 4000K sodium bay lamps, one flickering; the furnace mouth
    glows 1100K through its viewport
  material: concrete floor stained with decades of oil; the clock
    housing scratched by thousands of badge swipes
environment:
  - the preheating ladle explains the furnace glow and the crew's pace
  - a dropped glove records the handover moment
characters:
  - night foreman: purpose = report the night's faults; biography =
    twenty years on this floor
  - day worker: purpose = take the pour; moving with learned economy
camera:
  - observer stance: a safety cam at the time-clock, always on
  - hyperfocal
observation:
  - the rhythm of the plant is the subject, not a hero
```

### 31.9 Forest fire edge, dusk

```
ontology:
  - a boreal forest at the active edge of a wildfire, 19:30
  - a fire crew, a truck, burning canopy, rising embers
world_rules:
  - fire moves by fuel and wind; the crew works the flanking edge, not
    the front; the wind shifted at 18:00
history:
  - origin: the fire started by a downed line 3 days ago, 12km south
  - age: this stand is 90-year spruce, dense, dry from the heat dome
simulation:
  - current state: the crew wetting the flank; a spot fire jumped the
    line 40m east; the wind pushes embers toward the truck
  - off-frame: the incident command is 1km back; air support is grounded
physics:
  light: the fire is the source, 1500-2000K, chaotic; smoke scatters
    it into an orange dome; the unburnt side is in blue dusk
  material: spruce needles flash to ash; the truck's paint blistered
    on the fire-facing side
environment:
  - the shifted wind explains the spot fire and the ember vector
  - a melted traffic cone records the heat line
characters:
  - crew lead: purpose = hold the flank until dark; biography = seasonal,
    third fire this week
camera:
  - observer stance: a helmet cam of the lead, ash on the lens
  - hyperfocal, the fire is the only light budget
observation:
  - the frame is a slice of a process larger than the frame
```

### 31.10 Underwater cave, diver, dark

```
ontology:
  - a flooded limestone cave, 30m in, a solo technical diver
  - dive gear, a line, silt, a chamber
world_rules:
  - a cave diver never leaves the line; silt clouds on disturbance and
    can blind for minutes; gas is finite
history:
  - origin: the cave mapped in 2004; the line laid then, replaced 2018
  - age: the diver's tanks filled that morning; the line is 6 years old
simulation:
  - current state: the diver at a restriction, repositioning a reel;
    a fin kick has just stirred silt behind
  - off-frame: the exit is 30m back; the stage bottle is at the jump
physics:
  light: the diver's primary 6500K LED, narrow cone; beyond it, zero;
    the cone reveals suspended silt as a glowing fog
  material: limestone scoured smooth by flow; the line sheath abraded
    at the restriction where it snags
environment:
  - the stirred silt explains the narrowing visibility and the diver's
    stillness
  - a dropped clip records the moment of the kick
characters:
  - diver: purpose = pass the restriction and return; biography =
    trained 5 years, first solo in this cave
camera:
  - observer stance: the diver's chin-mounted light+cam, part of the
    rig, not a director
  - hyperfocal within the lit cone
observation:
  - the visible world is exactly the lit volume; the rest is inference
```

### 31.11 Meme — loyal objects

```
axiom_change: objects are loyal to their owners and follow when called
everything_else: normal physics, normal society, normal time
result:
  - a chair trails its owner to the kitchen, dragging a scrape mark
  - a forgotten umbrella waits by the door it was last used at
  - a library book, returned late, sulks on the lower shelf
  - the postman's satchel hugs his leg at the gate
  - no object moves without being called; the world is consistent
```

### 31.12 Game frame — 2006 RPG

```
engine:
  renderer: forward, single-pass, shader model 3.0
  gpu_limits: 256MB VRAM, 2006-era fillrate, no compute
  materials: vertex-lit with one spec map, 512px normal maps
  lod: 1/8 mesh beyond 80m, hard pop-in
  shadows: 1024px single cascade, static geometry baked
  lighting: one dynamic directional sun, AO baked into vertices
  textures: DXT1/3, 256-512px
  hardware_era: AGP 8x, single core CPU
result:
  - the hero's sword shows the engine's 512px normal map and a
    vertex-lit sheen
  - the far cliff shows LOD simplification and a pop-in seam
  - the shadow has the 1024px cascade's soft edge and a baked static
    shadow underneath
  - the palette is the 2006 texture compression's slightly washed tone
```

---

## 32. Prompt Critique Workshop

Each entry shows a picture-centric prompt, the failure codes it triggers, and a UGS rewrite. Study the transformation.

### 32.1

**Prompt:** "A beautiful girl with flowers, soft bokeh, golden hour, dreamy."
**Fails:** F4 (director camera), F5 (uncaused DOF), F7 (likely identity if ref), F10 (posing), F12 (decoration).
**UGS:**
> A woman who keeps a cutting garden because her mother did, photographed by her partner who set the camera on the fence post to cook. The light is 90 min before sunset at 52N in August, scattered by the hedge. The background is soft only because the partner's lens is 85mm f/1.8 — a choice of his, not the world's. She is not posing; she is checking the beans behind the blooms.

### 32.2

**Prompt:** "Epic dragon over castle, cinematic, fog."
**Fails:** world-rule gap (magic undefined), F3 (fog not modeled), F2 (era mix).
**UGS:**
> A fortress of 14th-c dressed stone, its bailey abandoned after a siege 6 years prior. The "dragon" is a war balloon of the besieging army, canvas and wicker, heated by a brazier, drifting on the morning inversion that fills the valley with shallow fog. The castle's banner still flies — someone remained. The balloon's shadow crosses the keep as it passes.

### 32.3

**Prompt:** "Sad lonely man on bridge, rain, moody."
**Fails:** F1 (floating), F3 (rain not physical), F10 (posing), F12.
**UGS:**
> A maintenance worker on the night shift, on the footbridge over the canal where he pumps stormwater. It has rained since 21:00; the deck is slick, his coat drips. He pauses because the pump tripped and he is deciding whether to wade down. The rain is the leading edge of the same front that passed the hills to the west an hour ago. He is not performing sadness; he is cold and calculating a wet descent.

### 32.4

**Prompt:** "Cyberpunk city, neon, rainy, cool."
**Fails:** F2 (era mix), style label, F3 (neon not sourced), F12.
**UGS:**
> A port district, 40 years after the container trade collapsed, rewired by squatters into a data bazaar. The "neon" is salvaged signage and LED strips run off stolen substation power, blue-shifted because the voltage sags. The rain is the monsoon's first night; puddles reflect the signs because they are still water, not because of mood. A customs drone, still autonomous, sweeps the alley — its IR is the only light not from the squatters.

### 32.5

**Prompt:** "Cute cat, bokeh, sunlight."
**Fails:** F5, F1, F12.
**UGS:**
> A barn cat, 6 years old, one ear torn from a fight, sitting on the milking stool because the sun warms that spot at 09:00 in October. The window is small and the light is a single shaft; the background is sharp because the farmer's phone is at f/8 on a tripod — the cat is indifferent to it. A mouse shadow flicks at the door; the cat's weight shifts a half-second before it moves.

### 32.6

**Prompt:** "Explosion, dramatic, debris flying."
**Fails:** F3 (light), F12 (random effect), causality gap.
**UGS:**
> A fuel tanker ruptured at the junction when its brake failed on the grade; the spark was the downed line the city deferred in 2019. The blast is 4 seconds old; debris arcs on ballistic curves set by the charge's center; the streetlamp nearest the tank is out, the next three flicker from the pressure wave. A pedestrian 20m away is already turning to run — his reaction is 0.3s old, causal, not staged.

### 32.7

**Prompt:** "Aesthetic desk setup, RGB, clean."
**Fails:** F8 (dead detail), F12, F1.
**UGS:**
> A freelance editor's desk, used 11 hours a day; the RGB strip is set to a specific hue because it reduces his migraine, not for looks. The keyboard is worn at W and A from a project shipped last month. A cold coffee records the hour he lost to a render. The cable tray sags where the power brick heats it. The room is lit by the monitor only; the blind is closed because the neighbor's security light is harsh.

### 32.8

**Prompt:** "Mysterious forest path, fog, creepy."
**Fails:** F3 (fog), F12, F17 (skipped level).
**UGS:**
> A logging road abandoned when the mill closed in 2008; the fog is the river's cold exhale pooling in the hollow at dusk. The path is two ruts where the truck's tires ran, now grassed over except where the runoff still cuts. A boot print, fresher than the grass, records that someone walked it this morning — and the spacing says they were hurrying. The creepiness is the inference that the hurrier knew the mill is gone.

---

## 33. Authoring Protocol (Step-by-Step)

A repeatable procedure for producing a UGS-compliant request.

1. **Choose ontology.** Name the kinds of things. (§20, §3)
2. **Set world rules.** At least one invariant law. (§20, §6.3)
3. **Write history.** For each key object: origin, age, owner. (§3)
4. **Describe simulation.** Current state, including off-frame. (§4)
5. **Model physics.** Light (6 attrs), material (4 dims), mass/inertia. (§6, §7, §12)
6. **Populate environment.** Every on-frame element has an off-frame cause. (§4, §11)
7. **Give characters purpose + biography.** No posing. (§13)
8. **Place the camera as observer.** Hyperfocal; biography if character. (§8)
9. **State the observation.** Witnessed slice, not composed. (§2)
10. **Run checklist (§21) and taxonomy (§23).** Fix upstream, never at render. (§21.1)
11. **Emit.** Prefer the structured template (§26.2) for machine use.

---

*End of UGS v2 specification (English edition).*
