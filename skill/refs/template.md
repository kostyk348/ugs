# UGS Prompt Template (fill field by field; empty field = failure)

```yaml
ontology:        # what kinds of things exist in this world
world_rules:     # >=1 invariant law (physical / social / magical)
history:         # origin, age, owner of key objects
  - origin:
  - age:
  - owner:
simulation:      # current state, INCLUDING off-frame causes
physics:
  light:        # power, temperature(K), scattering, reflections, falloff, atmosphere
  material:     # behavior, wear, history, physics
environment:     # off-frame causes that explain on-frame content
characters:      # purpose + biography; NO posing
  - purpose:
    biography:
camera:         # observer by chance; hyperfocal default; DOF only if caused
  - observer_stance:
  - focus: hyperfocal
observation:     # witnessed slice, not composed
```

## Video extension
```yaml
temporal:
  acceleration:
  inertia:
  mass:
  begin_moment:
  end_moment:
continuity:      # position continuous across cuts unless new observer explained
audio:
  sources:       # physical, diegetic only
  acoustics:     # space, reverb, medium
```

## Meme extension
```yaml
axiom_change:    # EXACTLY ONE altered axiom of the world
everything_else: normal
result:          # world develops logically around the axiom
```

## Game-frame extension
```yaml
engine:
  renderer:      # deferred/forward, API era
  gpu_limits:    # VRAM, fillrate, shader model
  materials:     # how the engine represents them
  lod:           # level-of-detail rules
  shadows:       # shadow map size, cascade count
  lighting:      # baked vs dynamic
  textures:      # resolution, compression
  hardware_era:  # what silicon this ran on
result:          # frame shows the engine's characteristic artifacts
```
