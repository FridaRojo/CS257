from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
  message =  "Match is a fun game where we try and get all the same numbers in the same color!"
  message = meassage + "Lets start!"
  return render_template("home.html", text = message)
  
@app.route('/newpage')
def match():
  return renter_template("match.html")

if __name__ == '__main__':
    my_port = 5225
    app.run(host='0.0.0.0', port = my_port) 
