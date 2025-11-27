import threading

variable = 0

lock = threading.Lock()

def increment():
    global variable
    for _ in range(100000000):
        # with lock:
        #     variable += 1
        variable += 1

threads = []

for i in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Final value of variable:", variable)
