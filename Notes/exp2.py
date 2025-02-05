def main():
    x = get_int()
    print(f' x is {x}')

def get_int():
    while True:
        try:
            return int(input("What the value of X? "))
        except ValueError:
            pass
        
main()