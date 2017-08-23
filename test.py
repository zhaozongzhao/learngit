amount='显示第 1 到第 10 条记录，总共 23 条记录'
substr='共'
l=amount.rfind(substr)
print(l)
h=amount[l+1:-3]
print(h)
w=h.strip().lstrip().rstrip(' ')
print(w)

是多少舒适


