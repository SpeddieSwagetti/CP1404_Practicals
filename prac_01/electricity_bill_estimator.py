"""electricity bill estimator"""

price = float(input("Enter price in cents per kWh:"))
daily_use = float(input("Enter kWh usage per day:"))
num_of_days = int(input("Enter number of days in billing period:"))

estimated_bill = price * 0.01 * daily_use * num_of_days
print("Congradulations you millenials! Your bill is: {}. Maybe stop buying icecream".format(estimated_bill))