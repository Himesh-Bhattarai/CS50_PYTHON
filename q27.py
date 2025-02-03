def main():
    # Ask for a number from the user
    number = input("Number: ")
    
    # Validate the input
    usernumber = check_valid_num(number)
    
    # If valid, check if it's a palindrome
    if usernumber is not None:
        if is_palindrome(usernumber):
            print("It's a Palindrome Number")
        else:
            print("It's Not a Palindrome Number")
    else:
        print("Invalid input. Please enter a valid number.")

def check_valid_num(number):
    # Check if user input is a valid number
    if number.isdigit():
        return int(number)
    return None  # Return None if the input is invalid

def is_palindrome(usernumber):
    # Check if the number is a palindrome
    str_num = str(usernumber)
    return str_num == str_num[::-1]

# Run the program
main()
