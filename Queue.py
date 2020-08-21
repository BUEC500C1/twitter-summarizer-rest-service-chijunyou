# author : noracnr@bu.edu
import queue
import multiprocessing
import time
import threading
from hw4 import word2vid

num_worker_threads = 10

class word2vid_task():
    def __init__(self,keyword=""):
        self.keyword = keyword
        self.state = -1
    def run(self):
        word2vid(self.keyword)

def source():
  keys = [
    "Boston University",
    "ECE",
    "Dota",
    "2020",
    "United States",
    "China",
    "NBA",
    "Kobe",
    "Obama",
    "Boston",
    "Beijing"
  ]
  return keys

def worker():
  i = 0
  while True:
    item = q.get()
    if item is None:
      print("break nothing in item")
      break
    api = word2vid_task(item)
    api.run()
    i += 1
    print("-----Task Number{0}----".format(i))
    q.task_done()


q = queue.Queue()
threads = []
for i in range(num_worker_threads):
  t = threading.Thread(target=worker)
  t.start()
  threads.append(t)

for item in source():
    q.put(item)

    # block until all tasks are done
q.join()

    # stop workers
for i in range(num_worker_threads):
  q.put(None)
for t in threads:
  t.join()




