import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/add/<num1>/<num2>')
def my_adding(num1,num2):
  added_num = int(num1) + int(num2)
  added_num = str(added_num)
  return num1 + "+" + num2 + "=" + added_num

@app.route('/pop/<abbrev>')
def state_pop(abbrev):
  cursor = conn.cursor()
  cursor.execute("SELECT state FROM states WHERE code ILIKE %s OR state ILIKE %s;", (state_input, state_input))
  curor.fetchone()

if __name__ == '__main__':
    my_port = 5225
    app.run(host='0.0.0.0', port = my_port) 
