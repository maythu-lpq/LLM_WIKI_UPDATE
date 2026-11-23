# Alcohols — Turning –OH into a Leaving Group (SN1 / SN2 / E1 links)

> Source feed: `raw/ch 10.pdf`, `raw/ch 11.pdf` (Wade, Chapters 10–11). This note only records how alcohol chemistry reuses the four core mechanisms. See [index](index.md).

## Overview

An alcohol is a weak electrophile because the hydroxy group (–OH) is a **poor leaving group**. Once the –OH is protonated (it becomes H₂O) or converted to a **tosylate** (–OTs), it becomes a **good leaving group**, and the usual substitution and elimination reactions become possible. Which one happens depends on whether the carbon is primary (1°), secondary (2°) or tertiary (3°).

Alcohols are also made by SN2: a hydroxide or similar nucleophile displaces a halide from an unhindered alkyl halide (this competes with elimination).

Alcohols are widely used as fuels, solvents, antiseptics, beverages and starting materials (ch 10, section 10-5).

## Kinetics & Rate Law

This note adds no new rate laws. Use the rate law of the mechanism that applies:
- 3° alcohol + HBr → [SN1](sn1.md), `Rate = k[substrate]`.
- 1° alcohol + HBr (from NaBr/H₂SO₄) → [SN2](sn2.md), `Rate = k[substrate][nucleophile]`.
- Acid-catalyzed dehydration → [E1](e1.md), `Rate = k[substrate]`.

## Step-by-Step Mechanism

**3° alcohol + HBr (SN1, ch 11 Mechanism 11-1):**
1. Protonation converts –OH to a good leaving group (–OH₂⁺).
2. Water leaves, forming a carbocation. The hindered 3° carbon cannot undergo SN2, but it can ionize.
3. Bromide attacks the carbocation.

**1° alcohol + HBr (SN2, ch 11 Mechanism 11-2):** the alcohol is protonated, then bromide attacks from the back side. Ionization to a primary carbocation is unfavorable, so SN2 is used.

**Tosylate route:** TsCl/pyridine converts R–OH to R–OTs. The C–O bond of the alcohol stays intact during tosylate formation. Tosylate is an excellent leaving group, often better than halides. SN2 on a tosylate needs an unhindered primary or secondary carbon.

**PBr₃:** no carbocation forms, so rearrangements are uncommon. The final step is SN2 attack by bromide from the back side. PBr₃ works poorly with 3° alcohols.

**Dehydration (H₂SO₄ or H₃PO₄, heat):** protonation, loss of water to give a carbocation, then loss of a proton to give an alkene. This is E1 of the protonated alcohol. The product is an alkene mixture that follows Zaitsev's rule.

## Stereochemistry

- SN2 on a tosylate gives **inversion**: (S)-2-butyl tosylate + iodide → (R)-2-butyl iodide.
- Tosylate formation itself keeps the configuration at carbon (the C–O bond is not broken).
- SOCl₂ reacts by different mechanisms depending on substrate, solvent and temperature. Do not predict stereochemistry unless the actual mechanism is known.

## Controlling Factors

| Goal | Best reagent (ch 11 summary table) |
|---|---|
| 1° alcohol → chloride | SOCl₂ |
| 1° or 2° alcohol → bromide | PBr₃ (or HBr for 1°) |
| 1° or 2° alcohol → iodide | P/I₂ |
| 3° alcohol → chloride / bromide / iodide | HCl / HBr / HI |

- HX works well for most 3° alcohols. SOCl₂, PBr₃ and P/I₂ work well for most 1° and 2° alcohols.
- Halide ions are weak bases, so they stay nucleophilic in acid. Most good nucleophiles lose their nucleophilicity in acid.
- Williamson ether synthesis: an alkoxide displaces a halide by SN2, so the halide must be unhindered (usually primary).

## Related Mechanisms

- [SN1 Mechanism](sn1.md) — 3° alcohol + HX.
- [SN2 Mechanism](sn2.md) — 1° alcohol + HX, tosylates, PBr₃, Williamson.
- [E1 Mechanism](e1.md) — acid-catalyzed dehydration.
- [E2 Mechanism](e2.md) — tosylates can also undergo elimination (ch 8 reaction map).
- [Alkenes](alkenes.md) and [Alkynes](alkynes.md) — products and starting materials.
