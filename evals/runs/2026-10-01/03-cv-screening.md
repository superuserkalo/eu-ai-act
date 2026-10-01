# EU AI Act assessment: CV screening SaaS

Date: 2026-10-01. Text: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. This is engineering guidance, not legal advice.

## 1. Facts
- System: SaaS that scores and ranks job applicants from CVs against job descriptions (fine-tuned classifier + LLM) and auto-rejects the bottom 50%. Recruiters see the ranked shortlist.
- Intended purpose (Art. 3(12)): recruitment/selection, filtering applications and evaluating candidates.
- Affected persons: job applicants. Users: employer recruiters.
- EU nexus: Polish company, sold to employers across the EU (Art. 2(1)(a)).
- Roles: the HR-tech company is **provider** (develops the system, places it on the market under its own name, Art. 3(3)). Customer employers are **deployers** (Art. 3(4)). If the company also uses it for its own hiring it is also deployer.
- Models: in-house fine-tuned classifier (company trains it); LLM, assumed third-party API (company is not a GPAI model provider under that assumption). Classifier trained on customers' historical hiring data.
- Outputs reach people as decisions: automatic rejection.
- GA: January 2027 (before the Annex III date of 2 Dec 2027).

## 2. Classification
1. Scope: meets Art. 3(1) (infers from input how to generate scores/decisions). No Art. 2 exclusion applies.
2. Prohibited (Art. 5(1)): no point matches on the stated facts. Watch Art. 5(1)(f) — if any feature infers emotions (e.g. video interviews, tone analysis), it is prohibited in the workplace context; Art. 5(1)(g) if biometric categorisation by protected traits. Art. 5(1)(c) social scoring not met (single recruitment context). Not prohibited.
3. **High-risk: yes.** Art. 6(2) with Annex III, point 4(a) ("analyse and filter job applications, and to evaluate candidates"). Art. 6(3) derogation is unavailable: (i) the system materially influences the outcome — it auto-rejects; (ii) scoring and ranking individuals on CV attributes is profiling of natural persons, and Art. 6(3) last subparagraph makes it always high-risk.
4. Transparency (Art. 50): no chatbot or direct interaction with applicants on the facts; Art. 50(1) would apply if an applicant-facing assistant exists. LLM-generated text shown to recruiters (e.g. summaries) could trigger Art. 50(2) marking — open question.
5. GPAI (Arts. 51-56): not applicable unless the company trains/places a GPAI model on the market (assumed not).
6. Art. 4 AI literacy applies to provider and deployers.

Tier: **high-risk (Annex III, point 4(a))**.

## 3. Dates (today 2026-10-01)
- Art. 4, Art. 5: apply now (since 2 Feb 2025).
- Art. 50: applies now (since 2 Aug 2026).
- Chapter III Sections 1-3 for Annex III systems: **2 Dec 2027** (Art. 113(c)(i) as replaced by 2026/1744).
- Legacy rule: high-risk systems placed on the market before the Chapter III date fall under it only after a significant change in design (Art. 111(2) as amended). A January 2027 launch would technically predate 2 Dec 2027. Agent inference: do not rely on this — the classifier will be retrained/updated (likely significant change), customers will demand compliance, and the window is short. Build for compliance at launch. Needs counsel if the company intends to rely on it.

## 4. Obligation register (provider unless noted)
| Obligation | Article | Applies from | Control | Evidence | Status |
|---|---|---|---|---|---|
| AI literacy | Art. 4 as replaced by 2026/1744 | now | Per-feature guide for staff and recruiter onboarding | Doc, training record | Open |
| No prohibited practice | Art. 5(1)(f),(g) | now | Block emotion inference/biometric features; review checklist | Classification note | Open |
| Risk management | Art. 9 | 2 Dec 2027 | Risk register: discriminatory rejection, proxy features, LLM hallucination, prompt injection via CVs | Register, release checklist | Open |
| Data governance, bias | Art. 10(2)(f),(g) as amended; Art. 4a | 2 Dec 2027 | Dataset cards for customer historical hiring data: provenance, original purpose, label bias (past hiring decisions encode bias), representativeness per Member State/language; bias eval by group; special-category data only under Art. 4a(1)(a)-(f) | Dataset cards, bias reports | Open |
| Technical documentation | Art. 11, Annex IV | 2 Dec 2027 | Generated from source: models, versions, training/eval, metrics, oversight design | docs/annex-iv | Open |
| Logging | Art. 12, 19 | 2 Dec 2027 | Per-decision log: job ID, applicant ID, model versions, score, rank, threshold, auto-reject flag, recruiter actions; retain ≥6 months | Log schema test | Open |
| Instructions for use | Art. 13 | 2 Dec 2027 | Deployer docs: purpose, accuracy per group, limits, oversight, log access | Shipped docs | Open |
| Human oversight | Art. 14 | 2 Dec 2027 | **Replace silent auto-reject**: rejected candidates visible and reviewable; recruiter can override/reverse; stop control; show score rationale and confidence; automation-bias warnings. Agent inference: a fixed 50% auto-reject with no human review is hard to reconcile with Art. 14 | UI tests on override/reverse/stop | Open |
| Accuracy, robustness, security | Art. 15 | 2 Dec 2027 | Eval suite in CI incl. group fairness metrics; prompt-injection tests with hostile CV text | Eval reports | Open |
| QMS | Art. 17 as amended | 2 Dec 2027 | Proportionate QMS (SME simplifications if eligible) | QMS doc | Open |
| Conformity, DoC, CE, registration | Arts. 43, 47, 48, 49 | 2 Dec 2027 (agent inference, see timeline note) | Internal control route expected for Annex III point 4 (agent inference; Art. 43 not re-read); EU declaration; EU database registration before placing on market | Declaration, registration ID | Open |
| Post-market monitoring | Art. 72 | 2 Dec 2027 | Drift and per-group outcome monitoring across customers | PMM plan | Open |
| Serious incidents | Art. 73 | 2 Dec 2027 | Incident runbook | Runbook | Open |
| Value chain | Art. 25 | 2 Dec 2027 | Contracts: customers who rebrand or change purpose become providers; LLM vendor information | Contracts | Open |
| Deployer duties (customers) | Art. 26(1),(2),(5),(6),(7),(11); Art. 86 | 2 Dec 2027 | Product features enabling them: overseer assignment, log export, applicant notice template (26(11)), worker-representative notice (26(7)), explanation-on-request endpoint (Art. 86) | Feature tests | Open |
| FRIA | Art. 27 as amended | 2 Dec 2027 | Only for certain deployers (public bodies/public-service providers); provide support pack | FRIA template | Open |

Step 4 (described, not built): tests that every auto-rejected candidate appears in a reviewable queue and can be reinstated; test that the stop control halts scoring; log-field schema test; CI fairness gate failing on group disparity thresholds; prompt-injection regression set; applicant-notice render test; Annex IV doc generation in CI.

## 5. Open questions
- Does the LLM come from a third party API, or is it fine-tuned/trained in-house? (If the company places a GPAI model on the market, Arts. 51-56 apply.)
- Do customers' data processing terms allow reuse of their historical hiring data for training (GDPR, outside this skill), and what special-category or proxy data does it contain?
- Any applicant-facing interaction (chatbot, video, emotion analysis)? Would trigger Art. 50(1) or Art. 5(1)(f).
- Is LLM-generated text shown or published (Art. 50(2))?
- Will the company rely on the Art. 111(2) legacy rule for a January 2027 launch? Counsel needed.
- Is the company an SME/SMC (simplified documentation, QMS)?

## Needs counsel / external
- Art. 111(2) legacy reliance; whether auto-reject satisfies Art. 14; conformity route under Art. 43; Commission Art. 6 guidelines and harmonised standards (external dependencies, not bundled); national employment/works-council law for Art. 26(7).

```json
{"roles": ["provider", "deployer (customer employers)"], "tier": "high-risk", "citations": ["Article 3(3)", "Article 3(4)", "Article 2(1)", "Article 4", "Article 5(1)(f)", "Article 5(1)(g)", "Article 6(2)", "Article 6(3)", "Annex III, point 4(a)", "Article 9", "Article 10(2) as amended by 2026/1744", "Article 4a", "Article 11", "Annex IV", "Article 12", "Article 13", "Article 14", "Article 15", "Article 17", "Article 43", "Article 49", "Article 72", "Article 73", "Article 25", "Article 26(7)", "Article 26(11)", "Article 27", "Article 86", "Article 50", "Article 111(2)", "Article 113(c)(i) as replaced by 2026/1744"], "key_findings": ["High-risk under Article 6(2) and Annex III point 4(a)", "Article 6(3) derogation unavailable: profiling and material influence via auto-reject", "Company is provider; employers are deployers", "High-risk obligations apply from 2 Dec 2027; Art. 4, 5 and 50 apply now (today 2026-10-01)", "January 2027 launch precedes 2 Dec 2027; Art. 111(2) legacy rule should not be relied on without counsel", "Automatic rejection of bottom 50% needs human oversight redesign under Article 14", "Historical hiring training data requires bias examination under Article 10(2)(f)"], "open_questions": ["Is the LLM third-party or trained in-house", "Rights to reuse customer hiring data and its special-category content", "Any applicant-facing interaction or emotion inference", "Will Article 111(2) legacy treatment be relied on", "SME/SMC status"], "files_read": ["skills/eu-ai-act/SKILL.md", "evals/cases/03-cv-screening.md", "references/timeline.md", "references/annexes/iii.md", "references/articles/006.md", "references/builder-playbook.md", "references/articles/005.md", "references/articles/113.md", "references/articles/010.md", "references/articles/004a.md", "references/articles/026.md"]}
```
