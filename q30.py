def main():
    w = int(input("Enter first integer: "))
    x = int(input("Enter second integer: "))
    z = int(input("Enter third integer: "))
    y = int(input("Enter fourth integer: "))
    
    check_greatest(w, x, y, z)
    
def check_greatest(w, x, y, z):
    # Find the greatest number among the four
    greatest = max(w, x, y, z)
    
    # Print the greatest number
    if greatest == w:
        print("w is the greatest")
    elif greatest == x:
        print("x is the greatest")
    elif greatest == y:
        print("y is the greatest")
    else:
        print("z is the greatest")

main()
