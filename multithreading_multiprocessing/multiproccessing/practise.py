#processes that run in parallel
#cpu bound tasks - tasks that are heavy on cpu usage like mathematical computations
#parallel execution - multiple cores of the cpu

import multiprocessing
import time

def sqaure_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"cube: {i*i*i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = sqaure_numbers)
    p2 = multiprocessing.Process(target = cube_numbers)

    t= time.time()

    #start the process
    p1.start()
    p2.start()

    #wait for the processes to complete

    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)
