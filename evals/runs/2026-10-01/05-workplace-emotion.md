# EU AI Act assessment: call-centre emotion monitoring

Date: 2026-10-01. Text used: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. This is engineering guidance, not legal advice.

## 1. Facts

- System: a vendor tool that analyses call-centre agents' voices in real time to infer stress, frustration and boredom. It shows supervisors a live mood dashboard for each agent, used for coaching and performance reviews.
- Intended purpose (Article 3(12)), as the deployer would use it: infer employees' emotions at work to inform coaching and performance evaluation.
- EU nexus: the system is used in Dublin, Ireland (Article 2(1)(b)).
- Roles: the Irish BPO is a **deployer** (Article 3(4)). The vendor is the **provider** (Article 3(3)). If the BPO put the tool into service under its own name or substantially modified it, Article 25 could make it a provider as well. On the facts given, it does not.
- Model: a third-party vendor API. The BPO trains no model, so the GPAI rules do not apply to it.
- Output: inferred emotional states about identifiable workers, shown to supervisors and used in decisions about them.
- Missing facts: none that change the outcome (see open questions).

## 2. Classification

**Tier: prohibited. Article 5(1)(f).**

- Scope: the tool infers emotions from voice, so it is an AI system (Article 3(1)). Voice features are behavioural or physiological characteristics, which makes them biometric data (Article 3(34)). That makes the tool an emotion recognition system (Article 3(39)). No Article 2 exclusion applies.
- Article 5(1)(f) prohibits "the use of AI systems to infer emotions of a natural person in the areas of workplace", except where the system is intended for medical or safety reasons. This tool infers employees' emotions at work for coaching and performance reviews. Those are neither medical nor safety reasons. The prohibition covers use, so it binds the BPO as deployer as well as the vendor.
- Application date: Article 5 has applied since 2 Feb 2025 (Article 113(a)), so it applies today, 2026-10-01.
- Penalty: fines of up to EUR 35 million or 7% of worldwide annual turnover, whichever is higher (Article 99(3)).
- Under the skill rules, a prohibited practice cannot be engineered into compliance. The analysis stops here. I did not complete high-risk or transparency mapping for the system as specified. For context only: if the practice were not prohibited, it would fall under Annex III, point 4(b), which covers AI used to monitor and evaluate workers' performance and behaviour. Article 50(3) deployer notice would also apply to an emotion recognition system. Neither makes the use lawful.

## 3 and 4. Obligations and controls

The integration should not be built. Requested work: **declined.**

Controls I would put in place instead:

1. **Block the integration.** Do not wire the vendor's emotion endpoint into the dashboard. If the vendor SDK is already present, add a CI check (a grep or an import-lint rule) that fails the build on any call to the emotion or mood endpoints.
2. **Feature flag held off.** If the vendor bundles other features, such as transcription or QA scoring without emotion inference, keep the emotion module disabled by configuration. Add a test that asserts the API is called without emotion or sentiment-of-speaker parameters and that responses contain no affect fields. Ingestion should strip any affect fields, and a test should cover that.
3. **No data retention.** Make sure no historic mood data from pilots feeds performance reviews. Delete it, and let counsel decide what to do about any pilot use that has already happened.
4. **Article 4 AI literacy** (applies from 2 Feb 2025): brief supervisors and procurement on why workplace emotion inference is prohibited, so the tool is not reintroduced later.

Lawful alternatives to evaluate separately: call-level, non-biometric QA (for example, scoring transcripts against a script) or customer-side analytics. These need their own classification. Worker monitoring and evaluation would likely still be high-risk under Annex III, point 4(b), with deployer duties under Article 26 from 2 Dec 2027 (agent inference; check the timeline before relying on it).

## 5. Obligation register

| Obligation | Article | Role | Applies from | Control | Evidence | Status |
|---|---|---|---|---|---|---|
| Do not use workplace emotion recognition | Article 5(1)(f) | Deployer | 2 Feb 2025 | Do not integrate; CI block; strip affect fields | CI rule and tests | Open (recommend not to proceed) |
| AI literacy | Article 4 | Deployer | 2 Feb 2025 | Supervisor and procurement briefing | Training record | Open |

## Open questions

- Is any part of the stated purpose genuinely medical or safety-related, for example detecting acute distress for occupational health? A real safety purpose might fall under the 5(1)(f) exception, but coaching and performance review would not. This needs counsel, and the Commission's guidelines on prohibited practices (an external dependency, not bundled) should be checked.
- Has the tool already been piloted? Past use since 2 Feb 2025 creates exposure.
- Does the vendor offer non-emotion features the BPO wants? Those need a separate classification.

## Needs counsel

- Any argument for the medical or safety exception under Article 5(1)(f).
- Handling of any past use, and vendor contract termination.
- GDPR (biometric data, employee monitoring) and Irish employment law fall outside this skill.

```json
{"roles": ["deployer"], "tier": "prohibited", "citations": ["Article 5(1)(f)", "Article 3(39)", "Article 3(34)", "Article 3(4)", "Article 2(1)", "Article 113(a)", "Article 99(3)", "Article 4", "Annex III, point 4(b)", "Article 50(3)", "Article 25"], "key_findings": ["Real-time voice emotion inference of call-centre agents for coaching and performance reviews is a prohibited practice under Article 5(1)(f)", "Prohibition applies to the deployer's use and has applied since 2 Feb 2025", "Medical/safety exception does not cover coaching or performance review", "Recommend declining the integration; fines up to EUR 35m or 7% turnover under Article 99(3)"], "open_questions": ["Is there a genuine medical or safety purpose?", "Has the tool already been used or piloted?", "Are non-emotion vendor features wanted, requiring separate classification?"], "files_read": ["SKILL.md", "references/timeline.md", "references/articles/005.md", "references/articles/003.md", "references/articles/099.md"]}
```
