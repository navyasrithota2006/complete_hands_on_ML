#multi threading
'''when to use multithreading
1. i/o bound tasks :tasks that spend more time waiting for i/o operations like file operations
2. concurrent execution : when you want to improve through put of your application by performing multiple operations at the same time
'''

import threading
import time 

def print_numbers():
    for i in range(5):
        time.sleep(2)   # this makes the output to be 2 s away from other output to print
        print(f"Number : {i}")
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: { letter}")

## the two functions are waiting 2 s to show their results
#now if i want like while numbers function is sleep then run letter and when letter function
#is sleep then run the number function
#if i want them to run concurrently i wanted to use multithreading

##create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target= print_letter)

t = time.time()
#start the threads
t1.start()
t2.start()
#wait for the threads to complete
t1.join()
t2.join()
#after comleting it joins to the main thread

finished_time = time.time() - t
print(finished_time)