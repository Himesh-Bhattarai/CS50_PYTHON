#write a program to find positive,negative and zero
user_input = int(input("Enter Number: "))
if user_input < 0:
    print("Negtive")
elif user_input > 0:
    print("postive")
else:
    print("Zero")