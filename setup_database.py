import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host='localhost',
    user='petPalAdmin',
    password='petPalAdmin1244',
)

# execute the SQL script to create the database

with open('DB/ds.sql', 'r') as file:
    sql_script = file.read()

    
# cursor object is used to interact with the database
cursor = connection.cursor()
cursor.execute(sql_script)
connection.commit()

# close the cursor and connection
cursor.close()

