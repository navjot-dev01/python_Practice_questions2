class Employee:
    def __init__(self):
        print("Constructor of Employee.")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer.")
        
    b=2

class Manager(Programmer):
    def __init__(self):
        Employee.__init__(self)
        Programmer.__init__(self)
        print("Constructor of Manager.")
    c=3

o=Manager()
print(o.a,o.b,o.c)

# next file super.py