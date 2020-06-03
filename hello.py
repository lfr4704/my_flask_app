# hello.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = 2 + 2
    print("visiting the home page")
    return f"Hello World! {x}"

@app.route("/about")
def about():
    print("visiting the about page")
    return "About me"
