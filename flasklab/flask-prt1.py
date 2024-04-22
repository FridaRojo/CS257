import flask

app = flask.Flask(__name__)

#
@app.route('/add/<num1>/<num2>')
def my_adding(num1,num2):
  added_num = int(num1) + int(num2)
  added_num = str(added_num)
  return num1 + "+" + num2 + "=" + added_num

if __name__ == '__main__':
    my_port = 5225
    app.run(host='0.0.0.0', port = my_port) 
