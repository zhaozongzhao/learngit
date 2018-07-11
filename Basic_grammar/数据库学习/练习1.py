
# import os, sqlite3
#
# db_file = os.path.join(os.path.dirname(__file__), 'test.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)
#
# # 初始数据:
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()
# cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
# cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
# cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
# cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
# cursor.close()
# conn.commit()
# conn.close()


import sqlite3

coon = sqlite3.connect('test.db')

cursor = coon.cursor()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    with sqlite3.connect('test.db') as coon:
         cursor = coon.cursor()
         cursor.execute('select * from user')
         value = cursor.fetchall()
         score_list = []
         name = []
         for i in range(len(value)):
              if value[i][2]>=low and value[i][2]<=high:
                   score_list.append(value[i])

    score_list = sorted(score_list,key =lambda score_list:score_list[2])
    for i in score_list:
       name.append(i[1])

    return name

assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60,100)
print('pass')