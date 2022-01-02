import threading, time ,random

mutex = threading.Lock()
class thread_one(threading.Thread):
    def run(self):
        global mutex
        print ("The first thread is now sleeping")
        time.sleep(random.randint(1, 5))
        print("First thread is finished")
        mutex.release()

mutex.acquire()
t1=thread_one()
t1.start()