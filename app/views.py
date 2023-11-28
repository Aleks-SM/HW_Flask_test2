from flask import render_template
from app import app
def index():
    return render_template("index.html",
                          title = "Home",
                          user = user)
