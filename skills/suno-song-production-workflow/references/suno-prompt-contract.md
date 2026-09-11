# Suno Prompt Contract

## Purpose

This reference defines the canonical copy-ready handoff for Suno generation. It keeps the user-facing block compact while preserving enough structure for reproducible iteration.

## Required order

Always present the production block in this order:

1. `Title`
2. `Lyrics`
3. `Style`
4. `Advanced controls` only when current Suno capabilities make them relevant

Do not add a catch-all `Other`, `Misc`, or `Sonstiges` section.

## Title

Use the confirmed title. If the title is not frozen, mark it explicitly as `Working title` rather than inventing finality.

## Lyrics

- Keep complete lyrics inside one copyable block.
- Use structural labels when they improve generation control.
- Write intended repetitions explicitly when repetition is part of the genre/arrangement.
- Avoid verbose production directions in the Lyrics field.
- Preserve narrative progression where repetition would damage meaning.

## Style

The Style block is the compact production specification. Include only relevant dimensions, normally in one dense paragraph or semicolon-separated vector:

- genre/subgenre;
- production era or sonic period;
- BPM and meter;
- key/mode;
- target length;
- groove / drum architecture;
- bass role;
- lead and supporting instrumentation;
- arrangement arc;
- vocals and melody behavior;
- energy/dynamics;
- production/mix character;
- negative constraints;
- neighboring-track differentiation for albums.

`Key`, `Target length`, and `Vocals / Melody` belong here rather than in a loose remainder field.

### Example shape

```text
Style
Early-90s-inspired hard trance with modern low-end control; 146 BPM, 4/4, F minor; target length 6:00-6:30; rolling offbeat bass, hard 909-style kick, tense minor-key arpeggio, wide rave stabs and a concise rising lead motif; sparse male spoken/processed hook with short melodic answers; long DJ-friendly intro, first build and drop, stripped breakdown, larger second build/peak, functional outro; energetic but not euphoric-pop, no rock guitars, no sentimental ballad chorus.
```

The example demonstrates structure only. Do not reuse it blindly across tracks.

## Advanced controls

Only include controls that are current, verified, and intentional, for example:

- selected model;
- exploration vs precision model choice;
- Voice / Style Persona / Custom Model;
- audio/reference influence;
- relevant creativity/structure/reference controls;
- Edit/Replace/Extend instruction after a first generation.

Never invent slider names, ranges, or values from memory. Verify current Suno capabilities first.

## Reference handling

Artist or track references may appear in the analysis notes, but final generation prompts should primarily express the abstracted musical craft:

- use one reference for rhythm/groove if relevant;
- another for arrangement or harmonic tension;
- another for vocal attitude or sound-design density;
- remove copied lyrical, melodic, sampled, or voice-specific content.

Do not produce an exact-clone prompt for a living artist.

## Prompt lint before generation

Reject or revise a prompt if it contains:

- contradictory BPM/tempo descriptions;
- mutually incompatible vocal instructions;
- too many genre labels without a clear hierarchy;
- a target length unsupported by the current selected model without an explicit extension/assembly strategy;
- arrangement instructions that cannot plausibly fit the target length;
- an album track that duplicates the neighboring track's entire sound vector;
- unauthorized sample, voice, or artist-imitation instructions.

## Length-specific guidance

When long-form duration is important:

1. state the target length explicitly in Style;
2. provide an arrangement arc with enough sections to occupy that duration;
3. for repetition-driven genres, write core hook/chorus blocks more than once where musically intentional;
4. prefer native full-length regeneration when the current model supports it;
5. use Extend only when preserving a strong existing candidate is worth the added workflow complexity;
6. log actual generated duration so future model-behavior assumptions are evidence-based.
