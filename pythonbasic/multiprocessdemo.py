from multiprocessing import Process
import os

def run_process(name):
    print('print child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    p = Process(target=run_process, args=('test',))
    print('Child Process start')
    p.start()
    p.join()
    print('Child Process end.')
