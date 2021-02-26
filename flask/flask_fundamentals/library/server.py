from flask import Flask, render_template,request,redirect
import random
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")
