''' Create a class with a class attribute a ; create an object from it and set "a" directly using object.a=0
Does this change the class attribute.
'''

class Demo:
    a=4

o=Demo()   # just call kiya class ko
print(o.a) # print the class attribute because instance attribute is not present

o.a=0       # set instance attribute  
print(o.a)  # print the instance attribute because instance attribute is present

print(Demo.a)  # print the class attribute