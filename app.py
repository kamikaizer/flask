from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home1():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/crud")
def crud():
    return render_template("crud.html")


if __name__ == "__main__":
    app.run(port = 5000, debug=True)