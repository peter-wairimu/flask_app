from flask import Flask, app

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "abncmxbjsuhdjjsjdh"


    return app