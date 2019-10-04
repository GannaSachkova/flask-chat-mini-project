import os

from flask import Flask, redirect


# we'll initialize our new Flask application: app = Flask(__name__)
app = Flask(__name__)
messages = []



# create our app root decorator, which is going to be for our index page, so that will just be ('/').
@app.route("/")
#we'll define the function that is going to be bound to our decorator: def index().It doesn't take any arguments.
def index():
#So if we go to our index page, it tells us how to use our app.So I'm going to put a message in here that says "To send a message use /<USERNAME>/<MESSAGE>"
# Unfortunately, the angle brackets will be interpreted by the browser as HTML
# And then I'm going to add in a docstring, which just says .

    """Main page with instructions"""    
    return "To send a message use: /USERNAME/MESSAGE"


def add_messages(username, message):
    """Add messages to the `messages` list"""
    messages.append("{}: {}".format(username, message))




def get_all_messages():
    """Get all of the messages and separate them with a `br`"""
    return "<br>".join(messages)
    
    
    
@app.route("/<username>")
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())



@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

    
if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=int(os.getenv("PORT")),
       debug=True)