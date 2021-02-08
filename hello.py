from flask import Flask, render_template
app = Flask(__name__)

name = "page"

@app.route("/")
def menu():
  return render_template("menu.html", name = name)

@app.route("/get")
def get():
  message = name + "は、get"
  return render_template("action.html", name = name, message = message)

@app.route("/post")
def post():
  message = name + "は、post"
  return render_template("action.html", name = name, message = message)