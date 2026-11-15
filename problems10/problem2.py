# Write a class "calculator" capable of finding square,cube,and square root of a number.

class Calculator:
  
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"The square of number is {self.n*self.n}")

    def cube(self):
        print(f"The cube of number is { self.n*self.n*self.n}")  

    def square_root(self):
        print(f"The square root of number is {self.n**0.5}")    # or self.n**(1/2)

num=int(input("Enter a number:"))           

calc=Calculator(num)
calc.square()
calc.cube()
calc.square_root()