def main():
    user_years = int(input("year: "))
    year(user_years)
    
def year(user_years):
    
    if user_years % 4 == 0:
        print("Leap year")
    elif user_years % 400 == 0:
        print("Leap year")
    else:
        print("Not leap year")
    
    return 

main()