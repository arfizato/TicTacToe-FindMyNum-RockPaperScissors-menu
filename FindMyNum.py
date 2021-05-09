from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from random import * 
import random as rand
import main

class findX:

    def ExitToMenu(self):
        global keepPlaying
        self.keepPlaying= FALSE
        self.root.destroy()
        self.app = main.MainMenu()
        self.app.openMenu()

    def outOfRange(self):
        global keepPlaying
        self.box = messagebox.askquestion("Error! Out Of Range!","Do You Want To Play Again ?",icon="warning")
        if self.box!="yes":
            self.ExitToMenu()
        else: 
            self.root.destroy()

    def goHigher(self):
        global guess, Min, Max
        self.Min=self.guess+1
        try :
            self.guess=rand.randint(self.Min,self.Max)
        except:
            self.outOfRange()
        self.compTxt.set(str(self.guess))

    def goLower(self):
        global guess, Min, Max
        self.Max=self.guess-1
        try :
            self.guess=rand.randint(self.Min,self.Max)
        except:
            self.outOfRange()
        self.compTxt.set(str(self.guess))

    def justRight(self):
        global keepPlaying, guess
        self.box = messagebox.askquestion("Your Number Is "+str(self.guess),"Do You Want To Play Again ?",icon="question")
        if self.box!="yes":
            self.ExitToMenu()
        else: 
            self.root.destroy()
        

    def ClickedOnce(self,guess):
        self.compTxt.set(str(self.guess))
        self.tooLow["state"]=NORMAL
        self.tooHigh["state"]=NORMAL
        self.right["state"]=NORMAL
        self.computer["state"]=DISABLED

    def OnClose(self):
        global keepPlaying
        self.keepPlaying=FALSE 
        self.root.destroy() 
        self.app = main.MainMenu()
        self.app.openMenu()
    
   
    """
    ███    ███  █████  ██ ███    ██     ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ 
    ████  ████ ██   ██ ██ ████   ██     ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ 
    ██ ████ ██ ███████ ██ ██ ██  ██     █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ 
    ██  ██  ██ ██   ██ ██ ██  ██ ██     ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ 
    ██      ██ ██   ██ ██ ██   ████     ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████                                                                                                       

    """
    def startGame(self):
        self.keepPlaying= TRUE
        while self.keepPlaying== TRUE:    
            self.root= tk.Tk()
            self.root.title("flippity flip")
            self.root.iconbitmap('images/FindMyNumDavid.ico')
            self.root.configure(bg="#FAF9FC")
            self.root.protocol('WM_DELETE_WINDOW', self.OnClose)

            self.CompGenFont= font.Font(family="Times",size=20,weight="bold",slant="italic")
            self.TextFont= font.Font(family="Times",weight="bold")

            global guess, Min, Max 
            self.Min=0
            self.Max=1000
            self.guess=rand.randint(self.Min,self.Max)

            #defining the buttons
            self.compTxt = tk.StringVar()
            self.computer= Button(self.root, bd=0, textvariable=self.compTxt, width=28, height=5, fg="#978DC1", disabledforeground="#978DC1", activeforeground ='#978DC1', bg="#DCD3FE", activebackground="#ECD3FD", command= lambda : self.ClickedOnce(self.guess)  )
            self.computer.grid(pady=2, row=1,column=0,columnspan=3)
            #computer["state"]=DISABLED
            self.computer["relief"]="sunken"
            self.compTxt.set("Choose a number in 0-1000 \nClick Me To Generate \nThe First Number")
            self.computer["font"]=self.CompGenFont

            self.tooLow= Button(self.root,bd=0,width=15,height=5,text="Too Low!",disabledforeground="#387DC1",activeforeground="#387DC1", fg="#387DC1",bg="#DCD3FE",activebackground="#AEE8FE",command= self.goHigher)
            self.tooLow.grid(padx=2,pady=2,row=2,column=0)
            self.tooLow["font"]=self.TextFont
            self.tooLow["state"]=DISABLED

            self.right= Button(self.root,bd=0,width=18,height=5,text="Correct!",disabledforeground="#5FB58E",activeforeground="#5FB58E",  fg="#5FB58E",bg="#DCD3FE",activebackground="#D9FED3",command= self.justRight)
            self.right.grid(padx=2,pady=2,row=2,column=1)
            self.right["font"]=self.TextFont
            self.right["state"]=DISABLED

            self.tooHigh= Button(self.root,bd=0,width=15,height=5,text="Too High!",disabledforeground="#B55A5A",activeforeground="#B55A5A", fg="#B55A5A",bg="#DCD3FE",activebackground="#FEC9DD",command= self.goLower)
            self.tooHigh.grid(padx=2,pady=2,row=2,column=2)
            self.tooHigh["font"]=self.TextFont
            self.tooHigh["state"]=DISABLED
            
            """-------------------MENU-----------------"""
            # create a menubar
            self.menubar = Menu(self.root)
            self.root.config(menu=self.menubar)

            # create a menu
            self.file_menu = Menu(self.menubar)

            # add a menu item to the menu
            self.file_menu.add_command(label='Exit To Main Menu', command=self.ExitToMenu)

            # add the File menu to the menubar
            self.menubar.add_cascade(label="Options", menu=self.file_menu)

            self.root.mainloop()
"""Coded By 
                 █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
                ███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
                ██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
                ██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""