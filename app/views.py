from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')


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
@app.route('/')
@app.route('/about')

def about():


    return render_template('about.html',
                          )
@app.route('/')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html',)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s" remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                          title = 'Sign In',
                          form=form,
                          providers=app.config['OPENID_PROVIDERS'])
