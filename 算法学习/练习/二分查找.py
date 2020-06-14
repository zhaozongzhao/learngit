# 二分查找


def binary_aearch(list, num):
    lef = 0
    right = len(list) - 1  # 获取列表最后一位数据
    print('左边界{}右边界{}'.format(lef,right) )
    while lef <= right:
        mid = (lef + right) // 2
        guess = list[int(mid)]
        if guess == num:
            return mid
        elif guess > num:
            right = mid - 1
        elif guess < num:
            lef = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_aearch(my_list, 7))
# print(type(my_list))



