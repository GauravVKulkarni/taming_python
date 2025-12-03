import time
import datetime

print(datetime.date(2025, 11, 30))

print(time.time())
print(time.monotonic())
print(time.perf_counter())

print(time.localtime(time.time()))
print(time.localtime(time.time()).tm_hour)

t = time.localtime(time.time())
print(f"{t.tm_hour} : {t.tm_min} : {t.tm_sec}")

start = time.time()

time.sleep(2)

print(f"{(time.time() - start):.2f}")