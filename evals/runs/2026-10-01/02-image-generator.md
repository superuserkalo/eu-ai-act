# EU AI Act assessment: consumer image and video generator app

- Date: 2026-10-01
- Text used: Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (bundled skill references)
- Mode: advisory. No repository was available. The case text supplies the facts. Step 4 describes the controls and checks rather than code.
- This is engineering guidance, not legal advice.

## 1. Facts

| Item | Finding |
|---|---|
| System | Consumer mobile app. It turns text prompts and uploaded selfies into stylised images and short videos. It adds an in-house face-swap step on top of a third-party diffusion model API. |
| Intended purpose (Art. 3(12)) | Generating stylised images and video of the user from prompts and selfies, for download and sharing. |
| Users / affected persons | Consumers, plus anyone whose face is uploaded (the user or third parties) and anyone who later sees the shared output. |
| EU nexus (Art. 2(1)) | A Dutch company places the app on the market through EU app stores. Clearly in scope. |
| Role | **Provider** of the AI system (Art. 3(3)). The startup develops the app, including its own face-swap step, and places it on the market under its own name. Calling a third-party diffusion model through an API does **not** make it a GPAI model provider. The API vendor is the model provider. The startup is a deployer only if it uses the system itself under its own authority, for example in marketing material (Art. 3(4)). |
| End users | Consumers using the app for personal, non-professional purposes are not deployers (Art. 3(4)), and Art. 2(10) excludes their deployer obligations. |
| Models | (1) A third-party diffusion model via API, placed on the market by the vendor. (2) The startup's own face-swap component, whose origin (in-house, open-weight, or fine-tuned) is not stated. |
| Outputs | Synthetic images and video that depict real, identifiable people (from selfies). |
| Placed on market | March 2026, before 2 Aug 2026. |
| Existing safeguard | A basic NSFW filter on **prompts only**. It does not check uploaded images or generated outputs. |

## 2. Classification

**Feature: text/selfie to stylised image and video with face-swap. Role: provider.**

1. **Scope.** The system infers from inputs how to generate content, so it meets the AI system definition (Art. 3(1)). No Art. 2 exclusion applies to the provider. Art. 2(10) only relieves personal-use consumers of deployer duties.
2. **Prohibited (Art. 5). This is the main risk.**
   - **Art. 5(1)(ba)**, inserted by 2026/1744, prohibits placing on the market an AI system that generates or manipulates realistic images or video of an identifiable natural person's intimate parts or sexually explicit activity without that person's explicit consent. **Art. 5(1)(bb)** prohibits the same for child sexual abuse material. Both apply from **2 Dec 2026** (Art. 113(a) as amended), 62 days from today (2026-10-01).
   - Under **Art. 5(1a)(a)**, a provider is caught if (i) such generation is the intended purpose, which it is not here, or (ii) the system's capabilities and user-facing functions make it a "reasonably foreseeable and reproducible outcome" and the system lacks "reasonable and adequate technical safety measures ... to reliably prevent" it, "taking into account reasonably foreseeable misuse", and to correct reported misuse.
   - Selfie upload plus face-swap plus video, with a filter on prompts only, makes non-consensual intimate imagery of an identifiable person (including of a third party whose photo is uploaded as a "selfie", or of a minor) reasonably foreseeable. Prompt-only filtering is easy to bypass with euphemisms, image inputs, or non-English prompts. *Agent inference:* as built, the app is unlikely to meet the "reasonable and adequate safeguards" condition. If it is unchanged on 2 Dec 2026, placing it on the market would fall under the Art. 5(1)(ba)/(bb) prohibition. This cannot be fixed with a label. It needs real preventive safeguards before that date. **Counsel review required.**
   - Art. 5(1b): stylisation that does not increase exposure of intimate parts or change sexual activity in the input is not "manipulation". That helps for ordinary stylisation but does not cover generating new content.
   - Other points (a) to (h): not triggered on the facts. No manipulative techniques, social scoring, risk assessment, facial-recognition database scraping, emotion inference, biometric categorisation, or RBI. *Assumption:* the face-swap only maps facial features and does not identify or categorise people. If uploaded faces were kept to build a face database through untargeted scraping, Art. 5(1)(e) would need review.
3. **High-risk (Art. 6).** Not a safety component of an Annex I product. No Annex III use case: consumer creative generation is not biometric identification, categorisation, or emotion recognition (Annex III point 1), and no other listed area applies. **Not high-risk.** *Agent inference:* face-swap processes biometric-like data but does not identify persons, so Annex III point 1 does not match. If it were used for identity verification, reassess.
4. **Transparency (Art. 50). Applies.**
   - **Art. 50(2) (provider):** outputs must be marked in a machine-readable format and be detectable as artificially generated or manipulated. The "assistive standard editing" exemption does not apply because the outputs substantially alter the input. Art. 50 has applied since 2 Aug 2026, but the app was placed on the market in March 2026, so **Art. 111(4)** (inserted by 2026/1744) gives a deadline of **2 Dec 2026** (today 2026-10-01). Any new system version that counts as newly placed after 2 Aug 2026 may not benefit. Treat it as due now for new features (agent inference).
   - **Art. 50(4) (deployer, deep fakes):** face-swapped realistic images or video of real people can be deep fakes (Art. 3(60)). Personal-use consumers are not bound (Art. 2(10)). The startup is bound whenever it publishes such content itself, for example app-store screenshots or social ads using real faces. *Agent inference / best practice:* also add a visible label on exports so downstream professional deployers can comply. The visible label is not strictly required of the provider.
   - **Art. 50(1):** not triggered unless the app has a conversational assistant. Art. 50(3): not triggered unless emotion recognition or biometric categorisation is added.
   - **Art. 50(5):** any disclosure must be clear, distinguishable, given no later than first exposure, and accessible.
5. **GPAI (Art. 51 to 56).** Not applicable to the startup, which does not train or place a GPAI model on the market. *Open:* if the face-swap model is a substantially modified GPAI model, revisit.
6. **AI literacy (Art. 4 as replaced by 2026/1744).** Applies from 2 Feb 2025 to the startup's staff who operate the system.

**Tier: limited risk (Art. 50 transparency), with an Art. 5(1)(ba)/(bb) prohibition risk that must be fixed before 2 Dec 2026. Not high-risk. Not GPAI.**

## 3. Obligation register (today 2026-10-01)

| # | Obligation | Article | Role | Applies from | Control | Evidence | Status |
|---|---|---|---|---|---|---|---|
| 1 | Prevent non-consensual intimate imagery of identifiable persons | Art. 5(1)(ba), 5(1a)(a)(ii), 5(1b) as inserted by 2026/1744 | Provider | 2 Dec 2026 | Multi-layer safeguards (see section 4) | Red-team suite, filter tests, misuse log | **Gap: prompt-only filter** |
| 2 | Prevent CSAM generation | Art. 5(1)(bb), 5(1a) | Provider | 2 Dec 2026 | Minor detection on inputs, CSAM hash matching, output classifier, hard block | Tests, reporting runbook | **Gap** |
| 3 | Correct observed/reported misuse | Art. 5(1a)(a)(ii) | Provider | 2 Dec 2026 | In-app report, takedown, account ban, filter update loop | Runbook, SLA metrics | Gap |
| 4 | Machine-readable marking of image/video outputs | Art. 50(2); Art. 111(4); Art. 50(7) as replaced by 2026/1744 | Provider | 2 Dec 2026 (legacy); now for newly placed versions | C2PA manifest + invisible watermark + metadata on every export | Export tests, detection tool | Not stated, assume gap |
| 5 | Deep-fake disclosure when the startup publishes real-person content | Art. 50(4), Art. 3(60) | Deployer (own marketing) | 2 Aug 2026 | Visible "AI-generated" label in marketing assets | Asset checklist | Open |
| 6 | Disclosure form and timing | Art. 50(5) | Provider/Deployer | 2 Aug 2026 | Clear, accessible labels at first exposure | Accessibility test | Open |
| 7 | AI literacy | Art. 4 as replaced by 2026/1744 | Provider | 2 Feb 2025 | Internal guide on model limits, misuse patterns, moderation escalation | Doc + training record | Unknown |

## 4. Controls and checks to build (advisory, no code)

**Art. 5 safeguards (priority, before 2 Dec 2026):**
- *Input image checks:* run an age-estimation/minor classifier and a nudity classifier on uploaded selfies. Block if a minor or nudity is detected. Hash-match against known CSAM lists through an established provider. Check: a test fixture set of benign, minor-like and nude inputs, with assertions that the pipeline blocks.
- *Consent / identity binding:* require a liveness check so the face being swapped belongs to the account holder, or an explicit consent flow for third-party faces. Check: a test that a face not matching the liveness capture is rejected.
- *Prompt filter upgrade:* use a multilingual semantic classifier instead of a keyword list, plus jailbreak red-team prompts. Check: a CI red-team suite with a target block rate. The build fails on regression.
- *Output filter:* run a nudity/sexual-content classifier on every generated frame of images and video before delivery. Block and log. Check: an integration test feeding sexual outputs from a stub model and asserting nothing is delivered.
- *Vendor settings:* enable the diffusion API's safety filters and record that in config. Check: a test asserting the safety flag in outbound requests.
- *Misuse correction:* in-app report button, takedown within a defined SLA, account bans, and feeding confirmed bypasses back into the red-team set. Check: an end-to-end test of report to removal.

**Art. 50(2) marking:**
- Embed a C2PA manifest stating that the content was AI-generated (with the generator and face-swap steps), add an invisible robust watermark, and write IPTC/XMP `DigitalSourceType=trainedAlgorithmicMedia`. Apply to every export path: download, share sheet, and video encode. Check: per output type, a test asserting the manifest validates and the watermark is detectable after the app's own re-encoding and resizing. Record why the method is the feasible state of the art and revisit when the Art. 50(7) code of practice or implementing act settles.
- Optional visible corner label on exports to support downstream Art. 50(4) compliance. Snapshot test.

**Art. 4:** maintain a literacy doc in the repo and record onboarding completion.

## 5. Open questions

1. Can users upload faces other than their own? This decides how foreseeable non-consensual imagery is (Art. 5(1a)(a)(ii)). If liveness binding is enforced, the risk drops sharply.
2. Is there any age gate? Are minors allowed as users? This bears on Art. 5(1)(bb) and the Art. 5(1)(b) vulnerability analysis.
3. What safety filtering does the third-party diffusion API apply to outputs, and is it enabled?
4. Origin of the face-swap model (in-house, open-weight, fine-tuned GPAI?). If it is a substantially modified GPAI model, Arts. 51 to 56 may apply.
5. Will a significant new version be released after 2 Aug 2026? If so, Art. 111(4)'s grace period may not cover it, and Art. 50(2) applies immediately (agent inference).
6. Does the startup publish user or demo real-person outputs in marketing? If so, Art. 50(4) applies to it as deployer.
7. Are uploaded faces retained or used for training? If so, check the Art. 5(1)(e) database question. GDPR is out of scope here.

## Items for counsel

- Whether the planned safeguards are "reasonable and adequate" under Art. 5(1a)(a)(ii) before 2 Dec 2026. This is a prohibited-practice edge case. Penalties under Art. 99 are at their highest for Art. 5.
- The scope of Art. 111(4) for versions released after 2 Aug 2026.
- External dependencies, not bundled: the Art. 50(7) code of practice on marking and labelling, any Commission guidelines on Art. 5(1)(ba)/(bb), and C2PA/watermarking standards. Do not rely on them from memory.

```json
{"roles": ["provider", "deployer (only for its own marketing use of outputs)"], "tier": "limited risk (Article 50 transparency) with Article 5(1)(ba)/(bb) prohibited-practice risk from 2 Dec 2026; not high-risk; not GPAI", "citations": ["Article 2(1)", "Article 2(10)", "Article 3(1)", "Article 3(3)", "Article 3(4)", "Article 3(12)", "Article 3(60)", "Article 4 as replaced by 2026/1744", "Article 5(1)(ba) as inserted by 2026/1744", "Article 5(1)(bb) as inserted by 2026/1744", "Article 5(1a)(a)(ii) as inserted by 2026/1744", "Article 5(1b) as inserted by 2026/1744", "Article 6", "Annex III, point 1", "Article 50(2)", "Article 50(4)", "Article 50(5)", "Article 50(7) as replaced by 2026/1744", "Article 111(4) as inserted by 2026/1744", "Article 113(a) as amended by 2026/1744", "Article 99"], "key_findings": ["Startup is provider of the AI system; calling a third-party diffusion API does not make it a GPAI model provider", "Selfie face-swap with only a prompt NSFW filter makes non-consensual intimate imagery and CSAM reasonably foreseeable; without input, consent and output safeguards it risks the Article 5(1)(ba)/(bb) prohibition from 2 Dec 2026", "Article 50(2) machine-readable marking (C2PA, watermark, metadata) of all image/video outputs required; legacy system placed March 2026 has until 2 Dec 2026 under Article 111(4)", "Consumers using it for personal purposes are not deployers (Article 2(10)); Article 50(4) deep-fake labelling binds the startup only for its own publication", "Not high-risk: no Annex I product or Annex III use case", "Article 4 AI literacy applies since 2 Feb 2025"], "open_questions": ["Can users upload faces other than their own; is liveness/consent enforced?", "Is there an age gate and are minors users?", "What output safety filtering does the diffusion API apply and is it enabled?", "Origin of the face-swap model and whether it is a modified GPAI model", "Will a significant new version ship after 2 Aug 2026, affecting Article 111(4) grace?", "Does the startup publish real-person outputs in marketing?", "Are uploaded faces retained or used for training?"], "files_read": ["skills/eu-ai-act/SKILL.md", "evals/cases/02-image-generator.md", "skills/eu-ai-act/references/timeline.md", "skills/eu-ai-act/references/builder-playbook.md", "skills/eu-ai-act/references/articles/050.md", "skills/eu-ai-act/references/articles/005.md", "skills/eu-ai-act/references/articles/111.md", "skills/eu-ai-act/references/articles/003.md", "skills/eu-ai-act/references/articles/004.md", "skills/eu-ai-act/references/articles/002.md"]}
```
