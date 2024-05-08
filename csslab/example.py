from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
  message =  "Match is a fun game where we try and get all the same numbers in the same color!"
  return render_template("home.html", text = message)

if __name__ == '__main__':
    my_port = 5225
    app.run(host='0.0.0.0', port = my_port) 
