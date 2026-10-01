# EU AI Act assessment: internal meeting summarizer

Date: 2026-10-01. Text: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744. This is engineering guidance, not legal advice.

## 1. Facts

- Feature: nightly batch job sends internal meeting transcripts to a third-party LLM API, stores summaries in the internal wiki for staff.
- Intended purpose (Article 3(12)): summarising internal meetings for staff reference. Not used to evaluate employees; not published outside the company; no chat interface.
- EU nexus: French company, used in France (Article 2(1)).
- Model source: third-party LLM via API. The consultancy does not place a model on the market, so it is not a GPAI model provider.
- Roles: built by the in-house platform team and used internally. Putting into service includes supply "for own use" (Article 3(11)), so the consultancy is **provider** (Article 3(3)) and **deployer** (Article 3(4)) of the AI system.
- Output: text summaries read by staff; no decisions about people.

## 2. Classification

| Tier | Result | Reason |
|---|---|---|
| Scope | In scope | LLM summarisation infers outputs (content) from input: AI system under Article 3(1). No Article 2 exclusion (professional use, not research/military/personal). |
| Prohibited (Article 5(1)) | Not applicable | Summarisation of meetings matches no point of Article 5(1), including (ba) and (bb). Agent inference: if transcripts were used to infer emotions of staff, Article 5(1)(f) (emotion recognition in the workplace) would need review; nothing in the facts suggests this. |
| High-risk | Not high-risk | No Annex I product. Annex III, point 4(b) (monitoring and evaluating performance and behaviour of workers) does not apply because summaries are not used to evaluate employees. This depends on that fact staying true. |
| Transparency (Article 50) | Article 50(2) likely applies as provider; 50(1), 50(3), 50(4) do not | 50(1): no direct interaction with natural persons (batch job). 50(2): the system generates synthetic text; outputs should be machine-readable marked unless the exception for systems that "do not substantially alter the input data ... or the semantics thereof" applies. A summary condenses but should preserve semantics; whether that exception covers abstractive summaries is unclear (agent inference; counsel / Commission code of practice under Article 50(7) as replaced by 2026/1744). 50(3): no emotion recognition/biometric categorisation. 50(4) second subparagraph: text is not published to inform the public on matters of public interest. |
| GPAI (Articles 51-56) | Not applicable | Only calls a third-party model. |
| AI literacy | Applies | Article 4 (as replaced by 2026/1744) to provider and deployer. |

## 3. Obligation register

| Obligation | Article | Role | Applies from (today 2026-10-01) | Control | Evidence | Status |
|---|---|---|---|---|---|---|
| AI literacy measures for staff operating and using the system | Article 4 as replaced by 2026/1744 | Provider, deployer | 2 Feb 2025 (already applies) | Short guidance for platform team and wiki readers: summaries are AI-generated, may omit or misstate content, check the transcript for decisions | Training/guidance page, attendance or acknowledgement record | Open |
| Machine-readable marking of AI-generated text | Article 50(2); Article 111(4) inserted by 2026/1744 | Provider | 2 Aug 2026 if put into service on/after that date (already applies); 2 Dec 2026 if put into service before 2 Aug 2026 | Write wiki pages with structured metadata (e.g. `ai_generated: true`, model id, generation timestamp, source transcript id) plus a visible "AI-generated summary" banner | Test that every page the job writes carries the metadata field and banner | Open (recommended even if the 50(2) exception applies) |
| Keep purpose bounded: no employee evaluation | Annex III point 4(b), Article 6(2) (avoidance) | Provider, deployer | High-risk duties from 2 Dec 2027 | Written intended purpose; wiki access policy; no per-person aggregation or scoring features | Documented intended purpose; review gate for new uses | Open |

## 4. Controls and checks I would build (advisory, no code written)

- In the batch job's write step, attach metadata `ai_generated=true`, `model`, `generated_at`, `source_transcript_id` to each wiki page and prepend a visible label. Unit test: the page-builder output always contains the field and label; integration test against a wiki sandbox that fails if missing.
- Log each run (transcript id, model, timestamp, page id) for traceability. Not mandated for non-high-risk systems; good practice.
- Purpose guard: a README/intended-purpose statement and a code-review checklist item rejecting features that score, rank, or profile individual employees (would trigger Annex III point 4(b)).
- AI literacy: a short guidance page linked from every summary.

## 5. Open questions

1. When was the system put into service? Before 2 Aug 2026 -> Article 50(2) marking due 2 Dec 2026 (Article 111(4)); on/after -> already due.
2. Does the Article 50(2) exception ("do not substantially alter ... semantics") cover these summaries? If yes, marking is not legally required but still recommended; if no, it is required.
3. Will summaries ever be used, even informally, to assess staff performance or behaviour? If yes -> high-risk under Article 6(2), Annex III point 4(b), Chapter III Sections 1-3 from 2 Dec 2027, plus deployer duties under Article 26.
4. Any emotion/sentiment analysis of participants? If yes -> check Article 5(1)(f) immediately.
5. Are external parties (clients) in the meetings, and could summaries be shared with them? Does not change the tier unless published to the public on matters of public interest (Article 50(4)).

## Items for counsel

- Scope of the Article 50(2) "no substantial alteration" exception for summaries; Commission code of practice/implementing act under Article 50(7) (external dependency, not bundled).
- GDPR and works-council issues for processing employee transcripts are outside this skill.

```json
{"roles": ["provider", "deployer"], "tier": "minimal risk with Article 50(2) transparency (machine-readable marking of AI-generated text, subject to exception); not prohibited, not high-risk", "citations": ["Article 2(1)", "Article 3(1)", "Article 3(3)", "Article 3(4)", "Article 3(11)", "Article 3(12)", "Article 4 as replaced by 2026/1744", "Article 5(1)", "Article 5(1)(f)", "Article 6(2)", "Annex III, point 4(b)", "Article 50(1)", "Article 50(2)", "Article 50(3)", "Article 50(4)", "Article 50(7) as replaced by 2026/1744", "Article 111(4) inserted by 2026/1744", "Article 113"], "key_findings": ["Consultancy is provider and deployer because it built the system for own use (Article 3(11)); not a GPAI model provider", "Not prohibited and not high-risk because summaries are not used to evaluate employees (Annex III point 4(b))", "Article 50(2) machine-readable marking likely applies to generated summaries, already from 2 Aug 2026 or by 2 Dec 2026 under Article 111(4) if put into service earlier; exception for non-substantial alteration is uncertain", "Article 50(1) and 50(4) do not apply: no direct interaction, not published to the public", "Article 4 AI literacy applies now"], "open_questions": ["Date the system was put into service", "Whether Article 50(2) exception for non-substantial alteration covers summaries", "Whether summaries will ever be used to evaluate staff", "Whether any emotion/sentiment analysis is performed", "Whether summaries are shared outside the company"], "files_read": ["skills/eu-ai-act/SKILL.md", "skills/eu-ai-act/references/timeline.md", "skills/eu-ai-act/references/articles/050.md", "skills/eu-ai-act/references/articles/004.md", "skills/eu-ai-act/references/articles/003.md", "skills/eu-ai-act/references/annexes/iii.md", "evals/cases/06-internal-summarizer.md"]}
```
