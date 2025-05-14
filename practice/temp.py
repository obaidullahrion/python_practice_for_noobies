from multiprocessing import cpu_count, process
import multiprocessing
import os 
import time 
proc = []
cpus = os.cpu_count()
def one():
    time.sleep(6)
    print("first")
if __name__ == "__main__":
    for i in range (6):
        p = multiprocessing.Process(target=one)
        proc.append(p)

    for p in proc:
        p.start()
    for p in proc:
        p.join()
