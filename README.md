# Mentee Skill Matching Assessment (MSMA)

A draft prototype of the Mentee Skill Matching Assessment, an interactive tool that
translates a mentee's identified needs into a specific mentoring skill focus.

**Live demo:** https://kakobubu000.github.io/msma-prototype/

## What it does

One app, three respondent views. A mentoring coordinator creates a case code and shares
role-specific links with the caregiver, the teacher, and the student. Each person selects
their top concerns. The tool compares those concerns against a mentoring skill crosswalk,
determines how closely they converge, and returns a primary skill focus with suggested
resources.

- **High convergence** — all responses map to the same mentoring skill
- **Partial convergence** — some but not all map to the same skill
- **Low convergence** — responses map to distinct skills, resolved through team decision questions

## Status

Early draft, for internal review. Not validated. The concern-to-skill crosswalk is
expert-derived and has not been empirically tested.

**Prototype limitations**

- Responses are stored in browser local storage, so they do not sync across devices.
  A shared backend is required before any real use, and student-level data raises
  questions that should be settled before a pilot.
- The 19 concerns are grouped into 8 canonical skills to make convergence computable.
  That grouping is a judgment call and is under review.
- Student-facing item wording is drafted and needs review.

This tool identifies skill focus areas for mentoring, a Tier 2 support. It is not a
clinical screener and does not assess risk.

## Running it

Single self-contained HTML file. No build step, no dependencies. Open `index.html`
in any browser, or visit the live demo above.

## Credits

Integrated School Mentoring · YESS Lab · University of South Carolina
