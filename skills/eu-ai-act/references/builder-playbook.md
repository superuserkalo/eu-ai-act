# Builder playbook

Plugin-authored routing from obligations to engineering controls. Every control below is agent guidance derived from the cited Article. Read the Article file, `articles/NNN.md`, before implementing. Amended Articles open with the 2026 amending text. The Act states outcomes, not implementations. Where a harmonised standard, code of practice, or Commission guideline exists, it may define what counts as adequate. Those are not bundled.

## Every provider and deployer

| Obligation | Article | Control | Evidence |
|---|---|---|---|
| AI literacy for staff operating AI systems | Art. 4 as replaced by 2026/1744 | Short internal guide per AI feature: what it does, limits, failure modes, escalation path. Onboarding checklist item. | Doc in repo, training record |
| No prohibited practice | Art. 5, incl. (ba), (bb) | Review prompts, product flows, and target users against each point of Art. 5(1). For image, video, or audio generation, add safeguards against intimate imagery of identifiable people and CSAM (Art. 5(1a)(a)(ii)). | Classification note, safety-filter tests, red-team cases |

## Transparency (Article 50)

Applies from 2 Aug 2026. Information must be clear, distinguishable, given at the latest at first interaction or exposure, and accessible (Art. 50(5)).

| Who | Trigger | Article | Control | Evidence |
|---|---|---|---|---|
| Provider | System interacts directly with people, such as a chatbot, voice agent, or AI email reply | 50(1) | Disclosure before or at the first message, for example a persistent "AI assistant" label and a first-turn notice. Voice: spoken notice at call start. Exception only when obvious to a reasonably well-informed person. Record why if you rely on it. | UI or E2E test asserting the notice renders before first output |
| Provider | System generates synthetic audio, image, video, or text | 50(2) | Machine-readable marking on every output: content credentials such as C2PA manifests, metadata, and watermarking where feasible, and a detection path. Text has no settled standard yet, so mark at the container: an HTML `meta` tag or JSON-LD on web pages, a custom header such as `X-AI-Generated` on email, and a field in any API or feed. Record why the chosen method is the feasible state of the art and revisit when the Art. 50(7) code of practice settles. There is no exception for internal use: an in-house tool whose outputs never leave the company is still covered. Exemption for assistive standard editing or no substantial alteration; whether a summary counts is unsettled, so record your reading. Legacy systems: by 2 Dec 2026 (Art. 111(4)). | Test that each output type carries the marking and survives your own export pipeline |
| Deployer | Emotion recognition or biometric categorisation | 50(3) | Notice to exposed persons. Also check Art. 5(1)(f) and (g) and Annex III point 1. GDPR applies. | Notice text, placement test |
| Deployer | Deep fake image, audio, or video | 50(4), first subpara. | Visible label. For evident art, satire, or fiction, a disclosure that does not hamper the work. | Label in rendered output, test |
| Deployer | AI-generated text published to inform the public on matters of public interest, such as news, newsletters, or reports | 50(4), second subpara.; recital 134 | Pick one path and record it. Disclose: a visible notice in every published item. Or exempt: a human review gate that a named person with editorial responsibility must pass before publishing, logged per item. Fully automatic publishing cannot use the exemption. When unsure whether the topic is a matter of public interest, disclose; it is cheap. | Test that the notice renders, or that publishing fails without a logged approval |

## High-risk systems: provider

Applies from 2 Dec 2027 (Annex III) or 2 Aug 2028 (Annex I). Chapter III Section 2 sets requirements. Section 3 sets obligations.

| Obligation | Article | Control | Evidence |
|---|---|---|---|
| Risk management across the lifecycle | 9 | Risk register per feature: hazard, affected group, likelihood, severity, mitigation, residual risk, test. Review on each release. | `risk-register` file, release checklist |
| Data governance | 10 as amended, 4a | Dataset cards: provenance, collection, labelling, preparation, assumptions, bias examination, gaps. Special-category data only under Art. 4a conditions. | Dataset cards, bias evaluation results |
| Technical documentation | 11, Annex IV | Generate from source: architecture, model versions, training and evaluation, metrics, human oversight design, change log. SMEs and SMCs may use the simplified Commission form (Art. 11(1) as amended). | `docs/annex-iv/` kept with the code |
| Automatic logging | 12, 19 | Structured event logs over the system's lifetime that allow identifying risk situations and substantial modifications and support post-market monitoring. For Annex III point 1(a), log period of use, reference database, matched input, and verifying persons (Art. 12(3)). Providers keep logs at least six months (Art. 19(1)). | Log schema, retention config, test asserting required fields |
| Instructions for use for deployers | 13 | Versioned instructions: purpose, accuracy and metrics, known limits, oversight measures, log access, maintenance. | Shipped docs |
| Human oversight | 14 | Design-in: show confidence and limits, let the overseer disregard, override, or reverse output, and provide a stop control. Mitigate automation bias. Annex III point 1(a): two-person verification. | UI tests for override and stop paths |
| Accuracy, robustness, cybersecurity | 15, 42(3) as amended | Declared metrics with eval suite in CI, fallback behaviour, defences against data poisoning, adversarial examples, prompt injection, and model extraction. CRA-compliant products are deemed compliant on cybersecurity (Art. 42(3)). | Eval reports, security tests |
| Quality management system | 17 as amended, 63 | Documented process covering design, testing, data, PMM, incidents, and change control. Proportionate for SMEs and SMCs. | QMS doc |
| Conformity, declaration, CE marking, registration | 43, 47, 48, 49, Annexes V to VIII | Pick the conformity route (Annex VI internal control or Annex VII notified body). Draft EU declaration of conformity. Register in the EU database before placing on the market. | Declaration file, registration ID |
| Post-market monitoring | 72 as amended | Telemetry and feedback loop feeding the risk register. Plan is part of Annex IV docs. | PMM plan, dashboards |
| Serious incident reporting | 73 | Runbook: report immediately after establishing a causal link and no later than 15 days. 2 days for widespread infringement or critical-infrastructure incidents. 10 days on death. | Incident runbook, on-call drill |
| Value chain | 25 as amended | Becoming a provider: rebranding, substantial modification, or changing intended purpose into high-risk. Written agreement with component and model suppliers (Art. 25(4)). | Contracts, supplier info pack |

## High-risk systems: deployer

| Obligation | Article | Control |
|---|---|---|
| Use per instructions, assign competent human oversight | 26(1), (2) | Named overseers, training record |
| Input data relevance under deployer control | 26(4) | Input validation, data-quality checks |
| Monitor and report risks and incidents to provider | 26(5) | Escalation path |
| Keep logs at least six months | 26(6) | Retention config |
| Inform workers before workplace use | 26(7) | Notice to worker representatives |
| Inform persons subject to decisions | 26(11) | Notice in decision flow |
| Fundamental rights impact assessment, where required | 27 as amended | FRIA, may cross-reference the DPIA |
| Explanation on request for Annex III decisions | 86 | Explanation endpoint or process |

## General-purpose AI model providers

Only when you place a GPAI model on the market, including after a substantial fine-tune that you distribute. Using a vendor model through an API does not trigger this.

| Obligation | Article | Control |
|---|---|---|
| Technical documentation for authorities | 53(1)(a), Annex XI | Model card with training, evaluation, compute |
| Information for downstream providers | 53(1)(b), Annex XII | Integrator documentation |
| Copyright policy, incl. text-and-data-mining opt-outs | 53(1)(c) | Crawler that honours opt-outs, written policy |
| Public training-content summary | 53(1)(d) | Published summary on the AI Office template |
| Systemic-risk models: evaluation, adversarial testing, incident reporting, cybersecurity | 51, 55, Annex XIII | Eval and red-team programme |

Models released under a qualifying free and open-source licence with public weights are exempt from Art. 53(1)(a) and (b) only, and not when they have systemic risk (Art. 53(2)). The copyright policy and training-content summary still apply.

## Fines

Maxima, whichever is higher for undertakings, lower for SMEs (Art. 99(6)) and SMCs (Art. 99(6a), inserted by 2026/1744): Art. 5 breaches up to EUR 35 million or 7 % of worldwide turnover (Art. 99(3)). Other operator obligations, including Art. 50, up to EUR 15 million or 3 % (Art. 99(4)). Misleading information to authorities up to EUR 7.5 million or 1 % (Art. 99(5)). GPAI providers: Art. 101.
