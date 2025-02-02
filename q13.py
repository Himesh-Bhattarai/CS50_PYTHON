#write a programm to to check student is pass or failed on marks

# Main functioon of programm
def main():
#Ask for user marks
    user_marks = float(input("What is your marks: "))
    pass_mark = 100
    
    
    #call function to check pass or fail
    is_pass(user_marks, pass_mark)
    is_fail(user_marks, pass_mark)

# function to check user is pass or not

def is_pass(user_marks, pass_mark):
    if user_marks > 50 <= pass_mark:
        print("you are pass.")
    else:
        print("you are fail")
    
    # function to check user is fail or not

def is_fail(user_marks, pass_mark):
    if user_marks < 50 >= pass_mark:
        print("You are faillll.")


main()