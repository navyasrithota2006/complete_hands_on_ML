## multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"number : {number}"

numbers = [1,2,3,4,5,6,7]

t = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:  #it creates 3 threads and executes them 
    results = executor.map(print_number,numbers) # we have to map them with a executor function

for result in results:
    print(result)

finished_time = time.time() - t
print(finished_time)
