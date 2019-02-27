
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)  
app.secret_key = 'secret'

@app.route('/')         
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0,11)
    if 'message' not in session:
        session['message'] = ""
    if 'color' not in session:
        session['color'] = "white"
    print(session)
    return render_template("index.html", message = session['message'], color = session['color'])

@app.route('/d', methods = ['POST'])
def guess():
    guess = int(request.form['number'])
    print(guess)
    if(guess == session['number']):
        session['message'] = "You Win!"
        session['color'] = "green"
    if(guess > session['number']):
        session['message'] = "Too Big!"
        session['color'] = "red"
    if(guess < session['number']):
        session['message'] = "Too Small!"
        session['color'] = "red"
    return redirect('/')
@app.route('/b')
def reset():
    session.clear()
    return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)

