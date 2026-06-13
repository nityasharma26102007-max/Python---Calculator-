print("calculator")
print("the operation whatever u want")
num1 = int(input("enter the value num1"))
num2 = int(input("enter the value num2"))
operator = input("+,*,-,/")
if operator == '+':
    print("result",num1 + num2)
elif operator == '-':
    print("result",num1 - num2)
elif operator == '*':
    print("result",num1 * num2)
elif operator == '/':
    print("reslul",num1 / num2)
else:
    print("it is invalid operation")
    
