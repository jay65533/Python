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
    mysql = connectToMySQL('library') 
    books = mysql.query_db("SELECT * FROM book_list")
    #print(books)
    #print(books[0]['id'])
    return render_template("index.html",books = books)
@app.route('/add')
def create():
#    mysql = connectToMySQL("friendsdb")
   
    return render_template('add_book.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    mysql = connectToMySQL('library')
    query = ("INSERT INTO book_list (name, description) VALUES (%(name)s, %(description)s)")
    
    data = {
        'name' : request.form['name'],
        'description' : request.form['description']
    }
    print(query)
    new_book_id = mysql.query_db(query,data)
      
    return redirect('/')

@app.route('/edit', methods = ['POST'])
def edit_book():
    data = {
        'edit' : request.form['edit']
    }
    print(data['edit'])
    return render_template('edit_book.html', book_id = data['edit'])

@app.route('/edit_book', methods = ['POST'])
def edit():
    mysql = connectToMySQL('library')
    query = ("UPDATE book_list SET name = %(name)s, description = %(description)s WHERE id = %(edit)s")
    
    data= {
        'name': request.form['name'],
        'description' : request.form['description'],
        'edit' : request.form['book_id']
    }
    
    print(data)
    print(query)
    new_book_id = mysql.query_db(query,data)
    return redirect('/')

@app.route('/delete', methods = ['POST'])
def delete():
    mysql = connectToMySQL('library')
    query = ("DELETE FROM book_list WHERE (id = %(del)s)")

    data = {
        'del' : request.form['del']
    }
    print(query)
    new_delete = mysql.query_db(query,data)

    return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)
