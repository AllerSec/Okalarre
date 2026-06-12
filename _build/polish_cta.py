# One-off: convert the flat forest CTA section into the photo cta-banner on every page.
import re
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
files = (
    list(root.glob("*.html"))
    + list(root.glob("en/*.html"))
    + list(root.glob("eu/*.html"))
    + list(root.glob("fr/*.html"))
)

LEAF = '''    <div class="leaf-divider" aria-hidden="true"><span class="rule"></span>
<svg viewBox="0 0 120 48" fill="none"><g stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M8 24 H112"/></g><g fill="currentColor"><path class="leaf-l" d="M46 24c-4-7-12-9-18-7 1 6 7 11 14 11 2 0 3-1 4-4z"/><path class="leaf-r" d="M60 24c4-7 12-9 18-7-1 6-7 11-14 11-2 0-3-1-4-4z"/><path class="leaf-t" d="M53 20c-3-6-2-13 2-18 4 5 5 12 2 18-1 1-3 1-4 0z"/></g></svg>
<span class="rule r"></span></div>'''

pat = re.compile(
    r'<section class="section bg-forest text-center">\n  <div class="container container--narrow">\n'
    + re.escape(LEAF)
    + r'\n    <h2 class="reveal" style="color:var\(--cream\)">(.*?)</h2>\n'
    + r'    <p class="reveal" style="color:rgba\(245,241,232,\.85\);margin:1rem auto 2rem">(.*?)</p>',
    re.S,
)

for f in files:
    txt = f.read_text(encoding="utf-8")
    prefix = "../" if f.parent != root else ""

    def rep(m, prefix=prefix):
        return (
            '<section class="cta-banner">\n'
            f'  <div class="cta-banner__bg"><img src="{prefix}assets/img/gallery/gallery-11.webp" alt="" loading="lazy" decoding="async" width="1200" height="800"></div>\n'
            '  <div class="container container--narrow">\n' + LEAF + '\n'
            f'    <h2 class="reveal">{m.group(1)}</h2>\n'
            f'    <p class="reveal" style="margin:1rem auto 2rem">{m.group(2)}</p>'
        )

    new, n = pat.subn(rep, txt)
    if n:
        f.write_text(new, encoding="utf-8")
        print(f.relative_to(root), n)
