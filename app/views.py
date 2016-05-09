from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/about')

def index():
    user = {'nickname': 'Kathure'}  # fake user
    posts = [#fake array of posts
      {
            "author":{"nickname":"Johnny"},
            "body":"Beautiful day in Portland !"
        },
        {
            "author":{"nickname":"Susan"},
            "body": "The Avengers movie was super cool!"
        },
        {
            "author":{"nickname":"Liz"},
            "body":"Captain America Civil War premieres on Friday"
        }

    ]
    return render_template('index.html',
                          user=user,
                          posts = posts
                          )
    return render_template('about.html',

                          )
