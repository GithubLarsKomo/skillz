# Award institution model

Last verified: 2026-09-09

This reference records only institutional mechanics used to shape the simulation. It does **not** claim that the awards publish a shared craft rubric.

## Hugo-inspired chamber

Official Hugo guidance describes a ranked-choice final ballot that includes **No Award**. A finalist placed below No Award is treated as not worthy of the award by that voter; a final No Award test is part of the outcome process.

Simulation consequence:

- preserve heterogeneous reader preferences;
- use rank/threshold thinking rather than one average score;
- include an explicit aboveNoAward|belowNoAward judgment.

Official source:
- https://www.thehugoawards.org/the-voting-system/

## Nebula-inspired chamber

Current Nebula rules state that eligible Full, Associate and Senior SFWA members nominate, the top six works form the final ballot (subject to tie/fewer-nomination rules), and eligible members cast one final vote per category.

Simulation consequence:

- model a professional-writer electorate;
- emphasize craft reasons that would motivate or prevent nomination;
- do not pretend that a seven-person simulated panel equals the real electorate.

Current rules also state that works written wholly or partially using generative LLM tools are not eligible and that works using LLMs at any point in the writing process must disclose this and are disqualified. This workflow therefore must never imply real Nebula eligibility for AI-assisted manuscripts.

Official source:
- https://nebulas.sfwa.org/about-the-nebulas/nebula-rules/

## World-Fantasy-inspired chamber

World Fantasy describes a hybrid process in which convention members contribute finalists and a panel of five judges adds nominees and decides the winner. The 2026 submission page lists five judges and states that AI-created work is not eligible.

Simulation consequence:

- use a five-role deliberative jury;
- emphasize close reading, literary distinctiveness and jury disagreement;
- do not impersonate current named judges or claim their personal tastes.

Official sources:
- https://worldfantasy.org/world-fantasy-awards-2025/
- https://worldfantasy.org/2026-world-fantasy-award-submissions/

## Boundary

The workflow uses these institutions as **perspective generators**. It does not:

- reproduce secret judging criteria;
- predict actual nominations;
- certify eligibility;
- estimate a probability of winning;
- impersonate named voters or judges.
