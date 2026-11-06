---
name: nex-ai-skills
description: "Use when choosing or installing a free skill from this Nex AI repository, or when a task matches one of its guides: developer checks, web and accessibility audits, browser extensions, compliance packs, finance and property admin, or small-business operations. Route to the matching guide in skills/ or the named plugin and follow that guide. Do not perform the guide's work from this file."
license: MIT
compatibility: "Cursor, Codex, and other SKILL.md agents. Plugin installs still use .claude-plugin/marketplace.json. This file adds no packages."
metadata:
  author: Nex AI
  version: "1.0"
  internal: true
---

# Nex AI Skills

This file is the repository-root entry point for the free Nex AI skill catalog. It routes a task to one existing guide. It is not itself a developer, audit, compliance, finance, or operations skill, and it is not a seventh plugin.

Directories that only look for `SKILL.md` in the repository root can read this file. The installable guides stay in [`skills/`](skills/). The six Claude Code plugins stay where [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) already points.

`metadata.internal` is set so a bulk `npx skills add NexaiGuy/nex-ai-skills` keeps installing those guides. The skills CLI stops at a normal root `SKILL.md` and would otherwise skip `skills/`. Ask for this file by name only when you want the router itself.

## Route the task

1. Read [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). If it disagrees with the table below, the manifest wins.
2. Pick the plugin whose description matches the task. Open that plugin directory and read only the `name` and `description` frontmatter of each `skills/<name>/SKILL.md` inside it.
3. Open the chosen guide at `skills/<name>/SKILL.md` and follow that file. Prefer that path. The copy under the plugin directory is the same guide packaged for the plugin. If the two copies disagree, stop and say so.
4. If no guide matches, say this catalog does not include it. Do not invent a skill, and do not draft one from a title that this repository does not contain. [`README.md`](README.md) names two omitted listings, `nex-systemd-starter` and `nex-1099-contractor-pack`, and points paid skills to Agensi. Those guides are not here.
5. Once the matching guide is open, do the work from that guide. Do not answer the domain task from this file.

| Plugin | What it covers | Plugin directory |
| --- | --- | --- |
| `nex-dev-essentials` | Free developer skills by Nex AI: secret scanning, prototype-to-production hardening, agent checkpoints, instruction-file writing, skill publishing, and self-hosted diagnostics. | [`plugins/nex-dev-essentials`](plugins/nex-dev-essentials) |
| `nex-web-audits` | Free web skills by Nex AI: landing-page conversion audits, agent-ready websites, EU and US accessibility checks, Belgian search copy, and a single-file HTML section. | [`plugins/nex-web-audits`](plugins/nex-web-audits) |
| `nex-browser-extensions` | Free Manifest V3 browser-extension skills by Nex AI: page monitoring, clean copy, screenshots, color and font tools, trust checks, prompt boosting, and local receipt capture. | [`plugins/nex-browser-extensions`](plugins/nex-browser-extensions) |
| `nex-compliance` | Free compliance skills by Nex AI: EU e-invoicing, GDPR, HIPAA, COPPA, EUDR, ISO 27001, webshop law, privacy, and hardware declarations. | [`plugins/nex-compliance`](plugins/nex-compliance) |
| `nex-finance-property` | Free finance and property skills by Nex AI: Belgian non-profit, rental, and syndicate admin, Flemish purchase costs, and US property and pay-app packs. | [`plugins/nex-finance-property`](plugins/nex-finance-property) |
| `nex-business-operations` | Free operations skills by Nex AI: proposals, outreach, sector admin packs for Belgian and US small businesses, and manufacturing handoff. | [`plugins/nex-business-operations`](plugins/nex-business-operations) |

## Install

Leave the existing commands as they are.

Claude Code marketplace:

```text
/plugin marketplace add NexaiGuy/nex-ai-skills
/plugin install nex-dev-essentials@nex-ai-skills
/plugin install nex-web-audits@nex-ai-skills
/plugin install nex-browser-extensions@nex-ai-skills
/plugin install nex-compliance@nex-ai-skills
/plugin install nex-finance-property@nex-ai-skills
/plugin install nex-business-operations@nex-ai-skills
```

Cursor, Codex, and the skills CLI:

```text
npx skills add NexaiGuy/nex-ai-skills
npx skills add NexaiGuy/nex-ai-skills --skill secret-scan
npx skills add NexaiGuy/nex-ai-skills -a cursor
npx skills add NexaiGuy/nex-ai-skills -a codex
```

You can also copy one folder from [`skills/`](skills/) into the agent skills directory. Copy a single guide, not this repository root.

## Example

**Request**

Check this repository for leaked API keys before it is published.

**Result**

Open [`skills/secret-scan/SKILL.md`](skills/secret-scan/SKILL.md) and follow that guide. `secret-scan` is in `nex-dev-essentials`. This router does not scan for secrets.

**Request**

Install the free web-audit plugin.

**Result**

```text
/plugin marketplace add NexaiGuy/nex-ai-skills
/plugin install nex-web-audits@nex-ai-skills
```

## Limits

- A directory that publishes only the repository-root skill will list this router. It will not list each guide as its own skill unless that directory also reads `skills/` and `plugins/`.
- The folders ship the public guides. Scripts, extension source, and templates named inside a guide are not in these folders. Say so when a guide names a file that is missing.
- License for the repository is [MIT](LICENSE).
- Do not move or rename the existing skill directories. Do not add this file to the marketplace manifest.
