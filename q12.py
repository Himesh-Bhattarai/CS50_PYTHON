def main():
        
    user_age = int(input("Your age: "))
    check_eligibility(user_age)

def check_eligibility(age):
    if age  >= 18:
        print("eligibialty for vote")
    elif age <= 0:
        print("please inpute valid input")
    else:
        print("Not eligible")      
    return age  

main()