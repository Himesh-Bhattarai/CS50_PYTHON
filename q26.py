def main():
    # Get inputs for triangle sides
    side1 = input("Enter the value for side1 (or 'x' if unknown): ")
    side2 = input("Enter the value for side2 (or 'x' if unknown): ")
    side3 = input("Enter the value for side3 (or 'x' if unknown): ")

    # Convert inputs to float or keep as 'x'
    side1 = float(side1) if side1 != 'x' else None
    side2 = float(side2) if side2 != 'x' else None
    side3 = float(side3) if side3 != 'x' else None

    # Check if the inputs can form a triangle
    if side1 and side2 and side3:
        if is_valid_triangle(side1, side2, side3):
            check_triangle(side1, side2, side3)
        else:
            print("The given sides do not form a valid triangle.")
    else:
        # If one side is unknown, calculate it
        find_x(side1, side2, side3)


def is_valid_triangle(a, b, c):
    # Check the triangle inequality
    return a + b > c and b + c > a and c + a > b


def check_triangle(a, b, c):
    if a == b == c:
        print("It's an Equilateral triangle.")
    elif a == b or b == c or c == a:
        print("It's an Isosceles triangle.")
    else:
        print("It's a Scalene triangle.")


def find_x(a, b, c):
    # Calculate the missing side using the Pythagorean theorem (for right-angled triangles)
    if a is None:
        a = (c ** 2 - b ** 2) ** 0.5
        print(f"The missing side1 is: {a}")
    elif b is None:
        b = (c ** 2 - a ** 2) ** 0.5
        print(f"The missing side2 is: {b}")
    elif c is None:
        c = (a ** 2 + b ** 2) ** 0.5
        print(f"The missing side3 is: {c}")
    else:
        print("Cannot determine the missing side.")


main()
