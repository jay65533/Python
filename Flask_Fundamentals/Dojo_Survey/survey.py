from flask import Flask, render_template, request, redirect,session, flash
import re
app = Flask(__name__)
app.secret_key = 'secret'
# our index route will handle rendering our form
@app.route('/')
def index():
    cities = ["San Jose", "Seattle", "Chicago", "New York"]
    languages = ["Python", "Java", "JavaScript", "Ruby"]
    return render_template("index.html", cities = cities, languages = languages)
@app.route('/create', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['languages'] = request.form['languages']
    session['comment'] = request.form['comment']

    if(len(session['name']) < 1):
        flash("Name cannot be blank", 'name')
    if(len(session['comment'])< 1):
        flash("Comment cannot be blank", 'comment')
    if(len(session['comment']) > 120):
        flash("Comment cannot have more than 120 characters ", 'comment')
    
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return redirect("/result")
    return redirect('/result')
@app.route('/result')
def return_results():
    return render_template("index2.html")
if __name__=="__main__":
    # run our server
    app.run(debug=True) 