from flask import Flask,render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def level1():
    return render_template("index.html", x=8, y = 8)

@app.route('/<x>/<y>')
def level2(x,y):
    return render_template("index.html", x = int(x), y = int(y))

#@app.route('/<x>/<y>')
#def level1():
#    return render_template("index.html")


if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True) 