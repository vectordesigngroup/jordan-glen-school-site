#!/usr/bin/env python3
"""Generate the static Jordan Glen redesign into site/."""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
BASE = "https://vectordesigngroup.github.io/jordan-glen-school-site"
OFFICIAL = "https://www.jordanglen.org"
TOUR = f"{OFFICIAL}/forms/request-information/"
APPLY = f"{OFFICIAL}/forms/admissions-application/"
CAMP_FORM = f"{OFFICIAL}/forms/summer-camp-up-emergency-form-permissions/"
CAMP_INFO = f"{OFFICIAL}/forms/request-information-for-summer-camp/"
DONATE = f"{OFFICIAL}/donate/"
DONATE_INQ = f"{OFFICIAL}/forms/donation-inquiries/"
ENROLL = f"{OFFICIAL}/forms/enrollment-form-release/"
ALUM_REG = f"{OFFICIAL}/forms/alumni-registration/"
ALUM_CHECK = f"{OFFICIAL}/forms/alumni-check-in/"
PARENT = f"{OFFICIAL}/parent-portal/"
FORMS = f"{OFFICIAL}/forms/"
MAP = "https://www.google.com/maps/search/?api=1&query=12425+SW+154th+Street+Archer+FL+32618"
CAL_PDF = f"{OFFICIAL}/wp-content/uploads/2026/08/26-27-JG-Calendar.pdf"
CAL_PNG = f"{OFFICIAL}/wp-content/uploads/2026/08/JG-Calendar-26-27.png"
SUPPLY = f"{OFFICIAL}/wp-content/uploads/2026/07/JG-Class-Supply-List-2026-27.pdf"
GCAL = "https://calendar.google.com/calendar/embed?src=info%40jordanglen.org&ctz=America%2FNew_York"
GCAL_OPEN = "https://calendar.google.com/calendar/u/0/render?cid=info%40jordanglen.org"
DON_PDF = f"{OFFICIAL}/wp-content/uploads/2022/08/Jordan-Glen-Donation-Form.pdf"
RECEIPT = f"{OFFICIAL}/wp-content/uploads/2022/08/Jordan-Glen-Donation-Receipt.pdf"
ARTICLE = "https://nextstepsblog.org/2025/10/free-school-microschool-unicorn-school-whatever-you-call-it-its-been-thriving-for-50-years/"
QUOTES = f"{OFFICIAL}/testimonials/"
WINTER_POST = f"{OFFICIAL}/jg-winter-2025-newsletter/"
WINTER_PDF = f"{OFFICIAL}/wp-content/uploads/2025/01/Newsletter-January-2025-1.pdf"
SPRING_POST = f"{OFFICIAL}/jg-spring-2024-newsletter/"
SPRING_PDF = f"{OFFICIAL}/wp-content/uploads/2024/02/Newsletter-February-2024.pdf"
SPRING_ELEC = f"{OFFICIAL}/wp-content/uploads/2024/02/3rd-Term-Electives-2023-24-.pdf"
FALL_POST = f"{OFFICIAL}/jg-fall-2023-newsletter/"
FALL_PDF = f"{OFFICIAL}/wp-content/uploads/2023/11/Newsletter-November-2023.pdf"
FALL_ELEC = f"{OFFICIAL}/wp-content/uploads/2023/11/Electives-2023-2024-Term-2.pdf"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Programs"),
    ("admissions.html", "Admissions"),
    ("summer-camp.html", "Summer Camp"),
    ("campus.html", "Campus Life"),
    ("calendar.html", "Calendar"),
    ("support.html", "Support"),
    ("contact.html", "Contact"),
]

STAFF = [
    ("jeff.jpg", "Jeff Davis", "Director", "5th–8th grade teacher"),
    ("jeremy.jpg", "Jeremy Primosch", "Associate Director", "5th–8th grade teacher"),
    ("kim.jpg", "Kim Smith", "Associate Director", "5th–8th grade teacher"),
    ("nicole.jpg", "Nicole Christie", "3rd–4th grade teacher", ""),
    ("", "Ryan Michael", "3rd–4th grade teacher aide", ""),
    ("gowri.jpg", "Gowri Navaratnam", "2nd grade teacher", ""),
    ("chandlar.jpg", "Chandlar Witt", "2nd grade teacher", ""),
    ("gen.jpg", "Genaveve Wooten", "1st grade teacher", ""),
    ("", "Esteban Novoa", "1st grade teacher aide", ""),
    ("", "Ana Martins", "Kindergarten teacher", ""),
    ("molly.jpg", "Molly Boles", "Kindergarten teacher", ""),
    ("sue.jpg", "Sue Micieli-Voutsinas", "PreK teacher", ""),
    ("ashley.jpg", "Ashley Daigle", "PreK teacher", ""),
    ("louis.jpg", "Louis Searcy", "Science teacher", ""),
    ("chelsee.jpg", "Chelsee Florence", "Art teacher", ""),
    ("miguel.jpg", "Miguel Ararat", "Spanish teacher", ""),
    ("trish.jpg", "Trish Lockwood", "Administration", ""),
    ("", "Billie Hanna", "Afterschool teacher", ""),
    ("", "Benny Cannon", "Music teacher", ""),
]


def initials(name: str) -> str:
    parts = [part for part in name.replace("–", " ").split() if part]
    return "".join(part[0] for part in parts[:2])


def staff_cards() -> str:
    cards = []
    for photo, name, role, extra in STAFF:
        if photo:
            media = (
                f'<img src="images/{photo}" alt="Photo of {name}" width="200" height="250">'
            )
        else:
            media = f'<p class="avatar-fallback" aria-hidden="true">{initials(name)}</p>'
        second = f"<p>{extra}</p>" if extra else ""
        cards.append(
            f"""<article class="person">
              {media}
              <h3>{name}</h3>
              <p class="role">{role}</p>
              {second}
            </article>"""
        )
    return "\n".join(cards)


def nav_html(current: str) -> str:
    items = []
    for href, label in NAV:
        if href == "index.html":
            continue
        current_attr = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{current_attr}>{label}</a></li>')
    return "\n".join(items)


def footer_links(current: str) -> str:
    items = []
    for href, label in NAV:
        if href == "index.html":
            label = "Home"
        current_attr = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{current_attr}>{label}</a></li>')
    items.append('<li><a href="faq.html">FAQ</a></li>')
    return "\n".join(items)


def schema(title: str, description: str, path: str) -> str:
    url = f"{BASE}/" if not path else f"{BASE}/{path}"
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{BASE}/#website",
                "name": "Jordan Glen School & Summer Camp — unofficial redesign",
                "url": f"{BASE}/",
                "description": "Unofficial redesign concept for Jordan Glen School & Summer Camp. Not the school's official website.",
            },
            {
                "@type": "WebPage",
                "@id": f"{url}#webpage",
                "url": url,
                "name": title,
                "description": description,
                "isPartOf": {"@id": f"{BASE}/#website"},
                "about": {"@id": f"{OFFICIAL}/#school"},
            },
            {
                "@type": ["School", "EducationalOrganization"],
                "@id": f"{OFFICIAL}/#school",
                "name": "Jordan Glen School & Summer Camp",
                "legalName": "Jordan Glen School & Summer Camp, Inc.",
                "url": f"{OFFICIAL}/",
                "foundingDate": "1974",
                "email": "info@jordanglen.org",
                "telephone": "+1-352-495-2728",
                "faxNumber": "+1-352-495-1539",
                "nonprofitStatus": "Nonprofit501c3",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "12425 SW 154th Street",
                    "addressLocality": "Archer",
                    "addressRegion": "FL",
                    "postalCode": "32618",
                    "addressCountry": "US",
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 29.5407862,
                    "longitude": -82.5062792,
                },
                "hasMap": MAP,
            },
        ],
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(data, indent=2)
        + "\n</script>"
    )


def layout(filename: str, title: str, description: str, body: str) -> str:
    path = "" if filename == "index.html" else filename
    canonical = f"{BASE}/" if filename == "index.html" else f"{BASE}/{filename}"
    title_html = html.escape(title, quote=True)
    description_html = html.escape(description, quote=True)
    home_current = ' aria-current="page"' if filename == "index.html" else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title_html}</title>
  <meta name="description" content="{description_html}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index,follow">
  <meta name="theme-color" content="#143028">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Jordan Glen School &amp; Summer Camp — unofficial redesign">
  <meta property="og:title" content="{title_html}">
  <meta property="og:description" content="{description_html}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/images/og.jpg">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="images/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="icon" href="images/favicon-192.png" type="image/png" sizes="192x192">
  <link rel="apple-touch-icon" href="images/favicon-192.png">
  <link rel="stylesheet" href="css/styles.css">
  {schema(title, description, path)}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="concept-banner">
    Unofficial redesign concept. Enrollment, camp registration, and donations stay on
    <a href="{OFFICIAL}/">jordanglen.org</a>.
  </div>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="index.html"{home_current}>
        <img src="images/logo-pine.png" width="164" height="56" alt="Jordan Glen School and Summer Camp">
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
        <span class="menu-bars" aria-hidden="true"></span>
        <span class="menu-label">Menu</span>
      </button>
      <nav class="site-nav" id="site-nav" aria-label="Primary">
        <ul>
          {nav_html(filename)}
        </ul>
      </nav>
    </div>
  </header>
  <main id="main">
    {body}
  </main>
  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <img class="footer-logo" src="images/logo-white.png" width="141" height="48" alt="">
        <p>
          Jordan Glen School &amp; Summer Camp<br>
          12425 SW 154th Street<br>
          Archer, FL 32618
        </p>
        <p>
          <a href="tel:+13524952728">(352) 495-2728</a><br>
          <a href="mailto:info@jordanglen.org">info@jordanglen.org</a><br>
          Fax 352-495-1539
        </p>
      </div>
      <nav aria-label="Footer">
        <h2>Explore</h2>
        <ul>
          {footer_links(filename)}
        </ul>
      </nav>
      <div>
        <h2>Take the next step</h2>
        <ul>
          <li><a href="{TOUR}">Schedule a tour</a></li>
          <li><a href="{APPLY}">Apply</a></li>
          <li><a href="{CAMP_FORM}">Camp registration</a></li>
          <li><a href="support.html">Support &amp; donate</a></li>
        </ul>
      </div>
      <div>
        <h2>Official school site</h2>
        <p>This page is an unofficial redesign. Use the school’s site for forms and the parent portal.</p>
        <ul>
          <li><a href="{OFFICIAL}/">jordanglen.org</a></li>
          <li><a href="{PARENT}">Parent portal</a></li>
          <li><a href="{FORMS}">Forms folder</a></li>
          <li><a href="contact.html">Contact &amp; map</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap legal">
      <p>Jordan Glen School &amp; Summer Camp is a 501(c)(3) nonprofit educational institution that does not discriminate on the basis of race, religion, gender, ethnicity, sexual orientation, or national origin. Donations are tax-deductible.</p>
      <p>Wording and facts were gathered from the public site jordanglen.org on October 23, 2026, and rewritten for clarity. This is an unofficial redesign concept, not a school publication.</p>
    </div>
  </footer>
  <script src="js/main.js"></script>
</body>
</html>
"""


def cta_band() -> str:
    return f"""<section class="section band-pine">
      <div class="wrap">
        <h2>Come see the campus.</h2>
        <p>To schedule a tour, call <a href="tel:+13524952728">(352) 495-2728</a> or send a message through the school’s information form. Applications and camp registration use the forms already on jordanglen.org.</p>
        <div class="cta-row">
          <a class="btn btn-light" href="{TOUR}">Schedule a tour</a>
          <a class="btn btn-primary" href="{APPLY}">Apply</a>
          <a class="btn btn-ghost" href="{CAMP_FORM}">Camp registration</a>
        </div>
      </div>
    </section>"""


GRADE_NOTE = """<aside class="todo">
  <p><strong>TODO — confirm which grades are enrolling.</strong> The homepage, program page, 2026–27 tuition, and faculty list describe PreK. The FAQ still says, “Jordan Glen now starts with Kindergarten and continues through 8th grade.” This redesign reports both and does not resolve the conflict.</p>
</aside>"""


def pages() -> dict:
    home = f"""
    <section class="wrap hero">
      <div>
        <p class="eyebrow">Archer, Florida · Since 1974</p>
        <h1>Enriching the lives of Gainesville children since 1974.</h1>
        <p class="lede">Jordan Glen School is a nonprofit school and summer camp in Archer, eight miles west of Gainesville, on 20 acres of field, orchard, and woods. Nature and the outdoors are primary resources for daily learning.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="{TOUR}">Schedule a tour</a>
          <a class="btn btn-ghost" href="{APPLY}">Apply</a>
          <a class="btn btn-ghost" href="summer-camp.html">Summer camp</a>
        </div>
        <p class="fine">Tour requests, applications, and camp registration use Jordan Glen’s existing forms.</p>
      </div>
      <figure class="hero-photo">
        <img src="images/hero-woods.jpg" width="1500" height="1000" alt="Children outdoors together in the woods at Jordan Glen" fetchpriority="high">
        <figcaption>Photo from Jordan Glen’s public site. The school describes the outdoor space as part of the learning environment.</figcaption>
      </figure>
    </section>
    <section class="wrap section" aria-label="At a glance">
      <div class="fact-row grid-3">
        <article class="fact"><strong>Since 1974</strong><span>A nonprofit educational institution, now past 45 years with families.</span></article>
        <article class="fact"><strong>About 20 acres</strong><span>Field, orchard, and woods, eight miles west of Gainesville.</span></article>
        <article class="fact"><strong>PreK–8</strong><span>Mixed-grade classrooms. See the grade note under Programs.</span></article>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap split">
        <div>
          <p class="eyebrow">A unique environment</p>
          <h2>The woods are part of the school, not a break from it.</h2>
          <p>Jordan Glen’s own description: the campus is a safe, physically beautiful environment and an exceptional learning resource. The integration of the outdoor space into the atmosphere of the school is what sets it apart.</p>
          <p>Teachers are known by first names. The day begins at 9:00 a.m. with Morning Meeting. The published student-to-teacher ratio is 15 to 1 on average.</p>
          <div class="cta-row">
            <a class="btn btn-primary" href="about.html">History &amp; philosophy</a>
            <a class="btn btn-ghost" href="programs.html">See the program</a>
          </div>
        </div>
        <figure class="photo-frame">
          <img src="images/grounds.jpg" width="1024" height="720" alt="School building and open yard at Jordan Glen" loading="lazy">
          <figcaption>The school building and yard, from Jordan Glen’s public photos.</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Programs</p>
          <h2>One campus, from the youngest classes through 8th grade.</h2>
          <p>Classroom groupings can change with the year’s enrollment. Academics are grouped by age and ability, and the mixed-grade philosophy asks older and younger students to mentor one another.</p>
        </div>
        {GRADE_NOTE}
        <div class="grid-3">
          <article class="card">
            <h3><a href="programs.html#prek">PreK–1st grade</a></h3>
            <p>Outdoor time and play sit alongside a traditional academic curriculum, with the aim of a foundation that loves learning.</p>
          </article>
          <article class="card">
            <h3><a href="programs.html#elementary">2nd–4th grades</a></h3>
            <p>Academic preparation for middle school, plus more chances to lead and to become thoughtful, well-rounded students.</p>
          </article>
          <article class="card">
            <h3><a href="programs.html#middle">5th–8th grades</a></h3>
            <p>Middle school uses a “work hard, play hard” approach. Graduates leave with tools for the next chapter.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap split">
        <figure class="quote">
          <blockquote>
            <p>“Jordan Glen made me the person I am today! A truly special school that focuses on creativity, fun, and personal responsibility.”</p>
          </blockquote>
          <figcaption>— JG Alum, published on jordanglen.org</figcaption>
        </figure>
        <figure class="quote">
          <blockquote>
            <p>“Jordan Glen is a magical place. I continue to be amazed on a daily basis watching children develop a love of life and learning. I wish every child could experience JG for themselves.”</p>
          </blockquote>
          <figcaption>— Jeremy Primosch, Associate Director</figcaption>
        </figure>
      </div>
      <div class="wrap">
        <p class="fine"><a href="about.html#voices">More published quotes</a> · <a href="{QUOTES}">All quotes on the official site</a></p>
      </div>
    </section>
    <section class="section" id="campus-preview">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Campus</p>
          <h2>Field, orchard, woods, pool, and a pond you can see from above.</h2>
          <p>The school locates itself on twenty acres of playing fields, orchards, and woods, just east of Archer. Summer camp materials also name a swimming pool, tennis court, playground, activity rooms, an art deck, a kitchen, and a piano.</p>
          <p>The satellite view shows the wooded property, the central clearing, buildings, a small pond, and the pool. Jordan Glen’s written pages do not describe the pond; it is visible in this aerial.</p>
          <div class="cta-row">
            <a class="btn btn-primary" href="campus.html">Campus life</a>
            <a class="btn btn-ghost" href="contact.html">Map &amp; directions</a>
          </div>
        </div>
        <figure class="photo-frame">
          <img src="images/aerial.jpg" width="1400" height="1097" alt="Satellite view of the Jordan Glen campus in Archer, showing woods, a clearing, buildings, a small pond, and a pool" loading="lazy">
          <figcaption>Satellite view supplied for this redesign. It is not a photo from the school’s website.</figcaption>
        </figure>
      </div>
    </section>
    <section class="section band-pine">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Summer camp 2026</p>
          <h2>June 8–July 17, for children entering grades K–8.</h2>
          <p>More than 50 summers. Campers swim daily when weather allows, choose afternoon electives, and eat outside when they can. Sibling discounts are offered, and spots are limited.</p>
          <div class="cta-row">
            <a class="btn btn-light" href="summer-camp.html">Camp details &amp; fees</a>
            <a class="btn btn-primary" href="{CAMP_FORM}">Camp registration</a>
          </div>
        </div>
        <figure class="photo-frame">
          <img src="images/camp.jpg" width="531" height="443" alt="Children outside during Jordan Glen summer camp" loading="lazy">
          <figcaption>Summer camp photo from Jordan Glen’s public site.</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">News</p>
          <h2>Recent letters from the school.</h2>
        </div>
        <div class="news-list">
          <article class="news-item">
            <time datetime="2025-10-21">October 21, 2025</time>
            <h3>JG Winter 2025 Newsletter</h3>
            <p>The school shared Term One updates and linked a newsletter PDF.</p>
            <p><a href="calendar.html#news">Read the news list</a></p>
          </article>
          <article class="news-item">
            <time datetime="2024-02-27">February 27, 2024</time>
            <h3>JG Spring 2024 Newsletter</h3>
            <p>Term Three happenings, plus that term’s electives.</p>
          </article>
          <article class="news-item">
            <time datetime="2023-11-14">November 14, 2023</time>
            <h3>JG Fall 2023 Newsletter</h3>
            <p>Term Two notes, electives, and an invitation to the Thanksgiving Feast.</p>
          </article>
        </div>
      </div>
    </section>
    {cta_band()}
    """

    about = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">About</p>
      <h1>Advocates of children and childhood.</h1>
      <p class="lede">Jordan Glen’s philosophy starts from a simple observation: children share predictable sequences of growth, and each child still has an individual pattern of timing.</p>
    </header>
    <section class="section">
      <div class="wrap prose">
        <h2>Our philosophy</h2>
        <p>The school’s commitment is to a program that values individual differences, exploration and discovery, meaningful academic study, sportsmanship, and personal and global responsibility.</p>
        <p>Staff are described as the way the school understands each child’s creative, social, emotional, and intellectual needs. Jordan Glen wants children to enjoy their time away from home, and says the joy of living and the love of learning need never be separated.</p>
        <p>The FAQ puts the same idea this way: every child is gifted, academics are meaningful and guided by the natural environment, and the joy of living and love of learning stay together.</p>
        <aside class="todo">
          <p><strong>TODO — fuller history.</strong> The history page says that for over 45 years Jordan Glen has celebrated, inspired, and empowered young minds. It mentions Jeff’s 2005 editorial in the Gainesville Sun, but the public HTML did not include a working link. Founders, and how the campus came to be, are not published there.</p>
        </aside>
        <p>The school also points readers to <a href="{ARTICLE}">a 2025 article about Jordan Glen</a> on Next Steps Blog.</p>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap split">
        <figure class="photo-frame">
          <img src="images/traditions.jpg" width="1400" height="788" alt="Students at a Jordan Glen gathering" loading="lazy">
          <figcaption>A gathering from the school’s public photo library.</figcaption>
        </figure>
        <div class="prose">
          <h2>A small faculty, known by first names</h2>
          <p>The atmosphere is informal and respectful. Morning Meeting at 9:00 a.m. is where students and teachers share the day’s activities, announcements, and news. Participation, group problem-solving, and cooperation are encouraged.</p>
          <p>The faculty page says academic achievement is watched through formal and informal inventories and testing, and that students who transfer out enter at or above grade level. Many alumni continue in Cambridge and International Baccalaureate programs.</p>
          <p>Some teachers were Jordan Glen students themselves and now have their own children at the school.</p>
        </div>
      </div>
    </section>
    <section class="section" id="faculty">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">Faculty &amp; staff</p>
          <h2>The team listed on the current site.</h2>
          <p>Names and roles are taken from the public team page. Five people are listed there without a photo.</p>
        </div>
        <aside class="todo">
          <p><strong>TODO — staff biographies and five photos.</strong> “More Info” on the team page did not include biography text in the public page content, so no bios are invented here. Photos were not published for Ryan Michael, Esteban Novoa, Ana Martins, Billie Hanna, and Benny Cannon.</p>
        </aside>
        <div class="person-grid">
          {staff_cards()}
        </div>
      </div>
    </section>
    <section class="section band-sand" id="voices">
      <div class="wrap">
        <div class="section-head">
          <h2>In their words</h2>
          <p>These quotes are published on jordanglen.org. They are not new testimonials.</p>
        </div>
        <div class="grid-2">
          <figure class="quote">
            <blockquote><p>“My children have attended Jordan Glen since Pre-K. They are now in the 6th and 8th grade. I feel blessed that they have never been bullied, and have always been excited to go to school. I think the outside setting and frequent outdoor activities are good for their bodies and souls.”</p></blockquote>
            <figcaption>— JG Parent</figcaption>
          </figure>
          <figure class="quote">
            <blockquote><p>“I am an alum who appreciated my experience at Jordan Glen so much that I did everything I could to be able to send my own children there. This school is a gem and I wish every child was lucky enough to attend and experience the MAGIC that is Jordan Glen.”</p></blockquote>
            <figcaption>— JG Alum/Parent</figcaption>
          </figure>
          <figure class="quote">
            <blockquote><p>“The way I sum Jordan Glen up is with the following example. There is an orange tree outside of the school. When all the oranges were ripe, the children picked and ate them. As the lower oranges disappeared, the bigger kids helped the smaller kids get the higher ones. When the higher ones disappeared, the biggest kid got a ladder and got the very highest ones down and shared them with the other kids. It operates as a family. …”</p></blockquote>
            <figcaption>— JG Parent</figcaption>
          </figure>
          <figure class="quote">
            <blockquote><p>“Jordan Glen’s impact on the lives of my children is immeasurable. The nurturing, creative, and highly skilled teachers made all the difference!”</p></blockquote>
            <figcaption>— JG Parent</figcaption>
          </figure>
        </div>
        <p><a href="{QUOTES}">Read the full set on the official testimonials page</a></p>
      </div>
    </section>
    <section class="section" id="alumni">
      <div class="wrap prose">
        <h2>Alumni</h2>
        <p>For over 45 years, Jordan Glen has celebrated, inspired, and empowered young minds. The alumni page invites graduates to register, check in, and support the nonprofit. Donations are tax-deductible.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="{ALUM_REG}">Register as an alumnus</a>
          <a class="btn btn-ghost" href="{ALUM_CHECK}">Alumni check-in</a>
          <a class="btn btn-ghost" href="support.html">Ways to give</a>
        </div>
      </div>
    </section>
    {cta_band()}
    """

    programs = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Programs</p>
      <h1>PreK through 8th grade, with the outdoors in the day.</h1>
      <p class="lede">Morning academics, afternoon electives, and a campus that is treated as a learning resource. Classrooms are multi-age, and the mix can change from year to year.</p>
    </header>
    <section class="section">
      <div class="wrap">
        {GRADE_NOTE}
        <div class="grid-3">
          <article class="card" id="prek">
            <h2>PreK–1st grade</h2>
            <p>By using outdoor spaces and giving ample play time alongside a traditional academic curriculum, the school aims to build a foundation that fosters a love of learning from a young age.</p>
          </article>
          <article class="card" id="elementary">
            <h2>2nd–4th grades</h2>
            <p>Students keep preparing academically for middle school and are given more leadership opportunities, with a focus on well-rounded, thoughtful students.</p>
          </article>
          <article class="card" id="middle">
            <h2>5th–8th grades</h2>
            <p>Middle school subscribes to a “work hard, play hard” mindset. The school says graduates leave prepared for the next chapter, with the tools to flourish.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap split">
        <div class="prose">
          <h2>How the day is organized</h2>
          <ul>
            <li>Drop-off begins at 8:30 a.m. Morning Meeting starts at 9:00 a.m.</li>
            <li>The school day is 9:00 a.m.–3:00 p.m.</li>
            <li>Foreign language and basic academic subjects are taught in the morning. Electives are in the afternoon.</li>
            <li>Core subjects named by the school: reading, math, social studies, science, and foreign language.</li>
            <li>For academics, children are grouped by age and ability and may move between groups to meet a learning need.</li>
            <li>Sports, outdoor time, and performing and fine arts are part of the curriculum, not an add-on.</li>
            <li>Aftercare, when offered, runs 3:00–6:00 p.m. on school days.</li>
          </ul>
          <p>The school follows its own calendar and tends to parallel local public school holidays. There is no school bus. Families can ask for help finding a carpool.</p>
        </div>
        <figure class="photo-frame">
          <img src="images/outdoors.jpg" width="1400" height="933" alt="Middle school students outdoors at Jordan Glen" loading="lazy">
          <figcaption>Middle schoolers outdoors, from the school’s public photos.</figcaption>
        </figure>
      </div>
    </section>
    <section class="section">
      <div class="wrap prose">
        <h2>Electives change every year</h2>
        <p>The FAQ lists examples, not a fixed menu: sports, karaoke, African drumming and dance, nature exploration, pottery, ukulele, doo-wop, drama, tennis, swimming, sewing, computer programming, sushi making, basketball, chorus, gardening, Ping Pong, and Random Act of Kindness.</p>
        <p>Recent newsletters have linked that term’s elective lists. Those PDFs are on the <a href="calendar.html#news">calendar and news page</a>.</p>
        <h2>After Jordan Glen</h2>
        <p>The school says most graduates enroll in high school magnet programs, including Eastside’s International Baccalaureate program, Gainesville High School’s Cambridge program, and P.K. Yonge’s performing arts program. Others enroll in public and private high schools in and around Gainesville.</p>
        <p><a href="admissions.html">Tuition, fees, and how to apply</a> · <a href="faq.html">FAQ</a></p>
      </div>
    </section>
    {cta_band()}
    """

    admissions = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Admissions</p>
      <h1>Tuition for 2026–27, and the forms the school already uses.</h1>
      <p class="lede">Figures below are copied from Jordan Glen’s tuition page for school year JG26-27. Nothing here is estimated.</p>
    </header>
    <section class="section">
      <div class="wrap">
        {GRADE_NOTE}
        <div class="table-wrap" tabindex="0">
          <table>
            <caption>Tuition for school year 2026–27</caption>
            <thead>
              <tr><th scope="col">Who</th><th scope="col">Amount</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">PreK</th><td>$11,000</td></tr>
              <tr><th scope="row">K–8th, one child</th><td>$14,200</td></tr>
              <tr><th scope="row">PreK–8th, two children</th><td>$12,350 per child</td></tr>
              <tr><th scope="row">PreK–8th, three or more children</th><td>$11,800 per child</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose">
          <p>Tuition is per school year. The school states there are no prorations or refunds. Jordan Glen does accept the Step Up Scholarship.</p>
          <aside class="todo">
            <p><strong>TODO — Step Up link.</strong> The tuition page says the school accepts the Step Up Scholarship and does not publish an application URL. Ask the school which scholarship program and how to apply.</p>
          </aside>
        </div>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap prose">
        <h2>Activity fee: $400 per student</h2>
        <p>The fee includes most books loaned for the school year, most field trips, pizza lunch on Fridays, and a softcover school yearbook.</p>
        <p>It does not include extracurricular activities, clubs, some special trips and events, student photocopier and printer use, or school supplies. The 2026–27 supply list is linked from the <a href="calendar.html">calendar page</a>.</p>
        <h2>Published forms</h2>
        <ol>
          <li><a href="{TOUR}">Request information</a> — the form the homepage uses, and the route the contact page gives for scheduling a tour along with a phone call.</li>
          <li><a href="{APPLY}">Admissions application</a>.</li>
          <li><a href="{ENROLL}">Enrollment form and release waiver</a>.</li>
        </ol>
        <p>The public pages do not spell out a numbered admissions timeline, deadlines, or what happens after the application is submitted. Those steps are intentionally not filled in here.</p>
        <aside class="todo">
          <p><strong>TODO — admissions timeline.</strong> Add decision dates, what families should expect after they apply, and whether a visit is required. None of that is on the current admissions or tuition pages.</p>
        </aside>
        <div class="cta-row">
          <a class="btn btn-primary" href="{APPLY}">Apply</a>
          <a class="btn btn-ghost" href="{TOUR}">Schedule a tour</a>
        </div>
      </div>
    </section>
    {cta_band()}
    """

    camp = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Summer camp 2026</p>
      <h1>Fifty summers and counting, on the same 20 acres.</h1>
      <p class="lede">June 8–July 17, 2026. For children entering grades K–8. Spots are limited, and there is a sibling discount.</p>
    </header>
    <section class="section">
      <div class="wrap split">
        <div class="prose">
          <h2>What camp is for</h2>
          <p>The camp’s main objective is for each child to enjoy time away from home through a wide variety of activities, and to build a healthy self-concept in a caring, supportive atmosphere. Staff are asked to respond to each child and to the group.</p>
          <p>The grounds include a large athletic field, swimming pool, tennis court, playground, woods, and a variety of plants and animals. The air-conditioned building has activity rooms, an art deck, a kitchen, a piano, and a multi-purpose room for large groups and rainy days.</p>
          <p>Most campers come from schools in greater Gainesville. Others visit from around the country and world, often when a parent is working at the University of Florida. The school has hosted campers and counselors from New York to California, and from Korea, Spain, France, Israel, Puerto Rico, Nicaragua, Colombia, Ecuador, and Brazil. There is no English-fluency requirement. The main spoken language is English.</p>
        </div>
        <figure class="photo-frame">
          <img src="images/playground.jpg" width="1400" height="931" alt="Students on the playground at Jordan Glen, with woods behind them" loading="lazy">
          <figcaption>Playground on the campus, from the school’s public photos.</figcaption>
        </figure>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap">
        <h2>2026 fees</h2>
        <p>There is no camp on Friday, July 3. Use one application for siblings. Each additional sibling receives a $100 discount per session. After you submit the application, Jordan Glen sends an invoice. Registration is confirmed once payment is received. Questions: <a href="mailto:info@jordanglen.org">info@jordanglen.org</a>.</p>
        <div class="table-wrap" tabindex="0">
          <table>
            <caption>Summer camp 2026 rates</caption>
            <thead>
              <tr><th scope="col">Session</th><th scope="col">Dates</th><th scope="col">Rate</th><th scope="col">JG student</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Sessions 1 &amp; 2</th><td>June 8–July 17 (6 weeks)</td><td>$2,050</td><td>$1,850</td></tr>
              <tr><th scope="row">Session 1</th><td>June 8–June 26 (3 weeks)</td><td>$1,250</td><td>$1,150</td></tr>
              <tr><th scope="row">Session 2</th><td>June 29–July 17 (3 weeks)</td><td>$1,250</td><td>$1,150</td></tr>
              <tr><th scope="row">Weekly</th><td>One week</td><td>$475</td><td>$425</td></tr>
            </tbody>
          </table>
        </div>
        <div class="cta-row">
          <a class="btn btn-primary" href="{CAMP_FORM}">Camp registration</a>
          <a class="btn btn-ghost" href="{CAMP_INFO}">Ask a camp question</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>A camp day</h2>
        <p>Camp runs 9:00 a.m.–2:30 p.m. Campers may arrive at 8:30 a.m. There is no official before-camp or after-camp childcare. Campers who need to stay are supervised until 3:00 p.m., and parents often arrange private childcare or rides with counselors.</p>
        <ol class="timeline">
          <li><time datetime="09:00">9:00–9:30</time><span>Morning Meeting in the auditorium. Groups take turns leading announcements, games, dances, and camp songs.</span></li>
          <li><time datetime="09:30">9:30–12:00</time><span>Sports, art, tennis, swimming, and group time. Junior campers usually skip morning tennis and can choose Beginning Tennis as an afternoon elective.</span></li>
          <li><time datetime="12:00">12:00–12:30</time><span>Lunch outside at picnic tables when weather allows. Junior campers usually eat at 11:30. On Fridays the camp eats together at noon.</span></li>
          <li><time datetime="12:30">12:30–2:15</time><span>Two afternoon electives. Campers choose four electives for the session. The menu changes each session and each season.</span></li>
          <li><time datetime="14:15">2:15–3:00</time><span>Cleanup and cool-down, then hangout and going home.</span></li>
        </ol>
        <p>Campers bring lunch Monday through Thursday. Friday is a pizza, cookout, or other special lunch the camp provides, always with a vegetarian option.</p>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap">
        <h2>Activities</h2>
        <p>Offerings change by year and by session. The school publishes these as the kinds of things camp includes.</p>
        <div class="grid-3">
          <article class="card"><h3>Swimming</h3><p>Daily when weather allows, including instruction for the youngest groups. Water activities are monitored by a certified lifeguard and camp staff.</p></article>
          <article class="card"><h3>Arts &amp; crafts</h3><p>Beading, tie-dye, jewelry, lanyards, macramé, puppetry, decoupage, wearable art, hair wraps, collage, doll making, quilting, friendship bracelets, sewing, knitting, paper craft, mosaic, weaving, and basketry.</p></article>
          <article class="card"><h3>Sports</h3><p>Soccer, tennis, basketball, baseball, ping pong, field hockey, gatorball, track and field, bocce, lacrosse, capture the flag, kickball, crab soccer, volleyball, flag football, table tennis, and disc golf.</p></article>
          <article class="card"><h3>Drama</h3><p>A variety of roles in performances, including an end-of-camp talent show.</p></article>
          <article class="card"><h3>Nature</h3><p>Time in the 20 acres of outdoor space.</p></article>
          <article class="card"><h3>And more</h3><p>Archery, cooking, dance, music, treasure hunts, shuffleboard, chess, Olympics, skyball, games, a carnival, and surprises.</p></article>
        </div>
        <div class="prose">
          <h2>Ages and ratios</h2>
          <p>Campers are typically 5–14 years old. The youngest are children entering kindergarten or currently in PreK. The oldest are children entering 9th grade. The overview page also says camp is for children entering grades K–8.</p>
          <ul>
            <li>Youngest group: about one counselor for every 4 or 5 campers.</li>
            <li>Intermediate group: about one counselor for every 7 or 8 campers.</li>
            <li>Oldest campers, ages 12–14: about one counselor for every dozen campers.</li>
            <li>Most groups also have one or two counselors-in-training.</li>
          </ul>
        </div>
      </div>
    </section>
    {cta_band()}
    """

    campus = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Campus life</p>
      <h1>A school day that starts outside the classroom door.</h1>
      <p class="lede">Informal and respectful. First names. Morning Meeting. A ratio the school puts at 15 students to 1 teacher, on average, with parents often helping in reading groups, math groups, lunch, and electives.</p>
    </header>
    <section class="section">
      <div class="wrap split">
        <figure class="photo-frame">
          <img src="images/aerial.jpg" width="1400" height="1097" alt="Satellite view of the Jordan Glen campus in Archer, showing woods, a clearing, buildings, a small pond, and a pool" loading="lazy">
          <figcaption>Satellite view supplied for this redesign, not from the school’s photo library.</figcaption>
        </figure>
        <div class="prose">
          <h2>What is on the grounds</h2>
          <p>Jordan Glen describes about 20 acres of field, orchard, and woods, eight miles west of Gainesville and just east of Archer. Camp materials add a large athletic field, swimming pool, tennis court, playground, activity rooms, art deck, kitchen, piano, and a multi-purpose room.</p>
          <p>From the air, the property is a wooded block with a clearing, several buildings, a small pond, and a bright pool. The school’s pages do not name the pond. It is called out here because it is visible in the satellite view.</p>
          <p>Directions, the map, and the phone number are on the <a href="contact.html">contact page</a>.</p>
        </div>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap">
        <h2>Hours</h2>
        <div class="table-wrap" tabindex="0">
          <table>
            <caption>School-day hours published on the parent portal</caption>
            <thead><tr><th scope="col">What</th><th scope="col">When</th></tr></thead>
            <tbody>
              <tr><th scope="row">Drop-off</th><td>From 8:30 a.m.</td></tr>
              <tr><th scope="row">School day</th><td>9:00 a.m.–3:00 p.m. Morning Meeting begins at 9:00.</td></tr>
              <tr><th scope="row">Pick-up</th><td>By 3:00 p.m.</td></tr>
              <tr><th scope="row">Aftercare</th><td>3:00–6:00 p.m., Monday–Friday, $15 a day per child</td></tr>
            </tbody>
          </table>
        </div>
        <div class="prose">
          <p>For aftercare, email <a href="mailto:info@jordanglen.org">info@jordanglen.org</a> or text <a href="tel:+13524952728">(352) 495-2728</a>. The school says billing is on the first Friday of each month, and lists Billie Hanna at <a href="tel:+13523630301">(352) 363-0301</a> as the aftercare contact.</p>
          <h2>Drop-off and pick-up</h2>
          <ol>
            <li>Use the drive-through lane in front of the school, or park in the gravel lot on the right as you enter.</li>
            <li>The drive-through lane parking is for teachers and staff. Please do not park there.</li>
            <li>If you walk in, park in the gravel lot and walk through the orchard and school.</li>
            <li>Leave toward the tennis and basketball courts. Do not exit back through the entrance.</li>
          </ol>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div class="prose">
          <h2>Lunch, snacks, and water</h2>
          <p>Pack a substantial, nourishing lunch. On Fridays the school provides pizza and lemonade, so no lunch is needed that day. The activity fee covers Friday pizza.</p>
          <p>Send at least two snacks. The school suggests fresh fruit, nuts or trail mix, granola bars, cut vegetables with hummus, and protein-rich snacks. Every child should bring a reusable water bottle. Snack donations are welcome, especially for younger students.</p>
        </div>
        <figure class="photo-frame">
          <img src="images/garden.jpg" width="768" height="510" alt="Students gardening at Jordan Glen" loading="lazy">
          <figcaption>Gardening, from the school’s public photos.</figcaption>
        </figure>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap">
        <h2>After-school activities</h2>
        <p>The school says offerings and cost can change. Several programs are paid directly to the provider, and several do not add an aftercare fee.</p>
        <div class="offer-grid">
          <article class="offer">
            <h3>Tennis lessons / clinics</h3>
            <p class="role">Mondays · grades K–8 · paid to the provider</p>
            <p>Beginner 3:30–4:30 p.m. Intermediate and advanced 3:30–5:00 p.m. Dave Porter, Jonesville Tennis Center. Start dates and payment are emailed.</p>
          </article>
          <article class="offer">
            <h3>Music</h3>
            <p class="role">Scheduled individually · all grades</p>
            <p>Private lessons with Benny Cannon, <a href="tel:+13523179376">(352) 317-9376</a>. Paid to the provider. No aftercare fee.</p>
          </article>
          <article class="offer">
            <h3>Art club</h3>
            <p class="role">Tuesdays and Wednesdays · 3:00–4:00 p.m.</p>
            <p>$150 per term. Term 1–3, 10 sessions. Chelsee Florence, <a href="tel:+16123861200">(612) 386-1200</a>. No aftercare fee.</p>
          </article>
          <article class="offer">
            <h3>Chess club</h3>
            <p class="role">Wednesdays · 3:00–4:45 p.m. · all grades</p>
            <p>Paid to the provider. Miguel Ararat, <a href="tel:+13522139707">(352) 213-9707</a>. No aftercare fee.</p>
          </article>
          <article class="offer">
            <h3>Study hall</h3>
            <p class="role">Monday–Friday · 3:00–4:00 p.m.</p>
            <p>$15 a day, including aftercare. Supervised by Jordan Glen. Students can join aftercare at 4:00 p.m.</p>
          </article>
          <article class="offer">
            <h3>Robotics</h3>
            <p class="role">Wednesday · 2:30–4:00 p.m. · grades 3–8</p>
            <p>$250 annually. Run by Jordan Glen. No aftercare fee.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <figure class="photo-frame">
          <img src="images/arts.jpg" width="640" height="640" alt="Students making art at Jordan Glen" loading="lazy">
        </figure>
        <figure class="photo-frame">
          <img src="images/trees.jpg" width="276" height="376" alt="Young children with a tree at Jordan Glen" loading="lazy">
        </figure>
      </div>
    </section>
    {cta_band()}
    """

    calendar = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Calendar &amp; news</p>
      <h1>The 2026–27 calendar, and letters the school has posted.</h1>
      <p class="lede">The school year runs on Jordan Glen’s own calendar, which tends to follow local public-school holidays. The day itself is 9:00 a.m.–3:00 p.m.</p>
    </header>
    <section class="section">
      <div class="wrap prose">
        <h2>2026–27 school calendar</h2>
        <p>The current site publishes the year as a PDF and as a PNG, and embeds the school Google Calendar. A typed list of dates was not published as HTML.</p>
        <aside class="todo">
          <p><strong>TODO — text calendar.</strong> Add the 2026–27 dates as text on this page. Right now families have to open the PDF, the PNG, or the Google Calendar.</p>
        </aside>
        <div class="cta-row">
          <a class="btn btn-primary" href="{CAL_PDF}">Download the 2026–27 calendar (PDF)</a>
          <a class="btn btn-ghost" href="{CAL_PNG}">View the calendar image</a>
          <a class="btn btn-ghost" href="{SUPPLY}">2026–27 supply list (PDF)</a>
          <a class="btn btn-ghost" href="{GCAL_OPEN}">Open in Google Calendar</a>
        </div>
        <div class="frame">
          <iframe title="Jordan Glen Google Calendar" src="{GCAL}" loading="lazy"></iframe>
        </div>
        <p class="fine">On October 23, 2026, the event list on jordanglen.org said “No upcoming events found.” The Google Calendar above is the live calendar the school publishes.</p>
      </div>
    </section>
    <section class="section band-sand" id="news">
      <div class="wrap">
        <h2>News</h2>
        <div class="news-list">
          <article class="news-item">
            <time datetime="2025-10-21">October 21, 2025</time>
            <h3>JG Winter 2025 Newsletter</h3>
            <p>As the new year started, the school shared Term One updates. The post links a PDF named Newsletter-January-2025.</p>
            <p><a href="{WINTER_POST}">Post</a> · <a href="{WINTER_PDF}">Newsletter PDF</a></p>
          </article>
          <article class="news-item">
            <time datetime="2024-02-27">February 27, 2024</time>
            <h3>JG Spring 2024 Newsletter</h3>
            <p>Term Three updates, signed “Love, Us,” with a link to that term’s electives.</p>
            <p><a href="{SPRING_POST}">Post</a> · <a href="{SPRING_PDF}">Newsletter PDF</a> · <a href="{SPRING_ELEC}">Term 3 electives PDF</a></p>
          </article>
          <article class="news-item">
            <time datetime="2023-11-14">November 14, 2023</time>
            <h3>JG Fall 2023 Newsletter</h3>
            <p>Term Two notes, that term’s electives, and an invitation to the JG Thanksgiving Feast.</p>
            <p><a href="{FALL_POST}">Post</a> · <a href="{FALL_PDF}">Newsletter PDF</a> · <a href="{FALL_ELEC}">Term 2 electives PDF</a></p>
          </article>
          <article class="news-item">
            <time datetime="2022-08-30">August 30, 2022</time>
            <h3>Our brand new website</h3>
            <p>The school announced the current jordanglen.org site and thanked Douglas at Rogue Media.</p>
            <p><a href="{OFFICIAL}/our-brand-new-website/">Post</a></p>
          </article>
          <article class="news-item">
            <time datetime="2022-08-29">August 29, 2022</time>
            <h3>A nod to our history</h3>
            <p>A short note pointing alumni and families to the history page.</p>
            <p><a href="{OFFICIAL}/a-nod-to-our-history/">Post</a></p>
          </article>
          <article class="news-item">
            <time datetime="2022-08-28">August 28, 2022</time>
            <h3>Are you an alum?</h3>
            <p>Graduates were invited to sign up for updates.</p>
            <p><a href="{OFFICIAL}/are-you-an-alumni/">Post</a> · <a href="{ALUM_REG}">Alumni registration</a></p>
          </article>
        </div>
      </div>
    </section>
    {cta_band()}
    """

    support = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Support &amp; donate</p>
      <h1>Give a little bit of love and it all comes back to you.</h1>
      <p class="lede">Jordan Glen School &amp; Summer Camp is a 501(c)(3) nonprofit. The school says donations are tax-deductible. Giving stays on the school’s own forms.</p>
    </header>
    <section class="section">
      <div class="wrap">
        <aside class="todo">
          <p><strong>TODO — EIN.</strong> The public site does not print a federal tax ID. Add the EIN before this page is used for gift receipts or employer matching.</p>
        </aside>
        <div class="grid-3">
          <article class="card">
            <h2>Card, monthly, or annual</h2>
            <p>The donate page takes credit cards and describes one-time, monthly, and annual gifts.</p>
            <p><a href="{DONATE}">Open the school’s donate form</a></p>
          </article>
          <article class="card">
            <h2>PayPal or Venmo</h2>
            <p>PayPal: info@jordanglen.org</p>
            <p>Venmo: (352) 495-2728</p>
          </article>
          <article class="card">
            <h2>Mail, fax, or email</h2>
            <p>Jordan Glen School, 12425 SW 154 St., Archer, FL 32618. Fax 352-495-1539.</p>
            <p><a href="{DON_PDF}">Printable donation form (PDF)</a><br><a href="{RECEIPT}">Donation receipt (PDF)</a></p>
          </article>
        </div>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap prose">
        <h2>Other ways the school invites support</h2>
        <h3>Leave a legacy</h3>
        <p>The donate page suggests a beneficiary form on a retirement account or insurance policy, a bequest in a will or trust, or naming Jordan Glen on a bank or investment account.</p>
        <h3>Retirement funds</h3>
        <p>If you are at least 70½, the school says you can contribute directly from an IRA. They ask you to contact your financial advisor to start a qualified charitable distribution.</p>
        <h3>Things, not only money</h3>
        <p>Non-cash gifts can be deductible. The school asks you to check before discarding a computer, books, furniture, or other goods that might be useful. They also accept school and office supplies, and household items such as paper towels, toilet paper, paper plates, and plastic cutlery. A receipt for tax purposes is available on request.</p>
        <div class="cta-row">
          <a class="btn btn-primary" href="{DONATE}">Donate</a>
          <a class="btn btn-ghost" href="{DONATE_INQ}">Donation inquiry</a>
          <a class="btn btn-ghost" href="{ALUM_REG}">Alumni registration</a>
        </div>
        <p>The school’s “Support our Nonprofit” page currently has no body text of its own. The options above come from the donate page.</p>
      </div>
    </section>
    {cta_band()}
    """

    contact = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">Contact</p>
      <h1>Twenty acres, just east of Archer.</h1>
      <p class="lede">Call or send a message to schedule a tour. The school is in a rural setting of playing fields, orchards, and woods, about ten minutes west of Gainesville.</p>
    </header>
    <section class="section">
      <div class="wrap split">
        <div class="prose">
          <h2>Jordan Glen School &amp; Summer Camp</h2>
          <p>
            12425 SW 154th Street<br>
            Archer, FL 32618
          </p>
          <p>
            <a href="tel:+13524952728">(352) 495-2728</a><br>
            <a href="mailto:info@jordanglen.org">info@jordanglen.org</a><br>
            Fax 352-495-1539
          </p>
          <h2>How to get here</h2>
          <p>From Gainesville, head west on Archer Road and turn left onto 154th Street at the Jordan Glen School sign. The homepage describes the drive as eight miles west of Gainesville. The contact page says about ten minutes west of Gainesville, just east of Archer.</p>
          <div class="cta-row">
            <a class="btn btn-primary" href="{TOUR}">Schedule a tour</a>
            <a class="btn btn-ghost" href="{MAP}">Open in Google Maps</a>
          </div>
          <p class="fine">There is no separate tour form. The contact page says to call or send a message. The button uses the school’s request-information form.</p>
        </div>
        <div>
          <div class="frame">
            <iframe title="Map showing Jordan Glen School at 12425 SW 154th Street, Archer, Florida" src="https://www.openstreetmap.org/export/embed.html?bbox=-82.5143%2C29.5358%2C-82.4983%2C29.5458&amp;layer=mapnik&amp;marker=29.5407862%2C-82.5062792" loading="lazy"></iframe>
          </div>
          <p class="fine"><a href="{MAP}">12425 SW 154th Street on Google Maps</a></p>
        </div>
      </div>
    </section>
    <section class="section band-sand">
      <div class="wrap prose">
        <h2>Employment</h2>
        <p>The FAQ says there are currently no new teacher positions anticipated. You may send a resume with your qualifications and experience for the school to keep on file. There is no separate jobs page on the current site. Send questions through <a href="{TOUR}">the information form</a> or call the office.</p>
        <p><a href="faq.html">Read the FAQ</a> · <a href="{PARENT}">Parent portal</a></p>
      </div>
    </section>
    {cta_band()}
    """

    faq_items = [
        ("philosophy", "Does Jordan Glen follow a particular philosophy?",
         "We believe that every child is gifted, and while there are universal and predictable sequences of change in children, each child is unique with an individual pattern of timing and growth. Our commitment is to an educational program that values individual differences, to a process of exploration and discovery, and to meaningful academic study inspired and guided by our natural environment. We would like our children to enjoy their time spent away from home and feel that we exemplify our belief that the joy of living and love of learning need never be separated."),
        ("teachers", "Who are Jordan Glen’s teachers?",
         "Our faculty is comprised of dedicated professionals with diverse backgrounds, some of whom were raised as Jordan Glen students themselves, and who now have their own children at the school. Jordan Glen’s teachers provide stimulating, challenging, and diverse curricula to spark interest. To understand the individual needs, skills, and interests of a child requires teachers with a wealth of knowledge and understanding of child development."),
        ("location", "Where are you located and how do I get there?",
         "Our address is 12425 SW 154th Street, Archer, Florida 32618. To find us from Gainesville, head west on Archer Road and turn left onto 154th Street at the Jordan Glen School sign."),
        ("schedule", "Does your school follow the public school schedule?",
         "Our school day is 9:00 a.m.–3:00 p.m. We follow our own independent calendar, but we tend to parallel the local public school calendar. Most of our school holidays are the same as the public school holidays."),
        ("ratio", "What is your student-to-teacher ratio?",
         "Student-to-teacher ratio is 15 to 1 on average. Parent volunteers frequently provide additional assistance with small reading and math groups, lunchtime supervision, and a variety of afternoon electives classes."),
        ("grades", "What grades do you offer? How are the grades divided?",
         "Jordan Glen now starts with Kindergarten and continues through 8th grade. The classroom organization can vary depending on that year’s demographics. While ability levels often separate for instruction, our mixed-grade teaching philosophy and small family atmosphere allow students of different ages and grades to assist and mentor each other, for example 5th–8th grade history groups, and Reading Buddies between the middle schoolers and K–1 students."),
        ("curriculum", "How does your curriculum compare with public schools?",
         "Jordan Glen provides a strong foundation in the core academic subjects, including reading, math, social studies, science, and foreign language. For academics, children are grouped by age and ability and may move from one group to another in order to meet specific learning needs. Foreign language and basic academic subjects are taught in the morning, with diverse electives offered in the afternoon. Also integrated as a focus of the curriculum are sports and other outdoor activities, as well as performing and fine arts."),
        ("electives", "What elective classes are typically offered?",
         "Electives vary from year to year and may include sports, karaoke, African drumming and dance, nature exploration, pottery, ukulele, doo-wop, drama, tennis, swimming, sewing, computer programming, sushi making, basketball, chorus, gardening, Ping Pong, and Random Act of Kindness."),
        ("jobs", "Are you accepting new teachers?",
         "Currently there are no new teacher positions anticipated. You are welcome to send a resume with your qualifications and experience for the school to keep on file."),
        ("bus", "Is there a school bus?",
         "We no longer offer school bus service. We will be happy to help suggest a carpool option with another Jordan Glen family."),
        ("aftercare", "Do you have an afterschool program?",
         "Jordan Glen typically offers an aftercare program on the school premises from 3:00 to 6:00 p.m. on school days. This program provides children with a safe and enjoyable place to be after school. The parent portal lists the cost as $15 a day per child."),
        ("graduates", "Where do students go after graduating?",
         "The majority of graduates enroll in high school magnet programs, such as Eastside’s International Baccalaureate program, Gainesville High School’s Cambridge program, and P.K. Yonge’s performing arts program. Students also enroll directly in public and private high schools in Gainesville and the surrounding area."),
        ("contact-faq", "What is the best way to contact Jordan Glen?",
         "You may call Jordan Glen at 352-495-2728, or use the request-information form."),
    ]
    details = []
    for fid, question, answer in faq_items:
        details.append(
            f"""<details id="{fid}">
              <summary>{question}</summary>
              <p>{answer}</p>
            </details>"""
        )
    faq = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">FAQ</p>
      <h1>Questions the school already answers.</h1>
      <p class="lede">Answers follow the public FAQ. Where another current page disagrees, that disagreement is marked.</p>
    </header>
    <section class="section">
      <div class="wrap prose faq-list">
        {GRADE_NOTE}
        {''.join(details)}
        <p>Something missing? <a href="{TOUR}">Send a message</a> or call <a href="tel:+13524952728">(352) 495-2728</a>.</p>
      </div>
    </section>
    {cta_band()}
    """

    missing = f"""
    <header class="wrap page-hero">
      <p class="eyebrow">404</p>
      <h1>That page is not on this redesign.</h1>
      <p class="lede">Try the main sections, or go back to the official Jordan Glen site.</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="index.html">Back home</a>
        <a class="btn btn-ghost" href="{OFFICIAL}/">jordanglen.org</a>
      </div>
    </header>
    """

    return {
        "index.html": (
            "Jordan Glen School & Summer Camp | Archer, Florida",
            "Nonprofit PreK–8 school and summer camp on 20 acres in Archer, Florida, eight miles west of Gainesville. Unofficial redesign concept.",
            home,
        ),
        "about.html": (
            "About Jordan Glen | History, Philosophy & Faculty",
            "Jordan Glen’s philosophy, the faculty listed on the current site, alumni links, and published parent and alumni quotes.",
            about,
        ),
        "programs.html": (
            "Programs | PreK–8 at Jordan Glen School",
            "PreK–1, 2nd–4th, and 5th–8th at Jordan Glen: mixed-grade classes, morning academics, afternoon electives, and daily outdoor time.",
            programs,
        ),
        "admissions.html": (
            "Admissions & Tuition | Jordan Glen School",
            "2026–27 tuition from Jordan Glen’s site: PreK $11,000, K–8 $14,200, sibling rates, a $400 activity fee, and links to the real application.",
            admissions,
        ),
        "summer-camp.html": (
            "Summer Camp 2026 | Jordan Glen",
            "Jordan Glen Summer Camp runs June 8–July 17, 2026 for children entering grades K–8. Fees, daily schedule, and the school’s registration form.",
            camp,
        ),
        "campus.html": (
            "Campus Life | Jordan Glen School",
            "Hours, drop-off, lunch, aftercare, and after-school clubs on Jordan Glen’s 20-acre campus in Archer, Florida.",
            campus,
        ),
        "calendar.html": (
            "Calendar & News | Jordan Glen School",
            "Jordan Glen’s 2026–27 calendar PDF, supply list, Google Calendar, and recent newsletters.",
            calendar,
        ),
        "support.html": (
            "Support & Donate | Jordan Glen School",
            "Tax-deductible ways to give to Jordan Glen School & Summer Camp, using the school’s existing donate form, PayPal, Venmo, and mail.",
            support,
        ),
        "contact.html": (
            "Contact | Jordan Glen School & Summer Camp",
            "Jordan Glen School & Summer Camp, 12425 SW 154th Street, Archer, FL 32618. Phone (352) 495-2728. Map and tour request.",
            contact,
        ),
        "faq.html": (
            "FAQ | Jordan Glen School",
            "Jordan Glen’s published answers on philosophy, grades, ratio, curriculum, aftercare, transportation, and what graduates do next.",
            faq,
        ),
        "404.html": (
            "Page not found | Jordan Glen redesign",
            "This unofficial Jordan Glen redesign does not have that page.",
            missing,
        ),
    }


def sitemap(names: list[str]) -> str:
    urls = []
    for name in names:
        if name == "404.html":
            continue
        loc = f"{BASE}/" if name == "index.html" else f"{BASE}/{name}"
        urls.append(
            f"  <url><loc>{loc}</loc><lastmod>2026-10-23</lastmod></url>"
        )
    body = "\n".join(urls)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n"
    )


def main() -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    rendered = pages()
    for name, (title, description, body) in rendered.items():
        html = layout(name, title, description, body)
        (SITE / name).write_text(html, encoding="utf-8")
        print("wrote", name)
    (SITE / "sitemap.xml").write_text(sitemap(list(rendered)), encoding="utf-8")
    (SITE / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: "
        f"{BASE}/sitemap.xml\n",
        encoding="utf-8",
    )
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    print("wrote sitemap, robots, .nojekyll")


if __name__ == "__main__":
    main()
