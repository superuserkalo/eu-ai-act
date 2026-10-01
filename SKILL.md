---
name: eu-ai-act
description: Use when building, changing, or reviewing software that uses AI and may be placed on the EU market or used in the EU, or when asked about EU AI Act scope, roles, prohibited practices, high-risk classification, transparency or labelling duties, general-purpose AI model obligations, deadlines, or fines. Classifies the system against the bundled official text of Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744, then turns the applicable obligations into code, tests, and documentation. GDPR, copyright, product liability, and non-EU AI laws fall outside this skill.
license: Official EU legal texts, reusable with attribution under Commission Decision 2011/833/EU. See NOTICE.md.
metadata:
  source: Regulation (EU) 2024/1689 (Artificial Intelligence Act), as amended by Regulation (EU) 2026/1744
  version: "0.1.0"
---

# EU AI Act

Classify the AI system from evidence, cite the Act for every obligation, and build the controls into the product. The bundled references are the official English text. Your output is engineering guidance, not legal advice. Say so once in the report.

## Rules that apply throughout

- **Read one Article at a time.** Each Article is its own file: `references/articles/NNN.md`, zero-padded, for example `articles/050.md` or `articles/004a.md`. Annexes are `references/annexes/<roman>.md`. Find files through [the index](references/index.md). Do not load whole chapters.
- **Amendments come first in the file.** An Article or Annex changed by a later act opens with the amending text, oldest act first, then the 2024 text. Where amending text replaces, inserts, or deletes wording, it controls, and a later act controls over an earlier one. Apply it to the 2024 text yourself and cite both, for example `Article 50(7) as replaced by 2026/1744`.
- **Check the date.** An obligation binds only from its application date. Use [the timeline](references/timeline.md) and state today's date next to every deadline you report.
- **Classify the system, not the model vendor.** Calling a third-party model through an API does not make you a model provider. Putting your name on an AI system, or making it available to others, usually makes you a provider of that system. Read Article 3 and Article 25 before you decide.
- **Facts over guesses.** If classification depends on a fact you cannot observe in the code or the conversation, such as the intended purpose, users, or EU nexus, ask the person. Do not assume the friendlier answer.

## 1. Establish the facts

Record from the code, product docs, and the person:

- what the system does, its **intended purpose** (Article 3(12)), and who uses it and who is affected.
- the EU nexus: placed on the EU market, used in the EU, or output used in the EU (Article 2(1)).
- the person's **role** for each system: provider, deployer, importer, distributor, product manufacturer, or authorised representative (Article 3(3) to (8)). One organisation can hold several roles.
- every model in use: third-party API, open-weight, fine-tuned, or trained in-house. Note who places each model on the market.
- whether outputs reach people as text, images, audio, video, or decisions about them.

Find AI call sites in the repository. Search for model SDK imports, inference endpoints, and prompt templates. List each feature that uses them.

This step is complete when each AI feature has an intended purpose, a role, and a model source. List missing facts as open questions.

## 2. Classify

Work through the tiers in this order. A system can fall into several. Use [the catalog](references/catalog.md) to go from a question to the Articles that answer it.

1. **Scope and definition.** Does it meet the AI system definition (Article 3(1))? Does an Article 2 exclusion apply, such as military use, scientific research, personal non-professional use, or the free and open-source exception in Article 2(12)?
2. **Prohibited.** Check every point of Article 5(1), including points (ba) and (bb) inserted by the amendment. A prohibited practice cannot be engineered into compliance. Stop and report it.
3. **High-risk.** Check Article 6(1) with Annex I (safety component of a regulated product) and Article 6(2) with Annex III (listed use cases). If Annex III matches, test the Article 6(3) derogation and remember that profiling of natural persons is always high-risk. A provider relying on the derogation must document it (Article 6(4)) and register it (Article 49(2)).
4. **Transparency.** Check every paragraph of Article 50: chatbots and other direct interaction, synthetic content marking, emotion recognition and biometric categorisation, deep fakes, and AI-generated text published on matters of public interest.
5. **General-purpose AI models.** Only when the person trains, substantially modifies, or places a GPAI model on the market. Read Articles 51 to 56 and Annexes XI to XIII.
6. **Everything else.** AI literacy (Article 4) applies to every provider and deployer.

This step is complete when each feature has a tier, the Article and point that put it there, and the reason each higher tier does not apply. If a fact decides the tier and is unknown, give the classification under each answer.

## 3. Map obligations to engineering work

Use [the builder playbook](references/builder-playbook.md) to turn each applicable obligation into controls: UI disclosures, content marking, logging, human oversight, data governance, documentation, monitoring, and incident handling. Read the cited Article text before you implement a control. The playbook routes. It does not replace the text.

Prefer controls in code over controls in policy documents. A disclosure that a test asserts is stronger than a sentence in a wiki.

This step is complete when the obligation register has one row per obligation with its Article, role, application date, control, and evidence.

## 4. Implement and verify

Make the smallest change that satisfies each obligation in scope for the task. For each control, add a check that fails if the control regresses, such as a UI test for the disclosure, a test that generated media carries the marking, or a test that logs contain the required fields. Run the project's existing test command.

Write documentation that the Act requires, such as Annex IV technical documentation or the Article 6(4) assessment, as files in the repository when the person agrees.

This step is complete when each implemented control has a passing check or a stated reason it cannot be tested automatically.

## 5. Report

Report:

- today's date and the version of the text used: 2024/1689 as amended by 2026/1744.
- each feature, its role, its tier, and the Article citations that decide it.
- the obligation register: obligation, Article, application date, control, evidence, status.
- open questions that would change the classification.
- items that need counsel or a notified body, such as prohibited-practice edge cases, Article 6(3) reliance, third-party conformity assessment, or a fundamental rights impact assessment (Article 27).
- the note that this is engineering guidance, not legal advice.

Cite the Article, paragraph, and point, for example `Article 50(2)` or `Annex III, point 4(a)`. Label any conclusion that goes beyond the text as agent inference. Commission guidelines, codes of practice, harmonised standards, and national implementing law are not bundled. When one matters, name it as an external dependency and do not quote it from memory. The official pages for these are listed under `watch` in `tracking.json`.

Read [source provenance](references/source-map.md) only when the person asks for the CELEX number, ELI, retrieval date, or hashes.

Stop when every AI feature is classified with citations and every in-scope obligation has a control or an open item. Also stop when a prohibited practice is found or the classification cannot proceed without facts only the person can provide.
