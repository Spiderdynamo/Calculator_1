def add():
    print("Addition")
    c=a+b
    print("Sum = ",c)
def sub():
    print("Substraction")
    d=a-b
    print("Sub = ",d)
def mul():
    print("Multiplication")
    e=a*b
    print("Mul = ",e)
def div():
    print("Division")
    f=a/b
    print("Div = ",f)
a=int(input("Enter a number = "))
b=int(input("Enter another number = "))
q=str(input("Enter an Operator = "))
if q=='+':
    add()
elif q=='-':
    sub()
elif q=='*':
    mul()
elif q=='/':
    div()
else:
    print ("ERROR!!! OPERATOR NOT FOUND")



