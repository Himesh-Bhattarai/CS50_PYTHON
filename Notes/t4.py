def main():
    x = int(input("Enter a Number: "))
    if is_even(x) is True:
        print("Even")
    elif is_even(x) is None:
        print("None")
    else:
        print("Odd")
        
def is_even(x):
    if x == 0:
        return None  
    elif x % 2 == 0:
        return True  
    else:
        return False  

main()
