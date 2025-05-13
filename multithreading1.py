import threading
import time

counter = 0
lock = threading.Lock()

def count_up(name):
    global counter
    for _ in range(5):
        time.sleep(0.1)
        with lock:
            counter += 1
            print(f"{name} incremented counter to {counter}")

t1 = threading.Thread(target=count_up, args=("Thread-A",))
t2 = threading.Thread(target=count_up, args=("Thread-B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final counter value:", counter)
