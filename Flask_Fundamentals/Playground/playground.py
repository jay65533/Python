from flask import Flask,render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
print(__name__)  

@app.route('/play')

def level1():
    return render_template("index.html")
@app.route('/play/<num_of_boxes>')
def level(num_of_boxes):
    return render_template("index2.html", num_of_boxes = int(num_of_boxes))
@app.route('/play/<num_of_boxes>/<color>')
def levelx(num_of_boxes,color):
    return render_template("index3.html", num_of_boxes = int(num_of_boxes), color = color)
if __name__=="__main__":   # If __name__ is "__main__" we know we are running this file directly and not importing
                           # it from a different module
    app.run(debug=True)    # Run the app in debug mode.
