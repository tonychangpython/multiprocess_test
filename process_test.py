from multiprocessing import Process

import os
import math


def calc():
    for i in range(0, 4000000):
        math.sqrt(i)


processes = []

for i in range(os.cpu_count()):
    print('cpu register %d' %i)
    processes.append(Process(target=calc))


if __name__=='__main__':
    for process in processes:
        process.start()

    for process in processes:
        process.join()        

