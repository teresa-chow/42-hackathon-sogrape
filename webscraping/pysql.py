import numpy
import mysql.connector
from mysql.connector import Error

# class Wine:
#     def __init__(self, name, store, year, capacity, price, curr, disc, loc):
#         self.name = name
#         self.store = store
#         self.year = year
#         self.capacity = capacity
#         self.price = price
#         self.curr = curr
#         self.disc = disc
#         self.loc = loc

# wine2 = Wine("Py test wine", "Store X", 2023, 750, 29.99, "EUR", 0.10, "Portugal")
# data = Wine("ricardo", "pingodoce", 2022, 750, 300.99, "USD", 0.15, "Portugal")

def insert_wine(obj):
	try:
		connection = mysql.connector.connect(host='localhost',
											database='mydb',
											user='user',
											password='H@ckathon#42',
											auth_plugin='mysql_native_password')
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ", db_Info)
			cursor = connection.cursor()
			cursor.execute("select database();")
			record = cursor.fetchone()
			print("Connected to database: ", record)
			
			insert_query = "INSERT INTO Wine (name, ean, store, year, capacity, price, curr, disc, loc, img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
			if not obj['wine']:
				print("Attempting to parse empty values")
			else:
				cursor = connection.cursor()
				print(f"Inserting wine {obj['wine']} from {obj['shop_name']}")
				cursor.execute(insert_query, (obj['wine'], obj['ean'], obj['shop_name'], obj['harv_year'], obj['capacity'], obj['price'], obj['currency'], obj['discount'], obj['location'], obj['path']))
				connection.commit()
	except Error as e:
		print("Error while connecting to MySQL", e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed")

def get_search_list():
	try:
		connection = mysql.connector.connect(host='localhost',
											database='mydb',
											user='user',
											password='H@ckathon#42',
											auth_plugin='mysql_native_password')
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ", db_Info)
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM List")
			result = cursor.fetchall()
			if not result:
				print("Error getting data from database.")
			else:
				print("Successfully retrieved data from the database.")
			return result
	except Error as e:
		print("Error while connecting to MySQL", e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed")