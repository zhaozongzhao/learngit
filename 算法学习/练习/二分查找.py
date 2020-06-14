# 二分查找
"""
知识点整理：
1， //  取整除 - 返回商的整数部分

"""

def binary_aearch(list, num):
    """
    接受有序数组和一个元素，返回这个元素的位置
    """
    lef = 0
    right = len(list) - 1  # 获取列表最后一位数据
    print('左边界{}右边界{}'.format(lef,right) )
    while lef <= right:
        mid = (lef + right) // 2   # 如果（lef + right）不是偶数，python会自动向下取整
        guess = list[int(mid)]   
        if guess == num:     # 找到了元素
            return mid
        elif guess > num:    # 预期结果大于实际结果
            right = mid - 1
        elif guess < num:    # 预期结果小鱼实际结果
            lef = mid + 1
    return None

def get_square(num):
    """
    num : 输入的数据
    return : 返回数据次方根
    """
    lef = 0
    right = int(num)
    print('左边界{}右边界{}'.format(lef,right) )
    while lef <= right:
        mid = (lef + right) // 2   # 如果（lef + right）不是偶数，python会自动向下取整
        if  num == 2 ** mid :   
             return mid
        elif 2**mid > num:
              right = mid - 1
        else:
              lef = mid + 1
    return None




if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_aearch(my_list, 7))

    print(get_square(128))






