# class Number:
#     def __init__(self,n):
#         self.n=n

# n=Number(1)
# m=Number(2)
                            # gives error of unsupported operand
# print(n+m)


                #  Right method 

class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n + num.n
n=Number(1)
m=Number(2)

print(n+m)

'''
oprator overloading:

p1+p2               p1.__add__(p2)                these __add__ and so on are dunder(double underscore) method
p1-p2               p1.__sub__(p2)
p1*p2               p1.__mul__(p2)
p1/p2               p1.__truediv__(p2)
p1//p2              p1.__floordiv__(p2)




Other dunder / magic method in python are:

__str__()    -> defines a user-friendly , human-readable string represented of an object

__len__()    -> returns the length of the DataFrame's


'''



