import psycopg2
from flask import Flask
from flask import render_template
import random
import os 


app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
adjectives = ['Wise', 'Brave', 'Kind', 'Clever', 'Funny']

def city():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,   
    database="rojof",
    user="rojof",
    password="spoon387ardi")

  #Testing connection
  if conn is not None:
    print( "Connection Worked!" )
  else:
    print( "Problem with Connection" )
  print()
  cursor = conn.cursor()

  cursor.execute("SELECT city FROM cities ORDER BY RANDOM() LIMIT 1;")
  city = cursor.fetchone()[0]
  return city


@app.route('/')
def welcome():
  return render_template("start.html")

@app.route('/sentence')
def sentence():
  name = random.choice(names)
  adjective = random.choice(adjectives)
  year = random.randint(1900,2024)
  city = city()
  
  sentence = f"{name} the {adjective} was born in {city} in {year}"  
  return render_template('sentence.html', sentence=sentence)
  #return render_template("name.html"," the" , "adj.html", "was born in " year)

if __name__ == '__main__':
    my_port = 5125
    app.run(host='0.0.0.0', port = my_port) 
