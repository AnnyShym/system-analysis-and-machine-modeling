import random

class Handler:

    def __init__(self, probability, generator):
        self.probability = probability
        self.generator = generator
        self.task = None

    def tick(self):

        if not self.is_busy():
            return None

        # ev = next(self.generator)
        ev = random.random()
        if ev <= self.probability:
            return None
        else:
            task = self.task
            self.task = None
            return task
            
    def set_task(self, task):
        self.task = task

    def is_busy(self):
        return self.task is not None

    def __str__(self):
        return '1' if self.is_busy() else '0'
