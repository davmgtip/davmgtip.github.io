import mysql.connector as sql

conn = sql.connect(
    host="127.0.0.1",
    username="root",
    password="123",
    db="test",
    charset="utf8"
)

def executeQuery(query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

while True:
    try:
        id = input("id: ")
        name = input("name: ")
        username = input ("username: ")
        password = input("password: ")
        executeQuery(f"INSERT INTO users VALUES({id}, '{name}', '{username}', '{password}');")
    except KeyboardInterrupt:
        break

conn.close()
