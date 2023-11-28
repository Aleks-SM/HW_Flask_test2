from flask import render_template
from app import app
def index():
    user = {"nickname": "Pavel"}
    posts = [
        {
            "author": {"nickname": "John"},
            "body": 'Beatiful day in Russia'
        },
        {
            "author": {"nickname": "Riddik"},
            "body": 'The Spiderman movie was is cool'
        }
    ]
    return render_template("index.html",
                          title = "Home",
                          user = user,
                          posts = posts)
