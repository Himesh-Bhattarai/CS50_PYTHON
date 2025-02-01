def main():
    num_mul = int(input("Number: "))
    mul(num_mul)
    
def mul(n):
    if n % 10 == 0:
        print("yes")
    else:
        print("No")
    
    
    
main()