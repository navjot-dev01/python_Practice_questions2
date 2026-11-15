# Write __str__() method to print the vector as follows: 7i+8j+10k  better to take input from user
#  Assume the vector of 3 dimensions for this problem.

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z   

    def __str__(self):
        return f'Vector is {self.x}i + {self.y}j + { self.z}k'
    
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))

v=Vector(x,y,z)
print(v)
