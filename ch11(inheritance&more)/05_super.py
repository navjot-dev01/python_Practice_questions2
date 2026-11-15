class Employee:
    def __init__(self):
        super().__init__()   # if i don't write super() here then it work perfectly because it is last class
        # of MRO chain (Method Resolution Order) [child -> mother -> father ]
        print("Constructor of Employee.")      
    a=1

class Programmer:
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer.")
        
    b=2

class Manager(Programmer,Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager.")
    c=3

o=Manager()
print(o.a,o.b,o.c)