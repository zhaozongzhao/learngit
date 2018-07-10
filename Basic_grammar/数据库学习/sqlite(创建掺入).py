import sqlite3

#连接数据库
coon = sqlite3.connect('test1.db')

#创建一个cursor

cursor = coon.cursor()

#执行一个数据sql,创建user表
cursor.execute('create table user(id varchar(20) primary key , name varchar(20))')


#执行插入语句
cursor.execute('insert into user(id,name) values (\'1\',\'TOM\')')


#获取插入的行数
print(cursor.rowcount)
#关闭cursor
cursor.close()
#提交事务
coon.commit()
#关闭connection
coon.close()

