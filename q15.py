# Write a Function to check number is a prime number or not

def main():
    user_input = int(input("Number: "))
    is_prime_number(user_input)
    
def is_prime_number(user_input):
    if user_input % user_input == 0 or user_input % 1 == 0:
        print("its prime Number")
    else:
        print("its not prime number")
main()