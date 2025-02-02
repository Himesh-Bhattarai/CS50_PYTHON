#Write a program to check user can vote or not.
def main():
    user_age = int(input("Please!, Enter your age: "))
    is_eligible_vote(user_age)
    
def is_eligible_vote(user_age):
    if user_age <= 18:
        print("You are not eligible for vote.")
    else:
        print("you can vote.")


main()