from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<input>') 
def say(input):
    return f'hello {input}'

@app.route('/repeat/<num>/<input>')
def repeat(num,input):
    return f'{word}'* int(num)

if __name__ == "__main__":
    app.run(debug=True)