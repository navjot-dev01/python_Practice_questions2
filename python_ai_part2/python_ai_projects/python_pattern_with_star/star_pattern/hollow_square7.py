# WAP to print store pattern

# * * *             * * * *
# *   *             *     *
# * * *             *     *
#                   * * * * 

n= int(input("Enter the number:"))

for i in range(1,n+1):            
    if(i==1 or i==n):
        print("* "*n)       
        
    else:
        print("* ",end="")
        print("  "*(n-2),end="")
        print("* ")
        

n= int(input("Enter the number:"))

for i in range(1,n+1):
    if(i==1 or i==n):
        for j in range(n):
            print("*",end=" ")
        print()            # for space after 1 and last line
    else:
        print("*",end=" ")     # for * at starting of all lines except 1 and n
        for j in range(n-2):
            print(" ",end=" ") # for space between 1 and last star of lines except 1 and n
        print("*")             # for * at last of all lines except 1 and n



        
              
