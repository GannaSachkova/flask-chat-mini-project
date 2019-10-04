import os

from flask import Flask


# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)




# create our app root decorator, which is going to be for our index page, so that will just be ('/').
@app.route("/")
#we'll define the function that is going to be bound to our decorator: def index().It doesn't take any arguments.
def index():
#So if we go to our index page, it tells us how to use our app.So I'm going to put a message in here that says "To send a message use /<USERNAME>/<MESSAGE>"
# Unfortunately, the angle brackets will be interpreted by the browser as HTML
# And then I'm going to add in a docstring, which just says .

    """Main page with instructions"""    
    return "To send a message use: /USERNAME/MESSAGE"



@app.route("/<username>")

def user(username):

    return "Hi " + username





@app.route("/<username>/<message>")

def send_message(username, message):

    return "{0}: {1}".format(username, message)



if __name__ =="__main__":

    app.run(host=os.getenv("IP"),

       port=int(os.getenv("PORT")),

       debug=True)