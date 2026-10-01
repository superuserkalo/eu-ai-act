# EU AI Act assessment: open-weight legal fine-tune

- Date: 2026-10-01
- Text used: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (bundled skill references)
- This is engineering guidance, not legal advice.

## 1. Facts

| Item | Fact / assumption |
|---|---|
| Artefact | Fine-tuned 70B general-purpose LLM (legal domain), weights only, published on Hugging Face under Apache-2.0 with a model card. No AI system (UI, app) is described. |
| Actor | German non-profit research lab (established in the EU). |
| Base model | Popular open-weight 70B GPAI model; its provider is outside the EU. |
| Modification | Fine-tune using ~2% of original pre-training compute. |
| Distribution | Public download, worldwide including the EU. Not part of a specific scientific research project. |
| Intended purpose | Not stated beyond "legal texts". **Assumption:** a general legal-domain model for downstream integration, with no specific high-risk use advertised. |

Missing facts (open questions): absolute training compute of the base model and of the fine-tune; whether the base model is designated or presumed GPAI with systemic risk; whether the fine-tune keeps significant generality; whether the lab also offers a hosted demo/chat interface; whether the release is in the course of a commercial activity; intended uses advertised in the model card (e.g. administration of justice).

## 2. Classification

### Scope and definitions
- The released artefact is an AI **model**, not an AI system (Recital 97: models need further components such as a UI to become systems). Article 2(12)'s open-source exclusion speaks only of AI *systems*, so it does not take a GPAI model out of Chapter V. Chapter V has its own open-source carve-outs (Articles 53(2), 54(6)).
- **GPAI model (Article 3(63))**: a 70B LLM fine-tuned on legal text very likely still "displays significant generality and is capable of competently performing a wide range of distinct tasks". Agent inference: it remains a GPAI model. If the fine-tune narrowed it to a single task, it may fall outside Chapter V; the answer would change to "no Chapter V obligations; Article 4 only if it is later used in a system".
- **Research exclusions do not apply**: Article 2(6) needs "sole purpose of scientific research and development", which the case rules out; Article 2(8) and the Article 3(63) research carve-out cover only activity *before* placing on the market, and public release ends that. Non-profit status does not matter: Article 3(3) covers placing on the market "whether for payment or free of charge".
- **EU nexus (Article 2(1)(a))**: public download available in the Union = first making available on the Union market (Article 3(9)). Open point: Article 3(10) "making available" refers to "in the course of a commercial activity". Agent inference: a public, general release by an organisation is likely to be treated as placing on the market, but this is a point for counsel / Commission guidance.

### Role
- **Provider of a (modified) GPAI model** (Article 3(3)): the lab developed the fine-tune and places it on the market under its own name. Whether a fine-tune makes the modifier a *new* provider is not settled by a compute threshold in the Act text. Recital 109 states that for a modification or fine-tuning, provider obligations "should be limited to that modification or fine-tuning". Commission GPAI guidelines set an indicative compute threshold for when a modifier becomes a provider; they are not bundled, so I do not quote the figure. **External dependency.** With ~2% of original compute the lab may fall below that threshold, in which case it may not be treated as a new GPAI provider at all; confirm against the guidelines.
- The lab is not an importer, distributor or authorised representative of the base model. The non-EU base model provider keeps its own Chapter V duties (Article 54(6) exempts it from appointing an EU representative only if its release is open-source and not systemic-risk).
- Not a deployer of an AI system on these facts.

### Tiers
| Tier | Result | Reason |
|---|---|---|
| Prohibited (Article 5) | Not applicable to the model as such | Article 5 targets placing/using AI systems for listed practices; no such practice is described. |
| High-risk (Article 6, Annex III) | Not applicable to the model | High-risk attaches to AI systems with an intended purpose. If the model card advertised use to assist judicial authorities in researching/interpreting facts and law (Annex III, point 8(a)), a system built on it could be high-risk; the downstream system provider would carry that. |
| Transparency (Article 50) | Not applicable to the bare weights | Article 50 attaches to AI systems. Applies if the lab hosts a chat demo (Article 50(1)) or a generative system (Article 50(2)). |
| **GPAI model (Chapter V)** | **Applies (likely), scope limited to the fine-tune** | Articles 3(63), 53, Recital 109. |
| GPAI with systemic risk (Articles 51, 55) | Depends on base model | Presumption at cumulative training compute > 10^25 FLOP (Article 51(2)); or Commission designation (Article 51(1)(b), 52(4)). If the base model is systemic-risk, the open-source exemptions in Article 53(2) and 54(6) fall away and Article 55 duties may apply to the modifier (scope per Recital 109 and Commission guidance). |
| AI literacy (Article 4) | Applies only to providers/deployers of AI systems | Relevant if the lab builds or operates a system on top. |

### Classification under each unknown answer
- **A. Not systemic risk (base < 10^25 FLOP cumulative and not designated), lab treated as provider:** Apache-2.0 with public weights, architecture and usage info qualifies for Article 53(2): exempt from Article 53(1)(a) and (b). Still owes Article 53(1)(c) copyright policy and 53(1)(d) public training-content summary (for the fine-tune data), plus Article 53(3) cooperation. Article 54 not relevant (lab is EU-established).
- **B. Systemic risk base model, lab treated as provider:** no open-source exemption; Article 53(1)(a)-(d) all apply (Annex XI, XII), plus Article 55 evaluation, adversarial testing, serious-incident reporting and cybersecurity, and Article 52 notification. Limited to the modification per Recital 109; counsel needed.
- **C. Fine-tune below the guidelines' modification threshold:** lab likely not a new GPAI provider; obligations rest with the base model provider. Good practice: still publish the copyright policy and data summary voluntarily (Recital 109 encourages voluntary compliance).

## 3. Obligation register (scenario A, the most likely reading)

| Obligation | Article | Role | Applies from (today 2026-10-01) | Control | Evidence | Status |
|---|---|---|---|---|---|---|
| Copyright compliance policy incl. honouring TDM opt-outs | Art. 53(1)(c) | GPAI provider | 2 Aug 2025 (Art. 113(b)); already in force | Written policy; data-ingest pipeline that checks robots.txt / machine-readable reservations and logs decisions per source | Policy file in repo; ingest logs; CI test that reserved sources are rejected | Open |
| Public summary of training content (fine-tune data) | Art. 53(1)(d) | GPAI provider | 2 Aug 2025; already in force | Generate summary using the AI Office template (external dependency) from the dataset manifest; publish with the model card | Summary file versioned with each release; release check fails if missing | Open |
| Open-source exemption conditions kept true | Art. 53(2) | GPAI provider | 2 Aug 2025 | Release gate: licence = Apache-2.0, weights public, architecture config and usage info in model card | Release-checklist script asserting LICENSE, config.json, model card usage section | Open |
| Cooperate with Commission / NCAs | Art. 53(3) | GPAI provider | 2 Aug 2025 | Named contact, document retention | Contact in model card; retention policy | Open |
| Technical documentation / downstream info (only if scenario B) | Art. 53(1)(a),(b); Annex XI, XII | GPAI provider | 2 Aug 2025 | Annex XI doc limited to modification (data sources, compute, evals) appended to base docs | Docs in repo | Conditional |
| Systemic-risk duties (only if scenario B) | Art. 52, 55 | GPAI provider | 2 Aug 2025 | Compute accounting, evals, red-teaming, incident reporting, security | Records | Conditional |
| Transitional: base model placed before 2 Aug 2025 | Art. 111(3) | Base provider | 2 Aug 2027 | Not the lab's duty; the lab's fine-tune is placed now, so no transitional relief for it (agent inference) | n/a | Note |

## 4. Controls and checks I would build (advisory, no code)
1. **Compute ledger**: record FLOP for the fine-tune and the base model's published compute; a check that flags if cumulative compute is near or over 10^25 or the guidelines' modification threshold.
2. **Data manifest + TDM opt-out filter**: every source with licence, origin and opt-out status; a test that fails the build if a reserved source is in the training set.
3. **Training-content summary generator** from the manifest, rendered into the AI Office template; release CI fails without it.
4. **Release gate** asserting the Article 53(2) conditions (open licence, weights, architecture info, usage info) and the presence of the copyright policy and summary.
5. **Model card intended-use section** that states limits and warns that integration for administration of justice (Annex III, point 8(a)) makes the downstream system high-risk; test that the section exists.
6. If a hosted demo is added: Article 50(1) disclosure in the UI with a UI test, and Article 50(2) machine-readable marking of outputs.

## 5. Items for counsel / external dependencies
- Whether a ~2% compute fine-tune makes the lab a new GPAI provider: Commission GPAI guidelines (not bundled).
- Whether free, non-profit publication is "placing on the market" (Article 3(9)-(10), commercial activity wording).
- Systemic-risk status of the base model (Commission list under Article 52(6)).
- Code of practice for GPAI (Article 56) and the AI Office summary template: external, not bundled.

## Open questions
1. Base model's cumulative training compute and whether it is on the Commission's systemic-risk list.
2. Absolute FLOP of the fine-tune and whether it crosses the Commission guidelines' threshold.
3. Does the model stay general-purpose, or is it narrowed to one task?
4. Is there a hosted demo or API (would make the lab an AI system provider, Article 50 and Article 4 apply)?
5. Does the model card promote use for judicial or legal-decision support (Annex III, point 8(a))?

```json
{"roles": ["provider of a general-purpose AI model (modification/fine-tune), subject to Commission guidelines threshold"], "tier": "general-purpose AI model without systemic risk, open-source exemption under Article 53(2) (conditional on base model not being systemic-risk)", "citations": ["Article 2(1)(a)", "Article 2(6)", "Article 2(8)", "Article 2(12)", "Article 3(3)", "Article 3(9)", "Article 3(10)", "Article 3(63)", "Article 51(1)", "Article 51(2)", "Article 52", "Article 53(1)(a)", "Article 53(1)(b)", "Article 53(1)(c)", "Article 53(1)(d)", "Article 53(2)", "Article 53(3)", "Article 54(6)", "Article 55", "Article 50(1)", "Article 50(2)", "Article 111(3)", "Article 113(b)", "Annex III, point 8(a)", "Annex XI", "Annex XII", "Recital 97", "Recital 102", "Recital 109"], "key_findings": ["The released weights are a GPAI model, not an AI system, so Article 2(12) does not exempt them; Chapter V applies", "Research exclusions (Article 2(6), 2(8)) do not apply because the model is publicly released and not for sole research purposes; non-profit and free release do not matter (Article 3(3))", "If treated as provider and base is not systemic-risk, Article 53(2) exempts 53(1)(a)-(b) but copyright policy 53(1)(c) and training-content summary 53(1)(d) still apply, already in force since 2 Aug 2025", "Obligations are limited to the fine-tune (Recital 109); whether 2% compute makes the lab a new provider depends on Commission guidelines not bundled", "If base model is systemic-risk (>10^25 FLOP or designated), open-source exemptions fall away and Article 55 may apply", "No Article 5, Article 6 or Article 50 obligations on bare weights; they arise if a hosted system or judicial use (Annex III 8(a)) is added"], "open_questions": ["Base model cumulative compute / systemic-risk designation", "Fine-tune FLOP vs Commission guidelines modification threshold", "Does the fine-tune retain significant generality", "Is there a hosted demo or API", "Does the model card target judicial use", "Is free non-profit release 'in the course of a commercial activity'"], "files_read": ["SKILL.md", "references/timeline.md", "references/catalog.md", "references/builder-playbook.md", "references/articles/002.md", "references/articles/003.md", "references/articles/004.md", "references/articles/051.md", "references/articles/052.md", "references/articles/053.md", "references/articles/054.md", "references/articles/111.md", "references/recitals/097.md", "references/recitals/102.md", "references/recitals/109.md"]}
```
