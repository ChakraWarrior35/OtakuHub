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

@app.route("/register")
def create_account():
    return render_template("create_account.html")

@app.route("/add_tocart")
def add_to_cart():
    return render_template("add_tocart.html")

@app.route("/anime")
def anime():
    return render_template("anime.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/spiritual")
def spiritual():
    return render_template("spiritual.html")


if __name__ == "__main__":
    app.run(debug=True)
