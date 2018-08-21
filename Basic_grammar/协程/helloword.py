import asyncio
import threading

@asyncio.coroutine
def hello():
    print('Hello word!{}'.format(threading.currentThread()))
    #异步调用asynico,sleep(1)
    r = yield from asyncio.sleep(5)
    print('hello again{}'.format(threading.currentThread()))

#获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
#执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()