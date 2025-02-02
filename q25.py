user_input = str(input("Enter a sentence or word: ")).strip()

if user_input == user_input.lower():
    print("its lower case")
elif user_input == user_input.upper():
    print("its upper case")
else:
    print("Your string must contain upper and lowercase.")