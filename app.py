import os

from flask import Flask, render_template, request, session
from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "portfolio-language-preference")


@app.route("/")
def index():
    language = session.get("language", "en")
    translations = TRANSLATIONS[language]
    return render_template(
        "10spage.html",
        t=translations,
        lang=language,
    )



@app.route("/home")
def home():
    requested_language = request.args.get("lang")
    if requested_language in TRANSLATIONS:
        session["language"] = requested_language

    language = session.get("language", "en")
    translations = TRANSLATIONS[language]
    return render_template(
        "index.html",
        t=translations,
        lang=language,
    )


if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5001, debug=True)
