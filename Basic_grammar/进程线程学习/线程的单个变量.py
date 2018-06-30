#多线程使用公共变量相互之间会产生影响,每个线程使用自己的局部变量比全部变量好,只有线程自己能看见,不会影响其他线程,全部变量必须加锁

#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，
# 任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前进程关联的student
    std  = local_school.student
    print('hell  {} in {}'.format(std,threading.current_thread().name))

def process_thead(name):
    #绑定threadlocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thead,args=('alice',),name='线程a')
t2 = threading.Thread(target=process_thead,args=('bob',),name='线程b')

t1.start()
t2.start()
t1.join()
t2.join()


