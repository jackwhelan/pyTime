import mysql.connector
from mysql.connector import Error
try:
	connection = mysql.connector.connect(host='[REDACTED]',database='pyTime',user='phpmyadmin',password='[REDACTED]')
	if connection.is_connected():
		print("CONNECTED! Returning Person Table...")
		query = "SELECT * FROM Person"
		cursor = connection.cursor()
		cursor.execute(query)
		records = cursor.fetchall()
		print("PERSON TABLE ROW COUNT: ", cursor.rowcount)
		print("# ******************************************************************** #")
		for row in records:
			print("Id = ", row[0])
			print("Password = ", row[1])
			print("First Name = ", row[2])
			print("Surname = ", row[3])
			print("# ******************************************************************** #")
		cursor.close()
	else:
		print("NOT CONNECTED")
except Error as e:
	print("e")