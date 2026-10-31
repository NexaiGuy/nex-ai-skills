# Nex AI Skills

Free agent skills for Claude Code, Cursor, and Codex, from [Nex AI](https://nex-ai.be), an applied-AI studio in Ghent. Each skill is a folder with a `SKILL.md` file. Your agent loads it when the task matches the description.

This repository is a [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugins/create-marketplace). It publishes the free skills from the Nex AI catalog. The full catalog has **311 skills, 81 of them free**. **79** are in this repo. Premium skills stay on Agensi.

**[Browse the full catalog (311 skills, 81 free)](https://www.agensi.io/creators/ch1n4-g3nd4x)**

## Install

### Claude Code

Add the marketplace, then install a plugin:

```text
/plugin marketplace add NexaiGuy/nex-ai-skills
/plugin install nex-dev-essentials@nex-ai-skills
```

Plugins in this marketplace:

| Plugin | Skills | Install |
| --- | ---: | --- |
| `nex-dev-essentials` | 10 | `/plugin install nex-dev-essentials@nex-ai-skills` |
| `nex-web-audits` | 7 | `/plugin install nex-web-audits@nex-ai-skills` |
| `nex-browser-extensions` | 14 | `/plugin install nex-browser-extensions@nex-ai-skills` |
| `nex-compliance` | 19 | `/plugin install nex-compliance@nex-ai-skills` |
| `nex-finance-property` | 8 | `/plugin install nex-finance-property@nex-ai-skills` |
| `nex-business-operations` | 21 | `/plugin install nex-business-operations@nex-ai-skills` |

### Cursor, Codex, and the skills CLI

[skills.sh](https://skills.sh) installs the same folders with `npx skills add`:

```text
npx skills add NexaiGuy/nex-ai-skills
```

One skill:

```text
npx skills add NexaiGuy/nex-ai-skills --skill secret-scan
```

Pick the agent. Cursor and Codex each get a copy in their skills directory:

```text
npx skills add NexaiGuy/nex-ai-skills -a cursor
npx skills add NexaiGuy/nex-ai-skills -a codex
npx skills add NexaiGuy/nex-ai-skills -a claude-code
```

You can also copy a folder from [`skills/`](skills/) into `.cursor/skills/`, `.codex/skills/`, or `.claude/skills/`.

## What is in each folder

Each `SKILL.md` is the public guide for that free skill: what it does, when to use it, limits, examples, and questions, as published on Agensi.

Agensi no longer serves a public zip of the original package (the old install URL returns HTTP 410), and the private source repository was not available when this mirror was built. Scripts, extension source, and templates named in a guide are not in these folders. The guide is what shipped here.

## Renamed skills

The Agent Skills `name` field cannot contain `claude` or `anthropic`. See the [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

| Agensi slug | Name in this repo |
| --- | --- |
| `claude-md-writer` | `md-context-writer` |

`md-context-writer` still writes and lints `CLAUDE.md`, `AGENTS.md`, and `.claude/rules`. Only the skill name changed.

## Free skills

### Nex Dev Essentials

`/plugin install nex-dev-essentials@nex-ai-skills`

Free developer skills by Nex AI: secret scanning, prototype-to-production hardening, agent checkpoints, instruction-file writing, skill publishing, and self-hosted diagnostics.

| Skill | Uses | What it does |
| --- | ---: | --- |
| [Skill Publisher CLI](skills/skill-publisher-cli/SKILL.md) | 7 | Validate, version, and package SKILL.md folders for multi-registry marketplace publishing. |
| [Selfhosted Env Doctor](skills/selfhosted-env-doctor/SKILL.md) | 5 | Safe, read-only diagnostic tool for troubleshooting self-hosted stacks, port conflicts, and service failures. |
| [X402 API Paywall](skills/x402-api-paywall/SKILL.md) | 4 | Add stablecoin micropayment paywalls to FastAPI and Express routes using the HTTP 402 standard. |
| [FastAPI Repo Security Preflight](skills/fastapi-repo-security-preflight/SKILL.md) | 3 | Automated security scanner for FastAPI repos to detect secrets, SQLi, insecure CORS, and unverified webhooks. |
| [Openclaw Agent Wallet](skills/openclaw-agent-wallet/SKILL.md) | 3 | Add budget limits, approval workflows, and a policy-gated wallet layer to your autonomous agents. |
| [Prototype to Production](skills/prototype-to-production/SKILL.md) | 3 | Hardens and prepares AI-generated prototypes (Bolt, Lovable, v0) for secure production deployment. |
| [Agent Checkpoint](skills/agent-checkpoint/SKILL.md) | 1 | An undo button for AI agent work: save the project before a risky change, see exactly what changed, roll back in one command. |
| [CLAUDE.md Writer](skills/md-context-writer/SKILL.md) | 1 | Write, audit and fix CLAUDE.md, AGENTS.md and .claude/rules from facts in your repository, with a linter that checks them against the code. |
| [Nex MCP Client Delivery](skills/nex-mcp-client-delivery/SKILL.md) | 1 | Secure, multi-tenant MCP server delivery kit for deploying remote LLM tools via Cloudflare Tunnels. |
| [Secret Scan](skills/secret-scan/SKILL.md) | 1 | Find leaked API keys, tokens and passwords in files, commits, history or pasted text, and stop your coding agent from writing or committing them. |

### Nex Web Audits

`/plugin install nex-web-audits@nex-ai-skills`

Free web skills by Nex AI: landing-page conversion audits, agent-ready websites, EU and US accessibility checks, Belgian search copy, and a single-file HTML section.

| Skill | Uses | What it does |
| --- | ---: | --- |
| [Landing Page Conversion Audit](skills/landing-page-conversion-audit/SKILL.md) | 15 | Identify conversion blockers and ad-budget leaks with a severity-ranked landing page audit. |
| [Agent Ready Website Converter](skills/agent-ready-website-converter/SKILL.md) | 5 | Convert websites into agent-consumable formats with JSON-LD, product feeds, and .well-known discovery files. |
| [Nex EU Accessibility Audit](skills/nex-eu-accessibility-audit/SKILL.md) | 4 | Audits a website or app against the European Accessibility Act and WCAG 2.1 AA, producing a scope memo, remediation report, and accessibility statement. |
| [Nex Ada Web Accessibility](skills/nex-ada-web-accessibility/SKILL.md) | 3 | Audit and document web accessibility to mitigate US ADA Title II/III litigation and meet DOJ compliance deadlines. |
| [Nex Belgian Search Trinity](skills/nex-belgian-search-trinity/SKILL.md) | 3 | Master the "Trinity" of Belgian Search: SEO, AEO, and GEO copy for SMEs to rank on Google and get cited by AI. |
| [Nex Brand Palette Lite](skills/nex-brand-palette-lite/SKILL.md) | 3 | Extract brand color hex codes from a website's CSS variables into a portable Python script. |
| [Nex Single Section HTML](skills/nex-single-section-html/SKILL.md) | 2 | Generate a zero-dependency, single-file HTML hero section for rapid prototyping and placeholder pages. |

### Nex Browser Extensions

`/plugin install nex-browser-extensions@nex-ai-skills`

Free Manifest V3 browser-extension skills by Nex AI: page monitoring, clean copy, screenshots, color and font tools, trust checks, prompt boosting, and local receipt capture.

| Skill | Uses | What it does |
| --- | ---: | --- |
| [Nex Clean Copy Ext](skills/nex-clean-copy-ext/SKILL.md) | 6 | A production-ready Manifest V3 extension to strip tracking parameters and hidden Unicode from copied text. |
| [Nex Page Watch](skills/nex-page-watch/SKILL.md) | 6 | Deploy a production-ready Manifest V3 Chrome extension for visual webpage monitoring and change alerts. |
| [Nex Meeting Finder](skills/nex-meeting-finder/SKILL.md) | 5 | Deploy a production-ready Manifest V3 extension that detects meeting links and injects Join buttons into any webpage. |
| [Nex Clean Page Ext](skills/nex-clean-page-ext/SKILL.md) | 4 | Deploy or fork a production-ready, no-build Manifest V3 Chrome extension that declutters websites in one click. |
| [Nex Font Grab Ext](skills/nex-font-grab-ext/SKILL.md) | 3 | Ship a professional Chrome extension that identifies fonts, extracts CSS, and finds Google Font matches. |
| [Nex Prompt Booster Ext](skills/nex-prompt-booster-ext/SKILL.md) | 3 | The complete Nex Prompt Booster Chrome extension (real shipped Manifest V3 source): turn short, lazy AI prompts into detailed, structured, expert-quality prompts instantly, right inside ChatGPT, Claude, Gemini, Perplexity and Grok, with no API calls. Ships the full extension plus the dev loop, customization guide, and Web Store packaging steps. No build step. |
| [Nex Receipt Vault](skills/nex-receipt-vault/SKILL.md) | 3 | Deploy a complete Manifest V3 extension to capture and dashboard online receipts locally without bank access. |
| [Nex Site Trust Ext](skills/nex-site-trust-ext/SKILL.md) | 3 | Ship a complete Manifest V3 website trust and safety checker extension with no build step required. |
| [Nex Accent Contrast Ext](skills/nex-accent-contrast-ext/SKILL.md) | 2 | Ship a Manifest V3 Chrome extension that applies a custom accent color theme across any website. |
| [Nex Color Spy Ext](skills/nex-color-spy-ext/SKILL.md) | 2 | Fully-functional, zero-build Chrome extension for inspecting CSS colors, fonts, and dimensions with Shadow-DOM. |
| [Nex Frame It Ext](skills/nex-frame-it-ext/SKILL.md) | 2 | A production-ready, no-build Chrome Extension for creating professional device mockups from browser screenshots. |
| [Nex Full Capture Ext](skills/nex-full-capture-ext/SKILL.md) | 2 | Ship a complete, production-ready Manifest V3 Chrome extension for scrolling screenshots and PDF exports. |
| [Nex Tab Cost Ext](skills/nex-tab-cost-ext/SKILL.md) | 2 | A production-ready Manifest V3 Chrome extension to monitor tab memory, manage resources, and gamify browser hygiene. |
| [Nex Trust Check](skills/nex-trust-check/SKILL.md) | 1 | Deploy or fork a production-ready Chrome extension for AI text detection and fake review analysis. |

### Nex Compliance

`/plugin install nex-compliance@nex-ai-skills`

Free compliance skills by Nex AI: EU e-invoicing, GDPR, HIPAA, COPPA, EUDR, ISO 27001, webshop law, privacy, and hardware declarations.

| Skill | Uses | What it does |
| --- | ---: | --- |
| [Nex Einvoice DE](skills/nex-einvoice-de/SKILL.md) | 4 | Expert guide for German E-Rechnung compliance, XRechnung/ZUGFeRD formats, and GoBD archiving. |
| [Nex COPPA 2026 Pack](skills/nex-coppa-2026-pack/SKILL.md) | 3 | Audit and generate compliance documentation for the 2026 FTC COPPA Rule amendments. |
| [Nex Einvoice ES](skills/nex-einvoice-es/SKILL.md) | 3 | Navigate Spanish VeriFactu and Crea y Crece compliance with updated 2027 deadlines and technical field requirements. |
| [Nex Einvoice FR](skills/nex-einvoice-fr/SKILL.md) | 3 | Implement the French e-invoicing mandate (2026/2027) with Factur-X specs, PDP selection, and e-reporting workflows. |
| [Nex EUDR Due Diligence](skills/nex-eudr-due-diligence/SKILL.md) | 3 | Builds a complete EUDR due diligence file, applicability decision, DDS structure, geolocation checklist, and risk assessment, from your product list. |
| [Nex FAVV Food Pack](skills/nex-favv-food-pack/SKILL.md) | 3 | Builds FAVV registration decision trees, EU 1169/2011 label checklists, HACCP plans, allergen matrices, and recall workflows for Belgian food businesses. |
| [Nex GDPR Deepening](skills/nex-gdpr-deepening/SKILL.md) | 3 | Generates GDPR Article 30 processing registers and Article 35 DPIAs for Belgian and EU SMEs, prefilled with common SME processing activities. |
| [Nex HIPAA Small Practice](skills/nex-hipaa-small-practice/SKILL.md) | 3 | Builds a HIPAA compliance file for a small US practice: risk analysis, policies, BAAs, workforce training log and breach response plan. |
| [Nex Webshop Compliance EU](skills/nex-webshop-compliance-eu/SKILL.md) | 3 | Audits an EU webshop against consumer law: pre-contract information, the order button, withdrawal rights, price display and cookie consent. |
| [Nex AI Literacy Pack](skills/nex-ai-literacy-pack/SKILL.md) | 2 | Generates EU AI Act Article 4 compliance packages including inventories, policies, and role-based training structures. |
| [Nex Einvoice PL](skills/nex-einvoice-pl/SKILL.md) | 2 | Technical implementation guide for Polish KSeF e-invoicing, FA(3) schemas, and API onboarding. |
| [Nex EU Hardware Compliance Docs](skills/nex-eu-hardware-compliance-docs/SKILL.md) | 2 | Generates CE Declaration of Conformity, RoHS statement, and REACH SVHC declaration templates from your hardware product details. |
| [Nex Iso27001 KMO Pack](skills/nex-iso27001-kmo-pack/SKILL.md) | 2 | Builds an ISO 27001 documentation set for a Belgian SME: scope, risk assessment, Statement of Applicability and the core Annex A policies. |
| [Nex Sales Tax Nexus](skills/nex-sales-tax-nexus/SKILL.md) | 2 | US sales tax economic nexus evaluation, registration checklists, and exemption certificate workflows for e-commerce. |
| [Nex Trucking Compliance](skills/nex-trucking-compliance/SKILL.md) | 2 | Automates FMCSA compliance, DQ files, IFTA filings, and audit readiness for small US motor carriers. |
| [Nex UK MTD Pack](skills/nex-uk-mtd-pack/SKILL.md) | 2 | Automate UK MTD for Income Tax compliance, applicability checks, and quarterly deadline scheduling for sole traders. |
| [Nex US Privacy Multistate](skills/nex-us-privacy-multistate/SKILL.md) | 2 | Automated US multi-state privacy compliance engine for threshold mapping, policy generation, and DSR workflows. |
| [Nex Veiligheidscoordinatie Bouw](skills/nex-veiligheidscoordinatie-bouw/SKILL.md) | 2 | Regelt de veiligheidscoordinatie op een Belgische werf: coordinatiedagboek, veiligheids- en gezondheidsplan, postinterventiedossier en werfverslagen. |
| [Nex VSME Sustainability Pack](skills/nex-vsme-sustainability-pack/SKILL.md) | 2 | Produces a VSME voluntary sustainability report for an SME: basic module metrics, energy and emissions, workforce data and the customer questionnaire answers. |

### Nex Finance and Property

`/plugin install nex-finance-property@nex-ai-skills`

Free finance and property skills by Nex AI: Belgian non-profit, rental, and syndicate admin, Flemish purchase costs, and US property and pay-app packs.

| Skill | Uses | What it does |
| --- | ---: | --- |
| [Nex HOA Management Pack](skills/nex-hoa-management-pack/SKILL.md) | 3 | Runs a US homeowners association: meeting notices and minutes, reserve study prompts, violation letters, dues collection and annual budget. |
| [Nex Property Mgmt US](skills/nex-property-mgmt-us/SKILL.md) | 3 | Runs a small US rental portfolio: tenant screening, lease packets, notices, maintenance workflow and move-out accounting. |
| [Nex VZW Admin Pack](skills/nex-vzw-admin-pack/SKILL.md) | 3 | Automate Belgian vzw (non-profit) administration, WVV-compliant bylaws, UBO filings, and GA minutes. |
| [Pachtcontract Checklist](skills/pachtcontract-checklist/SKILL.md) | 3 | Intelligente checklist voor pachtcontracten en landbouwgebruik conform het Vlaams Pachtdecreet. |
| [Nex Syndicus VME Pack](skills/nex-syndicus-vme-pack/SKILL.md) | 2 | Legally compliant document generator for Belgian VME syndici, covering AV minutes, agendas, and financial accounting. |
| [Nex US Construction Payapps](skills/nex-us-construction-payapps/SKILL.md) | 2 | Generate US construction pay applications, G702/G703 structures, lien waivers, and certified payroll drafts. |
| [Nex Verhuur Immobeheer](skills/nex-verhuur-immobeheer/SKILL.md) | 2 | Automated Belgian rental contracts, legal indexation calculations, and regional compliance for landlords. |
| [Kostprijs Calculator](skills/kostprijs-calculator/SKILL.md) | 1 | Berekent een concept-raming van de totale aankoopkosten van een onroerend goed in Vlaanderen (verkooprecht, ereloon, aktekosten, btw) via een Python-script met bewerkbaar tarievenbestand. |

### Nex Business Operations

`/plugin install nex-business-operations@nex-ai-skills`

Free operations skills by Nex AI: proposals, outreach, sector admin packs for Belgian and US small businesses, and manufacturing handoff.

| Skill | Uses | What it does |
| --- | ---: | --- |
| [Nex Cold Mail 1 Template](skills/nex-cold-mail-1-template/SKILL.md) | 5 | A proven Dutch cold-mail template for SME outreach using the no-price, demo-first framework. |
| [Nex Datasheet Extractor](skills/nex-datasheet-extractor/SKILL.md) | 5 | Extracts structured electrical specs, package data, and compliance status from component datasheet PDFs. |
| [Nex Component Library Formatter](skills/nex-component-library-formatter/SKILL.md) | 4 | Normalize and validate electronics component library metadata against a strict canonical schema. |
| [Nex Govcon Capture Pack](skills/nex-govcon-capture-pack/SKILL.md) | 3 | Takes a small business from SAM.gov registration to compliant federal RFP responses with capability statements and compliance matrices. |
| [Nex KMO Portefeuille Flow](skills/nex-kmo-portefeuille-flow/SKILL.md) | 3 | Loodst een Vlaamse kmo door de kmo-portefeuille: subsidiabiliteit, aanvraag, betaling via het portaal en de bewijsstukken. |
| [Nex Landbouw Admin](skills/nex-landbouw-admin/SKILL.md) | 3 | Regelt de administratie van een Vlaams landbouwbedrijf: verzamelaanvraag, mestbankaangifte, perceelsregistratie en dierenregisters. |
| [Nex Life Logger](skills/nex-life-logger/SKILL.md) | 3 | Logs browser history, active windows and watched videos locally, then lets your agent answer questions about what you were doing. |
| [Nex One Sector Classifier](skills/nex-one-sector-classifier/SKILL.md) | 3 | Classifies a business into a sector and a matching site archetype from its website and public data, so generation can be themed automatically. |
| [NL Humanizer AI Smell Detector](skills/nl-humanizer-ai-smell-detector/SKILL.md) | 3 | Detect and remove "AI smell" from Dutch text with a diagnostic scoring system and human-centric rewriting. |
| [Nex Auto Sector Pack](skills/nex-auto-sector-pack/SKILL.md) | 2 | Automates Belgian automotive sales docs, Car-Pass workflows, and 2022 warranty compliance for garages. |
| [Nex BOM Normalizer](skills/nex-bom-normalizer/SKILL.md) | 2 | Standardize, deduplicate, and clean messy Bill of Materials (BOM) files into procurement-ready CSVs. |
| [Nex Employee Handbook US](skills/nex-employee-handbook-us/SKILL.md) | 2 | Builds multi-state US employee handbooks using a core plus supplement model and NLRB-compliant conduct policies. |
| [Nex Grant Writer US](skills/nex-grant-writer-us/SKILL.md) | 2 | Guides a US nonprofit from grant prospect research to a submitted federal or foundation proposal with budget, narrative and compliance checks. |
| [Nex Kinderopvang Admin](skills/nex-kinderopvang-admin/SKILL.md) | 2 | Regelt de administratie van een Vlaamse kinderopvang: inschrijvingen, aanwezigheidsregistratie, facturatie en het fiscaal attest. |
| [Nex Manufacturing Handoff Pack](skills/nex-manufacturing-handoff-pack/SKILL.md) | 2 | Turns a design package into a manufacturing handoff: BOM, drawing checklist, tolerance notes, supplier RFQ and first-article inspection plan. |
| [Nex Medical Billing Priorauth](skills/nex-medical-billing-priorauth/SKILL.md) | 2 | Handles US prior authorisation and claim denials: payer requirement lookup, request packets, appeal letters and a denial tracking log. |
| [Nex Offerte Generator](skills/nex-offerte-generator/SKILL.md) | 2 | Generate high-converting, Belgian-compliant Dutch commercial proposals for SME prospects. |
| [Nex Overheidsopdrachten Tender](skills/nex-overheidsopdrachten-tender/SKILL.md) | 2 | Analyseert een Belgisch bestek en levert een go of no-go met knock-outs, gunningscriteria, weging en drempelbedragen. |
| [Nex RIZIV Zorgpraktijk](skills/nex-riziv-zorgpraktijk/SKILL.md) | 2 | Regelt de RIZIV-administratie van een Belgische zorgpraktijk: conventiestatus, nomenclatuur, getuigschriften en derdebetaler. |
| [Nex Screencast Cleaner](skills/nex-screencast-cleaner/SKILL.md) | 2 | Automatically crops OS taskbars and removes dead air from screen recordings for upload-ready demos. |
| [Nex Uitvaart Docs](skills/nex-uitvaart-docs/SKILL.md) | 2 | Generate Belgian death administration docs, roadmaps, and notification letters for funeral directors and families. |


## Not included

Two free listings were left out. Their public text describes a different skill, so publishing it would ship the wrong guide.

- `nex-systemd-starter` — The public listing text is the paid stock-image picker (nex-stock-image-picker), not a systemd guide.
- `nex-1099-contractor-pack` — The public listing text is a duplicate of fastapi-repo-security-preflight, not a 1099 contractor pack.

## More skills

The other **230 skills** are on Agensi, from $5: **https://www.agensi.io/creators/ch1n4-g3nd4x**

A few paid standouts, by link only:

- [MCP Server Kit](https://www.agensi.io/skills/mcp-server-kit) — a working, tested MCP server in Python or TypeScript that connects an agent to your own API, database, or tools.
- [Multi-LLM Fallback Router](https://www.agensi.io/skills/nex-multi-llm-fallback-router) — a Python provider that chains Claude, Gemini, Qwen, and Ollama so one outage does not stop the pipeline.
- [Webhook Handler Pattern](https://www.agensi.io/skills/nex-webhook-handler-pattern) — idempotent FastAPI webhook handlers with signature verification and an audit log.
- [Multi-tenant SaaS FastAPI](https://www.agensi.io/skills/nex-multitenant-saas-fastapi) — tenant-scoped data access for FastAPI SaaS apps.

This repository does not include those skills.

## Credit

Built by [Nex AI](https://nex-ai.be) in Ghent. License: [MIT](LICENSE).
