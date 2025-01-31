name = input("Enter your name: ")

match name:
    case "Himesh" | "himesh" | "HIMESH":
        print("Helo, Himesh")
    case "John" | "john" | "JOHN":
        print("Hello, John")
    case "Jane" | "jane" | "JANE":
        print("Hello, Jane")
    case _:
        print("Hello, Stranger")
