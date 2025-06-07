import random

list = []
fail = []
clear = []
great = []
fullscore = []


for i in range(20):
    randoms = random.randint(0, 100)
    list.append(randoms)
    if randoms <= 30:
        fail.append(randoms)
    elif randoms <= 69:
        clear.append(randoms)
    elif randoms <= 99:
        great.append(randoms)
    elif randoms == 100:
        fullscore.append(randoms)
    else:
        print("How did you get the score?")
        

print(list)
print(fail)
print(clear)
print(great)
print(fullscore)

