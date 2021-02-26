from flask import Flask , render_template  
app = Flask(__name__)    

@app.route('/play')          
def boxes():
    return render_template("boxes.html",num_square=3,user_color='lightskyblue')

@app.route('/play/<input>') 
def play_input(input):
    return render_template("index.html", input_box =int(input))

@app.route('/play/<input>/<color>')
def play_input_color(color):
    retrun render_template("index.html", input_box =int(input), user_color =color)
if __name__=="__main__":
    app.run(debug=True)