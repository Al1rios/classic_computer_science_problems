from dotenv import load_dotenv
load_dotenv()
import os
import mysql.connector

connection = mysql.connector.connect(
  host= os.getenv("HOST"),
  user=os.getenv("USERNAME"),
  passwd= os.getenv("PASSWORD"),
  db= os.getenv("DATABASE")
)

my_cursor = connection.cursor()

# my_cursor.execute("CREATE DATABASE dbpython")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])

# my_cursor.execute("CREATE TABLE users (name CHAR(255), mail VARCHAR(255), age INT(10), id_user INT AUTO_INCREMENT PRIMARY KEY)")
# my_cursor.execute("CREATE TABLE customers (name CHAR(255), address VARCHAR(255), id_customer INT AUTO_INCREMENT PRIMARY KEY)")

# my_cursor.execute("SHOW TABLES")
# for t in my_cursor:
#     print(t[0])

# sqlstuff = "INSERT INTO users (name, mail, age) VALUES (%s, %s, %s)"

# records = [
#     ("susan median", "susan@gmail.com", 40),
#     ("mary", "mary@gmail.com", 21),
#     ("steve", "steve@gmail.com", 29),
#     ("tina", "tina@gmail.com", 57),
#     ("tim", "tim@gmail", 32)
# ]


# my_cursor.executemany(sqlstuff, records)
# connection.commit()
# print("Records inserted successfully into users table")


# my_cursor.execute("SELECT * FROM users")

# result = my_cursor.fetchall()

# for row in result:
#     print(f"{row[0]} \t{row[1]}\t\t\t{row[2]}\t{row[3]}")

# where clause

# my_cursor.execute("SELECT * FROM users WHERE age = 57")
# my_cursor.execute("SELECT * FROM users WHERE name = 'ali rios'")

# result = my_cursor.fetchall()

# for row in result:
#     print(row)


# like clause and wildcards

# my_cursor.execute("SELECT * FROM users WHERE name LIKE '%u%'")
# result = my_cursor.fetchall()

# for row in result:
#     print(row)

# ##  AND END OR
# my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%' AND age >= 30 AND id_user=7")
# # my_cursor.execute("SELECT * FROM users WHERE name LIKE '%u%' OR age >= 30")
# result = my_cursor.fetchall()

# for row in result:
#     print(row)


# UPDATING RECORDS

# my_sql = "UPDATE users SET name = 'Ali Rios' WHERE id_user = 7"

# my_cursor.execute(my_sql)
# connection.commit()


# LIMIT RESULTS

# my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
# my_cursor.execute("SELECT * FROM users ORDER BY age ASC")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)


# DELETE RECORDS

# my_sql = "DELETE FROM users WHERE id_user = 12"

# my_cursor.execute(my_sql)
# connection.commit()

# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()

# for row in result:
#     print(row)

# DROP TABLES

my_slq = "DROP TABLE IF EXISTS customers"
my_cursor.execute(my_slq)

