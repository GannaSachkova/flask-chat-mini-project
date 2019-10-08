import os
from datetime import datetime
from flask import Flask, redirect, render_template,request, session, url_for



# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)
app.secret_key="randomString123"
messages = []









def add_message(username, message):
    """Add messages to the `messages` list"""
     #The strftime() method takes a date/time object and then converts that to a string according to a given format.
    now = datetime.now().strftime("%H:%M:%S")

    messages.append({"timestamp": now, "from": username, "message": message})


# create our app root decorator, which is going to be for our index page, so that will just be ('/').
@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))
    return render_template("index.html")
    
    

@app.route("/chat/<username>", methods=["GET", "POST"])

def user(username):

    """Add and display chat messages"""
    if request.method == "POST":

        username = session["username"]

        message = request.form["message"]

        add_message(username, message)

        return redirect(url_for("user", username=session["username"]))
    return render_template("chat.html", chat_messages =messages, username = username)





app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)