from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def fixed():
    return render_template('index.html',x=int(8), y=int(8))

@app.route('/<int:num>')
def boxes(num):
    return render_template('index.html', x=num, y=int(8))

@app.route('/<int:num>/<int:num2>')
def boxes1(num,num2):
    return render_template('index.html', x=num, y=num2)

if __name__ == '__main__':
    app.run(debug=True)