class reverse_iter:

    def __init__(self, lst):
        self.lst = lst
        self.idx = len(self.lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <= 0:
            raise StopIteration
        self.idx -= 1
        return self.lst[self.idx]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
