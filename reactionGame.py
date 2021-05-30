import tkinter as tk 
from tkinter import Button, Label, messagebox, font
from PIL import Image, ImageTk
import random
import time
import main

class reactionT:

    def ExitToMenu(self):
        global keepPlaying
        self.keepPlaying= False
        self.root.destroy()
        self.app = main.MainMenu()
        self.app.openMenu()

    def onClick(self):
        global start, keepPlaying, numOfClicks
        try: 
            self.reactionButton.forget()
        except:
            pass
        self.xCord="%.2f" %random.random() 
        if float(self.xCord)>0.6:
            self.xCord=0.6
        
        self.yCord="%.2f" %random.random()
        if float(self.yCord)>0.6:
            self.yCord=0.6
        self.reactionButton.place(relx=self.xCord,rely=self.yCord)

        """
        if time.time()- start >=5:
            box= messagebox.askquestion("Timer Ran Out","You Clicked The Circle "+str(numOfClicks)+" Times\nWould You Like To Play Again?",icon="question")
            if box!="yes":
                keepPlaying=False
            root.destroy()
        """
        self.numOfClicks+=1

    def gameOver(self):
        global keepPlaying
        self.box= messagebox.askquestion("Game Over","Would You Like To Play Again?",icon="question")
        if (self.box !='yes'):
            self.ExitToMenu()
        else: 
            self.root.destroy()

    def onClose(self):
        global keepPlaying
        self.keepPlaying=False
        self.root.destroy()
        self.app = main.MainMenu()
        self.app.openMenu() 

    def onHover(self, reactionButton):
        global buttonImage
        self.buttonImage= "images/greenCircle.png"
        self.root.buttonImage=ImageTk.PhotoImage(Image.open(self.buttonImage))
        reactionButton.configure(image=self.root.buttonImage)

    def onLeave(self, reactionButton):
        global buttonImage
        self.buttonImage= "images/whiteCircle.png"
        self.root.buttonImage=ImageTk.PhotoImage(Image.open(self.buttonImage))
        reactionButton.configure(image=self.root.buttonImage)

    def checkfortime(self, start):
        global timerText, keepPlaying, totalTime
        self.timerText.set(str(self.totalTime - int( time.time()- start) ) ) 
        if time.time()- start >=self.totalTime:
            self.box= messagebox.askquestion("Timer Ran Out","You Clicked The Circle "+str(self.numOfClicks)+" Times\nWould You Like To Play Again?",icon="question")
            if self.box!="yes":
                self.ExitToMenu()
            else: 
                self.root.destroy()

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
    def mainrg(self):
        self.keepPlaying= True ; self.firstTime=True
        self.bgColor="#D2FFBF" 
        self.totalTime=10
        while self.keepPlaying == True:
            self.numOfClicks= 0 
            

            self.root= tk.Tk()
            self.root.title("Reaction game")
            self.root.iconbitmap("images/reaction game.ico")
            self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            self.root.geometry("%dx%d" % (self.w/2, self.h/2))
            self.center(self.root)
            #root.attributes('-fullscreen', True)
            #root.geometry("500x500+400+100")
            self.root.protocol('WM_DELETE_WINDOW', self.onClose)
            
            self.background= Button(self.root,bg=self.bgColor,activebackground=self.bgColor,bd=0, command= self.gameOver).place(x=0,y=0,relheight=1,relwidth=1)

            if self.firstTime== True :
                self.box=messagebox.showinfo("Reaction Game","This game is all about reaction time\nClick on the circle when it appears on your screen\nIf you click on gray space you'll lose the game.\nYou have "+str(self.totalTime)+" seconds.",icon="info") 
                self.firstTime= False

            self.start = time.time()

            self.myFont= font.Font(family="reem kufi", size=40, weight="bold")#source sans pro

            self.timerText= tk.StringVar()
            self.timerText.set(str(self.totalTime - int( time.time()- self.start) ) )    
            self.timerLabel = Label(self.root,textvariable=self.timerText, padx=10,pady=0, bg= self.bgColor, fg="#fff")
            self.timerLabel.place(relx=0.5,rely=0)
            self.timerLabel["font"]=self.myFont
            
            self.buttonImage="images/whiteCircle.png"
            self.root.buttonImage=ImageTk.PhotoImage(Image.open(self.buttonImage))
            self.reactionButton= Button(self.root,bd=0,bg=self.bgColor ,width=256 , height=256,padx=0, pady=0, activebackground=self.bgColor, image= self.root.buttonImage ,cursor="trek", command= self.onClick)
            self.reactionButton.place(relx=0.5,rely=0.5)#,relwidth=0.1,relheight=0.1)

            self.reactionButton.bind("<Enter>", lambda e: self.onHover(self.reactionButton))
            self.reactionButton.bind("<Leave>", lambda e: self.onLeave(self.reactionButton))

            self.root.bind("<Motion>", lambda e: self.checkfortime(self.start))

            self.root.mainloop()
"""Coded By 
                 █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
                ██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
                ███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
                ██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
                ██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
"""