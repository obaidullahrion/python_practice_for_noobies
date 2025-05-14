from multiprocessing import Process
import os
import time

def square_numbers( ):
    for i in range(100):
        i * i
        time.sleep(0.1)
process = []
num_process = os.cpu_count()

for i in range(num_process):
    p = Process(target=square_numbers)
    process.append(p)

for p in process:
    p.start()

for p in process:
    p.join()


print('end main')