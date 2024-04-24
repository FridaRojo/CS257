import psycopg2
  
def test_query_one():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="rojof",
        user="rojof",
        password="spoon387ardi")

    cur = conn.cursor()

    sql_states =  """DROP TABLE IF EXISTS states;
CREATE TABLE states (
  code text,
  stateName text,
  pop real
);
"""

    cur.execute( sql_states )

    row = cur.fetchone()

    conn.commit()
    
    return row
