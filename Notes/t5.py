def main():
    x = int(input("Enter a Number 1: "))
    if is_even(x):
        print("Even")
    elif is_even(x) == None:
        print("None")
    else:
        print("Odd")
        
def is_even(x):
    return True if x % 2 == 0 else False
    
main()
