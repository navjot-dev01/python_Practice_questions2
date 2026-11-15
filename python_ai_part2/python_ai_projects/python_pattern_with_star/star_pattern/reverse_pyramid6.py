#       *******
#        *****
#         ***
#          *

n= int(input("Enter the number:"))

for i in range(n,0,-1):                                    # method 1
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print()   



# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")                              # method 2

#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()        
