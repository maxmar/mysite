from flask import Flask, render_template
from content import home, post

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html', **home)

@app.route('/content-page')
def content():
    return render_template('post.html', **post)
