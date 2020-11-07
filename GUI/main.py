from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.messagebox as tmsg
import matplotlib.pyplot as plt
from tkinter.ttk import *
from tkinter import *
import numpy as np
import random
#----tkinter window work
root=Tk()
root.minsize(900,420)
root.maxsize(900,420)
root.title("Trading Game")
#------
#----importing image
'''pic=PhotoImage(file="1.png")
pic_label=Label(image=pic)
pic_label.pack()'''
#icon photo
pic=PhotoImage(file="window icon.png")
root.iconphoto(False, pic)
#---
def pt():
    #----message work
    msg=tmsg.askquestion("Trade Information","Place This Trade")
    x=s1.get()
    if msg=="yes":
        #select the no. of time you want to repeat loop
        for i in range(1,x+1):
            #----importing random number
            xaxis=random.randint(1,15)
            yaxis=random.randint(1,15)
            #----
            #print(f"x={x}")
            #----graph work
            fig=plt.Figure(figsize=(6,4),dpi=100)
            fig.add_subplot(111).plot(xaxis,yaxis)
            chart=FigureCanvasTkAgg(fig,root)
            chart.get_tk_widget().place(x=260,y=10)
            #-----
            #condition for result
            '''if last num of graph is equal or greater than selected graph then print color full screenin tkinter'''
            #----start progressbar
            pgbar.start(s1.get()*7)
            #-----
            print("in msg loop true")
    else:
        print("in msg loop fals")

    
        '''if i==1:
            print(f"x={x}")
            pgbar.stop()
            print("in if loop")'''
            
    

#------time
Label(root,text="Time",fg="blue").place(x=5,y=19)
s1=Scale(root,from_=1,to=10,orient=HORIZONTAL)
s1.place(x=70,y=0)

#-----amount
Label(root,text="Amount",fg="blue").place(x=5,y=65)
s2=Scale(root,from_=1,to=150,orient=HORIZONTAL)
s2.place(x=70,y=45)
#-----

#----UP orDown
var=IntVar()
var.set(1)
Label(root,text="Graph",fg="blue").place(x=5,y=100)
#Label(root,text="Graph").grid(row=0,column=1)
rb=Radiobutton(root,text="UP",padx=14,variable=var,value=1)
rb.place(x=53,y=100)
rb=Radiobutton(root,text="DOWN",padx=14,variable=var,value=2)
rb.place(x=103,y=100)
#--------

#-----player selection
random_player_selection=random.choice(["Computer","Person"])
print(random_player_selection)
#display player turn
Label(root,text="Turn",fg="blue").place(x=7,y=130)
Label(root,text=f"{random_player_selection}",fg="peru").place(x=67,y=130)
#-----

#------Progressbar
pgbar=Progressbar(root,length=100,orient=HORIZONTAL,mode="determinate")
pgbar.place(x=5,y=160)
#-----
#----buttton work
but_pic=PhotoImage(file="start button.png")
Button(root,command=pt,image=but_pic,border=0).place(x=4,y=195)
#----

#----Result
Label(root,text="Result",fg="blue").place(x=4,y=250)
#---

'''#-------Load matplotlib graph in ktinter
x=[1,2,3,4,5]
y=[1,2,3,32,5]
#graph work
fig=plt.Figure(figsize=(6,4),dpi=100)
fig.add_subplot(111).plot(0,0)
#load graph in tkinter
chart=FigureCanvasTkAgg(fig,root)
chart.get_tk_widget().place(x=260,y=10)
#------'''

root.mainloop()
plt.show() 
