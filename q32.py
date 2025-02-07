def main():
    spec_syb = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "[", "]", "{", "}", ";", ":", "/", "?", ".", ">"]
    user_char = input("Enter any character or string: ")
    check_spec_syb(spec_syb, user_char)
    
def check_spec_syb(spec_syb, user_char):
    contains_special = False
    for char in user_char:
        if char in spec_syb:
            contains_special = True
            break
    
    if contains_special:
        print("The input contains a special character.")
    else:
        print("The input does not contain any special characters.")
        
main()
