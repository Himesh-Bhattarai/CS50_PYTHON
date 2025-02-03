def main():
    text = input("Enter anything: ")
    
    if check_contain_digit(text):  # Call the function and check the result
        print("The sentence contains digit.")
    else:
        print("The sentence does not contain any digits.")
    
def check_contain_digit(text):
    for char in text:  # Loop through each character in the text
        if char.isdigit():  # If any character is a digit, return True
            return True
    return False  # If no digits are found, return False

main()
