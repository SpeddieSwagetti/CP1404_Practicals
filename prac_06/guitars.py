from prac_06.guitar import Guitar


print("My Guitars!")
guitar_list = []
GUITAR_COUNT = 0


def guitar_input():
    user_input = True

    "Input Validation"
    while user_input is True:
        input_name = input("Name:")
        if input_name == "":
            user_input = False
        else:
            input_year = int(input("Year:"))
            if input_year == "":
                user_input = False
            else:
                input_cost = float(input("Cost:"))
                if input_cost == "":
                    user_input = False
                else:
                    GUITAR_COUNT + 1
                    append_guitar(input_name, input_year, input_cost)
                    print("{} added\n".format(guitar_list[GUITAR_COUNT-1]))

        "Finish loop"
        if user_input is False:
            print("\n ...snip...\n")
            if len(guitar_list) > 0:
                print("These are my guitars:")
                for i, guitar in enumerate(guitar_list):
                    print("Guitar {}: {}".format(i + 1, guitar_list[i]))
            else:
                print("No Guitars Present")


def append_guitar(input_name, input_year, input_cost):
    guitar_list.append(Guitar(input_name, input_year, input_cost))


def main():
    guitar_input()


main()