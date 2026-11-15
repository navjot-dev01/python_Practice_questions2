''' The game() function in a program let user to play a game and return a score as an integer. You need to
read a file named "hi-score.txt" which is either blank or contains the previous hiscore. You need to write
a program to up-date the hi-score whenever the game() function breaks the hi-score.
'''

import random

def game():
    print("Let's start this game!")
    score=random.randint(1,62)
    # fetch the hi-score
    with open("hiscore.txt","r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore = 0

    print(f"Your score:{score}")
    
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
        
    return score
game()        


