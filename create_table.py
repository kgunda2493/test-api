import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

# Create table
create_table = "CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
cursor.execute("INSERT INTO Users VALUES (NULL, ?, ?)", ('keerthana', 'iwillnottellyou'))

create_items = 'CREATE TABLE IF NOT EXISTS Items(id INTEGER PRIMARY KEY, name text, price real)'
cursor.execute(create_items)

#cursor.execute("INSERT INTO Items VALUES (NULL,?,?)", ('test', 12.44))

connection.commit()
connection.close()

