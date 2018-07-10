import sqlite3

coon = sqlite3.connect('test1.db')

cursor = coon.cursor()

cursor.execute('select * from user where Id = ?',('1',))

value = cursor.fetchall()

print(value)

cursor.close()
coon.close()