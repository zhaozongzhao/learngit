import multiprocessing

def proc1(pipe):
    pipe.send('hello')
    print('接收信息 1：',pipe.recv())



def proc2(pipe):
    print('接收信息2',pipe.recv())
    pipe.send('tooo')
 


if __name__ == '__main__':
    multiprocessing.freeze_support()
    pipe = multiprocessing.Pipe()


    p1 = multiprocessing.Process(target=proc1,args=(pipe[1],))


    p2 = multiprocessing.Process(target=proc2,args=(pipe[0],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
