def add(a,b):
    print("addition=",a+b)
def sub(a,b):
    print("subtraction=",a-b)
def mul(a,b):
    print("multiplication=",a*b)
def div(a,b):
    print("division=",a/b)
x=int(input("enter a value:"))
y=int(input("enter b value:"))
choice = input("enter operation(+,-,*,/)")
if choice == "+":
 add(x,y)
elif choice == "-":
 sub(x,y)
elif choice == "*":
 mul(x,y)
elif choice == "/":
 div(x,y)
else:
   print("invalid operation") 