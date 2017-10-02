
#Python OOP


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    @classmethod
    def raise_amt_new(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



#mp1 = Employee("Raj", "Shekar", "90000")

Employee.raise_amt_new(1.09)

print Employee.raise_amt

print " " \
      ""

import datetime
my_date = datetime.date(2013, 7, 26)

print Employee.is_workday(my_date)
