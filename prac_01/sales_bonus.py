"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $"))

if  sales < 1000 and sales >= 0:
    bonus = (sales*0.1)
    print(int(bonus))
elif sales >= 1000:
    bonus = (sales * 0.15)
    print(int(bonus))
else:
    print("No bonus or invalid number")