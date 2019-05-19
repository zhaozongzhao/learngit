#导入mysql驱动
import mysql.connector
#注意把password设置你的口令
coon = mysql.connector.connect(user = 'root',password = 'root1',database = 'test',use_unicode = True)
cursor = coon.cursor()

# #创建user表
# cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
#插入一条记录
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)

#提交事务
coon.commit()
cursor.close()
#运行查询
cursor = coon.cursor()
cursor.execute('select * from user where id = {}'.format('1',))
values = cursor.fetchall()
print(values)
cursor.close()
coon.close()