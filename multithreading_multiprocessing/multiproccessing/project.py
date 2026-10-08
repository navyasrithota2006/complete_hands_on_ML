'''
real world example  - multiprocessing for cpu bound tasks
scenario - factorial calculation
factorial calculation,especially for larger integers,
involves significant computational work .
multiprocessing is used to distribute workloads across multiple cpu cores,
which improves performances
'''


import multiprocessing
import math
import sys
import time

#increse the maximum nuber of digits for integer conversion
#because system takes it as someone is hacking as calculation goes to larger numbers
#we have to set the system to take larger components

sys.set_int_max_str_digits(1000000)

#function to compute factorials of a given number

def compute_factorial(number):
    print(f"computing factorial of {number}")
    result = math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers = [5000, 6000, 7000, 8000]
    start_time = time.time()

    #create pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial,numbers)

    end_time = time.time() - start_time

    print(f"results : {results}")
    print(f"time taken : {end_time}")