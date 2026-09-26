"""Build the static article index and article pages; no third-party packages required."""
import argparse, json, re
from pathlib import Path
from html import escape
from datetime import date

ROOT = Path(__file__).resolve().parent

def build(base_path=""):
    base_path = "/" + base_path.strip("/") if base_path.strip("/") else ""
    def site_links(html):
        return re.sub(r'(href|src)="/(?!/)', lambda m: m.group(1) + '="' + base_path + "/", html)
    home = (ROOT / 'content/home.html').read_text()
    articles = json.loads((ROOT / 'content/articles.json').read_text())
    published = [a for a in articles if a.get('published') is True]
    slugs = set()
    for a in published:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', a['slug']), 'Use a lowercase, hyphenated slug'
        assert a['slug'] not in slugs, 'Duplicate article slug'
        slugs.add(a['slug'])
        date.fromisoformat(a['date'])
        for key in ('title', 'summary', 'paragraphs'):
            assert a.get(key), f'Missing {key}'
    published.sort(key=lambda a: a['date'], reverse=True)
    cards = []
    for a in published:
        title, summary = escape(a['title']), escape(a['summary'], quote=True)
        formatted = date.fromisoformat(a['date']).strftime('%B %d, %Y')
        cards.append(f'<a class="article-row" href="/articles/{a["slug"]}/"><p class="eyebrow">{formatted}</p><h3>{title} ↗</h3><p>{summary}</p></a>')
        head = home.split('</head>')[0]
        head = re.sub(r'<title>.*?</title>', f'<title>{title} — Deke Baley</title>', head)
        head = re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{summary}">', head)
        body = ''.join(f'<p>{escape(p)}</p>' for p in a['paragraphs'])
        page = f'{head}</head><body><header class="header wrap"><a class="brand" href="/">Deke Baley</a><a href="/#articles">← All articles</a></header><main class="wrap article-body"><p class="eyebrow">FIELD NOTES / DEKE BALEY</p><h1>{title}</h1><time datetime="{a["date"]}">{formatted}</time>{body}<a class="text-link" href="/#contact">Connect with Deke ↗</a></main></body></html>'
        folder = ROOT / 'dist/articles' / a['slug']
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'index.html').write_text(site_links(page))
    # Remove only generated article pages whose records were removed or unpublished.
    for old in (ROOT / 'dist/articles').glob('*/index.html'):
        if old.parent.name not in slugs:
            old.unlink()
            old.parent.rmdir()
    if cards:
        home = re.sub(r'<div id="article-list">.*?</section>', '<div id="article-list">' + ''.join(cards) + '</div></section>', home, flags=re.S)
    (ROOT / 'dist/index.html').write_text(site_links(home))
    print(f'Built homepage and {len(published)} published articles.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-path', default='', help='URL prefix for a GitHub Pages project site')
    build(parser.parse_args().base_path)
