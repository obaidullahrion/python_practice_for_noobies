import threading
import time

threads = []
def one(sec):
    time.sleep(sec)
    print(f"first task slept {sec} sec")

def two():
    time.sleep(1)
    print("second task")
    
def three():
    time.sleep(1)
    print("third task")




x = threading.Thread(target= one , args=[5])
y = threading.Thread(target= two , args=())
z = threading.Thread(target= three , args=())


x.start()
y.start()
z.start()
# one()
# two()
# three()
x.join()
y.join()
z.join()

print(threading.enumerate())
print(threading.active_count())
print(time.perf_counter())

