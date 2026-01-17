class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity should be non-negative")
        self.capacity = capacity
        self.size=0

    def __str__(self):
            return "🍪" * self.size

    def deposit(self, n):
        if n+self.size > self.capacity :
            raise ValueError('Jar capacity exceeds')
        self.size +=n
        

    def withdraw(self, n):
        if self.size-n < 0:
            raise ValueError('Jar has insufficient cookies')
        self.size-=n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size
