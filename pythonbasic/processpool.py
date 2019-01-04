from multiprocessing import Pool
import os
import time
import random

# 被调用的进程执行部分


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    starttime = time.time()
    time.sleep(2)
    endtime = time.time()
    print('Task %s runs %0.2f secs' % (name, (endtime - starttime)))


if __name__ == "__main__":
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))

    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('all done.')
    