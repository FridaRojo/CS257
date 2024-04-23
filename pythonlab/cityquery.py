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
    #return None 

  cursor = conn.cursor()

  # Determining if Northfield is present in the database
  cursor.execute("SELECT city, state, lat, long FROM cities WHERE city = 'Northfield';")
  northfield_result = cursor.fetchone()
  if northfield_result:
    print("Northfield is present in the database. Location (Latitude, Longitude):", northfield_result[2], northfield_result[3])
  else:
    print("Northfield is not present in the database.")

    print()

   #Printing out the name of the city with the largest population
    cursor.execute("SELECT city FROM cities ORDER BY pop DESC LIMIT 1;")
    largest_pop_city = cursor.fetchone()[0]
    print("City with largest population:", largest_pop_city)

    #Printing out name of Minnesota city with the smallest pop
    cursor.execute("SELECT city FROM cities WHERE state = 'Minnesota' ORDER BY pop LIMIT 1;")
    smallest_pop_city_mn = cursor.fetchone()[0]
    print("Minnesota city with the smallest population:", smallest_pop_city_mn)

    print()


    #Printing out the cities furthest N, S, W, E
      #furthest N
    cursor.execute("SELECT city FROM cities ORDER BY lat DESC LIMIT 1;")
    furthest_n = cursor.fetchone()[0]
    print("City furthest North: ", furthest_n)
      #furthest S
    cursor.execute("SELECT city FROM cities ORDER BY lat LIMIT 1;")
    furthest_s = cursor.fetchone()[0]
    print("City furthest South: ", furthest_s)
      #furthest W
    cursor.execute("SELECT city FROM cities ORDER BY long LIMIT ")
    furthest_w = cursor.fetchone()[0]
    print("City furthest West: ", furthest_w)
      #furthest E
    cursor.execute("SELECT city FROM cities ORDER BY long DESC LIMIT ")
    furthest_w = cursor.fetchone()[0]
    print("City furthest East: ", furthest_w)


print(querys())
      






