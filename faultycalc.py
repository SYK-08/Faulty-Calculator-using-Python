print("Welcome!\n")

def calculator():
    print("Select Operation:\n","1.Addition(+)\n","2.Subtraction(-)\n","3.Multiplication(*)\n","4.Division(/)\n")

    try:
        op = input("Operator -->")
        num1 = input("First Number:")
        num2 = input("Second Number:")
        print("Result:")
        result = num1 + op + num2
        
        if result == "45*3":
            print(555)
        elif result == "56+9":
            print(77)
        elif result == "56/6":
            print(9)
        elif op == "+":
            print(float(num1) + float(num2))
        elif op == "-":
            print(float(num1) - float(num2))
        elif op == "*":
            print(float(num1) * float(num2))
        elif op == "/":
            print(float(num1) / float(num2))
        
        else:
            print("\n\t\tInvalid input! Please try again.\n")
            calculator()
    
    except Exception as e:
        print("\n\t\tSomething went wrong! Please try again.\n")
        calculator()

def run_again():
    while True:
        query = input("Do you want to calculate more?(y/n)").lower()
        if query == "n":
            exit()
        elif query == "y":
            calculator()
        else:
            print("\n\t\tInvalid input! Please try again.\n")
            run_again()

calculator()
run_again()
