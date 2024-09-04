class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_roman(cls, value):
        roman_num = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        result = 0
        for i in range(len(value)):
            num = roman_num[value[i]]
            if len(value) - 1 == i or num >= roman_num[value[i + 1]]:
                result += num
            else:
                result -= num
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            value = ''
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"



