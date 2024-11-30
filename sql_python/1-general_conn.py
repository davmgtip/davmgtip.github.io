import pandas as pd
import mysql.connector as sql

conn = sql.connect(host="localhost",user="root",passwd="123",database='test', charset='utf8')

data = pd.read_sql('SELECT * FROM users;', conn)

print(data)

if conn.is_connected():
    conn.close()