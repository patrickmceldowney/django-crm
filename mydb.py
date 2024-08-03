import mysql.connector

db = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd= 'password123'
	)

# prepare cursor
cursor_object = db.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE mceldowneycrm")
print("All done!")