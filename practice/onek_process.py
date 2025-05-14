import multiprocessing
import time 


start = time.perf_counter()
def one(sec):
    print("sleep for one sec")
    time.sleep(sec)
    print("output 1")
    
def two(sec):
    print("sleep for two sec")
    time.sleep(sec)
    print("output 2")



if __name__ == '__main__':
    x = multiprocessing.Process(target=one , args=[5])
    y = multiprocessing.Process(target=two , args=[5])

    x.start()
    y.start()
    
    x.join()
    y.join()

print(f"Finished in {round(time.perf_counter()-start, 2)} sec" )
