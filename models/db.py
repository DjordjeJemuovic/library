import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="12345678",
    db="libreby",
    cursorclass=pymysql.cursors.DictCursor
)
if connection.open:
    print("Conected :D")
else:
    print("Not connected :(")
