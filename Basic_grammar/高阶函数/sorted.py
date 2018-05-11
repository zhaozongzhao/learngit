L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    x = []
    x.append(t[1])
    return x

L2 = sorted(L,key = by_score,reverse = True)
print(L2)

by_score(L)