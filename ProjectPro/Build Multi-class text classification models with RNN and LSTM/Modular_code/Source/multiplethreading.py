import logging
from concurrent import futures

import threading
import queue

logger = logging.getLogger(__name__)

class TaskExecutor():
    """
    Executor class for task parallelization
    """
    def __init__(self, max_workers=None):
        self.executor = futures.ThreadPoolExecutor(max_workers=max_workers)

    def __del__(self):
        self.executor.shutdown()

    def wait_on_futures(self,futures_iter):
        """
        Wait for parallel processes to end
        """
        logger.info("TaskExecutor: starting to wait")
        _, not_done = futures.wait(futures_iter)
        logger.info("TaskExecutor: done waiting. ")
        if not_done:
            logger.info("TaskExecutor: there are some tasks that did not complete successfully: %s", not_done)

    def submit(self, fn, **kwargs):
        """
        Submit a task to the executor
        """
        return self.executor.submit(fn, **kwargs)

executor = TaskExecutor(max_workers=None)

class MultiThreadHandler:
    """
    Class to handle multiple threads
    """
    def __init__(self, max_queue_size=1000):
        self.threads = []
        self.tasks = []
        self.results = queue.Queue(maxsize=max_queue_size)
        self.errors = queue.Queue()

    def add_task(self, **kwargs):
        """
        Task addition to threads if available threads present
        """
        if self.results.full():
            logger.error("Result queue is full. Cannot add more tasks.")
            return
        self.tasks.append(kwargs)

    def worker(self, task):
        """
        Task worker
        """
        try:
            method = task['method']
            kwargs = {key: val for key, val in task.items() if key not in ['obj', 'method']}
            result = method(**kwargs)
            self.results.put(result)
            logger.info('Process completed!!! Task: %s', task['task_name'])
        except Exception as e:
            logger.error('Process not completed!!! Task: %s', task['task_name'], exc_info=True)
            self.errors.put((task, e))

    def run(self):
        """
        Task runner
        """
        try:
            for task in self.tasks:
                t = threading.Thread(target=self.worker, args=(task,))
                self.threads.append(t)
                t.start()
        except Exception:
            logger.critical("Failed to create thread: %s", exc_info=True)

        for t in self.threads:
            t.join()

        if not self.errors.empty():
            logger.warning("Some threads encountered errors.")

        return [self.results.get() for _ in range(self.results.qsize())]
