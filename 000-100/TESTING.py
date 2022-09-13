class Foo:
    def __init__(self, x0, x1, p, q):
        ...
        self.x0 = x0
        self.x1 = x1
        self.p = p
        self.q = q

    def __iter__(self):
        a, b, = (
            self.x0,
            self.x1,
        )
        yield a
        yield b
        p, q = self.p, self.q
        while True:
            a, b = b, p * b - q * a
            yield b


f = Foo(0, 1, 1, -1)
it = iter(f)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
