#     *
#     *
# * * * * *
#     *
#     *  

n=int(input("Enter the number: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(i==(n+1)/2 or j==(n+1)/2):
#             print("*",end="")        # if you want to space in star then give one more space to else option (" ")
#         else:
#             print(" ",end="")
#     print()            


for i in range(n):
    for j in range(n):
        if(i==(n)//2 or j==(n)//2):      
            print("*",end="")       
        else:
            print(" ",end="")
    print()            
