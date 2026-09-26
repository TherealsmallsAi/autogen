# Cinematic Motion Prompt Specification

## Purpose

Cinematic motion is a design-system layer, separate from static visual
references. A visual reference establishes the composition; a motion prompt
establishes how that composition behaves over time and in response to user
input. Keeping the two layers distinct gives an implementation agent enough
direction to create intentional scenes rather than applying generic scroll
animations.

The motion system should support the narrative progression:

```text
WORLD -> NEWS -> SIGNAL -> VERIFICATION -> ANALYSIS -> DEMO -> AI EMPLOYEE
```

Motion must communicate a state change in that progression. It must not be
added solely as decoration.

## Motion Prompt Stack

| Layer | Responsibilities |
| --- | --- |
| Camera | Slow push-ins, orbital reveals, parallax drift, crane/descent shots, tunnel fly-throughs, and rack-focus transitions. |
| Scroll | Pinned scenes, scroll-scrubbed cameras, depth-based parallax, chapter transitions, and velocity-reactive elements. |
| Object | Magnetic attraction, orbital motion, floating suspension, mechanical deployment, particle assembly, and holographic emergence. |
| UI | Glass refraction, signal pulses, scanning lines, data streams, progressive disclosure, and micro-interactions. |
| Transitions | Match cuts, light sweeps, particle dissolves, dimensional wipes, camera-through-object shots, and environmental morphs. |
| Atmosphere | Volumetric light, dust or particles, restrained film grain, depth of field, bloom, and ambient environmental motion. |

## Prompting Rules

Write prompts as cinematography, not as lists of animation names. Each prompt
must state:

1. **Anchor**: the subject that stabilizes the shot.
2. **Trigger**: the event that advances the shot, usually scroll progress.
3. **Camera path**: distance, direction, orbit, and any occlusion.
4. **Depth behavior**: relative foreground, midground, and background motion.
5. **Semantic response**: what activates, accepts, pauses, rejects, or
   transforms—and why.
6. **Exit**: the held composition and transition to the next chapter.

For example, use a concrete instruction such as: "Lock the camera to the
central Signal Core. Advance 18% into the chamber; move surrounding
architecture at 0.65x camera velocity. At 70% scroll progress, orbit 12
degrees while a foreground frame occludes the lens. Hold for 400 ms before the
next chamber." Do not use a request such as "add a cool scroll animation."

## Motion Grammar

Represent every implementation-ready motion prompt with metadata. Values below
are defaults and may be overridden by a named scene.

```yaml
motion:
  category: camera
  trigger: scroll
  duration: 2400ms
  easing: cinematic
  intensity: low
  depth: high
  camera:
    movement: dolly_forward
    distance: 1.8
    orbit: 8deg
  parallax:
    foreground: 1.0
    midground: 0.65
    background: 0.25
  atmosphere:
    particles: subtle
    volumetricLight: subtle
  reducedMotion:
    preserveOpacity: true
    disableCameraMovement: true
```

`reducedMotion` is required for every scene. When enabled, retain meaningful
opacity and content-reveal states, but replace continuous camera movement,
parallax, and particle travel with stable compositions.

## Scene Library

### 01 — Signal Core Awakening

Begin in a dark architectural chamber that is nearly still. A small emerald
signal appears at the room's center and pulses once; a second pulse travels
through embedded conduits. The camera performs an extremely slow forward dolly
as hundreds of small data particles move toward the Signal Core. Increase the
core's intensity gradually—never with an explosion or cyberpunk flash. At full
scroll progress, the illuminated chamber reveals the next scene through the
core. The intended feeling is controlled, expensive, technological, and
physically believable.

### 02 — Intelligence Tunnel

Scroll controls a forward cinematic camera move through a long architectural
tunnel. Thousands of wall channels activate only as the camera passes them.
Foreground geometry moves quickly, midground geometry moves moderately, and
background geometry moves extremely slowly to create differential parallax.
Allow occasional particles to cross the lens. The camera should feel like a
planned shot, not a translation through a 3D model.

### 03 — Verify

Introduce a large floating intelligence artifact. Three independent signal
streams approach it: accept the first, pause the second, and reject the third
by letting it disappear. Slowly rotate the artifact while the camera makes a
subtle orbit. A thin circular verification ring completes around it; only at
100% completion may the environment transition. The motion communicates the
verification result rather than decorating the object.

### 04 — News to Signal

Present a conventional news headline as a physical data object and slowly
approach it with the camera. Fragment the headline into individually verified
claims, then send those claims through separate illuminated channels. Follow
one channel as the editorial-typography environment transforms into the
intelligence facility. The shot should make the user feel that they are
entering the machinery underneath the news.

## Implementation Constraints

- Keep intensity low by default; reserve high-intensity motion for meaningful
  chapter changes.
- Use natural occlusion, differential parallax, and a brief final hold to make
  scene boundaries feel like camera edits rather than UI swaps.
- Avoid flashy explosions, perpetual motion, and effects that do not reveal
  information or advance the narrative.
- Provide a stable, accessible reduced-motion version of every scene.
