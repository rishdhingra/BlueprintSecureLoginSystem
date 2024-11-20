import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS usernames
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user TEXT,
                   pass TEXT)''')

# Insert data into the table
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user", "p@ss"))
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user2", "passWord"))
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user3", "password1"))
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user4", "password13"))
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user5", "passw2"))
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user6", "p@ss2"))
cursor.execute("INSERT INTO usernames (user, pass) VALUES (?, ?)", ("user7", "pass36"))


# Commit the changes and close the connection
conn.commit()
conn.close()
# Retrieve data from the table
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM usernames")
rows = cursor.fetchall() 

# Display the retrieved data
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# Close the connection
conn.close()