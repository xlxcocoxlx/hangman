
#TODO: hangan
#TODO: Turtle for hangman, draw the hangman
#TODO: List for words in categories
#TODO: prompts for hte words
#TODO:  check if hte letter submitted is in the word
#TODO: option to make a guess of the word
#TODO: Menu to choose the category
#TODO: draw the body parts for the hangman on hte turtle
from turtle import *
from time import sleep
import random
word = ["test", "apple", "orange", "green"]
wordSelected = random.choice(word)
print (wordSelected)
letterSubmitted = None
limbs = 0


def newGame():
    width(5)
    Screen()
    penup()
    backward(100)
    pendown()
    backward(50)
    forward(25)
    left(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(20)
    game()

def drawLimbs():
    global limbs
    if limbs == 0:
        #Head
        right(90)
        circle(17)
    elif limbs == 1:
        #Body
        left(90)
        penup()
        forward(34)
        pendown()
        forward(100)
    elif limbs == 2:
        #right leg
        left(45)
        forward(25)
        backward(25)
    elif limbs == 3:
        #Left leg
        right(90)
        forward(25)
        backward(25)
        right(135)
    elif limbs == 4:
        #left arm
        forward(80)
        left(90)
        forward(25)
    elif limbs == 5:
        #right arm
        backward(80)
        gameOver()
    limbs = limbs + 1
    tries = str(6 - limbs)
    if limbs == 5:
        print("you have "+ tries +" try left")
    else:
        print("you have "+ tries +" tries left")  
    game()

def gameOver():
    #make turtle draw gameover
    print("Gameover")
    sleep(2)
    quit()

def writeWord():
    wordSize = len(wordSelected)
    print(wordSize)

def game():
    writeWord()
    print("guess the letter of the word")
    letterSubmitted = input()
    if letterSubmitted in wordSelected:
        game()
    else:
        drawLimbs()  
    

newGame()
