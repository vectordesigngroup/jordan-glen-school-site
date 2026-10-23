# Jordan Glen School & Summer Camp — unofficial redesign

An unofficial, static redesign concept for [Jordan Glen School & Summer Camp](https://www.jordanglen.org/) in Archer, Florida. It is not the school’s website, and it does not replace [jordanglen.org](https://www.jordanglen.org/). Tours, applications, camp registration, and donations link to the forms the school already publishes.

Jordan Glen is a 501(c)(3) nonprofit at 12425 SW 154th Street, Archer, FL 32618, about eight miles west of Gainesville. The public site describes a nature-based program on about 20 acres of field, orchard, and woods, plus a summer camp.

## Preview locally

No install step. From the repository root:

```bash
python3 scripts/build_site.py
python3 scripts/check_links.py
python3 -m http.server 8000 --directory site
```

Open http://localhost:8000 . `scripts/build_site.py` rewrites the HTML in `site/` from `scripts/build_site.py`. CSS, JavaScript, fonts, and images are already in `site/` and are not regenerated.

## Pages

| Page | File |
| --- | --- |
| Home | `site/index.html` |
| About (philosophy, faculty, quotes, alumni) | `site/about.html` |
| Programs | `site/programs.html` |
| Admissions & tuition | `site/admissions.html` |
| Summer camp | `site/summer-camp.html` |
| Campus life | `site/campus.html` |
| Calendar & news | `site/calendar.html` |
| Support & donate | `site/support.html` |
| Contact & map | `site/contact.html` |
| FAQ | `site/faq.html` |

## Content sources

Facts, fees, staff names, and quotes come from the public site on October 23, 2026. Copy was rewritten for clarity. Nothing was added for tuition, enrollment counts, testimonials, or staff names.

Primary pages crawled:

- https://www.jordanglen.org/
- https://www.jordanglen.org/history-philosophy/
- https://www.jordanglen.org/prek-8th-grade-program/
- https://www.jordanglen.org/school-life/
- https://www.jordanglen.org/team-2/
- https://www.jordanglen.org/tuition-fees/
- https://www.jordanglen.org/faqs/
- https://www.jordanglen.org/summer-camp/
- https://www.jordanglen.org/summer-camp/signup/
- https://www.jordanglen.org/calendar/
- https://www.jordanglen.org/news/ and the newsletter posts linked from it
- https://www.jordanglen.org/donate/
- https://www.jordanglen.org/contact/
- https://www.jordanglen.org/testimonials/
- https://www.jordanglen.org/alumni/
- https://www.jordanglen.org/forms/
- Parent-portal pages that are published without a login: school information, lunch and snacks, and after-school activities

Calls to action:

- Schedule a tour → https://www.jordanglen.org/forms/request-information/
- Apply → https://www.jordanglen.org/forms/admissions-application/
- Camp registration → https://www.jordanglen.org/forms/summer-camp-up-emergency-form-permissions/
- Donate → https://www.jordanglen.org/donate/

The homepage, program page, 2026–27 tuition, and faculty list describe PreK. The FAQ says the school now starts with Kindergarten. Both statements are shown. PreK is included because the current site supports it, and the conflict is marked rather than smoothed over.

An enrollment figure is not published on the site, so none is shown.

## TODO — content the school has not published

These are marked on the pages themselves:

- Which grades are enrolling this year (PreK on the program, tuition, and team pages; Kindergarten in the FAQ)
- A fuller history: founders, campus story, and a working link to Jeff’s 2005 Gainesville Sun editorial
- Staff biographies, and photos for Ryan Michael, Esteban Novoa, Ana Martins, Billie Hanna, and Benny Cannon
- The Step Up Scholarship application URL
- An admissions timeline (deadlines and what happens after the application)
- The organization’s EIN
- A text version of the 2026–27 calendar dates (only a PDF, a PNG, and a Google Calendar are published)

## Images and logo

Photographs, the favicon tree, and the wordmark are copied from public files on jordanglen.org (July 2022–October 2025 uploads). The wordmark used in the header is the school’s white logo, recolored pine (`#143028`) so it is readable on the light background. The footer uses the original white wordmark.

The campus satellite picture (`site/images/aerial.jpg`) was supplied for this redesign. It is not from the school’s website. The school’s text does not mention a pond; the caption says the pond is visible in that aerial.

Fonts are self-hosted so the site does not call Google at view time:

- [Fraunces](https://github.com/undercasetype/fraunces) (SIL Open Font License)
- [Source Sans 3](https://github.com/adobe-fonts/source-sans) (SIL Open Font License)

## GitHub Pages

The site is plain HTML, CSS, and JavaScript. `.github/workflows/pages.yml` rebuilds it, checks internal links, and on `main` deploys the `site/` directory with GitHub Actions.

To turn on Pages for this public repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions** (not “Deploy from a branch”).
3. Merge this work to `main`. The workflow runs on every push to `main` and on manual `workflow_dispatch`.
4. If GitHub asks you to approve the `github-pages` environment the first time, approve it. That environment is created by the workflow.
5. The site should then be at https://vectordesigngroup.github.io/jordan-glen-school-site/

Pull requests build and link-check only. They do not deploy.

Do not point a custom domain at this project unless the school decides to adopt it. jordanglen.org should keep serving the official site.

Canonical and Open Graph URLs in the HTML assume that Pages address. If the repository name changes, update `BASE` in `scripts/build_site.py` and rebuild.
