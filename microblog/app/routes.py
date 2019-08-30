from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tom'}
    posts  = [
        {
            'author': {'username': 'John'},
            'body': "Het is hier echt fantastisch enzo."
        },
        {
            'author': {'username': 'Frank'},
            'body': "Alles is kut."
        }
    ]
    return render_template('index.html', title='home', user=user, posts=posts)
