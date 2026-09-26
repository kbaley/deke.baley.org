# Deke Baley professional website

A responsive, dependency-free website with a static article publishing workflow.

## Preview

From this directory, run `python3 -m http.server 4173 --directory dist`, then open http://localhost:4173.

## Edit the homepage

Edit `content/home.html` and run `python3 build.py`. Styling is in `dist/styles.css`.

## Publish an article

Add an object to the array in `content/articles.json`:

```json
{
  "slug": "your-article-title",
  "title": "Your article title",
  "date": "2026-10-01",
  "summary": "A short description for the homepage.",
  "published": false,
  "paragraphs": ["First paragraph.", "Second paragraph."]
}
```

Set `published` to `true` when ready, run `python3 build.py`, and publish the updated site. Each article gets a separate URL and the homepage lists the newest first. Keep draft records unpublished. Text is escaped automatically. No sample articles are presented as Deke's writing. This is a file-based workflow, not a browser-based content editor.

## Content evidence and review

- User brief: desired AutoCAD drafting, plan checking and project management work; experience in civil, land development, oil/gas and geomatics.
- https://www.c2innovate.com/our-c2-team — Deke's Project Manager / QA/QC role and supplied portrait.
- https://www.c2innovate.com/ — business services.
- https://www.geoverra.com/project/padcom-russell-mcauley-deposit/ — project context and attributed client quote. Team accomplishments are not presented as Deke's individual work.
- https://www.linkedin.com/in/deke-baley/ — linked for visitors; its content could not be retrieved during authoring.

Contact email: deke@baley.org, supplied by the user. Confirm employment history with Deke before making the site public. No years-of-experience total, employment dates, licensing credentials or unverified software proficiency claims were invented. The company-wide 75 years of combined experience is deliberately not attributed to him. The site initially deploys privately for review.
