# Suno Prompt Contract

## Purpose

This reference defines the canonical copy-ready handoff for Suno generation. It keeps user-facing output compact, reproducible, and practical on mobile devices.

The governing UX rule is:

> **One real Suno input field = one dedicated copyable block containing only paste-ready text.**

This rule is mandatory for every Suno track handoff, not only when the user explicitly asks for a mobile or copy-ready format. Field labels and explanations stay outside the copyable block.

## Required order and grouping

For every track, always present the production handoff in this order:

1. `Title`
2. `Lyrics`
3. `Style`
4. `Advanced controls` only when current Suno capabilities make them relevant

`Title`, `Lyrics`, and `Style` are always three separate copyable blocks. Never combine them into one large block.

Complete one track before starting the next. Do not group all album titles first, then all lyrics, then all styles.

Do not add a catch-all `Other`, `Misc`, or `Sonstiges` section.

## Copy-block contract

Each actual Suno field gets exactly one dedicated copyable block.

Rules:

- Put the field label outside the block.
- Put only the exact text to paste into Suno inside the block.
- Do not include `Title`, `Lyrics`, `Style`, commentary, bullets, quotes, or instructions inside a paste block unless they are intentionally part of the field content.
- Do not make the user manually select a subsection from a larger mixed block.
- Do not create empty blocks for unused Suno fields.
- Keep each track self-contained so a mobile user can copy Title -> switch to Suno -> paste -> return -> copy Lyrics -> paste -> return -> copy Style -> paste, without searching elsewhere in the response.
- This contract is mandatory for all Suno production handoffs.

## Suno field length limits

Treat these as hard preflight limits for every Suno-ready handoff:

- `Lyrics`: **maximum 5000 characters**.
- `Style`: **maximum 1000 characters**.

Before presenting a track package, count the final paste-ready content and revise it if either field exceeds its limit. Do not rely on the user to shorten the text manually after handoff. Prefer leaving a small margin below the maximum when the same meaning can be preserved more compactly.

## Title

Use the confirmed title. If the title is not frozen, explain outside the block that it is a working title. The block itself still contains only the title text.

Example:

**Title**

```text
NO BRAKES
```

## Lyrics

- Keep complete lyrics inside one copyable block.
- Never exceed **5000 characters** in the final Lyrics field.
- Use structural labels when they improve generation control.
- Write intended repetitions explicitly when repetition is part of the genre/arrangement.
- Avoid verbose production directions in the Lyrics field.
- Preserve narrative progression where repetition would damage meaning.
- For long-form repetition-driven dance, trance, hard-trance, makina, rave, or workout tracks, build/drop cycles and intentionally repeated hook blocks may be written directly into the Lyrics field when they are being used to control arrangement and duration.

Example:

**Lyrics**

```text
[Intro]
You came this far
Don't slow down now

[Build]
Push
Push
Push

[Drop]
NO BRAKES
Forward
Forward
Forward
```

## Style

The Style block is the compact production specification. It must never exceed **1000 characters**. Include only relevant dimensions, normally in one dense paragraph or semicolon-separated vector:

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

`Key`, `Target length`, and `Vocals / Melody` belong here rather than in a loose remainder field when Suno does not provide dedicated fields for them.

Example:

**Style**

```text
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

If an Advanced control corresponds to a separate Suno input field, give that field its own copyable block under an external label. If it is a setting the user must choose rather than paste, present it as concise prose outside the Title/Lyrics/Style blocks.

Never invent slider names, ranges, or values from memory. Verify current Suno capabilities first.

## Album completion contract

For every Suno **album project**, the workflow has two mandatory completion artifacts in addition to the per-track packages.

### Final playlist

After the final album title and track order are frozen, output one compact playlist that contains:

- the final **album title**;
- the final numbered **track sequence in listening order**;
- exactly the same track titles used in the final Title blocks.

The playlist is the canonical human-readable album sequence. It must be regenerated whenever the album title or track order changes.

### Album cover

A Suno album project is not complete without an actually generated album cover.

Requirements:

- square **1:1** format;
- visually derived from the album's lyrics, musical identity, emotional arc, and confirmed artist/project direction;
- no generic unrelated artwork merely to fill the requirement;
- use the available image-generation capability to create the image, not only a cover prompt or brief;
- do not directly imitate a living visual artist or use uncleared copyrighted assets;
- if the cover direction is materially underdetermined, run a focused Grilling-v2 follow-up for the unresolved visual decisions only; do not repeat already answered project questions;
- if the existing Grilling/Second Brain already determines a coherent visual direction, proceed without unnecessary re-grilling;
- store the binary image in the documented external artifact store and keep its reference/provenance in the Project Second Brain.

If the user has already accepted a fitting square cover for the same frozen album version, reuse it rather than generating a replacement without a reason.

## Reference handling

Artist or track references may appear in the analysis notes, but final generation prompts should primarily express the abstracted musical craft:

- use one reference for rhythm/groove if relevant;
- another for arrangement or harmonic tension;
- another for vocal attitude or sound-design density;
- remove copied lyrical, melodic, sampled, or voice-specific content.

Do not produce an exact-clone prompt for a living artist.

## Prompt lint before generation

Reject or revise a prompt if it contains:

- Lyrics longer than **5000 characters**;
- Style longer than **1000 characters**;
- Title, Lyrics, and Style combined in one copy block;
- contradictory BPM/tempo descriptions;
- mutually incompatible vocal instructions;
- too many genre labels without a clear hierarchy;
- a target length unsupported by the current selected model without an explicit extension/assembly strategy;
- arrangement instructions that cannot plausibly fit the target length;
- an album track that duplicates the neighboring track's entire sound vector;
- unauthorized sample, voice, or artist-imitation instructions;
- mixed prose and paste text inside the same copy block;
- a field label inside the paste text;
- album-wide grouping that forces repeated searching between tracks.

For album completion, fail the final album handoff if:

- the final playlist is missing or does not match the frozen album title/order;
- the album cover is missing;
- the cover is not square;
- the cover is unrelated to the album concept;
- a cover brief exists but no actual image was generated.

## Length-specific guidance

When long-form duration is important:

1. state the target length explicitly in Style;
2. provide an arrangement arc with enough sections to occupy that duration;
3. for repetition-driven genres, write core hook/chorus blocks more than once where musically intentional;
4. prefer native full-length regeneration when the current model supports it;
5. use Extend only when preserving a strong existing candidate is worth the added workflow complexity;
6. log actual generated duration so future model-behavior assumptions are evidence-based.
