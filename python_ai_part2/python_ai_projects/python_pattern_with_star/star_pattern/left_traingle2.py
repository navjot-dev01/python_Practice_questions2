# WAP to print following pattern:
# *                                    # left triangle star pattern
# **
# ***  for n=3

n=int(input("Enter the number :"))

for i in range(1,n+1):
    print("* "*(i),end="")
    print("")
    # print("\n")                    # give space of 2 enter   

print("\n")   # if i write outside the loop then after loop done it givee sapce of n no.



for i in range(1,n+1):
    for j in  range(i):
        print("*",end="")
    
    for j in range(n-i):
        print(" ",end="")      
    print()        