class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        self.current_number += self.step
        return self.current_number - self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
