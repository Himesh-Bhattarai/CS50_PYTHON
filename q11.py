def main():
    a = float(input("Number"))
    b = float(input("Number"))
    c = float(input("Number"))
    
    is_small_one(a, b, c)
    
def is_small_one(x, y,z):
    if x < y and x > z:
        print("Num 3 is small")
    elif y > x and y > z:
        print("")
    
main()