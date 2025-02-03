#write a programm to check char is digit or not
def main():
    char = input("Input:")
    check_is_digit(char)

def check_is_digit(char):
    if char.isdigit():
        print("Your string contain number.")
    else:
        print(None)
main()