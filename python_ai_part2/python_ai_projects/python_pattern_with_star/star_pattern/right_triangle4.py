#     *
#    **
#   ***
#  ****
# *****   

n=int(input("Enter the number:"))

for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*i)                                  # method 1


for i in range(1,n+1):
    for j in  range(n-i):
        print(" ",end="")                       # method 2
    
    for j in range(i):
        print("*",end="")      
    print()    



# for i in range(1,n+1):
#     for j in  range(i):
#         print("*",end="")                           # for left aligned triangle
    
#     for j in range(n-i):
#         print(" ",end="")      
#     print()        