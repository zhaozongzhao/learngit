
#作业 
```
"""
1、使用字典倒导式将下面字符串格式的数据，改成字典类型的数据 cook_str='BIDUPSID=D0727533D7147B7;PSTM=1530348042;
BAIDUID=B1005C9BC2EB28; sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'
等号前面的是键，后面的是值。
"""

cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042;BAIDUID=B1005C9BC2EB28; sugstore=0;_' \
           '_cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'

# 方法1 字典推导式
dict1 = {dictsir.split('=')[0]: dictsir.split('=')[1] for dictsir in cook_str.split(';')}

# 方法2 列表推导式

dict2 = dict([dictsir.split('=') for dictsir in cook_str.split(';')])

"""
2、请描述什么是可迭代对象？ 什么是迭代器？ 迭代器和生成器的区别？

  可迭代对象: 指内部含有'__iter__'方法的对象,可以用for… in…循环访问
  迭代器: 拥有__iter__方法和__next__方法的称之为迭代器
  迭代器和生成器的区别: 生成器是一种特殊的迭代器,生成器在迭代的过程中可以改变当前迭代值,迭代器不能修改



"""

"""
3、 【】第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，
不够50往后累加，加到最后如果不够50也直接返回，因为没有可加的数据了
例子1

 a = [[1,3],[2,51],[3,49],[4,42],[5,42]] #入参

a1 = [[2,54],[4,91],[5,42]] #返回



例子2

 b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]] #入参

 b1 = [[1,50],[4,57],[6,52]] #返回


"""

a = [[1, 3], [2, 51], [3, 49], [4, 42], [5, 42]]
b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]]

list1 = iter(b)
list2 = []

for i in list1:
    if i[1] >= 50:
        list2.append(i)
    while i[1] < 50:
        try:
            h = next(list1)
            i[1] = i[1] + h[1]
            if i[1] > 50:
                i[0] = h[0]
                list2.append(i)
        except StopIteration as e:
            list2.append(i)
            break


print(list2)

```

### 笔记:
#### 工程结构化

- readme : 对于项目的整体介绍,包含项目的使用手册,通常显示为README.rst/README.md
- license : 项目的授权
- setup.sh : 通过setup核心代码打包,离线安装文件
- sample : 存储项目的核心代码
- requirements.txt : 虚拟环境第三方库,用户恢复环境
- dosc : 包的参靠文档
- test: 所有的代码测试
- makfefile : 用于项目的命令 
### 命名元祖
- 数值: 整数,浮点数,布尔类型
- 序列类型 : 字符串,元素,列表
- 散列: 字典,集合









