score = int(input("Enter Red team score: "))
if score >= 90 and score <= 100:
    print("Bright Student")
elif score >= 80 and score <= 89:
    print("Good Student")
elif score >= 70 and score <= 79:
    print("Average Student")
else:
    print("Poor Student")