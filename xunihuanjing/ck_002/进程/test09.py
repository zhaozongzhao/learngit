'''
1,队列初始化
'''

# 初始化
from queue import Queue,LifoQueue,PriorityQueue
# cq = Queue()  #先入先出
# lq = LifoQueue() #后入先出
pQ = PriorityQueue() #优先级
pQ.put((1,11))
pQ.put((2,10))
pQ.put((2,9))
print(pQ.get())
print(pQ.get())
# #
# # cq.put('11')
# # cq.put('12')
# # lq.put('11')
# # lq.put('12')


# #
# # print(cq.get())
# # print(lq.get())


# # 队列中的参数
# from queue import Queue, LifoQueue, PriorityQueue
#
# cq = Queue(5)  # 设备队列为5
#
# for i in range(5):
#     cq.put(i, timeout=3)
#
# #获取当前队列中有多少个元素
# print(cq.qsize())
#
# # 判断队列是否已满
# print(cq.full())
# for i in range(5):
#     cq.get(block=False)
#     cq.task_done()        #告诉队列执行完成
# cq.join()                 #等待队列执行完成
# # 判断队列是否为空
# print(cq.empty())
#