#方法重写

class FooParent(object):

    def __init__(self):
        self.parent = 'I \'m the parent'

        print('Parent')

    def bar(self,message):

        print('{} from Parent'.format(message))



class  Foochild(FooParent):
     def __init__(self):
         #super(Foochild(,self)首先找到Foochild的父类(FooParent),然后把类b的对象FooParent转化为FooParent的对象
        super(Foochild,self).__init__()
        print('Child')


     def bar(self,message):
         super(Foochild,self).bar(message)
         print('Child bar fuction')
         print(self.parent)

if __name__ == '__main__':
    foochild = Foochild()
    foochild.bar('Helloword')