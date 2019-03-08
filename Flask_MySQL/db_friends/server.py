from flask import Flask, render_template, request, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'

# now, we may invoke the query_db method
#friends = mysql.query_db("SELECT * FROM friends;")
#print("all the users", mysql.query_db("SELECT * FROM friends;"))

@app.route('/') 
def index():
    mysql = connectToMySQL('friendsdb')
    friends = mysql.query_db("SELECT * FROM friends;")
    print(friends)
   
    return render_template("index.html", friends = friends)
@app.route('/update' , methods = ['POST'])
def create():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    new_friend_id = mysql.query_db(query, data)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
