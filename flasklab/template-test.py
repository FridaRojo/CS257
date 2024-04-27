from flask import Flask
from flask import render_template
import random
import os 

#app = Flask(__name__)
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

#@app.route('/')

#current_directory = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def welcome():
    #html_file_path = os.path.join(current_directory, 'index.html')
    #return render_template(html_file_path)
    return render_template("index.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    
    #html_file_path = os.path.join(current_directory, 'random.html')
    #return render_template(html_file_path, randNum=num)
    return render_template("random.html", randNum = num)

if __name__ == '__main__':
    my_port = 5125
    app.run(host='0.0.0.0', port = my_port) 
