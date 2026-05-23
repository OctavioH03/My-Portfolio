# 📄 Document Corpus — Single Source of Truth

These Markdown files are the canonical facts for the portfolio and for RAG chunking. Keep the site UI in sync with this folder.

## 📁 Layout

| Path | Purpose |
|------|---------|
| `bio.md` | About me, narrative voice, strengths |
| `goals.md` | Career direction, what I want next |
| `contact.md` | How recruiters may reach me |
| `resume.md` | Dense resume-style facts (education, skills, headline) |
| `experience/` | One file per role; copy `TEMPLATE-role.md` |
| `projects/` | One file per project; copy `TEMPLATE-project.md` |
| `faq.md` | Expected recruiter questions as `##` headings |

## 🏷️ Frontmatter Rules

Every file should include the following YAML frontmatter:

```yaml
---
id: kebab-case-unique-id
section: bio | goals | contact | resume | experience | project | faq
title: Human-readable title
last_reviewed: YYYY-MM-DD
---
```

- **`id`** — Stable, unique string. Never rename casually; it anchors citations.
- **`section`** — Controls retrieval filtering and site routing.
- **`title`** — Used for citations and UI display.
- **`last_reviewed`** — Date you last verified the facts in this file.

Optional fields help retrieval and filtering; see templates.

## ✍️ Authoring Tips

- One main idea per short paragraph where possible.
- Prefer concrete facts: dates, stack names, metrics, and your specific role vs the team's.