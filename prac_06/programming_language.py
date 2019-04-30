"""Module for programming_language"""


class ProgrammingLanguage:
    """Represents a Programming Language Object"""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        return "{},{} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        if self.typing is "Static":
            self.typing = False
            return bool(self.typing)
        else:
            self.typing = True
            return bool(self.typing)
