def main():
    user_inp  = str(input("Write somthing: "))
    is_string_empty(user_inp)
    
def is_string_empty(empty):
    if len(empty) == 0:
        print("Empty string")
    else:
        print("thanku string available")
    return empty
    
main()