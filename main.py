from flask import Flask,render_template
import os,requests


app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/about")
def about():
    
    return render_template("about.html")
    
@app.route("/help")
def help():
    return render_template("help.html")


@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")
    
 