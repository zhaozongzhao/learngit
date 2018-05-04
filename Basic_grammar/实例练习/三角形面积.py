import cmath

def  area(a,b,c):
    if a+b>c or a+c>b or c+b>a:
        p = (a+b+c)/2
        s = cmath.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    else:
        print('不能构成三角形')


if __name__ == '__main__':
    a,b,c = input('请输入三角形的边长 以 , 分割').split(',')
    print(a,b,c)
    print(area(float(a),float(b),float(c)))
