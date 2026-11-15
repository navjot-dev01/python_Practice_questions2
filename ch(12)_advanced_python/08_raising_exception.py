a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

if(b==0):
    raise ZeroDivisionError("Hey are program is not meant to be divided by zero...")
else:
    print(f'The division of numbers are:{a/b}')