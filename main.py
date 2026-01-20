from flask import Flask, render_template

app = Flask(__name__)

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/book")
def books():
    return render_template("book.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
