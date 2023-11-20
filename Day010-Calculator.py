logo = """
 _____________________
|  _________________  |
| | Josyedaju    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def calculator():
    first_no = float(input("What's the first number?: "))
    print("+\n-\n*\n%")
    n=0
    while n == 0:
        operation = input("Pick an operation: ")
        second_no = float(input("What's the next number?: "))



        def addition(first_no,second_no):
            return first_no+second_no
        def substration(first_no,second_no):
            return first_no-second_no
        def multiplication(first_no,second_no):
            return first_no*second_no
        def division(first_no,second_no):
            return first_no/second_no        

        if operation == "+":
            total = addition(first_no,second_no)
            print(f"{first_no} + {second_no} = {total}")
        elif operation =="-":
            total = substration(first_no,second_no)
            print(f"{first_no} - {second_no} = {total}")

        elif operation == "*":
            total = multiplication(first_no,second_no)
            print(f"{first_no} * {second_no} = {total}")

        elif operation == "/":
            total = division(first_no,second_no)
            print(f"{first_no} / {second_no} = {total}")

        else:    
            print("Error with operation")
        first_no = total
        proceed = input(f"Type 'y' to continue calculating with {first_no}, or type 'n' to start a new calculation? ").lower()      
        if proceed =='n':
            calculator()





calculator()