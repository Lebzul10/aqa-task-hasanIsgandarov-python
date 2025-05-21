def check_number():
    try:
        num = int(input("Enter a number: "))
        
        if num > 7:
            print("Hello")
        else:
            print("The number is not greater than 7")
    except ValueError:
        print("Invalid input. Please enter a valid number")

def check_name():
    name = input("Enter a name: ").strip()

    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def filter_multiples():
    try:
        nums = input("Enter numbers seperated by spaces: ")
        nums_list = [int(x) for x in nums.split()]
        multiples = [x for x in nums_list if x % 3 == 0 and x > 0]
        print("Multiples of 3:", multiples)
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces")

def handle_input(arg):
    match arg:
        case 1:
            fun = check_number()
        case 2:
            fun = check_name()
        case 3:
            fun = filter_multiples()
    return fun

if __name__ == "__main__":
    print("QA Automation Task - Python\n")
    print("1. Number check")
    print("2. Name check")
    print("3. Filter multiples\n")

    try:
        choice = int(input("Pick a test number: "))

        if choice >=1 and choice <= 3:
            handle_input(choice)
        else:
            print("Please enter a number from 1 to 3")
    except ValueError:
        print("Invalid input. Please enter a valid number")
