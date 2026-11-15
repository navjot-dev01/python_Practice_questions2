# Write a program to find the file is identical & matches the content of another file.

with open("this.txt","r") as f:
    content=f.read()

with open("this_copy.txt") as f:
    content1=f.read()

if(content==content1):
    print("files are identical")

else:
    print("files are not identical")