import threading
from Queue import Queue

class DelayedJobProcessor(threading.Thread):
  def __init__(self, jobs_queue):
    """ A processor that pop functions from a queue and runs them. """
    self.jobs_queue = jobs_queue
    
  def run(self):
    while True:
      try:
        if !self.jobs_queue.empty():
          fn, data = self.jobs_queue.get()
          if fn is not None:
            if data is not None:
              fn(data)
            else:
              fn()
              
          self.jobs_queue.task_done()
        else:
          time.sleep(15)
      except Exception as e:
        # log the error, but don't do anything. Just list the process as a failure.
        # TODO : Add a callback for when an error occurs.

jobs_queue = Queue()
processor = DelayedJobProcessor(jobs_queue)
processor.start()

def add_delayed_job(fn, data=None):
  """ Add a job to the jobs queue. """
  jobs_queue.put((fn, data))
        
