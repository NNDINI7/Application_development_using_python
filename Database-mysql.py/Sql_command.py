import mysql.connector as connector 

mydb = connector.connect(
    host="localhost",
    user="root",
    password="2004",
    database="user_management",
    port = 3306
)

print("Connected to the database successfully!", mydb)

cursor = mydb.cursor()
 
#for reading databases: 

# result = cursor.execute("show databases")
# result = cursor.fetchall()
# for db in result:
#     print(db)

#for creating a database if it does not exist:
# query = "create database if not exists user_management"

query = "use user_management"
cursor.execute(query)
query = """create table if not exists users (
    id int auto_increment primary key,
    name varchar(20) not null,
    email varchar(20) not null
)"""
cursor.execute(query)

query = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
values = [
    (1, 'John Doe', 'johndeo@gmail.com'),
    (2, 'Jane Smith', 'jane@24gmail.com'),
    (3, 'Alice Johnson', 'johnson@rknec.edu')
]
# cursor.executemany(query, values)
mydb.commit()  # Commit the changes to the database

cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
for row in result:
    print(row)

#update row with id 1 and set email as jd@example.com

query = "UPDATE users SET email = 'jd@example.com' WHERE id = 1"
cursor.execute(query)
mydb.commit()  # Commit the changes to the database
query = "SELECT * FROM users"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

#delete from users id = 1
query = "DELETE FROM users WHERE id = 1"
cursor.execute(query)
mydb.commit()  # Commit the changes to the database
query = "SELECT * FROM users"
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

