# Mentee Skill Matching Assessment (MSMA)

A draft prototype of the Mentee Skill Matching Assessment, an interactive tool that
translates a mentee's identified needs into a specific mentoring skill focus.

**Live demo:** https://kakobubu000.github.io/msma-prototype/

## Who completes it

One member of the student's school team, after the Top Needs Assessment interviews
are finished. That person already holds the caregiver, teacher, and mentee responses
and transcribes them here. The role is a fill-in field, since teams name that position
differently (school counselor, school psychologist, mentoring coordinator, and so on).

## What it does

The tool compares the entered Top Needs against the mentoring skill crosswalk and
determines how closely they converge.

- **High Convergence** — the concerns map to the same mentoring skills
- **Partial Convergence** — the concern maps to two related mentoring skills
- **Low Convergence** — the concerns map to three distinct mentoring skill areas,
  resolved through the Decision Questions

It then populates the Needs Convergence Matrix and a summary.

## Still to be written

`build.py` holds two dictionaries, `BLURBS` and `RESOURCES`, keyed by skill. Both are
empty. Any skill left empty renders a placeholder in the app instead of substitute text.

- `BLURBS[skill]` — what this skill focus specifically looks like
- `RESOURCES[skill]` — list of `[label, url]` pairs

Fill those in and run `python3 build.py` to regenerate `index.html`.

## Status

Early draft, for internal review. Not validated. The concern-to-skill crosswalk is
expert-derived and has not been empirically tested. Concerns are grouped into skill
areas so that convergence can be computed; that grouping is a judgment call and is
under review.

All user-facing wording is taken from the MSMA documentation and the GCS Mentee
Decision Tree crosswalk. Where the documentation marks something as still to be
written, the app shows a placeholder rather than substitute text.

## Running it

Single self-contained HTML file. No build step to view, no dependencies. Open
`index.html` in any browser, or visit the live demo above. Use `build.py` only when
regenerating the page from the source data.

## Credits

Integrated School Mentoring - YESS Lab - University of South Carolina
