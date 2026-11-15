f=open("file2.txt")
print(f.read())
f.close()
  
       # OR

with open("file2.txt") as f:   # you don't have to explicitly close the file
    print(f.read())