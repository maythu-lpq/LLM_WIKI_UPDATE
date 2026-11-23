# Reference Sources Log

> **Directory:** `wiki/sources.md`  
> **Rule Reference:** `AGENTS.md` Section 2 & Section 9  
> This file tracks every source material placed in `raw/`, summarizing its topic, key concepts, and which `wiki/*.md` entries it feeds.

---

## Current Sources in `raw/`

### 1. `raw/Organic Chemistry ch 5-7.pdf`
- **Source Type:** Textbook Reference (L.G. Wade, *Organic Chemistry*, Chapters 5–7)
- **Topic:** Stereochemistry, Nucleophilic Substitutions, and Eliminations
- **Key Concepts Covered:**
  - **Chapter 5 (Stereochemistry):** Chirality, enantiomers, diastereomers, $(R)/(S)$ stereocenters, optical activity, Walden inversion.
  - **Chapter 6 (Substitution Reactions):** $\text{S}_\text{N}2$ mechanism (concerted backside attack, 2nd-order kinetics, steric hindrance, polar aprotic solvents), $\text{S}_\text{N}1$ mechanism (two-step carbocation intermediate, 1st-order kinetics, racemization, carbocation stability, 1,2-hydride and 1,2-methyl shifts, polar protic solvent stabilization).
  - **Chapter 7 (Elimination Reactions):** $\text{E}1$ mechanism (carbocation intermediate, Zaitsev's rule, heat promotion), $\text{E}2$ mechanism (concerted, anti-periplanar $180^\circ$ geometry, Zaitsev vs. Hofmann selectivity with bulky bases like $\text{KO}t\text{Bu}$), competition frameworks ($\text{S}_\text{N}2$ vs. $\text{E}2$, $\text{S}_\text{N}1$ vs. $\text{E}1$).
- **Wiki Pages Fed:**
  - `wiki/sn1.md` (Full coverage: kinetics, mechanism, stereochemistry, factors)
  - `wiki/sn2.md` (Full coverage: kinetics, backside attack, stereochemistry, factors)
  - `wiki/e1.md` (Full coverage: kinetics, mechanism, Zaitsev rule, factors)
  - `wiki/e2.md` (Full coverage: kinetics, anti-periplanar geometry, Hofmann vs. Zaitsev)
  - `wiki/index.md` (Master comparison table, mechanism summaries, decision trees)

---

### 2. `raw/ch 8.pdf`
- **Source Type:** Textbook Reference (L.G. Wade, *Organic Chemistry*, Chapter 8, Reactions of Alkenes)
- **Topic:** Electrophilic additions, halonium ions, reaction summary maps
- **Key Concepts Used:** carbocation in HX addition (like SN1 step 2), back-side attack on halonium ions (like SN2) giving anti addition, rearrangements, E1/E2 as the two ways to make alkenes.
- **Wiki Pages Fed:** `wiki/alkenes.md`

### 3. `raw/ch 9.pdf`
- **Source Type:** Textbook Reference (Wade, Chapter 9, Alkynes)
- **Topic:** Acetylide ions and elimination syntheses of alkynes
- **Key Concepts Used:** acetylide alkylation is SN2 (needs 1° halide), E2 competes when hindered, double dehydrohalogenation, pKa of terminal alkynes vs NH₃.
- **Wiki Pages Fed:** `wiki/alkynes.md`

### 4. `raw/ch 10.pdf`
- **Source Type:** Textbook Reference (Wade, Chapter 10, Structure and Synthesis of Alcohols)
- **Topic:** Alcohol properties and syntheses; uses of alcohols
- **Key Concepts Used:** alcohols made by SN2 on alkyl halides (competes with elimination), commercial uses of alcohols, thiols by SN2.
- **Wiki Pages Fed:** `wiki/alcohols.md`, `wiki/index.md` (uses)

### 5. `raw/ch 11.pdf`
- **Source Type:** Textbook Reference (Wade, Chapter 11, Reactions of Alcohols)
- **Topic:** Converting –OH to a leaving group; HX, PBr₃, SOCl₂, tosylates, dehydration, Williamson
- **Key Concepts Used:** SN1 for 3° alcohol + HBr, SN2 for 1° alcohol + HBr, tosylate inversion, PBr₃ avoids carbocations, dehydration is E1 of the protonated alcohol, best-reagent table.
- **Wiki Pages Fed:** `wiki/alcohols.md`

> Note on `raw/Organic Chemistry ch 5-7.pdf` section 6-3 (Common Uses of Alkyl Halides): also feeds `wiki/index.md` (Why It Matters section).

---

## Source Count & Status

- **Current Distinct Files in `raw/`:** **5**
- **Target Minimum Sources:** **5**
- **Gap:** **0** (requirement met; ingest of sources 2–5 was done in the fix run, see `logs/slides-run-log.md`)

---

*Log maintained according to `AGENTS.md` Section 9. Sources 2–5 only add links to the four core mechanisms; they do not change `wiki/sn1.md`, `sn2.md`, `e1.md`, `e2.md`.*
