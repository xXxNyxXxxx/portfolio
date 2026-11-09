# Developer Portfolio (Flask)

## Run locally
```bash
python -m venv venv
source venv/Scripts/activate      # Git Bash on Windows (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
python main.py                    # http://127.0.0.1:5000
```

## Add a project
Append a dictionary to `PROJECTS` in `data.py` (set `"featured": True` to show it on the homepage). No HTML edits needed.

## Push to GitHub
```bash
git init && git add . && git commit -m "Initial portfolio"
git branch -M main
git remote add origin https://github.com/your-username/portfolio.git
git push -u origin main
```

## Deploy on Render
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn main:app`
- Environment variables: `SECRET_KEY` (long random string), `FLASK_DEBUG=0`

## Deploy on PythonAnywhere
Create a virtualenv, `pip install -r requirements.txt`, point the WSGI file at `from main import app as application`, and set `SECRET_KEY` in the WSGI file via `os.environ`.
