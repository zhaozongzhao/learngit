"""
测试开发第一次作业
1、使用字典推倒是将下面字符串格式的数据，改成字典类型的数据
cook_str='BIDUPSID=D0727533D7147B7;PSTM=1530348042; BAIDUID=B1005C9BC2EB28;
 sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'

 2、请描述什么是可迭代对象？ 什么是迭代器？ 迭代器和生成器的区别？

3、 【】第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，

不够50往后累加，加到最后如果不够50也直接返回，因为没有可加的数据了

例子1

 a = [[1,3],[2,51],[3,49],[4,42],[5,42]] #入参

a1 = [[2,54],[4,91],[5,42]] #返回

例子2

 b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]] #入参

 b1 = [[1,50],[4,57],[6,52]] #返回

"""
# 第一题
cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042;BAIDUID=B1005C9BC2EB28;' \
           'sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'


def s_dir(cook_str):
    '''

    :param cook_str:  传入符合格式要求的字符串
    :return:
    '''
    return {i.split('=')[0]: i.split('=')[1] for i in cook_str.split(';')}




def r_list(list2):
    list_1 = []
    b = 0
    for i in list2:
        if b + i[1] >= 50:
            i[1] = i[1] + b
            list_1.append(i)
            b = 0
        elif len(list2) == i[0]:
            i[1] = i[1] + b
            list_1.append(i)
        else:
            b += i[1]
    return list_1


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

if __name__ == '__main__':
    a = [[1, 3], [2, 51], [3, 49], [4, 42], [5, 42]]
    b = [[1, 50], [2, 5], [3, 10], [4, 42], [5, 42], [6, 10]]

    print(s_dir(cook_str))
    # print(r_list(a))
    # print(r_list(b))
    print(r_list2(a))
    print(r_list2(b))
