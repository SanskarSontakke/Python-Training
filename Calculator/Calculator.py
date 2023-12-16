# Devoloped By Sanskar Sontakke
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
sign = input("Enter your sign")

if sign == '+' :
    print(num1 + num2)
elif sign == '-':
    print(num1-num2)
elif sign == '*':
    print(num1*num2)
elif sign == '/':
    print(num1/num2)
else:
    print("Incorrect Option")
