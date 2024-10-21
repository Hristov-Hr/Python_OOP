def fibonacci():

    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
