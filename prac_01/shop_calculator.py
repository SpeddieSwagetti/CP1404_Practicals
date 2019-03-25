
"""Variable Definition"""
number_of_items = 0
item_index = 0
costlist = []

"""Input Validation Loop"""
while number_of_items <= 0:
    try:
        number_of_items = int(input("Enter number of items:"))
    except ValueError or number_of_items < 0:
        print("Invalid number of items!")

"""Cost Check for each item"""
for item_index in range(number_of_items):
    while True:
        try:
            cost = float(input("Price of item: $"))
            break
        except ValueError:
            print("Invalid price")
    costlist.append(cost)

total_cost = sum(costlist[0:number_of_items])

"""Check for eligible discount"""
if total_cost > 100:
    discounted_cost = total_cost * 0.9
    print("Total discounted price for", number_of_items, "items is ${:.2f}".format(discounted_cost))
else:
    print("Total price for", number_of_items, "items is ${:.2f}".format(total_cost))