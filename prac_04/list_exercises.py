numbers = []

print("Type 5 numbers")
for i in range(0, 5, 1):
    while True:
        try:
            user_input = int(input("Number: "))
            numbers.append(user_input)
            break
        except ValueError or NameError:
            print("Try Again")
print("The first number is", numbers[0])
print("The last number is", numbers[4])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers)/len(numbers))