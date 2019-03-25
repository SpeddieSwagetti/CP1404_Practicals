"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
while not finished:
    try:
        result = input("Please enter a valid integer: ")
        integar_check = int(result)
    except ValueError:
        continue
    else:
        print("Valid result is:", integar_check)
        finished = True