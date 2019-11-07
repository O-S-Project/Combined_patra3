import time
import threading
start = time.perf_counter()

def dosom(sllep):
    print("ok")
    time.sleep(sllep)

#
# t1 = threading.Thread(target = dosom)
# t2 = threading.Thread(target = dosom)

threads = []

for _ in range(10):
    t = threading.Thread(target = dosom,args = [1])
    t.start()
    threads.append(t)


for thre in threads:
    thre.join()

print(threads)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

finish = time.perf_counter()

print(f'finesh {round(finish-start,2)} seconds(s)')
