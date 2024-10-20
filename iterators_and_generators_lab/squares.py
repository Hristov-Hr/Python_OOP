def squares(num):

    for n in (el ** 2 for el in range(1, num + 1)):
        yield n


print(list(squares(5)))