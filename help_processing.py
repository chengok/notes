# coding: utf-8

'''
该文件介绍多进程的使用。
'''

#-----------------------------------------------------分割线--------------------------------------------

##----------创建单进程

'''
创建进程需要导入Process模块:

from multiprocess import Process

使用p = Process(target=function, args=(parament,...)创建子进程实例.
其中target=传入子进程需执行的函数本身function,args传入函数需要的参数.参数数量不固定. 

之后使用p.start()运行实例.

要等待该子进程运行结束再运行之后的代码可以使用:p.join()
'''

#------ Example:

# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print ('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print ('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',)) # 创建子进程实例
#     print ('Process will start.')
#     p.start() # 运行实例
#     p.join() # 等待该子进程运行结束再运行之后的代码
#     print ('Process end.')


#-----------------------------------------------------分割线--------------------------------------------

##----------需启动大量子进程的情况

'''
对于需启动大量子进程的情况,可使用Pool模块:
from multiprocessing import Pool  # 对于需启动大量子进程的情况,可使用Pool模块

使用: p = Pool(number) 创建进程池.其中number为进程池包含子进程数量.不写默认为CPU核数.

使用: p.apply_async(function, args=(parament,...)运行子进程.

之后需关闭进程池: p.close()

同时,需等待所有子进程运行结束可使用: p.join()

'''

#------ Example:

# from multiprocessing import Pool  # 对于需启动大量子进程的情况,可使用Pool模块
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool()
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


#-----------------------------------------------------分割线--------------------------------------------

##----------进程间通讯

'''
不同进程间可以通过Queue,Pipe来通信.Pipe用于两个进程间通信,Quene用于多个进程间通信.
在只有两个进程通信的情况下Pipe效率高于Queue

1. Pipe

导入Pipe模块:
from multiprocessing import Pipe

创建Pipe通信的两端(返回一个双元素的list):
p = Pipe(duplex=False) 
其中duplex=False表示该Pipe只能单向通信.默认不写该参数为双向通信.

p[0],p[1]可以分别作为两个子进程的参数传递给子进程函数.也可以只传递一端给子进程,另一端交给父进程.

Pipe的两端可通过p.send()传送值,p.recv()接收值.

2. Queue

导入Queue模块:
from multiprocessing import Queue

创建Queue对象:
q = Queue(max) 其中max表示对象中可以存放的最大数量.
q可作为全局变量使用,也可以作为参数传递给子进程. 

使用q.put()在Queue对象中放入需传递的值,q.get()取出值.

'''
#------------------------
#------Pipe Example_1:
#------------------------

# from multiprocessing import Process, Pipe  # 在只有两个进程通信的情况下Pipe效率高于Queue

# def f(conn):
#     conn.send([42, None, 'hello']) # 传送值
#     conn.close()

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(parent_conn,))
#     p.start()
#     print(child_conn.recv())   # 接收值[42, None, 'hello']
#     p.join()

#------------------------
#------Pipe Example_2:
#------------------------

# import multiprocessing as mul

# def proc1(pipe):
#     pipe.send('hello')  # 传送值'hello'
#     print('proc1 rec:',pipe.recv()) # 接收值 'hello, too'

# def proc2(pipe):
#     # print('proc2 rec:',pipe.recv()) # 接收值'hello'
#     pipe.send('hello, too') # 传送值 'hello, too'

# if __name__ == '__main__':
#     # Build a pipe
#     pipe = mul.Pipe()   # pipe有两个子进程的参数，一个负责传送，一个负责接收. 

#     # Pass an end of the pipe to process 1
#     p1 = mul.Process(target=proc1, args=(pipe[0],))  # p[0],p[1]可以分别作为两个子进程的参数传递给子进程函数

#     # Pass the other end of the pipe to process 2
#     p2 = mul.Process(target=proc2, args=(pipe[1],))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#------------------------
#------Queue Example_1:
#------------------------
# from multiprocessing import Process,Queue

# def writer_proc(q):
#    q.put(100)

# def reader_proc(q):
#    print(q.get())

# if __name__ == '__main__':
#     q = Queue()
#     reader = Process(target=reader_proc,args=(q,))
#     reader.start()
#     writer = Process(target=writer_proc,args=(q,))
#     writer.start()
#     reader.join()
#     writer.join()

#------------------------
#------Queue Example_2:
#------------------------

import multiprocessing

def reader_proc(q):
    print(q.get())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()
    q.put(100)
    reader.join()

