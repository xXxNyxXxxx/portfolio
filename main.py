"""Flask entry point for the developer portfolio."""
import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, abort, render_template

from data import CREDENTIALS, EXPERIENCE, PROFILE, PROJECTS, SKILLS

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")


@app.context_processor
def inject_globals():
    """Make profile data and the current year available in every template."""
    return {"profile": PROFILE, "year": datetime.now().year}


@app.route("/")
def index():
    featured = [p for p in PROJECTS if p.get("featured")]
    return render_template(
        "index.html",
        projects=featured,
        skills=SKILLS,
        experience=EXPERIENCE,
        credentials=CREDENTIALS,
    )


@app.route("/project/<string:project_id>")
def project(project_id):
    item = next((p for p in PROJECTS if p["id"] == project_id), None)
    if item is None:
        abort(404)
    return render_template("project.html", project=item)


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(_error):
    return render_template("404.html", server_error=True), 500


if __name__ == "__main__":
    # Debug is OFF unless FLASK_DEBUG=1 is set in your local .env
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
