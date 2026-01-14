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
