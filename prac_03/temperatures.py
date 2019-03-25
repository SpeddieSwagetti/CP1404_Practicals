"""Prac 03: Refactor temperatures.py to create seperate functions"""
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5 + 32)

def convert_fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit - 32) * 5 / 9)

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            while True:
                try:
                    celsius = float(input("Celsius: "))
                except ValueError or NameError:
                    continue
                fahrenheit = convert_celsius_to_fahrenheit(celsius)
                print("Result: {:.2f} F".format(fahrenheit))
                break
        elif choice == "F":
            while True:
                try:
                    fahrenheit = float(input("Fahrenheit: "))
                except ValueError or NameError:
                    continue
                celsius = convert_fahrenheit_to_celsius(fahrenheit)
                print("Result: {:.2f} C".format(celsius))
                break
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()