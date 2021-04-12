from tkinter import *
from tkinter import ttk


file1 = open('output.txt', 'r')
lines = file1.readlines()


final=[]

for x in lines:
    y=x.split()
    a=[]
    a.append(y[0])
    a.append(y[1])
    a.append(y[2])
    a.append("".join(y[3:]))
    a=tuple(a)
    
    final.append(a)
    

def hello():
    print("HI")


#global variables

frame=0
kill=0
label=0


app=Tk()
app.geometry("625x600")
app.configure(bg='white')
app.title("TASK MANAGER")

def hide():
    global frame,kill
    if frame:
        frame.place(x=1000,y=1000)
        frame=0
    if kill:
        kill.place(x=2000,y=2000)
        kill=0
    

def process():
    hide()
    global frame,table,flag1,kill
    if frame==0:
        frame = Frame(app, bg = "gray", height = "600",width="590")
        frame.place(x=5,y=5)
    def onselect(event):
        
        curItem = table.selection()
        print(table.item(curItem)['values'][2])

    table=ttk.Treeview(frame,columns=(1,2,3,4),show="headings",height="25")
    table.pack()
    kill=Button(app,text="KILL",width=10,command=hello)
    kill.place(x=260,y=550)
    

    table.heading("1",text="Memory")
    table.column("1", minwidth=0, width=60, stretch=NO)
    table.heading("2",text="CPU")
    table.column("2", minwidth=0, width=100, stretch=NO)
    table.heading("3",text="Pid")
    table.column("3", minwidth=0, width=150, stretch=NO)
    table.heading("4",text="Name")
    table.column("4", minwidth=0, width=300, stretch=NO)

    for x in final:
        table.insert("","end",values=x)

    table.bind('<<TreeviewSelect>>', onselect)    


content=["cpu","memory","disk","temperature"]


def remove_label():
    global label
    if label:
        label.place(x=1000,y=1000)
        label=0
    

def showOnRight1():
    global right,label
    remove_label()
    if label==0:
        label=Label(right,text=content[0])
        label.place(x=50,y=50)

def showOnRight2():
    global right,label
    label=Label(right,text=content[1])
    label.place(x=50,y=50)

def showOnRight3():
    global right,label
    remove_label()
    if label==0:
        label=Label(right,text=content[2])
        label.place(x=50,y=50)

def showOnRight4():
    global right,label
    remove_label()
    if label==0:
        label=Label(right,text=content[3])
        label.place(x=50,y=50)    

def performance():
    
    global frame,left,right
    hide()

    if frame==0:
        frame = Frame(app, bg = "gray", height = "600",width="590")
        frame.place(x=5,y=5)
        left = Frame(frame, bg = "lightblue", height = "500",width="150")
        left.pack(side=LEFT,padx=3,pady=10)
        right = Frame(frame, bg = "white", height = "500",width="450")
        right.pack(side=LEFT,padx=3,pady=10)
        
        button_cpu=Button(left,text="CPU",width=19,height=5,bg="white",command=showOnRight1)
        button_mem=Button(left,text="MEMORY",width=19,height=5,bg="white",command=showOnRight2)
        button_disk=Button(left,text="DISK",width=19,height=5,bg="white",command=showOnRight3)
        button_temp=Button(left,text="TEMPERATURE",width=19,height=5,bg="white",command=showOnRight4)

        button_cpu.place(x=5,y=10)
        button_mem.place(x=5,y=100)
        button_disk.place(x=5,y=190)
        button_temp.place(x=5,y=280)

        

    
menubar = Menu(app)

menubar.add_command(label =' PROCESS ',command=process )
menubar.add_command(label =' PERFORMANCE ',command=performance )
menubar.add_command(label =' USERS ',command=hello )





app.config(menu = menubar)
app.mainloop()


