# EU AI Act check: US-only maintenance-ticket classifier

- Date: 2026-10-01
- Text used: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (bundled official text)
- This is engineering guidance, not legal advice.

## 1. Facts
- Feature: an internal LLM tool that sorts US truck-maintenance tickets into categories. Intended purpose (Article 3(12)): internal operations triage.
- Users and affected people: the company's own US staff. Data and outputs stay in the US.
- Role: the company built the tool and uses it itself, so it would be provider (putting into service for own use, Article 3(11)) and deployer. Under Article 2, though, those roles only matter if the system has an EU link.
- Model source: an LLM, assumed to be a third-party or open-weight model the company calls but does not place on the market. That makes the company a downstream user, not a GPAI model provider.
- EU nexus: none. The company has no EU customers, offices, or operations, and outputs are not used in the EU.

## 2. Classification
**Tier: out of scope. Article 2(1) does not apply.**
- Article 2(1)(a): not placed on the market or put into service in the Union.
- Article 2(1)(b): the deployer is not established or located in the Union.
- Article 2(1)(c): the provider/deployer is in a third country, and no output is used in the Union.
- Article 2(1)(d) to (g): no importer, distributor, EU product manufacturer, or authorised representative is involved, and no affected persons are located in the Union.
- The 2026/1744 amendments to Article 2 (paragraphs 2, 7, and 13) do not widen territorial scope.

As a result, no Article 4 AI-literacy, Article 5, Article 6, or Article 50 obligations attach. For completeness, even if the tool were in scope (my inference): sorting equipment tickets is not an Annex III use case and is not a prohibited practice under Article 5(1). Staff using an internal tool would at most raise Article 50(1) chatbot disclosure, and Article 4 literacy would apply. That would mean minimal risk.

## 3. Obligation register
| Obligation | Article | Date | Control | Evidence | Status |
|---|---|---|---|---|---|
| None (out of scope) | Article 2(1) | n/a | Scope tripwires below | Record of this scoping decision | Not applicable |

## 4. Controls I would build (advisory, no code)
Their job is to catch the moment the facts change:
- A data-residency check: a CI or config test that fails if the tool's hosting region, data store, or output sinks are outside the US.
- An access guard: SSO restricted to the US workforce, with alerts on logins from EU IP addresses or by EU-based staff.
- A scope-review trigger in the change process: re-run this assessment before the tool is offered to anyone else, before an EU entity, customer, or fleet is added, before outputs are sent to EU parties, and before the purpose changes to decisions about workers (Annex III, point 4 would then need checking).
- A short scoping record kept in the repo with today's date.

## 5. Open questions and assumptions
- Assumption: no ticket outputs reach EU parties, such as EU parts suppliers or an EU parent company. If they do, Article 2(1)(c) could bring the tool into scope. It would then likely be minimal risk with Article 4 literacy, plus Article 50(1) only if people interact with it directly.
- Assumption: the company does not distribute or sell the tool or a model to anyone. If it did and that reached the EU, Article 2(1)(a) would apply.
- Assumption: the tool does not evaluate drivers or mechanics. If it were used to monitor or evaluate workers and became EU-linked, Annex III, point 4(b) would need assessment.
- No counsel or notified body is needed on these facts. Only US law and other non-EU laws would govern, and they are outside this skill.

```json
{"roles": ["none under the EU AI Act (would be provider and deployer if an EU nexus existed)"], "tier": "out of scope (Article 2(1) not met)", "citations": ["Article 2(1)(a)", "Article 2(1)(b)", "Article 2(1)(c)", "Article 3(11)", "Article 3(12)", "Article 4", "Article 50(1)", "Annex III, point 4"], "key_findings": ["No EU nexus under any point of Article 2(1), so the AI Act does not apply", "Even if it were in scope, ticket classification would be minimal risk (inference)", "Add residency and access tripwires and re-assess if EU users, outputs, or entities appear"], "open_questions": ["Are any outputs shared with EU parties?", "Is the tool or model ever supplied to third parties?", "Is the tool ever used to evaluate workers?"], "files_read": ["skills/eu-ai-act/SKILL.md", "skills/eu-ai-act/references/articles/002.md", "skills/eu-ai-act/references/timeline.md", "evals/cases/08-no-eu-nexus.md"]}
```
