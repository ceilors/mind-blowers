class Sequence:
    def __init__(self, *args):
        self.sequences = args

    def __iter__(self):
        for s in self.sequences:
            if callable(s):
                s = s()
            for e in s:
                yield e

    def __add__(self, other):
        def gen():
            i1 = self.__iter__()
            i2 = other.__iter__()
            while True:
                yield i1.__next__() + i2.__next__()

        return Sequence(gen)

    def take(self, n):
        iter = self.__iter__()
        return [iter.__next__() for i in range(n)]

#
# fib =  1, 1, 2, 3,  5,  8, ...
# fib1 = 1, 2, 3, 5,  8, 13, ...
# fib2 = 2, 3, 5, 8, 13, 21, ...
#
# so
# 
# fib  = 1, fib1
# fib1 = 1, fib2
# fib2 = fib + fib1
#

fib = Sequence([1], lambda: fib1)
fib1 = Sequence([1], lambda: fib2)
fib2 = fib + fib1

print(fib.take(10))
