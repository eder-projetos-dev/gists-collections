from flask import Flask
from flask import render_template
import random
from gists import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
  tags = menu_tags(tags_dic)
  return render_template('index.html', tags=tags, len_tags=len(tags))


@app.route('/filtro')
def filtro():
  gists = Gists('eder-projetos-dev')
  gists_list = gists.get_gists()
  tag = "PHP"

  filtro = filtro_tag(gists_list, tag)
  return render_template('filtro.html', filtro=filtro)


if __name__ == "__main__":  # Makes sure this is the main process
  app.run(  # Starts the site
    host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
    port=random.randint(2000,
                        9000)  # Randomly select the port the machine hosts on.
  )
