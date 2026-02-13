from flask import Flask, render_template, request

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

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
       name =request.form.get("name")
       email =request.form.get("email")
    message =request.form.get("message")
    return render_template("contact.html", name=name, email=email, message=message)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = mongo.db.user.find_one({
            "email": email,
            "password": password
        })
        if user:
            return "Login successful!"
        else:
            return "Invalid email or password." 
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def create_account():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        mongo.db.user.insert_one({
            "name": name,
            "email": email,
            "password": password
        })
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
