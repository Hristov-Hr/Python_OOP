import calendar


class DVD:

    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    def __init__(self, name: str, id_: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        return cls(name, id_, int(year), calendar.month_name[int(month)], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction \
{self.age_restriction}. Status: {'not ' if not self.is_rented else ''}rented"