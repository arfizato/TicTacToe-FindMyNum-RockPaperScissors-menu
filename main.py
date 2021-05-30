import circularLoophole
import RockPaperScissors
import FindMyNum
import TicTacToe
import flipTheTwins
import reactionGame

from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import Menu

class MainMenu:
    def playttt(self): 
        #print("ttt")
        self.menu.destroy()
        self.appThree= TicTacToe.tripleT()
        self.appThree.startPlaying()   

    def playrps(self): 
        #print("rps")
        self.menu.destroy()
        self.appTwo=RockPaperScissors.RockPS()
        self.appTwo.playTheGame()
    """
    def playfmn(self): 
        #print("fmn")
        self.menu.destroy()
        self.appOne=FindMyNum.findX()
        self.appOne.startGame() """

    def playftt(self): 
        #print("fmn")
        self.menu.destroy()
        self.appOne=flipTheTwins.FlipTheT()
        self.appOne.mainftt() 

    def playrg(self): 
        #print("fmn")
        self.menu.destroy()
        self.app=reactionGame.reactionT()
        self.app.mainrg()

    def center(self, win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        self.width = win.winfo_width()
        self.frm_width = win.winfo_rootx() - win.winfo_x()
        self.win_width = self.width + 2 * self.frm_width
        self.height = win.winfo_height()
        self.titlebar_height = win.winfo_rooty() - win.winfo_y()
        self.win_height = self.height + self.titlebar_height + self.frm_width
        self.x = win.winfo_screenwidth() // 2 - self.win_width // 2
        self.y = win.winfo_screenheight() // 2 - self.win_height // 2
        win.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x,self. y))
        win.deiconify()

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
        self.menu.configure(bg="#272727")
        self.menu.resizable(False, False) 
        self.menu.geometry("857x490")
        self.center(self.menu)

        self.labelFont= font.Font(family="Times",size=40,weight="bold",slant="italic")
        self.myFont=font.Font(family="Times",size=20,weight="bold",slant="italic")
        self.buttonColor="#353535" #"#a07ab1"
        self.textColor="#BAF9FF" #"#411a52"

        self.welcome = Label(self.menu, text='Welcome\nPick A Game', font=self.labelFont,padx=40,pady=20,bg="#272727",fg=self.textColor)
        self.welcome.grid(row=1,column=1,pady=4, columnspan=2)

        self.tttImage=PhotoImage(file="images/TicTacToe.png")
        self.tttImage=self.tttImage.subsample(6,6)
        self.ttt= Button(self.menu,command= lambda :self.playttt(), text="TicTacToe",font=self.myFont,image=self.tttImage,width=420,height=150,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=2,column=1,pady=2, padx=2)#" #8feff9"

        #self.tttt= Button(self.menu,command= lambda :self.playttt(), text="TicTacToe",font=self.myFont,image=self.tttImage,width=416,height=146,compound="top",bd=0,bg="#fff",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=2,column=1,pady=2)

        #self.ttt= Button(self.menu,command= lambda :self.playttt(), text="TicTacToe",font=self.myFont,image=self.tttImage,width=412,height=142,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=2,column=1,pady=2)

        self.rpsImage=PhotoImage(file="images/RockPaperScissors.png")
        self.rpsImage=self.rpsImage.subsample(6,6)
        self.rps= Button(self.menu,command= lambda :self.playrps(), text="Rock Paper Scissors",font=self.myFont,image=self.rpsImage,width=420,height=150,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=1,pady=2, padx=2)#"#f9ed80 " 

        #self.rps= Button(self.menu,command= lambda :self.playrps(), text="Rock Paper Scissors",font=self.myFont,image=self.rpsImage,width=416,height=146,compound="top",bd=0,bg="#fff",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=1,pady=2)

        #self.rps= Button(self.menu,command= lambda :self.playrps(), text="Rock Paper Scissors",font=self.myFont,image=self.rpsImage,width=412,height=142,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=1,pady=2)


        self.fttImage=PhotoImage(file="images/flip the twins.png")
        self.fttImage=self.fttImage.subsample(6,6)
        self.ftt= Button(self.menu,command= lambda :self.playftt(), text="Flip the Twins",font=self.myFont,image=self.fttImage,width=420,height=150,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=2,column=2,pady=2,padx=2)#"#f9ed80 " 


        self.rgImage=PhotoImage(file="images/reaction game.png")
        self.rgImage=self.rgImage.subsample(6,6)
        self.rg= Button(self.menu,command= lambda :self.playrg(), text="Reaction Game",font=self.myFont,image=self.rgImage,width=420,height=150,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=2,pady=2,padx=2)#"#f9ed80 " 

        #self.rps= Button(self.menu,command= lambda :self.playrps(), text="Rock Paper Scissors",font=self.myFont,image=self.rpsImage,width=416,height=146,compound="top",bd=0,bg="#fff",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=1,pady=2)

        #self.rps= Button(self.menu,command= lambda :self.playrps(), text="Rock Paper Scissors",font=self.myFont,image=self.rpsImage,width=412,height=142,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=3,column=1,pady=2)

        """ #find My Num 
        self.fmnImage=PhotoImage(file="images/FindMyNum.png")
        self.fmnImage=self.fmnImage.subsample(6,6)
        self.fmn=Button(self.menu,command= lambda :self.playfmn(), text="Find My Number",font=self.myFont,image=self.fmnImage,width=420,height=150,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=4,column=1,pady=2)#"#f39faf"

        #self.fmn=Button(self.menu,command= lambda :self.playfmn(), text="Find My Number",font=self.myFont,image=self.fmnImage,width=416,height=146,compound="top",bd=0,bg="#fff",fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=4,column=1,pady=2)

        self.fmn=Button(self.menu,command= lambda :self.playfmn(), text="Find My Number",font=self.myFont,image=self.fmnImage,width=412,height=142,compound="top",bd=0,bg=self.buttonColor,fg=self.textColor,activebackground=self.buttonColor,activeforeground=self.textColor).grid(row=4,column=1,pady=2)
        """
        self.menu.mainloop() 
"""Coded By 
                 █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
                ███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
                ██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
                ██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""

