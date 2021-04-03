import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

UPLOAD_FOLDER = '/static/uploaded_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    try:
        session["user"]
    except KeyError:
        return redirect(url_for("login"))
    places = mongo.db.places.find({"created_by": username})
    # This generates the urser's username from my db with session method, temporary cookie.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # If session user cookie is true return to profile page
    if session["user"]:
        return render_template(
            "profile.html", username=username,
            places=places)

    return redirect(url_for("login"))


@app.route("/places")
def places():
    return render_template("places.html")


@app.route("/logout")
def logout():
    # User session cookie is removed with session pop method
    flash("Logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Saves input from the add place form and post to mongodb
@app.route("/add_place", methods=["GET", "POST"])
def add_place():
    try:
        session["user"]
    except KeyError:
        return redirect(url_for("login"))
    if request.method == "POST":
        f = request.files['file']
        f.save("static/uploaded_images/"+secure_filename(f.filename))
        place = {
            "place_city": request.form.get("place_city"),
            "place_country": request.form.get("place_country"),
            "place_description": request.form.get("place_description"),
            "place_pros": request.form.get("place_pros"),
            "place_cons": request.form.get("place_cons"),
            "place_file": "../static/uploaded_images/" + f.filename,
            "created_by": session["user"]
        }
        mongo.db.places.insert_one(place)
        flash("Place Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    places = mongo.db.places.find()
    return render_template("add_place.html", places=places)


# Editing id, shows previously inserted data for uploaded id
@app.route("/edit_place/<place_id>", methods=["GET", "POST"])
def edit_place(place_id):
    try:
        session["user"]
    except KeyError:
        return redirect(url_for("login"))
    if request.method == "POST":
        f = request.files['file']
        f.save("static/uploaded_images/"+secure_filename(f.filename))
        submit = {
            "place_city": request.form.get("place_city"),
            "place_country": request.form.get("place_country"),
            "place_description": request.form.get("place_description"),
            "place_pros": request.form.get("place_pros"),
            "place_cons": request.form.get("place_cons"),
            "place_file": "../static/uploaded_images/" + f.filename,
            "created_by": session["user"]
        }
        mongo.db.places.update({"_id": ObjectId(place_id)}, submit)
        flash("Place Successfully Updated, go back to My Place!")

    place = mongo.db.places.find_one({"_id": ObjectId(place_id)})
    return render_template("edit_place.html", place=place, places=places)


# deleting previously added place
@app.route("/delete_place/<place_id>")
def delete_place(place_id):
    try:
        session["user"]
    except KeyError:
        return redirect(url_for("login"))
    mongo.db.places.remove({"_id": ObjectId(place_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
