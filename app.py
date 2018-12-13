from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    import content
    return render_template('home.html', **content.home)

@app.route('/content-page')
def content():
    import content
    return render_template('post.html', **content.post)
