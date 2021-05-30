import tkinter as tk
import random as rand
from tkinter.constants import DISABLED
from PIL import Image, ImageTk
from tkinter import Button, messagebox
import tkinter.font as font   
import main


class FlipTheT:

    def ExitToMenu(self):
        global keepPlaying
        self.keepPlaying= False
        self.root.destroy()
        self.app = main.MainMenu()
        self.app.openMenu()

    def buttonClick(self,l,c,x,button):
        button.grid_forget()
        global firstOrSecond, firstImage, firstL, firstC, firstButton, livesLeft,keepPlaying, picsFlipped, lifeImage,livesList
        if self.firstOrSecond==1 :
            self.firstImage= self.mat[l-1][c-1]
            self.firstL=l
            self.firstC=c
            self.firstButton= button
        else:
            if self.mat[l-1][c-1]!= self.firstImage : 
                self.livesLeft -= 1     

                self.lifeImage=self.livesList[self.livesLeft]    
                self.root.lifeImage= ImageTk.PhotoImage(Image.open(self.lifeImage))
                self.livesButton.configure(image=self.root.lifeImage)

                self.firstButton.grid(row=self.firstL,column=self.firstC,pady=2)
                button.grid(row=l,column=c,pady=2)
                if self.livesLeft==0:
                    self.box= messagebox.askquestion("Game Over!","You Have No Lives Yet\nWould you like to play again?",icon="question")
                    if self.box!="yes":   
                        self.ExitToMenu()
                    else: 
                        self.root.destroy()
            else:
                self.picsFlipped+=1
                if self.picsFlipped==4:
                    self.box= messagebox.askquestion("You Won!","You have Flipped all the images\nWould you like to play again?",icon="question")
                    if self.box!="yes":   
                        self.ExitToMenu()
                    else: 
                        self.root.destroy()       

        if self.firstOrSecond ==1:
            self.firstOrSecond=2
        else:
            self.firstOrSecond=1

    def coverButtons(self):

        self.button1 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(1,1,1,self.button1))
        self.button1.grid(row=1,column=1,padx=2,pady=2)

        self.button2 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(1,2,2,self.button2))
        self.button2.grid(row=1,column=2,padx=2,pady=2)

        self.button3 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(1,3,3,self.button3))
        self.button3.grid(row=1,column=3,padx=2,pady=2)

        self.button4 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(1,4,4,self.button4))
        self.button4.grid(row=1,column=4,padx=2,pady=2)

        self.button5 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(2,1,5,self.button5))
        self.button5.grid(row=2,column=1,padx=2,pady=2)

        self.button6 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(2,2,6,self.button6))
        self.button6.grid(row=2,column=2,padx=2,pady=2)

        self.button7 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(2,3,7,self.button7))
        self.button7.grid(row=2,column=3,padx=2,pady=2)

        self.button8 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(2,4,8,self.button8))
        self.button8.grid(row=2,column=4,padx=2,pady=2)

    def changeLayout(self):
        global t1
        try: 
            self.welcomeMessage.destroy()
        except:
            pass        
        self.root.geometry("425x200")    
        #image11= tk.PhotoImage(file=imageList[1]).subsample(8,8)
        self.button11 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image11,state= DISABLED,)# command= lambda: buttonClick(root.image11,1,1))
        self.button11.grid(row=1,column=1,padx=2,pady=2)

        #image12= tk.PhotoImage(file=imageList[2]).subsample(8,8)
        self.button12 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image12,state= DISABLED,)#  command= lambda: buttonClick(root.image12,1,2))
        self.button12.grid(row=1,column=2,padx=2,pady=2)

        #image13= tk.PhotoImage(file=imageList[3]).subsample(8,8)
        self.button13 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image13,state= DISABLED,)# command= lambda: buttonClick(root.image13,1,3))
        self.button13.grid(row=1,column=3,padx=2,pady=2)

        #image14= tk.PhotoImage(file=imageList[4]).subsample(8,8)
        self.button14 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image14,state= DISABLED,)# command= lambda: buttonClick(root.image14,1,4))
        self.button14.grid(row=1,column=4,padx=2,pady=2)

        #image21= tk.PhotoImage(file=imageList[1]).subsample(8,8)
        self.button21 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image21,state= DISABLED,)# command= lambda: buttonClick(root.image21,2,1))
        self.button21.grid(row=2,column=1,padx=2,pady=2)

        #image22= tk.PhotoImage(file=imageList[2]).subsample(8,8)
        self.button22 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image22,state= DISABLED,)# command= lambda: buttonClick(root.image22,2,2))
        self.button22.grid(row=2,column=2,padx=2,pady=2)

        #image23= tk.PhotoImage(file=imageList[3]).subsample(8,8)
        self.button23 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image23,state= DISABLED,)# command= lambda: buttonClick(root.image23,2,3))
        self.button23.grid(row=2,column=3,padx=2,pady=2)

        #image24= tk.PhotoImage(file=imageList[4]).subsample(8,8)
        self.button24 = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image= self.root.image24,state= DISABLED,)# command= lambda: buttonClick(root.image24,2,4))
        self.button24.grid(row=2,column=4,padx=2,pady=2)   

        self.livesButton.grid(row=0,column=1,pady=2, columnspan=4)
        
        self.root.after(2000, self.coverButtons)

    def OnClose(self):
        global keepPlaying
        self.keepPlaying=False 
        self.root.destroy()
        self.app = main.MainMenu()
        self.app.openMenu()
       
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
    def mainftt(self):
        self.keepPlaying=True ;self.playedOnce=0
        while self.keepPlaying==True:   
            self.firstImage="" ; self.firstL=0 ; self.firstC=0 ; self.livesLeft=3; self.picsFlipped=0; self.firstOrSecond=1
            self.imageList=["images/gray.png","images/axe.png","images/flower.png","images/pistol.png","images/shovel.png"]
            self.livesList=["images/0lives.png","images/1lives.png","images/2lives.png","images/3lives.png"]
            self.mat=[[""]*4,[""]*4]
            for self.a in range(0,4):
                while True :
                    self.l=rand.randint(0,1)
                    self.c=rand.randint(0,3)
                    if self.mat[self.l][self.c]=="":
                        break
                self.mat[self.l][self.c]=self.imageList[self.a+1]
                
                while True :
                    self.l=rand.randint(0,1)
                    self.c=rand.randint(0,3)
                    if self.mat[self.l][self.c]=="":
                        break
                self.mat[self.l][self.c]=self.imageList[self.a+1]

                

            self.root= tk.Tk()
            self.root.title("Twin Cards")
            self.root.iconbitmap("images/poker.ico")
            self.root.configure(bg="#272727")
            self.root.geometry("500x130")
            self.center(self.root)
            self.root.resizable(False, False) 
            self.root.protocol('WM_DELETE_WINDOW', self.OnClose)
            

            self.image00=self.imageList[0]
            self.root.image00= ImageTk.PhotoImage(Image.open(self.image00))
            self.firstButton = tk.Button(self.root,text='',width=100,height=80,bg='#353535',bd=0,image=self.root.image00, command= lambda: self.buttonClick(1,1,1,self.firstButton))


            self.lifeImage=self.livesList[3]
            self.root.lifeImage= ImageTk.PhotoImage(Image.open(self.lifeImage))
            
            self.image11=self.mat[0][0]
            self.root.image11= ImageTk.PhotoImage(Image.open(self.image11))

            self.image12=self.mat[0][1]
            self.root.image12= ImageTk.PhotoImage(Image.open(self.image12))

            self.image13=self.mat[0][2]
            self.root.image13= ImageTk.PhotoImage(Image.open(self.image13))

            self.image14=self.mat[0][3]
            self.root.image14= ImageTk.PhotoImage(Image.open(self.image14))

            self.image21=self.mat[1][0]
            self.root.image21= ImageTk.PhotoImage(Image.open(self.image21))

            self.image22=self.mat[1][1]
            self.root.image22= ImageTk.PhotoImage(Image.open(self.image22))

            self.image23=self.mat[1][2]
            self.root.image23= ImageTk.PhotoImage(Image.open(self.image23))

            self.image24=self.mat[1][3]
            self.root.image24= ImageTk.PhotoImage(Image.open(self.image24))     

            self.livesFont= font.Font(family="source sans pro", size=11, slant="italic")
            self.livesButton = tk.Button(self.root,compound="right", text="\t\t\t\t\t    Lives Left:", width=420,height=20,bg="#353535", bd=0, image=self.root.lifeImage, state=DISABLED,  )#"\t\t\t\t\t\t\t     "
            self.livesButton["font"]=self.livesFont


            self.firstFont = font.Font(family="source sans pro",size=15, )# Reem kufi, Modern M, Raleway MS, Gothic, Microsoft uighur,
            self.textColor="#BAF9FF"
            if self.playedOnce==0:
                self.welcomeMessage= tk.Button(self.root,text="ONCE YOU CLICK ME YOU WILL HAVE\n5 SECONDS TO REMEMBER THE POSITIONS\nOF EACH PAIR OF PHOTOS",width=45,height=5,bg="#353535",bd=0,fg=self.textColor,command=lambda: self.changeLayout())#Once you click me you'll have\n5 seconds to remember the positions\n of each pair of photos
                #welcomeMessage= tk.Button(root,text="Once you click me you'll have\n5 seconds to remember the positions\n of each pair of photos",padx=120,pady=30,bg="#353535",bd=0,fg="#fff",command=lambda: changeLayout())
                self.welcomeMessage.grid(columnspan= 4,row= 0, column=1, pady=2)  
                self.welcomeMessage["font"]=self.firstFont
                self.playedOnce=1 
            else:
                self.changeLayout()

            self.root.mainloop() 
    """Coded By 
                    █████╗ ██████╗ ███████╗██╗███████╗ █████╗ ████████╗ ██████╗ 
                    ██╔══██╗██╔══██╗██╔════╝██║╚══███╔╝██╔══██╗╚══██╔══╝██╔═══██╗
                    ███████║██████╔╝█████╗  ██║  ███╔╝ ███████║   ██║   ██║   ██║
                    ██╔══██║██╔══██╗██╔══╝  ██║ ███╔╝  ██╔══██║   ██║   ██║   ██║
                    ██║  ██║██║  ██║██║     ██║███████╗██║  ██║   ██║   ╚██████╔╝
                    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ 
    """

"""
    print("\n\n\n\n\n")
    x=0
    for a in range(1,3):
        for b in range(1,5):
            x+=1
            #print("root.image"+str(a)+str(b)+".subsample(8,8)")
            #print("image"+str(a)+str(b)+"=mat["+str(a-1)+"]["+str(b-1)+"]")
            #print("root.image"+str(a)+str(b)+"= ImageTk.PhotoImage(Image.open(image"+str(a)+str(b)+") ).subsample(8,8)")
            #print("button"+str(x)+" = tk.Button(root,text='',width=100,height=80,bg='#353535',bd=0,image=root.image00, command= lambda: buttonClick("+str(a)+","+str(b)+","+str(x)+",button"+str(x)+"))")
            #print("button"+str(x)+".grid(row="+str(a)+",column="+str(b)+",padx=2,pady=2)\n")
"""