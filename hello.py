from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = "piyo"
    enemies = ["スライム", "モンスター", "ドラゴン"]
    return render_template("index.html", name = name, enemies = enemies)

@app.route("/info")
def info():
    return "Info"