from flask import Flask, render_template, request, escape
from search4letters import search_for_letters
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig']={'host': '127.0.0.1', 'user': 'vsearch', 'password': 'king_9999', 'database': 'vsearchlogDB'}

def log_request(req: 'flask_request',res: str) -> None:
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s,%s)'''
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res,))

@app.route('/search', methods=['POST'])
def do_search() -> 'html' :
    letters = request.form['letters']
    phrase = request.form['phrase']
    title = 'here are your results'
    results = str(search_for_letters(phrase,letters))
    log_request(request,results)
    return render_template('results.html', the_phrase = phrase, the_letters=letters, the_tile=title, the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='welcome to search on teh web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents=[]
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles=('form date', 'remote_addr', 'user_agent', 'results')
    return render_template('viewlog.html', the_title='view log', the_row_titles=titles, the_data=contents)

if __name__ == '__main__':
    app.run(debug=True)