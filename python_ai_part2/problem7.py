# #WAP to find out the line number where python is present from que6

# with open("file7.txt","r") as f:
#     lines=f.readlines()

# found=False
# lineno=1
# for line in lines:
#     if("python" in line.lower()):
#         print(f'yes python is present.Line no.:{lineno}')
#         found=True
#     lineno +=1
#     # else:                if i write like this it gives all lines answer , try it              
#      #     print("not present")

# if not found:               # because found is your logic , not python's loop logic 
#     print("No python is not present")


#                           or

with open("file7.txt","r") as f:
    found=False
    for lineno,line in enumerate(f,start=1):
        if("python" in line.lower()):
            print(f'yes,python is present.line no.:{lineno}')
            found=True
            
    if not found:
        print("not present ")   

