# WAP to make a long file and find out whether it contains "python"

with open("file6.txt")as f:
    content=f.read()

if("python" in content.lower()):
    print("yes!,python is present")

else:
    print("python is not present")