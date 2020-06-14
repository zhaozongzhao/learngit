"""
测试开发第一次作业
1、使用字典推倒是将下面字符串格式的数据，改成字典类型的数据
cook_str='BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28;
 sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'

"""
cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28;' \
           'sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'


def cook_str_dicr(str):
    '''
    处理特定格式的字符串
    :param  传入需要处理的字符串
    :type   str
    :return:  返回处理后的字典
    '''

    return {value.split('=')[0]: value.split('=')[1] for value in str.split(';')}


print(cook_str_dicr(cook_str))
print(cook_str_dicr.__doc__)

"""
2、请描述什么是可迭代对象？ 什么是迭代器？ 迭代器和生成器的区别？
答：
 可迭代对象：
         实现了迭代协议
         对象内部实现__iter__方法
         可以用for循环迭代
 迭代器：
         实现了迭代协议
         内部实现__next__方法
         通过iter可以将迭代对象转换为迭代器
         生成器式一种特殊的迭代器
 迭代器和生成器的区别：
         生成器式一种特殊的迭代器
         生成器式比迭代器多了3个方法 send(),close(),throw()
           
"""

'''
3、 【】第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，

不够50往后累加，加到最后如果不够50也直接返回，因为没有可加的数据了

'''

a = [[1, 3], [2, 51], [3, 49], [4, 42], [5, 42]]  # 入参
a1 = [[2, 54], [4, 91], [5, 42]]  # 返回
b = [[1, 50], [2, 5], [3, 10], [4, 42], [5, 42], [6, 10]]  # 入参
b1 = [[1, 50], [4, 57], [6, 52]]  # 返回

#方法1
import copy
def num(list1):
    """
    :param list1:  符合格式要求的列表
    :return: 计算处理后的数组
    """
    b = 0
    _list1 = []
    _list2 = copy.deepcopy(list1)  # 进行深层复制，不会操作原有数据
    for i in _list2:
        if i[1] + b >= 50:
            i[1] = i[1] + b
            _list1.append(i)
            b = 0
        elif len(_list2) == i[0]:
            i[1] = i[1] + b
            _list1.append(i)
        else:
            b += i[1]
    return _list1



#方法2
def r_list2(list2):
    list1 = []
    r_list1 = iter(list2)
    for i in r_list1:
       while True:
        if i[1] >= 50:
            list1.append(i)
            break
        try:
            g = next(r_list1)
            i = [g[0], g[1] + i[1]]
        except StopIteration:
            list1.append(i)
            break
    return list1


print(num(a))
print(num(b))

print(r_list2(a))
print(r_list2(b))
