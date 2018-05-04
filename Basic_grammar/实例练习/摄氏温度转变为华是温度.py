

#摄氏温度转变为化石维度
def tem(a):

    tem1 = a * 9 / 5 + 32
    return tem1






if __name__ == '__main__':

    temperature = int(input('请输入当前温度'))
    print(tem(temperature))