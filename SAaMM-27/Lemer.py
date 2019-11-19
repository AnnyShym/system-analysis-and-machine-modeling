class LemerGenerator:

    def __init__(self, m, r0, a):
        self.r0 = r0
        self.last_r = r0
        self.m = m
        self.a = a

    def __iter__(self):
        return self

    def __next__(self):

        self.last_r = (self.a * self.last_r) % self.m
        
        res = self.last_r / self.m
        return res


