from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'secret'
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/info', methods=['POST'])         
def checkout():
    
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    print(session)
    return redirect('/checkout')
    #return render_template("checkout.html")

@app.route('/checkout')         
def checkout1():
    return render_template("checkout.html")

if __name__=="__main__":   
    app.run(debug=True)    