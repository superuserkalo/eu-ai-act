# EU AI Act assessment: consumer-loan credit scoring and fraud flagging

- Date: 2026-10-01
- Text used: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (bundled official English text)
- Scope: advisory. Steps 1, 2, 3 and 5 done. For step 4 I describe the controls and checks instead of writing code.
- This is engineering guidance, not legal advice.

## 1. Facts

| Feature | Intended purpose (Art. 3(12)) | Users / affected | Model source | Output |
|---|---|---|---|---|
| A. Credit scoring | Score how creditworthy natural-person loan applicants are, using their bank transaction data. The score **automatically** decides approval and interest rate. | Run by the fintech itself. Affects consumers in Spain and Portugal. | In-house gradient-boosted model, built by the company's own data team | A decision about a person (approve or reject, and the price) |
| B. Fraud flagging | Flag applications that are likely fraudulent | Run by the fintech itself. Affects applicants. | In-house model | A flag. Whether it blocks or rejects applicants automatically is not known. |

- EU link: the company is established in Spain and serves consumers in Spain and Portugal, so Article 2(1)(a) and (b) apply.
- Roles: for both systems the company is the **provider**, because it develops the system and puts it into service for its own use (Art. 3(3), 3(11)). It is also the **deployer**, because it uses the system under its own authority (Art. 3(4)). No third-party model is involved. Nothing indicates it places a general-purpose AI model on the market.
- Both systems are already in production as of 2026-10-01.

## 2. Classification

### A. Credit scoring: high-risk (Annex III, point 5(b)), with a legacy-system timing question

1. **Scope.** A gradient-boosted model that infers scores from input data meets the AI system definition in Art. 3(1). No Article 2 exclusion applies.
2. **Prohibited practices.** None of the Art. 5(1) points is met on these facts.
   - Art. 5(1)(c), social scoring: credit scoring based on financial data, used for credit, is not a score of "social behaviour" applied in unrelated social contexts. This is agent inference.
   - Art. 5(1)(b), exploiting vulnerabilities: needs checking if pricing targets people in financial distress in a way that distorts their behaviour. Nothing in the facts suggests this.
   - Points (ba) and (bb), which apply from 2 Dec 2026, concern intimate imagery and child sexual abuse material. They are not relevant here.
3. **High-risk.** Annex III, point 5(b) covers AI systems "intended to be used to evaluate the creditworthiness of natural persons or establish their credit score". That is a direct match, so the system is high-risk under Art. 6(2).
   - The Art. 6(3) derogation does not apply. The score decides the outcome automatically, so it materially influences the decision. None of conditions (a) to (d) fits.
   - Scoring individuals from their transaction data is also profiling of natural persons, and under the last subparagraph of Art. 6(3) profiling is always high-risk.
   - Art. 6(1) and Annex I do not apply, because this is not a safety component of a regulated product.
4. **Timing (this decides when the high-risk duties bite).** Chapter III Sections 1 to 3 apply to Annex III systems from **2 Dec 2027** (Art. 113(c)(i) as amended by 2026/1744). Today is 2026-10-01, so the high-risk requirements do not yet apply.
   - Under Art. 111(2) as replaced by 2026/1744, a high-risk system placed on the market or put into service before the Chapter III date is covered only if it undergoes **significant changes in its design** from that date.
   - The model is in production today, so it is a legacy system. If it is not significantly redesigned after 2 Dec 2027, the Chapter III duties would not attach to it.
   - A credit model is usually retrained and re-featured regularly. In practice the company will likely make a significant design change after 2 Dec 2027, and from that point Chapter III applies in full. This is agent inference. Whether routine retraining counts as a "significant change in design" is not defined in the bundled text; compare the Art. 3(23) definition of "substantial modification". **Counsel should decide.**
   - Recommendation: build towards full compliance by 2 Dec 2027 rather than relying on the legacy exemption.
5. **Transparency (Art. 50).** No chatbot, no synthetic content, no emotion recognition and no deep fake are involved, so Art. 50 does not apply. If an AI chat assistant is added to the loan flow, Art. 50(1) applies.
6. **General-purpose AI models.** Not applicable.
7. **AI literacy (Art. 4, as replaced by 2026/1744).** Applies now (from 2 Feb 2025).

### B. Fraud flagging: not high-risk (excluded by the wording of Annex III, point 5(b)); minimal-risk tier

- Annex III, point 5(b) expressly excludes "AI systems used for the purpose of detecting financial fraud". If the fraud model's intended purpose is only to detect fraud, it is not high-risk under Annex III.
- No other Annex III point fits. Point 5(a) concerns public assistance benefits. Points 1 and 6 concern biometrics and law enforcement, and nothing indicates either.
- Art. 5 is not triggered. Art. 50 does not apply. Art. 4 AI literacy applies.
- **The answer changes if the fraud score is fed into the creditworthiness decision or pricing** (for example as a feature, or by rejecting borderline applicants on "risk"). Then it serves the creditworthiness purpose and falls under point 5(b), as part of system A or as a high-risk system of its own. This is agent inference. Keep the purposes separate and document it.
- Because this exclusion is written into Annex III itself, rather than being the Art. 6(3) derogation, the Art. 6(4) documentation and Art. 49(2) registration do not apply. This is agent inference. Still record the intended-purpose reasoning.

## 3. Obligation register

Status key: today is 2026-10-01. "Not yet due" means the obligation binds from the date shown, subject to the Art. 111(2) legacy question above.

| # | Obligation | Article | Role | Applies from | Control | Evidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | AI literacy of staff running and overseeing both models | Art. 4 as replaced by 2026/1744 | Provider + deployer | 2 Feb 2025 (in force) | Internal guide per model covering purpose, limits, failure modes, escalation, and override; added to onboarding | Guide in repo, training records | **Due now**. Gap unknown. |
| 2 | Prohibited-practice check | Art. 5(1) | Provider + deployer | 2 Feb 2025 | Recorded review against each point, especially (b) for pricing aimed at vulnerable or distressed applicants | Classification note | Done in this report. Re-check when pricing logic changes. |
| 3 | Risk management system | Art. 9 | Provider (A) | 2 Dec 2027* | Risk register: discrimination, proxy features in transaction data (for example merchant categories acting as proxies for health or religion), drift, wrongful denials | Risk register, release checklist | Not yet due |
| 4 | Data governance, bias examination | Art. 10 as amended; Art. 4a for special-category data | Provider (A) | 2 Dec 2027* | Dataset cards; bias evaluation across protected groups; Art. 4a conditions before processing special-category data | Dataset cards, fairness eval report in CI | Not yet due |
| 5 | Technical documentation | Art. 11, Annex IV | Provider (A) | 2 Dec 2027* | `docs/annex-iv/` generated from the pipeline: features, model versions, metrics, oversight design, change log. Simplified form if SME or SMC (Art. 11(1) as amended). | Doc kept with the code | Not yet due |
| 6 | Automatic logging; keep logs | Arts. 12, 19, 26(6) | Provider + deployer (A) | 2 Dec 2027* | Per decision: application ID, model version, input feature snapshot hash, score, threshold, decision, price, override flag, overseer ID, timestamp; retention of at least 6 months | Log schema, retention config, test that fails if a required field is missing | Not yet due |
| 7 | Transparency to the deployer (instructions for use) | Art. 13 | Provider (A) | 2 Dec 2027* | Internal versioned instructions: purpose, accuracy, known limits, oversight steps | Versioned doc | Not yet due |
| 8 | Human oversight | Arts. 14, 26(1)-(2) | Provider + deployer (A) | 2 Dec 2027* | Today decisions are fully automatic. Add a review queue for rejections and borderline scores, override and reverse actions, a kill switch that falls back to manual underwriting, and named trained overseers. | E2E tests for the override, reverse and stop paths; an overseer roster | Not yet due. **Design gap.** |
| 9 | Accuracy, robustness, cybersecurity | Art. 15 | Provider (A) | 2 Dec 2027* | Declared metrics with an evaluation gate in CI that blocks deployment on regression; drift monitoring; defences against poisoning and manipulated transaction data | CI gate, eval reports | Not yet due |
| 10 | Quality management system | Art. 17 as amended | Provider (A) | 2 Dec 2027* | Documented design, testing, change-control and incident process. Financial-institution integration with internal-governance rules may apply (check Art. 17(4)). | QMS doc | Not yet due |
| 11 | Conformity assessment, EU declaration, CE marking, registration | Arts. 16, 43, 47, 48, 49; Annex VI | Provider (A) | 2 Dec 2027* (Section 5 nominally from 2 Aug 2026; see the inference note in the timeline) | Internal-control route (Annex VI) for Annex III point 5. Draft the declaration. Register in the EU database before (re)deployment. | Declaration file, registration ID | Not yet due |
| 12 | Post-market monitoring | Art. 72 as amended | Provider (A) | 2 Dec 2027* | Telemetry on approval rates, defaults and group disparities feeding the risk register | Monitoring plan, dashboards | Not yet due |
| 13 | Serious incident reporting | Art. 73 | Provider (A) | 2 Dec 2027* | Incident runbook with the 15 / 10 / 2-day deadlines | Runbook, drill record | Not yet due |
| 14 | Inform applicants they are subject to a high-risk AI system | Art. 26(11) | Deployer (A) | 2 Dec 2027* | Notice in the application flow before submission | UI test that the notice renders on the application page | Not yet due |
| 15 | Fundamental rights impact assessment | Art. 27(1) (explicitly covers Annex III point 5(b)), as amended | Deployer (A) | 2 Dec 2027* | FRIA before deploying; may cross-reference the GDPR DPIA (Art. 27(4) as amended); notify the market surveillance authority (Art. 27(3)) | FRIA document, notification record | Not yet due. **Counsel.** |
| 16 | Right to explanation | Art. 86 | Deployer (A) | 2 Dec 2027* | An explanation endpoint or process giving the AI's role and the main elements of the decision (for example reason codes from feature attributions) | API test that every rejection has retrievable reasons | Not yet due |
| 17 | Fraud model purpose boundary | Annex III, point 5(b) exclusion | Provider (B) | Now (classification) | Written intended purpose; technical separation so the fraud score is not a credit or pricing feature | Test or lint that fails if the fraud score appears in the credit model's feature set or pricing rules | Recommended now |

\* Subject to Art. 111(2) as replaced by 2026/1744: for this legacy system the duties attach only after a significant design change made on or after 2 Dec 2027.

## 4. Controls and checks I would build (described, not implemented)

- **Decision log contract test.** A schema test that fails if any scoring event lacks the model version, input hash, score, decision, price or override fields. Plus a retention configuration of at least 6 months.
- **Human oversight paths.** E2E tests showing that a reviewer can override and reverse a decision, and that the stop switch routes all applications to manual underwriting.
- **Fairness and accuracy gate in CI.** It blocks model promotion when AUC or calibration drops, or when disparity metrics across groups exceed declared thresholds.
- **Feature-set guard.** It fails the build if the fraud score or a special-category proxy is added to the credit model's features without a recorded review.
- **Applicant notice test.** The application flow renders the Art. 26(11) notice. An adverse decision exposes Art. 86 reasons.
- **Significant-change tracker.** Each model release records whether it changes the design, which decides when Art. 111(2) stops protecting the legacy system.

## 5. Open questions that change the answer

1. Does the fraud flag automatically reject applicants, or feed the credit score or price? If yes, system B probably falls under Annex III point 5(b) and is high-risk.
2. Will system A undergo significant design changes on or after 2 Dec 2027? If no, Art. 111(2) keeps Chapter III off it. If yes (likely), full high-risk duties apply from the change.
3. Is the company an SME or SMC? If so, the simplified technical documentation (Art. 11(1) as amended), proportionate QMS, and lower fine caps (Art. 99(6), 99(6a)) apply.
4. Is the company a credit institution or other regulated financial institution? If so, the financial-services integration provisions (for example Arts. 17(4), 26(5)) and the supervisory authority as market surveillance authority affect how the obligations are met. Check the text with counsel.
5. Does the transaction data allow special-category inferences (health, religion)? If so, Art. 10 and Art. 4a conditions apply, plus GDPR, which is outside this skill.

## Items for counsel or external dependencies

- How to read "significant changes in their designs" in Art. 111(2) for a model that is retrained regularly.
- FRIA under Art. 27 and the notification to the market surveillance authority.
- Commission guidelines on Art. 6 high-risk classification (Art. 6(5)) and harmonised standards for Arts. 9 to 15. These are external and not bundled.
- GDPR Art. 22 automated decision-making and consumer-credit law (fully automatic approval and pricing). These are outside this skill but highly relevant.
- Spanish and Portuguese national competent authorities and penalty regimes.

```json
{"roles": ["provider", "deployer"], "tier": "high-risk (Annex III, point 5(b)) for credit scoring, with Chapter III applying from 2 Dec 2027 subject to Art. 111(2) legacy rule; fraud detection not high-risk (excluded in Annex III point 5(b)), minimal risk with Art. 4 literacy", "citations": ["Article 2(1)", "Article 3(1)", "Article 3(3)", "Article 3(4)", "Article 3(11)", "Article 3(23)", "Article 4 as replaced by 2026/1744", "Article 5(1)(b)", "Article 5(1)(c)", "Article 6(2)", "Article 6(3)", "Annex III, point 5(b)", "Article 9", "Article 10", "Article 11", "Annex IV", "Article 12", "Article 13", "Article 14", "Article 15", "Article 17", "Article 19", "Article 26(1)", "Article 26(6)", "Article 26(11)", "Article 27(1)", "Article 27(4) as replaced by 2026/1744", "Article 43", "Article 49", "Article 72", "Article 73", "Article 86", "Article 111(2) as replaced by 2026/1744", "Article 113(c)(i) as amended by 2026/1744"], "key_findings": ["Credit scoring is high-risk under Article 6(2) and Annex III point 5(b); the Article 6(3) derogation is unavailable because it decides outcomes automatically and profiles natural persons", "Fraud detection is excluded from Annex III point 5(b) as long as it is not used for creditworthiness or pricing", "Company is both provider and deployer of both in-house systems", "High-risk obligations apply from 2 Dec 2027; as a system already in production, Article 111(2) applies them only after a significant design change, which regular retraining likely triggers", "Deployer must do a FRIA (Article 27(1) names point 5(b)), inform applicants (Article 26(11)) and give explanations (Article 86)", "Fully automated decisions need a human oversight design (Article 14) before Chapter III applies", "Article 4 AI literacy applies now; Article 50 does not apply"], "open_questions": ["Does the fraud flag feed credit decisions or pricing, or auto-reject?", "Will the credit model be significantly changed on or after 2 Dec 2027?", "Is the company an SME or SMC?", "Is it a regulated credit or financial institution?", "Does transaction data enable special-category inferences?"], "files_read": ["SKILL.md", "references/timeline.md", "references/annexes/iii.md", "references/articles/111.md", "references/articles/006.md", "references/builder-playbook.md", "references/articles/003.md", "references/articles/027.md", "references/articles/004.md", "references/articles/005.md", "references/articles/086.md", "references/articles/026.md"]}
```
