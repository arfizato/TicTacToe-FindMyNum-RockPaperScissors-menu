import circularLoophole
import RockPaperScissors
import FindMyNum
import TicTacToe

from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import Menu

class MainMenu:
    def playttt(self):
        self.menu.destroy()
        self.appThree= TicTacToe.tripleT()
        self.appThree.startPlaying()   


    def playrps(self):
        self.menu.destroy()
        self.appTwo=RockPaperScissors.RockPS()
        self.appTwo.playTheGame()

    def playfmn(self):
        self.menu.destroy()
        self.app=FindMyNum.findX()
        self.app.startGame() 

    """
        ███    ███  █████  ██ ███    ██     ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
        ████  ████ ██   ██ ██ ████   ██     ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
        ██ ████ ██ ███████ ██ ██ ██  ██     █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
        ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
        ██      ██ ██   ██ ██ ██   ████     ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████                                                                                                       

    """
    def openMenu(self):
        self.menu=tk.Tk()
        self.menu.title("Main Menu")
        self.menu.iconbitmap("images/menuDavid.ico")
        self.menu.configure(bg="#a07ab1")

        self.labelFont= font.Font(family="Times",size=40,weight="bold",slant="italic")
        self.myFont=font.Font(family="Times",size=20,weight="bold",slant="italic")
        self.buttonColor="#a07ab1"
        self.textColor="#411a52"

        self.welcome = Label(self.menu, text='Marhbé Sahbi\nAkhtar Game', font=self.labelFont,padx=40,pady=20,bg=self.buttonColor,fg="#fff")
        self.welcome.grid(row=1,column=1,pady=4)

        self.tttImage=PhotoImage(file="images/TicTacToe.png")
        self.tttImage=self.tttImage.subsample(6,6)
        self.ttt= Button(self.menu,command= lambda :self.playttt(), text="Click to Play 'TicTacToe'",font=self.myFont,image=self.tttImage,width=420,height=150,compound="top",bd=0,bg="#8feff9",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=2,column=1,pady=2)

        self.rpsImage=PhotoImage(file="images/RockPaperScissors.png")
        self.rpsImage=self.rpsImage.subsample(6,6)
        self.rps= Button(self.menu,command= lambda :self.playrps(), text="Click to Play 'Rock Paper Scissors'",font=self.myFont,image=self.rpsImage,width=420,height=150,compound="top",bd=0,bg="#f9ed80",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=1,pady=2)

        self.fmnImage=PhotoImage(file="images/FindMyNum.png")
        self.fmnImage=self.fmnImage.subsample(6,6)
        self.fmn=Button(self.menu,command= lambda :self.playfmn(), text="Click to Play 'Find My Number'",font=self.myFont,image=self.fmnImage,width=420,height=150,compound="top",bd=0,bg="#f39faf",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=4,column=1,pady=2)

        self.menu.mainloop() 

