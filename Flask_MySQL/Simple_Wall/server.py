from flask import Flask, render_template, request, redirect, flash, session
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
app.secret_key = 'secret'
bcrypt = Bcrypt(app)
# now, we may invoke the query_db method
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+copy_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/') 
def index():
    return render_template("index.html")

@app.route('/register', methods = ['POST'])
def register():
    mysql = connectToMySQL('flaskwall') 
    if 'reg_submit' in request.form:
        valid = True
        if ((len(request.form['reg_first_name']) < 2) or request.form['reg_first_name'].isalpha() == False):
            flash('First name must include at least 2 characters and only alphabets.', 'reg_first_name')
            valid = False
        if ((len(request.form['reg_last_name']) < 2) or request.form['reg_last_name'].isalpha() == False):
            flash('Last name must include at least 2 characters and only alphabets.', 'reg_last_name')
            valid = False
        if not EMAIL_REGEX.match(request.form['reg_email']):
            flash('Please provide a valid email.', 'reg_email')
            valid = False
        mysql = connectToMySQL('flaskwall') 
        query = ("SELECT * FROM users WHERE email = %(email)s")
        data = {
            'email' : request.form['reg_email']
        }
        emails = mysql.query_db(query,data)
        if emails:
            flash("Email already exists lel", 'reg_email')
            valid = False
        if len(request.form['reg_password']) < 8:
            flash('Password must include no fewer than eight characters.', 'reg_password')
            valid = False
        if request.form['reg_confirm'] != request.form['reg_password']:
            flash('Password does not match.', 'reg_confirm')
            valid = False
        if valid == True:
            mysql = connectToMySQL('flaskwall') 
            query = ("INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())")
            data = {
                'first_name' : request.form['reg_first_name'],
                'last_name' : request.form['reg_last_name'],
                'email' : request.form['reg_email'],
                'password' : bcrypt.generate_password_hash(request.form['reg_password'])
            }
            #session['user'] = mysql.query_db(query,data)
            #print(session['user'])
            new_user = mysql.query_db(query, data)
            mysql = connectToMySQL("flaskwall")
            userid = mysql.query_db("SELECT id FROM users WHERE email = %(email)s;", data)
            
            session['userid'] = userid[0]['id']
            print(session['userid'])
            session['first_name'] = request.form['reg_first_name']
            session['action'] = 'registered'

            return redirect('/dashboard')
    elif 'login_submit' in request.form:
        mysql = connectToMySQL('flaskwall') 
        query = ('SELECT * FROM users WHERE users.email = %(log_email)s')
        data = {
            'log_email' : request.form['log_email'],
            
        }
        print(query)
        grab_hash = mysql.query_db(query,data)
        print(grab_hash)
        if grab_hash:
            if bcrypt.check_password_hash(grab_hash[0]['password'], request.form['log_password']):
                print(request.form['log_password'])
                session['userid'] = grab_hash[0]['id']
                print(session['userid'])
                session['first_name'] = grab_hash[0]['first_name']
                session['action'] = 'logged in'
                return redirect ('/dashboard')
            flash('Invalid login attempt >:(', 'log_password')
        else:
            
            print(request.form['log_password'] + "in else")
            flash('Invalid login attempt >:(', 'log_password')
    return redirect ('/')        

@app.route('/dashboard')
def dash():
    if 'userid' not in session:
        return redirect('/')
    else:
        mysql = connectToMySQL('flaskwall') 
        data = {
            'id': session['userid'] 
        }
        query = ("SELECT message, messages.created_at,messages.id, first_name FROM messages JOIN users ON users.id = messages.s_id WHERE messages.r_id = %(id)s")
        messages = mysql.query_db(query, data)
        
        print(messages)
        count_recieved = len(messages)
        
        mysql = connectToMySQL('flaskwall')
        users = mysql.query_db("SELECT * FROM users")
        
        mysql = connectToMySQL('flaskwall')
        query = ("SELECT COUNT(messages.message) as sent_count FROM messages WHERE messages.s_id = %(id)s")
        count_sent = mysql.query_db(query, data)

        return render_template("dashboard.html",messages = messages, users = users, count_recieved = str(count_recieved), count_sent = count_sent[0]['sent_count'])

@app.route('/create', methods = ['POST'])
def create():
    if len(request.form['message_content']) < 1:
        flash("Message cannot be blank.")
        return redirect('/dashboard')
    else:
        mysql = connectToMySQL('flaskwall')
        query = "INSERT INTO messages (message, created_at, updated_at, s_id, r_id) VALUES (%(message)s, NOW(), NOW(), %(s_id)s, %(r_id)s);"
        data = {
            'message': request.form['message_content'],
            's_id': session['userid'],
            'r_id': request.form['recipient_id']
        }

        new_message = mysql.query_db(query, data)
        return redirect('/dashboard')

@app.route('/remove/message/<id>')
def delete(id):
    mysql = connectToMySQL('flaskwall')
    query = "DELETE FROM messages WHERE messages.id = %(mid)s AND messages.r_id = %(r_id)s;"
    data = {
        
        'mid': id,
        'r_id': session['userid']
        }

    new_message = mysql.query_db(query, data)
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)