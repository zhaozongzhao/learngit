# from www.orm import Model,StringField,IntegerField
#
# class User(Model):
#     __table__ = 'users'
#     id = IntegerField(primary_key=True)
#     name = StringField()
# if __name__ == '__main__':
#     user = User(id = 123,name = 'Michael')
#     user.insert()
#     # 查询所有User对象:
#     users = User.findAll()



h =filter(lambda s: s and len(s.strip()) > 0,['test', None, '', 'str', '  ', 'END'])
print(list(h))