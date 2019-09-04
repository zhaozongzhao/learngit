lt = [3, 5, 2, 1, 8, 4]
n= len(lt)
for x in range(n-1):
   for y in range(n-1-x):
      if lt[y]>lt[y+1]:
         lt[y],lt[y+1]=lt[y+1],lt[y]
print(lt)