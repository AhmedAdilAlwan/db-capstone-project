import mysql.connector as connector

connection = connector.connect(user = "Ahmed", password = "413aBg97J9$L")

cursor = connection.cursor()
cursor.execute('USE little_lemon')
show_tables_query = "SHOW tables" 
cursor.execute(show_tables_query)

data = cursor.fetchall()
print(data)