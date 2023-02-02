from flask import Flask, jsonify         #from the flask module import the flask class
app = Flask(__name__)           #create an instance of the flask class into the app variable (now an object) - "class is to object, like blueprint is to house"


@app.get("/")   #Flask decorator that creates routes. decorator is a function that wraps another function.
def index():    #flask calls these "view functions". A wrapped function is referred to as view functions.
    me = {      #python dictionary with key/value pairs. Before colon is key, after colon is the value.
        "first_name": "Jim",
        "last_name": "Barnett",
        "hobbies": "Weightlifting",
        "is_active": True
    }

    return jsonify(me)   #when a view function returns a dict. Flask automatically converts it to JSON.