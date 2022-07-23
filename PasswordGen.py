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

# GUI module
from tkinter import *
window = Tk()

# add widgets here
lbl = Label(window, text="Test", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
btn = Button(window, text="Generate Password", fg='blue')
btn.place(x=80, y=100)
window.title('Password Generator')
window.geometry("300x200+10+20")
window.mainloop()


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
