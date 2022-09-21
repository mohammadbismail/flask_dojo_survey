from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def make_user():
    name_from_form = request.form["name"]
    location_from_form = request.form["location"]
    language_from_form = request.form["language"]
    comment_from_form = request.form["comment"]
    return render_template(
        "result.html",
        name=name_from_form,
        location=location_from_form,
        language=language_from_form,
        comment=comment_from_form,
    )
