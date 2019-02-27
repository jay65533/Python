from flask import Flask, render_template, request, redirect,session, flash
import re
app = Flask(__name__)
app.secret_key = 'secret'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/create', methods=['POST'])
def create_user():
    session[]
