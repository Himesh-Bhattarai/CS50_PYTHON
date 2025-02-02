# Write a programm to check that string start with vowel or not
def main(): # Starting Function
    user_input = str(input("Any word: ")).strip().lower()
    check_vowel(user_input)
    print(user_input)
    
    
def check_vowel(user_input):
    if user_input.startswith('a','e','i','o','u'):
        print("Your word start with vowel.")
    else:
        print("Your word doesn't start with vowel.")
    
    
main()