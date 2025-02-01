#largets of three number
def main():
    a = float(input("Number: "))
    b = float(input("Number: "))
    c = float(input("Number: "))
    check_largest_num(a, b, c)
    
def check_largest_num(num1, num2, num3):
    if num1 > num2 and num3:
        print("Num 3 is largest")
    elif num2 > num1 and num3:
        print("Num2 is greater")  
    else:
        print("Num3 is greater")
        
main()
    
    