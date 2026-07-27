# C817 — AI Application for Google Sheet

Work smarter and faster in **Google Sheets** with AI. This one-day, hands-on course teaches you to
use **Google's Gemini** inside Google Sheets to generate and explain formulas, clean and transform
messy data, analyse datasets, and build tables, charts and visualisations — always verifying the
AI's output before you trust it.

## Course Information

- **Course Code:** C817
- **Course Title:** AI Application for Google Sheet
- **Duration:** 1 day / 7.5 hours
- **Level:** Beginner
- **Mode:** Instructor-led, hands-on practical labs
- **Course Registration:** [AI Application for Google Sheet](https://www.tertiarycourses.com.sg/ai-application-for-google-sheet.html)

## One Connected Dataset

Every lab works the **same** dataset — a messy quarter of orders for a fictional retailer,
**Riverside Supplies**. You take a raw export in Lab 1 and, with Gemini AI, turn it into clean,
analysed, charted data you can trust by Lab 8. Wherever possible you use your **own**
non-confidential data, so you leave applying the skills to your own work; a Riverside Supplies
sample sheet is supplied for everyone to follow along.

There is **no assessment** — this is a commercial short course. Each lab proves itself with an
explicit *Test it* verification step instead.

## What You'll Learn

| Topic | Coverage |
|---|---|
| 01 — Getting Started with AI in Google Sheets | Generative AI & Gemini in Sheets · setting up and accessing AI · generating and explaining formulas · effective prompting for spreadsheet tasks |
| 02 — Analysing and Automating Data with AI in Sheets | Cleaning, transforming & organising data · summarising and analysing datasets · tables, charts & visualisations · validating AI output and applying AI safely |

## Labs

Eight connected hands-on labs (4 per topic). See [labs/README.md](labs/README.md) for the index and
[labs/tools.md](labs/tools.md) for the accounts and apps used.

## Courseware

Built artifacts live in [`courseware/`](courseware/):

- Trainer slide deck — `AI Application for Google Sheet (C817)-v1.0.pptx` (+ PDF)
- Learner Guide — `LG-*.docx` (+ PDF); the Markdown mirror is at the repo root
- Lesson Plan — `LP-*.docx` (+ PDF)

## Building the Courseware

Everything is generated from a single source (`course_data.py` + `data_domainN.py`) so the deck,
Lesson Plan, Learner Guide and labs stay 100% aligned:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

## Non-WSQ

This is a **non-WSQ** commercial short course. It carries **no** WSQ, SSG/SkillsFuture, TRAQOM,
digital-attendance, funding/subsidy or assessment content — those are deliberately excluded.

---

© 2026 Tertiary Infotech Academy Pte Ltd · UEN 201200696W
