# Ke'niah Williams
# December 2nd, 2022
# Creates a GUI game of Rock Paper Scissors asks for users input and generates a computer number


from tkinter import *
root = Tk()
from random import randint
computer_choice = randint(0,2)

# importing necessary functions into code

def game():
    Uchoice = int(menuEntry.get())
    #getting input from GUI entry to use in funtion
    Cchoice = computer_choice
    #making a separate variable that assigns the number in the game to text e.g. 0 is rock
    if Cchoice == 0:
        Cchoice = "Rock"
    elif Cchoice == 1:
        Cchoice = "Paper"
    else:
        Cchoice = "Scissors"
    
    Utext = Uchoice
    if Utext == 0:
        Utext = "Rock"
    elif Utext == 1:
        Utext = "Paper"
    else:
        Utext = "Scissors"
   #rock paper scissors game 
    if (computer_choice == 0 and Uchoice == 2) or (computer_choice == 1 and Uchoice == 0) or (computer_choice == 2 and Uchoice == 1):
        winnerText["text"] =f"Computer wins they chose {Cchoice}"
    elif computer_choice == Uchoice:
        winnerText["text"]= "Tie"
    else:
        winnerText["text"] =f"User wins they chose {Utext}"
    #inserting user choice and computer choice onto GUI
    comchoiceLabel["text"] =f"{Cchoice}"
    choiceLabel["text"] =f"{Utext}"
    
    #deleting user input so new value can be entered
    menuEntry.delete(0, END)
    

#Below I set up the GUI based on text and placement
root.title("Rock, Paper, Scissors Game")

menuLabel = Label(root, text = "Enter 0(Rock), 1(Paper), 2(Scissors)")
menuLabel.grid(row = 0, column = 0)

menuEntry = Entry(root, width = 10)
menuEntry.grid(row = 0, column = 1)

button = Button(root, text = "PLAY", width = 15, height = 1, command = game)
button.grid(row = 1, column = 0)

userLabel = Label(root, text = "User played")
userLabel.grid(row = 2, column = 0)

choiceLabel = Label(root, text = "-")
choiceLabel.grid(row = 2, column = 1)

computerLabel = Label(root, text = "Computer played")
computerLabel.grid(row = 3, column = 0)

comchoiceLabel = Label(root, text = "-")
comchoiceLabel.grid(row = 3, column = 1)

winnerLabel = Label(root, text = "Winner")
winnerLabel.grid(row = 4, column = 0)

winnerText = Label(root, text = "-")
winnerText.grid(row = 4, column = 1)
