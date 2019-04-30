"""CP1404/CP5632 Practical - guitar class."""


CURRENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = float(cost)

    def __str__(self):
        vintage_status = ""
        if self.is_vintage() is True:
            vintage_status = "(Vintage)"
        return "{}({}), worth ${} {}".format(self.name, self.year, self.cost, vintage_status)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

