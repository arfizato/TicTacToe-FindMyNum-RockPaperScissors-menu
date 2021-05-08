from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from random import * 
import random as rand
from PIL import Image, ImageTk

class RockPS:
    def choicemade(self,choicePlayer):
        global comScore, playScore, scoreText, imageList, computerImage, playerImage,bestOfNum, keepPlaying
        self.choiceComputer= rand.randint(0,2)

        self.computerImage=self.imageList[self.choiceComputer]
        self.root.computerImage=ImageTk.PhotoImage(Image.open(self.computerImage))
        self.computer.configure(image=self.root.computerImage)

        self.playerImage=self.imageList[choicePlayer]
        self.root.playerImage=ImageTk.PhotoImage(Image.open(self.playerImage))
        self.player.configure(image=self.root.playerImage)
        

        if (choicePlayer == self.choiceComputer-1 or  (self.choiceComputer==0 and choicePlayer==2)):
            self.comScore+=1
        elif (choicePlayer-1 == self.choiceComputer or  (self.choiceComputer==2 and choicePlayer==0)):
            self.playScore+=1
        self.scoreText.set(str(self.comScore)+" - "+str(self.playScore))
        if self.comScore== self.bestOfNum :
            #print("computer won "+str(self.comScore)+" - "+str(self.playScore))
            self.box= messagebox.askquestion("Computer Won!","\t      "+str(self.comScore)+" - "+str(self.playScore)+"\nWould you like to keep playing?",icon="question")
            if self.box!="yes":         
                self.keepPlaying=FALSE  
            self.root.destroy()         
            
        elif self.playScore== self.bestOfNum:        
            #print("player Won "+str(self.comScore)+" - "+str(self.playScore))
            self.box= messagebox.askquestion("Player Won!","\t      "+str(self.comScore)+" - "+str(self.playScore)+"\nWould you like to keep playing?",icon="question")
            if self.box!="yes":      
                self.keepPlaying=FALSE
            self.root.destroy()
            
    
    def startgame(self):

        self.startButton.destroy()
        self.bestOfButton.destroy()
        self.rpsButton.destroy()
        self.sprButton.destroy()
        
            

        global computerImage, playerImage, rockImage, paperImage, scissorsImage, scoreText
        
        #computer= Button(self.root,bd=0,height=120,width=110,bg="#c1c1c1",image=computerImage,compound= BOTTOM,text="The Computer \nPicked: ")
        self.computer.grid(row=1, column=0)
        self.computer["state"]=DISABLED
        self.computer["font"]= self.gameFont

        
        self.scoreText.set("Click a Button\nto \nStart Playing")
        self.scoreImage= PhotoImage(file= r'images/empty.png')
        self.score= Button(self.root, bd=0, height=120, width=110,disabledforeground ="#c1c1c1", bg="#426973",textvariable=self.scoreText,image=self.scoreImage, compound= BOTTOM )
        self.score.grid(row=1,column=1)
        self.score["state"]=DISABLED
        self.score["font"]= self.gameFont
        
        
        self.player.grid(row=1, column=2)
        self.player["state"]=DISABLED
        self.player["font"]= self.gameFont

        #rockImage= rockImage.subsample(8,8)
        self.rock = Button(self.root,bd=0,height=80,width=112, bg="#426973", activebackground ="#ECEAEF",image=self.root.rockImage,command=lambda : self.choicemade(0))
        self.rock.grid(padx=2,pady=3,row=2,column=0)

        
        self.paper = Button(self.root,bd=0,height=80,width=112, bg="#426973", activebackground ="#ECEAEF",image=self.root.paperImage,command=lambda : self.choicemade(1))
        self.paper.grid(padx=2,pady=3,row=2,column=1)

        
        self.scissors= Button(self.root,bd=0,height=80,width=112, bg="#426973", activebackground ="#ECEAEF",image=self.root.scissorsImage,command=lambda : self.choicemade(2))
        self.scissors.grid(padx=2,pady=3,row=2,column=2)
        

    def bestOfWhat(self):
        global bestOfNum
        self.bestOfNum= self.bestOfNum+2 if self.bestOfNum < 7 else 1
        self.bestOfText.set("Best Of "+str(self.bestOfNum))

    def OnClose(self):
        global keepPlaying
        self.keepPlaying=FALSE 
        self.root.destroy()

    """-------------------------------main-------------------------------"""
    def playTheGame(self):
        self.imageList=['images/rock.png','images/paper.png','images/scissors.png','images/empty.png']
        self.keepPlaying= TRUE

        while self.keepPlaying==TRUE : 
            self.root = tk.Tk()
            self.root.title("Rock Paper Scissors")
            self.root.iconbitmap(r'images/scissors.ico')
            self.root.configure(bg="#fff")
            self.bestOfNum=3
            self.playScore=0
            self.comScore=0
            
            self.root.protocol('WM_DELETE_WINDOW', self.OnClose)



            #declaring the image variables (tip: they cannot be declared in a function)
            try:
                self.computerImage=self.imageList[3]
                self.root.computerImage=ImageTk.PhotoImage(Image.open(self.computerImage))

                self.playerImage=self.imageList[3]
                self.root.playerImage=ImageTk.PhotoImage(Image.open(self.playerImage))

                self.rpsImage = "images/rps.png"
                self.root.rpsImage=ImageTk.PhotoImage(Image.open(self.rpsImage))
                self.sprImage = "images/spr.png"
                self.root.sprImage=ImageTk.PhotoImage(Image.open(self.sprImage))

                self.rockImage=self.imageList[0]
                self.paperImage=self.imageList[1]
                self.scissorsImage=self.imageList[2]
                self.root.rockImage=ImageTk.PhotoImage(Image.open(self.rockImage))
                self.root.paperImage=ImageTk.PhotoImage(Image.open(self.paperImage))
                self.root.scissorsImage=ImageTk.PhotoImage(Image.open(self.scissorsImage)) 
            except:
                print("rouh")

            self.scoreText= tk.StringVar()

            #declaring buttons 
            self.computer= Button(self.root,bd=0,height=120,width=110,disabledforeground ="#c1c1c1",bg="#426973",image=self.root.computerImage,compound= BOTTOM,text="The Computer \nPicked: ")
            self.player= Button(self.root,bd=0,height=120,width=110, disabledforeground ="#c1c1c1", bg="#426973",image=self.root.playerImage,compound= BOTTOM,text="The Player \nPicked: ")

            #declaring the fonts 
            self.textFont =font.Font(family="Times",size=20,weight="bold",slant="italic")
            self.gameFont =font.Font(family="Times",weight="bold",slant="italic")

            self.bestOfText= tk.StringVar()
            self.bestOfText.set("Best Of 3\n Click To Change")
            self.bestOfButton= Button(self.root,activebackground ="#6097A5", activeforeground ="#c1c1c1", textvariable= self.bestOfText,height=5,width=20,bd=0,fg="#c1c1c1",bg="#426973",command= self.bestOfWhat)
            self.bestOfButton.grid(row=1,column=0)
            self.bestOfButton["font"]=self.textFont

            self.startButton= Button(self.root,activebackground ="#6097A5", activeforeground ="#c1c1c1", text="Click To Start",height=5,width=20,bd=0,fg="#c1c1c1",bg="#426973",command= self.startgame)
            self.startButton.grid(row=2,column=1)
            self.startButton["font"]=self.textFont
            
            self.rpsButton= Button(self.root,image=self.root.sprImage,text=" ",height=150,width=120,bd=0,fg="#c1c1c1",bg="#fff",disabledforeground="#fff")
            self.rpsButton.grid(row=1,column=1)
            self.rpsButton["font"]=self.textFont
            self.rpsButton["state"]=DISABLED

            self.sprButton= Button(self.root,image=self.root.rpsImage,text=" ",height=150,width=120,bd=0,fg="#c1c1c1",bg="#fff",disabledforeground="#fff")
            self.sprButton.grid(row=2,column=0)
            self.sprButton["font"]=self.textFont
            self.sprButton["state"]=DISABLED

            self.root.mainloop()

#appTwo=RockPS()
#appTwo.playTheGame()