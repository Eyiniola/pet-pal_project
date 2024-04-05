import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host='localhost',
    user='petPalAdmin',
    password='$fg43$#ter'
)

# execute the SQL script to create the database

with open('DB/ds.sql', 'r') as file:
    sql_script = file.read()

    
    # 

