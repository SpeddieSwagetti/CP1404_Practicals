"""count in odd numbers from 1 to 20"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""a. count up in 10s from 0 to 100"""

for i in range(0, 110, 10):
    print(i, end=' ')
print()

"""b. count down in 1s from 20 to 1"""

for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""c. print n amount of stars"""

n = int(input("Enter Number: "))
for i in range(1, n+1, 1):
    print("*", end=' ')
print()

"""d. print n amount of stars and lines"""

n = int(input("Enter Number: "))
for i in range(1, n+1, 1):
    print("*"*i, end='\n')
print()