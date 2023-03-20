def add(x,y):
    print("Sum is: ",x+y)

def sub(x,y):
    print("Difference is: ",x-y)

def mul(x,y):
    print("Product is: ",x*y)

def div(x,y):
    try:
        print("Quotient  is: ",x/y)
    except ZeroDivisionError:
        print("Division by zero not possible")

c=1
while c==1:
    print("Operations")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    o=int(input("Enter your choice "))
    if o==1:
        a=int(input("Enter first number "))
        b=int(input("Enter second number "))
        add(a,b)
    elif o==2:
        a=int(input("Enter first number "))
        b=int(input("Enter second number "))
        sub(a,b)
    elif o==3:
        a=int(input("Enter first number "))
        b=int(input("Enter second number "))
        mul(a,b)
    elif o==4:
        a=int(input("Enter first number "))
        b=int(input("Enter second number "))
        div(a,b)
    else:
        print("Invalid choice")
    c=int(input("Do you want to continue(0(no)/1(yes))? "))

#using class

# class Calculator:
#     def add(self):
#         n1=int(input("Enter number1 "))
#         n2=int(input("Enter number2 "))
#         print("Sum: ",n1+n2)
#     def sub(self):
#         n1=int(input("Enter number1 "))
#         n2=int(input("Enter number2 "))
#         print("Difference: ",n1-n2)
#     def mul(self):
#         n1=int(input("Enter number1 "))
#         n2=int(input("Enter number2 "))
#         print("Product: ",n1*n2)
#     def div(self):
#         n1=int(input("Enter number1 "))
#         n2=int(input("Enter number2 "))
#         print("Quotient: ",n1/n2)
# c=1
# n=Calculator()
# while c==1:
#     print("Operations")
#     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
#     o=int(input("Enter your choice "))
#     if o==1:
#         n.add()
#     elif o==2:
#         n.sub()
#     elif o==3:
#         n.mul()
#     elif o==4:
#         n.div()
#     else:
#         print("Invalid choice")
#     c=int(input("Do you want to continue(0(no)/1(yes))? "))