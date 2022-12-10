from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
#url_for('static', filename='style.css')

""" @app.route("/")
def hello_world():
    return "<p/>Hello, world!</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!" """

""" @app.route('/')
def index():
    print('hell')
    return "Indes page"

@app.route('/hello')
def hello():
    print('mell')
    return "Hello, world"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"

@app.route('/projects/')
def projects():
    return "The projects page"

@app.route('/about')
def about():
    return 'The about page'
 """


""" @app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{usernamme}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile', username = 'John  Doe')) """



""" @app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
 """

""" 
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('login')
def login_post():
    return do_the_login()

 """

""" @app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name = name) """
    
"""@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "Invalid username/password"
    # the code below is executed if the request method
     # ws GET or the credentials were invalid
    return render_template('login.html', error = error)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the file']
        f.save('/var/www/uploads/uploads_file.txt')

"""

@app.route('/')
def index():
    username = request.cookies.get('username')
    #use cookies.get(key) instead of cookies[key] to not get  KeyError if the cookie is missing
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookies('username', 'the username')
    return resp
    