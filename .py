from tkinter import *
import random
import tkinter
user = int
computer = int
win = 0
lose = 0
def rps(win, lose, user):
    computer = random.randrange(1,4)
    if user == computer:
        var.set("It's a draw. \n No Points")  
    elif user == 1 and computer == 3:
        var.set("You chose Rock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
            
    elif user == 1 and computer == 2:
        var.set("You chose Rock, I chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 2 and computer == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        wins.set(wins.get() - 1)    
    elif user == 2 and computer == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)   
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 3:
        var.set("You chose Spock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 1:
        var.set("You chose Spock, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set("You chose Spock, I chose Lizard. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 4 and computer == 2:
        var.set("You chose Spock, I chose Paper. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 1:
        var.set("You chose Lizard, I chose Rock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 2:
        var.set("You chose Lizard, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 5 and computer == 3:
        var.set("You chose Lizard, I chose Scissors. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 4:
        var.set("You chose Rock, I chose Spock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 2 and computer == 4:
        var.set("You chose Paper, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 3 and computer == 4:
        var.set("You chose Scissors, I chose Spock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 5:
        var.set("You chose Rock, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 2 and computer == 5:
        var.set("You chose Paper, I chose Lizard. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 3 and computer == 5:
        var.set("You chose Scissors, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set("You chose Spock, I chose Lizard. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)  
    else:
        var.set("Thanks for playing. \nYou have " + str(win) + " wins and " + str(lose) + " losses.")


    
top = tkinter.Tk()
top.wm_title("RPS Python GUI")
top.minsize(width=350, height=150)
top.maxsize(width=350, height=150)
B1 = tkinter.Button(top, text ="Rock", command = lambda: rps(win, lose, 1))
B1.grid(row=0, column=1)
B2 = tkinter.Button(top, text ="Paper", command = lambda: rps(win, lose, 2))
B2.grid(row=0, column=2)
B3 = tkinter.Button(top, text ="Scissors", command = lambda: rps(win, lose, 3))
B3.grid(row=0, column=3)
space = tkinter.Label(top, text="")
space.grid(row=1)
var = StringVar()
var.set('Welcome!')
l = Label(top, textvariable = var)
l.grid(row=2, column=2)
wins = IntVar()
wins.set(win)
w = Label(top, textvariable = wins)
w.grid(row=4, column=2)
labeled = Label(top, text = "Score:")
labeled.grid(row=3, column=2)
copy = Label(top, text= "RPS GUI on Tkinter on Python. By Praveen 2016")
copy.grid(row=5, column=2)
top.mainloop(
