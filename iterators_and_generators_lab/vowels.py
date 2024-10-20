class vowels:

    def __init__(self, text):
        self.text = text
        self.vowels = [el for el in self.text if el.lower() in "aeiouy"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.vowels):
            raise StopIteration
        return self.vowels[self.index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
