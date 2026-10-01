# Evals

Scenario tests for the skill. Each case in `cases/` is given to a fresh agent
that has only `skills/eu-ai-act/` and today's date, with no web access and no
view of `expected.json`. Its report goes to `runs/<date>/<case>.md`, ending in
a JSON block. A human or agent grades it against `expected.json`: roles, tier,
`must_cite`, `must_not`, and `key_points`.

Rerun after any change to SKILL.md, the playbook, the timeline, or the bundled
text, and add a case for every real-world mistake found.

## 2026-10-01 results

| Case | Tier expected | Result | Notes |
|---|---|---|---|
| 01 support chatbot | transparency | Pass | Persona defeats the "obvious" exception; no 2 Dec 2026 grace for a post-August launch |
| 02 image generator | transparency + prohibition risk | Pass | Also found Art. 2(10): private users are not deployers |
| 03 CV screening | high-risk | Pass | Also found the Art. 111(2) legacy-rule question for a pre-Dec-2027 launch and sent it to counsel |
| 04 credit scoring | high-risk | Pass | Fraud model carved out; impact assessment, Art. 86 explanation, legacy rule |
| 05 workplace emotion | prohibited | Pass | Declined the integration |
| 06 internal summarizer | minimal + Art. 50(2) | Pass | Answer key was wrong; agent correctly applied Art. 50(2) to an own-use system |
| 07 open-weight fine-tune | GPAI model | Pass | Weights are not an AI system, so Art. 2(12) does not apply; flagged the unbundled modification threshold |
| 08 no EU nexus | out of scope | Pass | No invented obligations |

Each run read 3 to 15 reference files (about 50k to 65k tokens in total per agent).

Skill change from this run: the playbook now says Art. 50(2) has no
internal-use exception.

Not yet tested: Annex I product safety components, public-sector deployers,
importers and distributors, systemic-risk models, and real code repositories
rather than written briefs.
