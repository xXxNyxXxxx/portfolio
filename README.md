# Camille Contemprato | Developer Portfolio

A responsive, dark-mode portfolio built with Flask and Jinja2. All content lives in one Python data file, so updating the site never means editing HTML.

**Live site:** https://camille-portfolio.onrender.com

> The site is hosted on Render's free plan. If it hasn't had visitors for a while, the first load can take up to a minute while the server wakes up.

## Features

- Content separated from layout: projects, skills, and experience are defined in `data.py`
- Dynamic project pages through slug routing (`/project/<project_id>`)
- Jinja2 template inheritance with a shared base layout
- Responsive Bootstrap 5 layout with custom dark theme styling
- Custom 404 and 500 error pages
- Secrets loaded from environment variables, with debug mode off by default

## Tech stack

| Area | Tools |
| --- | --- |
| Backend | Python, Flask, Werkzeug |
| Frontend | HTML5, Jinja2, Bootstrap 5, CSS3 |
| Config | python-dotenv |
| Deployment | Gunicorn, Render, GitHub |

## Project structure

```
portfolio/
├── main.py              # Flask app, routes, error handlers
├── data.py              # All site content (profile, skills, projects, experience)
├── requirements.txt     # Pinned dependencies
├── .env.example         # Template for environment variables
├── static/css/style.css # Custom styling
└── templates/
    ├── base.html        # Shared layout: navbar and footer
    ├── index.html       # Home page
    ├── project.html     # Project detail page
    └── 404.html         # Error page
```

## Run locally

```bash
git clone https://github.com/xXxNyxXxxx/portfolio.git
cd portfolio
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
cp .env.example .env               # then set SECRET_KEY in .env
python main.py
```

Open http://127.0.0.1:5000. Generate a secret key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Set `FLASK_DEBUG=1` in your local `.env` for development. Leave it unset in production.

## Add a project

Append a dictionary to `PROJECTS` in `data.py`:

```python
{
    "id": "my-project",            # becomes /project/my-project
    "title": "My Project",
    "summary": "One line shown on the card.",
    "description": "A short paragraph for the detail page.",
    "highlights": ["What I did", "Another point"],
    "tech": ["Python", "Flask"],
    "github": None,                # or a URL
    "live": None,                  # or a URL
    "featured": True,              # show on the home page
}
```

No HTML changes are needed.

## Deployment

Deployed on Render as a web service connected to this repository:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn main:app`
- Environment variable: `SECRET_KEY`

Pushing to `main` triggers an automatic redeploy.

## Contact

- Email: millecontemprato02@gmail.com
- LinkedIn: https://linkedin.com/in/camille-contemprato
- GitHub: https://github.com/xXxNyxXxxx