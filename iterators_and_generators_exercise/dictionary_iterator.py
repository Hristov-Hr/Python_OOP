class dictionary_iter:

    def __init__(self, dict_iter):
        self.elements = [x for x in dict_iter.items()]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.elements):
            raise StopIteration
        return self.elements[self.index]



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
