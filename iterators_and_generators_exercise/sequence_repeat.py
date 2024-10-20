class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.number -= 1
        if self.number >= 0:
            try:
                return self.sequence[self.index]
            except IndexError:
                self.index -= len(self.sequence)
                return self.sequence[self.index]
        raise StopIteration



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
