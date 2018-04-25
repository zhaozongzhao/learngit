

def rabbit(a):

        if a  == 1:
            return 1
        elif a == 2:
            return 1
        else:
          b = rabbit((a-1))+rabbit(a-2)
          return b

a=1
while a < 1000:
    print(rabbit(a),end=',')
    a+=1

