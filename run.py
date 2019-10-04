import os

from flask import Flask


# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)




# create our app root decorator, which is going to be for our index page, so that will just be ('/').
@app.route("/")
#we'll define the function that is going to be bound to our decorator: def index().It doesn't take any arguments.
def index():
#And just for now, we're going to return a <h1> that says Hello There!.
    return "<h1>Hello There</h1>"





if __name__ =="__main__":

    app.run(host=os.getenv("IP"),

       port=int(os.getenv("PORT")),

       debug=True)