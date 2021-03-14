import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # User check in database if existing
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into session/temporary cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # Redirects the user to the profile of its own
        return redirect(url_for("profile", username=session["user"]))

    # Render register.html template if method is not POST, GET
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # username check in mongodb
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # makes sure hashed password matches
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    # If it exists username will temporary be saved to session, which is a temporary cookie
                    session["user"] = request.form.get("username").lower()
                    # If successful flash message is shown
                    flash("Welcome, {}!".format(
                        request.form.get("username")))
                    # Redirects the user to the profile of its own
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # the username/&password is invalid, flash message appears, redirecting to login page
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # if username doesnt exist flash message generated, user gets redirected to login page again
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    # Render login.html template if method is not POST, GET
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # This generates the urser's username from my db with session method, temporary cookie.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
