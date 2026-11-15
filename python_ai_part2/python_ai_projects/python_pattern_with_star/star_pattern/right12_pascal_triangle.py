#   *
#   **
#   ***
#   ****
#   ***
#   **
#   *

# n=int(input("Enter the number:"))

# for i in range(1,n+1):
#     print("*"*i,end="") 
#     print()                                  M-1
# for i in range(n-1,0,-1):
#     print("*"*(i),end="")
#     print()      




n=int(input("Enter the number :"))

for i in range(1,2*n):
    if(i<=n):
        print("*"*i)                        # M-2

    else:
        print("*" * (2*n-i))  





n=int(input("Enter the number:"))

for i  in range(1,n+1):
    for j in range(i):                      
        print("*",end="")
    print()
for i in range(n-1,0,-1):                     # M-3
    for j in range(i):
        print("*",end="")
    print()        