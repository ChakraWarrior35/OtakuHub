from flask import Flask, render_template,request
import flask

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        # Handle login logic here
        pass
        return render_template("index.html")
    else:
        return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def create_account():
    if flask.request.method == 'POST':
        # Handle registration logic here
        pass
        return render_template("login.html")
    else:
        return render_template("create_account.html")

@app.route("/add_tocart")
def add_to_cart():
    return render_template("add_tocart.html")

if __name__ == "__main__":
    app.run(debug=True)
