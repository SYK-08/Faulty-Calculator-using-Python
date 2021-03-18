print("Welcome!\n")
print("Select Operation:\n","1.Addition(+)\n","2.Subtraction(-)\n","3.Multiplication(*)\n","4.Division(/)\n")
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
    print(int(num1) + int(num2))
elif op == "-":
    print(int(num1) - int(num2))
elif op == "*":
    print(int(num1) * int(num2))
elif op == "/":
    print(int(num1) / int(num2))
