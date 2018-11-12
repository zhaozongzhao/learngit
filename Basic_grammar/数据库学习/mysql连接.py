from pymysql import cursors,connect

#连接数据库

coon = connect(host='127.0.0.1',
               user = 'root',
               password ='12345678',
               db='guest',
               charset = 'utf8mb4',
               cursorclass = cursors.DictCursor)

try:
    with coon.cursor() as cursors:
      #创建嘉宾数据
       sql = 'insert into sign_guest(realname,phone,email,sign,event_id,create_time) ' \
          'values ("tom",18800110002,"tom@mail.com",0,1,now());'
       cursors.execute(sql)
      #提交事务
       coon.commit()


    # with coon.cursor() as cursor:
    #     sql = 'select realname,phone,email,sign FROM sign_guest where phone = %s'
    #     cursor.execute(sql,('18800110002',))
    #     result = cursor.fetchone()with coon.cursor() as cursors:
    #   #创建嘉宾数据
    #    sql = 'inster into sign_guest(realname,phone,email,sign,event_id,create_time) ' \
    #       'values ("tom",18800110002,"tom@mail.com",0,1,now());'
    #    cursors.execute(sql)
    #   #提交事务
    #    coon.commit()
    #     print(result)


finally:
    coon.close()