


def add(n, i):
    return n+1


def test():
    for i in range(4):
        yield i

g = test()

for n in [1, 10, 5]:
   g = (add(n, i) for i in g)

for i in g:
    print(i)
