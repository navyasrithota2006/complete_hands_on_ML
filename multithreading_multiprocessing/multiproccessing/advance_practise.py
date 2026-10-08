##multiprocessing with processpoolexecutor\

from concurrent.futures import ProcessPoolExecutor
import time

def sqaure_numbers(number):
    time.sleep(1)
    return f"square : {number * number}"


nums = [1,2,3,4,5,6,7]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sqaure_numbers,nums)

    for res in results:
        print(res)
