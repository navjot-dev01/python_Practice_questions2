# Override the __len__() method vector of problem 5 to display the dimensions to the vector .

class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z   

    def __str__(self):
        return f'Vector is {self.x}i + {self.y}j + { self.z}k'
    
    # def __len__(self):                    # tuple
    #     return len((self.x,self.y,self.z))

    # def __len__(self):
    #     return len([self.x,self.y,self.z])             # list

    def __len__(self):
        return len(self.__dict__)                     # dictionary
    
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))

v=Vector(x,y,z)
print(v)
print("length of vector is ",len(v))       # TypeError: object of type 'Vector' has no len()
                                          # if don't write __len__()
                                          # for exam write 3 
                                          # for project use tuple /list tuple slightly better