from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)


@app.route('/')
def homepage():
    
    return "<h1>koukou</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 80))