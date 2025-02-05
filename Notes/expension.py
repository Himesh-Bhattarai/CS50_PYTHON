def main():
    x = get_int()
    print(f' x is {x}')

def get_int():
    while True:
        try:
            x = int(input("What the value of X? "))
        except ValueError:
            print("Value is not an intiger")
        else:
            return x
main()