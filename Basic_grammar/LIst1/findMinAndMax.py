
#迭代显示
def findMimAndMax(L):
    max = L[0]
    min = L[0]
    for i in L:
        if max < i:
            max = i
        elif min > i:
            min = i

    return (max,min)

print(findMimAndMax([7,1,3,9,5]))