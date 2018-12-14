from flask import Flask, render_template
from mysite.content import homeContent, meContent, postContent

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html', **homeContent)

@app.route('/me')
def me():
    return render_template('post.html', **meContent)

@app.route('/content-page')
def content():
    return render_template('post.html', **postContent)
