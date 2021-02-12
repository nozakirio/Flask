from flask import Flask, request, render_template
app = Flask(__name__)

name = "book"

@app.route("/")
def menu():
  return render_template("menu.html", name = name)

@app.route("/show")
def show():
  message = name + "の、post"
  return render_template("show.html", name = name, message = message)

@app.route("/form")
def form():
  return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
  title = request.form["title"]
  comment = request.form["comment"]
  return render_template("show.html", title = title, comment = comment)

@app.route("/search")
def search():
  words = request.args.get("words")
  return render_template("search.html", words = words)