from flask import Flask, render_template,request,redirect
import random
app = Flask(__name__)

def game(key1,key2):
    option ={ "rock":{"rock":"tie","paper":"lose","scissor":"win"},
            "paper":{"rock":"win","paper":"tie","scissor":"lose"},
            "scissor":{"rock":"lose","paper":"win","scissor":"tie"}
    }
    return option[key1][key2]

@app.route("/")
def index():
    return render_template("index.html")

@app.route ('/game', methods = ['POST']) 
def  game1():
    x = request.form['game']
    arr=["rock","paper","scissor"]
    c = random.choice(arr)
    return render_template('index.html',x=x,c=c,result = game(x,c))
    

if __name__=="__main__":
    app.run(debug=True)

