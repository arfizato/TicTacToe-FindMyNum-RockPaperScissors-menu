from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
#from main import MainMenu
import main
""" GREAT COLOR PALETTES :https://imgur.com/Jmk6LEH """
class tripleT:
    def insertWinButtons(self,xo,l,c,nextl,nextc,prevl,prevc):
        self.winButtonOne= Button(self.root,bd=0,text=xo,width=12,height=5,fg="#323831",bg="#a6e22e")
        self.winButtonOne.grid(row=l+1,column=c)
        self.winButtonOne["font"]= self.myFont
            
        self.winButtonTwo= Button(self.root,bd=0,text=xo,width=12,height=5,fg="#323831",bg="#a6e22e")
        self.winButtonTwo.grid(row=nextl+1,column=nextc)
        self.winButtonTwo["font"]= self.myFont
            
        self.winButtonThree= Button(self.root,bd=0,text=xo,width=12,height=5,fg="#323831",bg="#a6e22e")
        self.winButtonThree.grid(row=prevl+1,column=prevc)
        self.winButtonThree["font"]= self.myFont
    # checking if one of the players won 
    def checkForWin(self,mat,l,c,xo):
        
        prevl=l-1 if l>0 else 2
        prevc=c-1 if c>0 else 2
        nextl=l+1 if l<2 else 0
        nextc=c+1 if c<2 else 0    
        
        # checking main diagonal
        if (l==c):
            if (self.mat[prevl][prevc]+self.mat[nextl][nextc]+self.mat[l][c]==xo*3):
                self.insertWinButtons(xo,l,c,nextl,nextc,prevl,prevc)
                return TRUE
        # checking the opposite diagonal 
        elif (l+c==2): 
            if (self.mat[prevl][nextc]+self.mat[nextl][prevc]+self.mat[l][c]==xo*3):
                self.insertWinButtons(xo,l,c,prevl,nextc,nextl,prevc)
                return TRUE   
        #checking lines and columns 
        if(self.mat[prevl][c]+self.mat[nextl][c]+self.mat[l][c]==xo*3 ):
            self.insertWinButtons(xo,l,c,nextl,c,prevl,c)
            return TRUE
        elif self.mat[l][prevc]+self.mat[l][nextc]+self.mat[l][c]==xo*3:
            self.insertWinButtons(xo,l,c,l,nextc,l,prevc)
            return TRUE
        else: 
            return FALSE
            
    # Defining the functions for the buttons 
    def buttonClicked(self,text,button,l,c):
        global x, numOfButtonsDisabled, stopPlaying, firstChar, secondChar, playerOneWins, playerTwoWins
        self.x+=1
        self.atLeastOnePlayerWon=FALSE

        self.choiceButton["state"]= DISABLED
        self.choiceButton["bg"]="#404040"
        self.choiceButton["fg"]="#000000"

        button["state"]= DISABLED
        if (self.x%2==0):   
            #only changes color if the player chooses the "only color" option before he starts playing
            if (self.firstChar==""):     
                button["bg"]="#feecaa"
                #button["relief"]= "sunken"        

            text.set(self.firstChar)
            self.mat[l-1][c]=self.firstChar 
            if self.checkForWin(self.mat,l-1,c,self.firstChar):
                self.playerTwoWins+=1
                self.atLeastOnePlayerWon= TRUE
                self.box = messagebox.askquestion("Player 2 Won", "\tSCORE:  "+str(self.playerOneWins)+" - "+str(self.playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
                if (self.box !='yes'):
                    self.stopPlaying=TRUE         
                self.root.destroy()      
        else:
            #only changes color if the player chooses the "only color" option before he starts playing
            if (self.firstChar ==""):
                #Color Combinations pink and pastel(bb8082,f6dfeb)  white and gray(ffffff,353535) brown and gray(897853,353535) pastel purple and pink(f6dfeb,dbd0ff) red and black(630000,1b1717)
                button["bg"]="#decc8c"
                #button["relief"]= "sunken"

            text.set(self.secondChar)
            self.mat[l-1][c]=self.secondChar
            if self.checkForWin(self.mat,l-1,c,self.secondChar):
                self.playerOneWins+=1
                self.atLeastOnePlayerWon= TRUE
                self.box=messagebox.askquestion("Player 1 Won","\tSCORE:  "+str(self.playerOneWins)+" - "+str(self.playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
                if (self.box!='yes'):
                    self.stopPlaying=TRUE          
                self.root.destroy()  

        #in case of self.numOfButtonsDisabled==9 then we know it's a draw unless someone won with the last button click 
        self.numOfButtonsDisabled+=1
        if self.numOfButtonsDisabled==9 and self.atLeastOnePlayerWon == FALSE:
            self.box=messagebox.askquestion("It's a TIE ", "\tSCORE:  "+str(self.playerOneWins)+" - "+str(self.playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
            if (self.box!='yes'):
                self.stopPlaying=TRUE
            self.root.destroy()

    #picking what to fill the buttons with
    def changeText(self,text,button):
        global firstChar, secondChar, charList, charNumber
        self.charNumber= self.charNumber+1 if self.charNumber<4 else 0 #self.charNumber is the variables traversing the self.charList[][] 
        self.firstChar=self.charList[self.charNumber][0] 
        self.secondChar=self.charList[self.charNumber][1]
        text.set(self.charList[self.charNumber][2])   

    def onClose(self):
        global stopPlaying
        self.stopPlaying=TRUE
        self.root.destroy()
    
    def ExitToMenu(self):
        global stopPlaying
        self.stopPlaying= TRUE
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
    def startPlaying(self): 
        global stopPlaying, playerOneWins, playerTwoWins
        self.stopPlaying=FALSE #boolean deciding when to stop the while loop: only becomes true if the player clicks no on the popup 
        self.playerTwoWins=0 #tracking how many times player 1 won 
        self.playerOneWins=0#tracking how many times player 2 won
        while (self.stopPlaying==FALSE):
            
            self.charNumber=0#variable selecing the subarrays containing the preferred symbols
            self.charList=[["O","X","X O"],["+","-","- +"],["B","A","A B"],["Y","X","X Y"],[""," ","Only Color"]] # list of preferred symbols ("X O","A B", etc...) the user has to pick from
            self.mat=[["."]*3,["."]*3,["."]*3] # matrix keeping count of who marked where 
            self.numOfButtonsDisabled=0 # tracking if there's a draw or not 
                
            self.root = tk.Tk()
            self.root.title("Tic Tac toe")
            self.root.iconbitmap(r'images/TicTacToeDavid.ico')
            self.root.configure(bg="#c7dabf")
            self.root.protocol('WM_DELETE_WINDOW', self.onClose)
            
            # define font
            self.myFontChoice = font.Font(family='Times',weight="bold",slant="italic")
            self.myFont = font.Font(family='Times',weight="bold")


            global x, firstChar, secondChar
            self.firstChar="O"
            self.secondChar="X"    
            self.x=0 

            """------------------------------------Defining each button and putting it on the grid------------------------------------"""
            #self.choiceButton is the button the user has to click on to pick preferred symbols "X O","A B", etc...
            
            self.text0  = tk.StringVar()
            self.text0.set("Click To Pick Variant")
            self.choiceButton  = Button(self.root,bd=0,textvariable=self.text0,width=38,height=5,fg="#323831",bg="#a3b996", command= lambda: self.changeText(self.text0,self.choiceButton))
            self.choiceButton.grid(padx=1,pady=1,row=0 ,column=0, columnspan=3)
            self.choiceButton["font"]= self.myFontChoice

            #Row of [1,2,3]
            self.text1  = tk.StringVar()
            self.button1  = Button(self.root,bd=0,textvariable=self.text1,text="",width=12,height=5,bg="#bbca95", command= lambda: self.buttonClicked(self.text1,self.button1,3,0) )
            self.button1.grid(padx=2,pady=1,row=3 ,column=0)
            self.button1["font"]= self.myFont

            self.text2  = tk.StringVar()
            self.button2  = Button(self.root,bd=0,textvariable=self.text2,text="",width=12,height=5,bg="#a3b996", command= lambda: self.buttonClicked(self.text2,self.button2,3,1) )
            self.button2.grid(padx=1,pady=1,row=3 ,column=1)
            self.button2["font"]= self.myFont

            self.text3  = tk.StringVar()
            self.button3  = Button(self.root,bd=0,textvariable=self.text3,text="",width=12,height=5,bg="#bbca95", command= lambda: self.buttonClicked(self.text3,self.button3,3,2) )
            self.button3.grid(padx=2,pady=1,row=3 ,column=2)
            self.button3["font"]= self.myFont

            #Row of [4,5,6]
            self.text4  = tk.StringVar()
            self.button4  = Button(self.root,bd=0,textvariable=self.text4,text="",width=12,height=5,bg="#a3b996", command= lambda: self.buttonClicked(self.text4,self.button4,2,0) )
            self.button4.grid(padx=2,pady=1,row=2 ,column=0)
            self.button4["font"]= self.myFont

            self.text5  = tk.StringVar()
            self.button5  = Button(self.root,bd=0,textvariable=self.text5,text="",width=12,height=5,bg="#bbca95", command= lambda: self.buttonClicked(self.text5,self.button5,2,1) )
            self.button5.grid(padx=1,pady=1,row=2 ,column=1)
            self.button5["font"]= self.myFont

            self.text6  = tk.StringVar()
            self.button6  = Button(self.root,bd=0,textvariable=self.text6,text="",width=12,height=5,bg="#a3b996", command= lambda: self.buttonClicked(self.text6,self.button6,2,2) )
            self.button6.grid(padx=2,pady=1,row=2 ,column=2)
            self.button6["font"]= self.myFont

            #Row of [7,8,9]
            self.text7  = tk.StringVar()
            self.button7  = Button(self.root,bd=0,textvariable=self.text7,text="",width=12,height=5,bg="#bbca95", command= lambda: self.buttonClicked(self.text7,self.button7,1,0) )
            self.button7.grid(padx=2,pady=1,row=1 ,column=0)
            self.button7["font"]= self.myFont

            self.text8  = tk.StringVar()
            self.button8  = Button(self.root,bd=0,textvariable=self.text8,text="",width=12,height=5,bg="#a3b996", command= lambda: self.buttonClicked(self.text8,self.button8,1,1) )
            self.button8.grid(padx=1,pady=1,row=1 ,column=1)
            self.button8["font"]= self.myFont

            self.text9  = tk.StringVar()
            self.button9  = Button(self.root,bd=0,textvariable=self.text9,text="",width=12,height=5,bg="#bbca95", command= lambda: self.buttonClicked(self.text9,self.button9,1,2) )
            self.button9.grid(padx=2,pady=1,row=1 ,column=2) 
            self.button9["font"]= self.myFont

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

#appThree= tripleT()
#appThree.startPlaying()            
"""


 █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 

 ▄▄▄· ▄• ▄▌▄▄▄▄▄▪  .▄▄ · ▄▄▄▄▄▪   ▄▄·     • ▌ ▄ ·.        ▐ ▄ ▄ •▄ ▄▄▄ . ▄· ▄▌
▐█ ▀█ █▪██▌•██  ██ ▐█ ▀. •██  ██ ▐█ ▌▪    ·██ ▐███▪▪     •█▌▐██▌▄▌▪▀▄.▀·▐█▪██▌
▄█▀▀█ █▌▐█▌ ▐█.▪▐█·▄▀▀▀█▄ ▐█.▪▐█·██ ▄▄    ▐█ ▌▐▌▐█· ▄█▀▄ ▐█▐▐▌▐▀▀▄·▐▀▀▪▄▐█▌▐█▪
▐█ ▪▐▌▐█▄█▌ ▐█▌·▐█▌▐█▄▪▐█ ▐█▌·▐█▌▐███▌    ██ ██▌▐█▌▐█▌.▐▌██▐█▌▐█.█▌▐█▄▄▌ ▐█▀·.
 ▀  ▀  ▀▀▀  ▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀ ▀▀▀·▀▀▀     ▀▀  █▪▀▀▀ ▀█▄▀▪▀▀ █▪·▀  ▀ ▀▀▀   ▀ • 
                                                             

"""