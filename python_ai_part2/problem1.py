# WAP to read the text from a given file"poems.txt" and  find out whether it contain the word "twinkle"

f=open("1poem.txt","r")
content=f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("Twinkle word is not present in the content")

f.close()