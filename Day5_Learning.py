
import threading
import multiprocessing
import asyncio
import time

#Multithreading
def thread_task(n):
    time.sleep(1)
    print(f"Thread {n} completed")

#Multiprocessing
def process_task(n):
    return n * n

#AsyncIO
async def async_task(n):
    await asyncio.sleep(1)
    print(f"Async task {n} completed")

async def run_async():
    await asyncio.gather(async_task(1), async_task(2))

#Synchronization
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1

#Semaphore
semaphore = threading.Semaphore(2)

def limited_task(n):
    with semaphore:
        print(f"Task {n} accessing resource")
        time.sleep(0.5)

#Deadlock prevention
lock_a = threading.Lock()
lock_b = threading.Lock()

def safe_task():
    with lock_a:
        with lock_b:
            print("Locks acquired safely")

def main():
    threads = [threading.Thread(target=thread_task, args=(i,)) for i in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    with multiprocessing.Pool(2) as pool:
        print("Process results:", pool.map(process_task, [1, 2, 3, 4]))

    asyncio.run(run_async())

    # GIL: Standard CPython builds limit parallel Python bytecode execution
    print("GIL: Threads are generally best for I/O-bound work.")

    # Lock and race-condition protection
    global counter
    threads = [threading.Thread(target=increment) for _ in range(1000)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Synchronized counter:", counter)

    threads = [threading.Thread(target=limited_task, args=(i,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    safe_task()

if __name__ == "__main__":
    main()
