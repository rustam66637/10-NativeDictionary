class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        p = 0.33
        summ = 0
        for i in key:
            summ += ord(i) * p
        return int(summ % self.size)

    def is_key(self, key):
        if key in self.slots:
            return True
        else:
            return False

    def put(self, key, value):
        if self.is_key(key):
            self.values[key] = value
        else:
            i = self.hash_fun(value)
            self.slots[i] = i
            self.values[i] = value

    def get(self, key):
        if self.is_key(key):
            return self.values[key]
        else:
            return None
