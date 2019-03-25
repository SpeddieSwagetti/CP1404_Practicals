"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    determine_status(score)

def determine_status(score):
    result = False
    if score < 0 or score > 100:
         result = "Invalid score"
    elif 50 <= score < 90:
        result = "Passable"
    elif 90 <= score <= 100:
        result = "Excellent"
    elif 0 <= score < 50:
        result = "Bad"
    return result
main()

