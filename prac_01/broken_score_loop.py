

score = float(input("Enter score: "))
while 0 < score <= 100:
    if 50 <= score < 90:
        print("Passable")
        score = float(input("Enter score: "))
    if 90 <= score <= 100:
        print("Excellent")
        score = float(input("Enter score: "))
    if score < 50:
        print("Bad")
        score = float(input("Enter score: "))
else:
    print("Invalid score")
