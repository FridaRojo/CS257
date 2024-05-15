from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
  return render_template("home.html")
  
@app.route('/match')
def match():
  return render_template("match.html")

if __name__ == '__main__':
    my_port = 5225
    app.run(host='0.0.0.0', port = my_port) 
