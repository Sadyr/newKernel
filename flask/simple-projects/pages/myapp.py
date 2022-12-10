from flask import Flask
from flask import render_template

app = Flask(__name__)  # a nother arg ,static_url_path='/static'


@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/')
@app.route('/index')
def index():
    nav = [
        {'name' : ' Home', 'url':'/index'},
        {'name' : ' About', 'url':'/about'},
        {'name' : ' Contact', 'url':'/contact'},
        {'name' : ' Services', 'url':'services'}]
    return render_template(
        'index.html',
        nav = nav,
        title = 'This is main page',
        description = 'This is our company site')





if __name__ == '__main__': 
    app.run() 

