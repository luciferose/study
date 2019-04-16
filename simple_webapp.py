from flask import Flask, session
from checker import check_logged_in

app=Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'hello from the simple webapp'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'this is page1'

@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'this is page2'

@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'this is page3'

@app.route('/login')
def do_login() -> str:
    session['logged_in']=True
    return 'you are now logged in'

app.secret_key='king_9999'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'you are now logged out'

@app.route('/status')
def cheeck_status() -> str:
    if 'logged_in' in session:
        return 'you are currently logged in'
    return 'you are not logged in'

if __name__ == '__main__':
    app.run(debug=True)