from flask import Blueprint, render_template
from loremipsum import get_sentences

about_text = get_sentences(10, True)

about_app = Blueprint("about_app", __name__)

@about_app.route("/", endpoint="about")
def get_about():
    return render_template("about/about.html", context = about_text)