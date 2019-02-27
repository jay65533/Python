from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'secret'

@app.route('/')         
def index():
    if 'incr' not in session:
        session['incr'] = 0
    print(session)
    session['incr'] += 1
    return render_template("index.html")
@app.route('/d', methods = ['POST'])
def sdfsd():
    session['incr'] +=1
    return redirect('/')
@app.route('/b', methods = ['POST'])
def sdfsdd():
    session['incr'] = 0
    return redirect('/')
if __name__=="__main__":   
    app.run(debug=True)