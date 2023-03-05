from flask import Flask
from flask import render_template
from gists import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    tags = menu_tags(tags_dic)
    return render_template('index.html', tags=tags, len_tags=len(tags))

# @app.route('/')
# @app.route('/index')
# def index():
#     name = 'Rosalia'
#     return render_template('index.html', title='Welcome', username=name)

