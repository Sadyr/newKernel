from flask import Flask
from flask import render_template, request

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
        {'name' : ' call me', 'url':'/writetofile'},
        {'name' : ' Services', 'url':'services'}]
    return render_template(
        'index.html',
        nav = nav,
        title = 'This is main page',
        description = 'This is our company site')


def write(fname,lname):
    with open('user.txt', 'a') as writer:
        writer.write(f"\n {fname}, {lname}")

def read():
    with open('user.txt', 'r') as reader:
         return reader.read()


@app.route('/writetofile', methods=['GET', 'POST'])
def write_to_file():
    if request.method == 'POST':
        data = request.form
        fname = data['fname']
        lname = data['lname']
        write(fname,lname)

        return  'Данные успешно отправлены' + read()
    else:
        return render_template('simple_form.html')





if __name__ == '__main__': 
    app.run(debug=True) 

