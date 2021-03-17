print("Welcome!\n")
print("Choose an operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
operator = input("-->")
num1 = input("First Number:")
num2 = input("Second Number:")
print("Result:")
result = num1 + operator + num2
if result == "45*3":
    print(555)
elif result == "56+9":
    print(77)
elif result == "56/6":
    print(9)
elif operator == "+":
    print(int(num1) + int(num2))
elif operator == "-":
    print(int(num1) - int(num2))
elif operator == "*":
    print(int(num1) * int(num2))
elif operator == "/":
    print(int(num1) / int(num2))
