# square star pattern
# *****
# *****
# *****
# *****

num=int(input("Enter the number you want :"))

for i in range(1,num+1):
    print("*" * num,end="")
    print(" ")       # or print(end="")       but \n give 2 times space of end="" 

# or

for i in range(1 ,num+1):
    for j in range(num):
        print("*",end="")
    print()
