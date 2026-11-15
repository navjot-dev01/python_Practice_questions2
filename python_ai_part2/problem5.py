# # Repeat program 4 for a list of such words to be censored

# list=["donkey","photos","reading", "prove"]

# with open("donkey5.txt","r") as f:
#     content=f.read()

# for word in list:
#     content=content.replace(word,"#"*len(word))

# with open("donkey5.txt","w")as f:
#     f.write(content)

                                                    #  OR

import re

list=["donkey","photos","reading", "prove"]

with open("donkey5.txt","r")as f:
    content=f.read()

for word in list:
    content=re.sub(word,"#"*len(word),content,flags=re.IGNORECASE)

with open("donkey5.txt","w")as f:
    f.write(content)
