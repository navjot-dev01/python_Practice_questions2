#   A
#   AB          
#   ABC
#   ABCD

# print(ord("A"))
# print(chr(97))

# print(ord("Z"))
# print(chr(6))
# print(chr(1000000))

n=int(input("Enter the number:"))

for i in range(1,n+1):
    for j in range(i):
        print(chr(ord("A")+j),end="")
    print()