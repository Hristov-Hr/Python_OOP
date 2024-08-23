class Rhombus:
    def __init__(self, size):
        self.size = size

    def print_upper_part(self):
        for row in range(1, self.size + 1):
            print(' ' * (self.size - row), end='')
            print(row * '* ')

    def print_down_part(self):
        for row in range(self.size - 1, 0, -1):
            print(' ' * (self.size - row), end='')
            print('* ' * row)


rhombus = Rhombus(int(input()))
rhombus.print_upper_part()
rhombus.print_down_part()
