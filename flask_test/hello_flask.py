from flask import Flask
from search4letters import search_for_letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return  'hello world from Flask!'

@app.route('/search')
def do_search() -> str:
    return str(search_for_letters('life,the universe,and ererything@','eiru,!'))

app.run()