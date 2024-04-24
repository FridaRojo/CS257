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
  conn = psycopg2.connect(
    host="localhost",
    port=5432,   
    database="rojof",
    user="rojof",
    password="spoon387ardi")
  
  abbrev = 
  cur = conn.cursor()
  cur.execute("SELECT pop FROM states WHERE abbrev = ILIKE %s;", (abbrev,))
  pop = cur.fetchone()
  return abbrev + "'s population is " + str(pop)

if __name__ == '__main__':
    my_port = 5225
    app.run(host='0.0.0.0', port = my_port) 
