from Task import Task

class Source:

    def __init__(self):
        self.current_tick = 1
        self.first_time = True

    def tick(self):

        if self.current_tick == 1:
            self.current_tick += 1
            if not self.first_time:
                return Task()
            self.first_time = False
        else:
            self.current_tick -= 1
            return None

    def __str__(self):
        return str(self.current_tick)
