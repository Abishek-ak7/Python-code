# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Abishek7."
)

# Printing the connection object
print(mydb)
