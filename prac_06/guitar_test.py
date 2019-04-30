from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    gibson.get_age()
    gibson.is_vintage()

    another_guitar = Guitar("Another Guitar", 2012)
    another_guitar.get_age()
    another_guitar.is_vintage()

    print("{} get_age() - Expected 96. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 6. Got {}".format(another_guitar.name, another_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
