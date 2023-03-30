from flask import Flask ,render_template,request , url_for,flash
from  flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key='asdf'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Phongkham'
 
mysql = MySQL(app)

@app.route('/')
def index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM accounts')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html',accounts=data)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
