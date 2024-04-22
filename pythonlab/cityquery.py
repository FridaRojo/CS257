import psycopg2

def querys():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,   
    database="rojof",
    user="rojof",
    password="spoon387ardi")

  if conn is not None:
    print( "Connection Worked!" )
  else:
    print( "Problem with Connection" )
    return None 

  cursor = conn.cursor()

  # Determining if Northfield is present in the database
  cursor.execute("SELECT city, state, lat, long FROM cities WHERE city = 'Northfield';")
  northfield_result = cursor.fetchone()
  if northfield_result:
    print("Northfield is present in the database. Location (Latitude, Longitude):", northfield_result[2], northfield_result[3])
  else:
    print("Northfield is not present in the database.")

   #Printing out the name of the city with the largest population
    cursor.execute("SELECT city FROM cities ORDER BY pop DESC LIMIT 1;")
    largest_pop_city = cursor.fetchone()
    print("City with largest population:", largest_pop_city)

    


print(querys())
      






