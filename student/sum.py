def sum1(max):
    i=1
    h=0
    while i<=max:
        h=h+i
        i=i+1
    return h

def sum2(max):
   if max==1:
       return 1
   else:
      return sum2(max-1)+1



m=sum2(100)
print(m)