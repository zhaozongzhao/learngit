import os
print(os.name)
#如果返回posix说明系统是liunx,nt是windows系统
print(os.uname())
#uname查询系统详情,在wondow不支持


#环境变量
#在操作系统中定义的环境变量
print(os.environ)
print(os.environ.get('PATH'))


#操作文件和目录的函数一部分放在os模块中,一部分放在os.path模块中,
#查看当前目录的绝对路径
print(os.path.abspath('.'))

#在某个目录下创建一个新目录,首先把新目录的完整路径表示出来

h = os.path.join('/Users/hnbl009/gitfile/learngit/Basic_grammar/文件读写','testdir')
os.mkdir(h)
print(os.getcwd())
os.rmdir(h)
#os.path.split()这样可以把一个路径拆分为两部分,后一部分总是最后最后级别目录和文件名
print(os.path.split(h))
#os.path.splittext()可以直接获取文件扩展名
print(os.path.splitext('/Users/hnbl009/zzz.txt'))

#文件操作使用下面的函数,假定当前目录下有一个test.txt
# os.rename('file1.0.py','文件读写.py')
# os.remove('test.py')

for i in os.walk('/Users/hnbl009/gitfile/learngit/Basic_grammar/文件读写'):
    print(i)
