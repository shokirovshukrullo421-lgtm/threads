import threading
import time
import random
##1-masala
def masala1():
    time.sleep(1) 
    print("Joriy thread:", threading.current_thread().name)
t1 = threading.Thread(target=masala1, name="Thread-1")
t1.start()
##2-masala

boshlanish = time.time()
def masala2():
    thread_name = threading.current_thread().name
    print(
        f"Dastur boshlangan vaqt: {boshlanish} | "
        f"Thread: {thread_name}"
    )

threads = []

for i in range(4):
    t = threading.Thread(target=masala2, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()
##3-masala
def masala3():
    sec = random.randint(1, 3) 
    time.sleep(sec)
    print(f"{threading.current_thread().name} | {sec} sekund kutdi")
threads = []
for i in range(5):
    t = threading.Thread(target=masala3, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()
for t in threads:
    t.join()
##4-masala

results = [] 
def task_9(number):
    kvadrat = number ** 2
    results.append(kvadrat) 
threads = []
sonlar = [1, 2, 3, 4, 5]
for i in range(5):
    t = threading.Thread(target=task_9, args=(sonlar[i],))
    threads.append(t)
    t.start()

##5-masalani tuhsunmadim