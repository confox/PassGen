#     Password Generator V1
#
#   Author
#   ████████████████████████████████████████
#   █─▄─▄─█▄─██─▄█▄─▄▄▀█▄─█─▄█▄─▄█─▄▄▄▄█─█─█
#   ███─████─██─███─▄─▄██─▄▀███─██▄▄▄▄─█─▄─█
#   ▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀

#     Date 20/07/2022
#     Creation For SABP Service Desk Staff

# import required module
import random

# Pick random number from file
numA = random.randint(1, 9)
numB = random.randint(1, 9)
numC = random.randint(1, 9)

# Pick random word from file
wordA = random.choice(open("wordA.txt", "r").readlines())
wordB = random.choice(open("wordB.txt", "r").readlines())
wordC = random.choice(open("wordC.txt", "r").readlines())


#   prints password
print(wordA, + numA, "-", wordB, + numB, "-", wordC, + numC, sep='')
