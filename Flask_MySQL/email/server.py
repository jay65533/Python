from flask import Flask, render_template, request, redirect, flash, session
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
    
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
app.secret_key = 'secret'
# now, we may invoke the query_db method
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+copy_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/') 
def index():
    return render_template("index.html")
@app.route('/process', methods=['POST'])
def submit():
    session['email'] = request.form['email']
    print(session['email'])
    if len(session['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address")
    # else if email doesn't match regular expression display an "invalid email address" message
    else:
        flash("Success!")
    if '_flashes' in session.keys():
        return redirect("/")
    
    
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)