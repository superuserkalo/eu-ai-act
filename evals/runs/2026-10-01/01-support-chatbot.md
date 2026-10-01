# EU AI Act assessment: help-centre support chatbot ("Mia")

- Date: 2026-10-01
- Text used: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (bundled official English text)
- This is engineering guidance, not legal advice.

## 1. Facts

| Item | Finding |
|---|---|
| Feature | Help-centre chat widget. Customers type questions; Claude (Anthropic API) generates answers grounded on the company's help articles (retrieval). Streams replies; no human review before display. |
| Intended purpose (Art. 3(12)) | Answer customer support questions about the company's SaaS product. |
| Users / affected persons | EU customers (natural persons) interacting directly with the widget. |
| EU nexus (Art. 2(1)(a)) | Berlin company putting the system into service in the EU for EU users. In scope. |
| Role | **Provider** of the chatbot AI system (it builds the system and puts it into service under its own name and the "Mia" brand; Art. 3(3), 3(11)) and **deployer** (it uses the system under its authority; Art. 3(4)). Not a GPAI model provider: Anthropic places Claude on the market; calling it via API does not make the company a model provider. |
| Model source | Third-party API (Anthropic Claude). No training or fine-tuning stated. |
| Output | Text shown to people in a chat UI. No decisions about the person stated. |
| Launch | September 2026, i.e. after 2 Aug 2026; no legacy transition under Art. 111(4). |

## 2. Classification

1. **Scope/definition.** An LLM-based system inferring answers from input is an AI system (Art. 3(1)). No Art. 2 exclusion applies (commercial, not research, not personal non-professional, not military; Art. 2(12) open-source exception irrelevant).
2. **Prohibited (Art. 5(1)).** None of points (a)-(h), (ba), (bb) match. No subliminal/manipulative intent (a), no exploitation of vulnerabilities (b), no social scoring (c), no criminal risk prediction (d), no face scraping (e), no emotion inference at work/education (f), no biometric categorisation (g), no RBI (h), no intimate imagery or CSAM generation (ba)/(bb) - text-only support bot. Caveat (agent inference): the human-like persona "Mia" plus human-like streaming must not be used deceptively; that is handled by Art. 50(1), not Art. 5.
3. **High-risk.** Art. 6(1)/Annex I: not a safety component of a regulated product. Art. 6(2)/Annex III: customer support is not a listed use case. Not high-risk, **provided** the bot does not evaluate eligibility for essential services, creditworthiness, insurance pricing (Annex III, point 5), employment (point 4), etc.
4. **Transparency (Art. 50).**
   - **Art. 50(1) applies** (provider): system intended to interact directly with natural persons. The "obvious" exception cannot be relied on: a human name, avatar and human-like streaming point the other way. Disclosure required at the latest at first interaction, clear, distinguishable, accessible (Art. 50(5)).
   - **Art. 50(2) applies** (provider): system generates synthetic text. Outputs must be machine-readable marked and detectable. The "assistive function for standard editing" exemption does not fit: answers are generated, not edits of user input (agent inference; RAG grounding does not make it a non-substantial alteration). Since launch is after 2 Aug 2026, the Art. 111(4) 2 Dec 2026 grace period does not apply: applicable now. Note: whether Anthropic's own measures satisfy this for the company's system is not settled by the text; the company as system provider must ensure it.
   - Art. 50(3): no emotion recognition/biometric categorisation (assumed). Art. 50(4): no deep fakes; replies are private support answers, not text published to inform the public on matters of public interest.
5. **GPAI (Arts. 51-56).** Not applicable: the company does not train, modify or place a GPAI model on the market.
6. **AI literacy (Art. 4 as replaced by 2026/1744).** Applies as provider and deployer since 2 Feb 2025.

**Tier: limited risk / transparency obligations (Art. 50(1), 50(2)) + Art. 4.**

## 3. Obligation register

Today: 2026-10-01.

| # | Obligation | Article | Role | Applies from | Control | Evidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | Inform users they interact with an AI | Art. 50(1), 50(5) | Provider | 2 Aug 2026 (Art. 113) - already in force | Persistent "AI assistant" label next to "Mia" name/avatar in header and on each bot message; first-turn notice rendered before the first generated token; accessible (aria-label, screen-reader text, contrast); localised for all supported languages | E2E test: open widget, assert notice visible and in a11y tree before first bot output; snapshot test of every message bubble carrying AI badge | **Gap - likely non-compliant now** (no disclosure stated) |
| 2 | Machine-readable marking of generated text | Art. 50(2); Art. 50(7) as replaced by 2026/1744 | Provider | 2 Aug 2026 - already in force | Mark at container: `ai_generated: true` + model/provenance field in the chat API/SSE payload, `data-ai-generated` attribute/JSON-LD on rendered messages, same flag in transcripts/email exports of the chat | Contract test on API response schema; DOM test on rendered messages; export test that the flag survives transcript/email export | Gap |
| 3 | AI literacy of staff operating the bot | Art. 4 as replaced by 2026/1744 | Provider + deployer | 2 Feb 2025 | Short training for support/product staff on limits, hallucination, escalation; record completion | Training records | Unknown |
| 4 | Keep classification valid | Art. 6(2), Annex III; Art. 5 | Provider | - | Tool/feature gate: block bot from making eligibility, pricing, account-termination or credit decisions; review on any new tool | Code review checklist; test that no decision tools are registered | Recommended |

Recommended (not mandated by the Act for this tier, agent inference): human handoff button, logging of conversations for quality, guardrails against off-topic/harmful output.

## 4. Controls and checks (advisory, no code written)

- **Disclosure component**: header text "Mia - AI assistant" plus first-turn system message "You are chatting with an AI assistant. Answers are generated automatically and may contain errors. [Talk to a human]". Rendered client-side before the stream starts, not generated by the model (so it cannot be omitted). Checks: Playwright test asserting notice visible before first streamed token; axe a11y test; i18n test that each locale has the string; test that the persona prompt cannot claim to be human (eval prompt "are you a human?" expects an AI answer).
- **Marking**: server adds `{"ai_generated": true, "generator": "anthropic/claude", "system": "mia-support"}` to every message object; frontend adds `data-ai-generated="true"`; transcript exports include header/field. Checks: schema test failing if the field is missing; DOM test; export test. Record rationale that container marking is the feasible state of the art for text and revisit when the Art. 50(7) code of practice / implementing act settles.
- **Scope guard**: CI check listing registered tools; fail if a tool tagged as decision-making about persons is added without re-review.

## 5. Open questions

1. Is the "AI" nature already disclosed anywhere (widget, help centre)? If yes and it is clear at first interaction, item 1 may be satisfied; the Mia persona makes the "obvious" exception unlikely either way.
2. Does the bot take actions or decisions about customers (refunds, account suspension, credit/eligibility, pricing)? If it touches Annex III point 5 areas (e.g. creditworthiness, life/health insurance pricing), classification may become high-risk (Chapter III applies to Annex III systems from 2 Dec 2027) - requires re-assessment and counsel.
3. Are customers consumers or only business users? Does not change Art. 50(1) (natural persons are still interacting), noted for completeness.
4. Is any voice, image or sentiment/emotion analysis used? Emotion recognition would trigger Art. 50(3) and check of Art. 5(1)(f).
5. Are bot answers ever published (e.g. auto-generated FAQ pages)? If on matters of public interest, Art. 50(4) second subparagraph could apply; also extends Art. 50(2) marking to those pages.
6. Exact launch date: assumed after 2 Aug 2026 (September 2026), so no Art. 111(4) grace for marking.

## Counsel / external dependencies

- No notified body, conformity assessment or FRIA (Art. 27) needed under current facts.
- External, not bundled: Art. 50(7) code of practice on marking/labelling, Commission guidelines on Art. 50, harmonised standards; GDPR (out of scope of this skill) applies to chat logs.
- Fines context: Art. 50 breaches up to EUR 15 million or 3 % of worldwide turnover, lower for SMEs (Art. 99(4), 99(6)).

```json
{"roles": ["provider", "deployer"], "tier": "limited risk (transparency obligations under Article 50); not prohibited, not high-risk, not GPAI", "citations": ["Article 2(1)(a)", "Article 3(1)", "Article 3(3)", "Article 3(4)", "Article 3(11)", "Article 3(12)", "Article 4 as replaced by 2026/1744", "Article 5(1)", "Article 6(1)", "Article 6(2)", "Annex III", "Article 50(1)", "Article 50(2)", "Article 50(5)", "Article 50(7) as replaced by 2026/1744", "Article 111(4)", "Article 113", "Article 99(4)"], "key_findings": ["Company is provider and deployer of the chatbot; Anthropic is the GPAI model provider, not the company", "No Article 5 prohibited practice and no Annex III high-risk use case", "Article 50(1) disclosure required from 2 Aug 2026; the human-like Mia persona and streaming defeat the 'obvious' exception; currently a gap", "Article 50(2) machine-readable marking of generated text applies now; launch after 2 Aug 2026 so no Article 111(4) grace until 2 Dec 2026", "Article 4 AI literacy applies", "Disclosure must be clear, at first interaction and accessible (Article 50(5)); enforce with E2E and a11y tests"], "open_questions": ["Is AI nature already disclosed at first interaction?", "Does the bot make or influence decisions on refunds, eligibility, credit, insurance or pricing (Annex III point 5)?", "Any emotion recognition or biometric processing?", "Are bot outputs ever published publicly?", "Exact launch date relative to 2 Aug 2026"], "files_read": ["skills/eu-ai-act/SKILL.md", "evals/cases/01-support-chatbot.md", "skills/eu-ai-act/references/timeline.md", "skills/eu-ai-act/references/articles/050.md", "skills/eu-ai-act/references/articles/004.md", "skills/eu-ai-act/references/builder-playbook.md", "skills/eu-ai-act/references/articles/003.md", "skills/eu-ai-act/references/articles/002.md", "skills/eu-ai-act/references/articles/005.md", "skills/eu-ai-act/references/articles/113.md", "skills/eu-ai-act/references/annexes/iii.md"]}
```
