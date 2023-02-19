class Counter:
    def __init__(self):
        self.value = 0
    
    def incr(self):
        self.value += 1
    
    def decr(self):
        self.value -= 1
    
    def incrby(self, n):
        self.value += n

    def decby(self, n):
        self.value -= n
        
    def show(self):
        print(self.value)


def main():
    c = Counter()
    c.incr()
    c.show()
    c.decr()
    c.show()
    c.incrby(50)
    c.show()
    c.decby(30)
    c.show()

if __name__ == "__main__":
    main()