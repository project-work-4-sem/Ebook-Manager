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
flag1=0
flag2=0
frame=0
table=0
left=0
right=0
kill=0


app=Tk()
app.geometry("600x600")
app.configure(bg='white')
app.title("TASK MANAGER")

def hide(widget):
    widget.pack_forget()

def show(widget):
    widget.pack(side=LEFT,padx=5,pady=2)


def process_remove():
    global table,flag1,frame,kill
    
    if table or kill:
        hide(table)
        kill.place(x=260,y=5501)
        flag1=1
def performance_remove():
    global left,right,flag2

    if left:
        hide(left)
        hide(right)
        flag2=1
    
    
def process():
    
    performance_remove()
    global frame,table,flag1,kill
    if frame:
        frame.place(x=5,y=5)
    def onselect(event):
        
        curItem = table.selection()
        print(table.item(curItem)['values'][2])
        

   
    if flag1==0:
        table=ttk.Treeview(frame,columns=(1,2,3,4),show="headings",height="25")
        table.pack()
        kill=Button(app,text="KILL",width=10)
        kill.place(x=260,y=550)
    else:
        show(table)
        kill.place(x=260,y=550)
        flag1=0

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
label=0
def remove_label():
    global label
    label.place(x=8512,y=5000)
    

def showOnRight1():
    global right,label
    if label:
        remove_label()
    label=Label(right,text=content[0])
    label.place(x=50,y=50)



def showOnRight2():
    global right,label
    if label:
        remove_label()
    label=Label(right,text=content[1])
    label.place(x=50,y=50)


def showOnRight3():
    global right,label
    if label:
        remove_label()
    label=Label(right,text=content[2])
    label.place(x=50,y=50)

def showOnRight4():
    global right,label
    if label:
        remove_label()
    label=Label(right,text=content[3])
    label.place(x=50,y=50)    

def performance():
    
    global frame,left,right,flag2
    if frame:
        frame.place(x=5,y=5)
    process_remove()

    if flag2==0:
        left = Frame(frame, bg = "lightblue", height = "500",width="150")
        left.pack(side=LEFT,padx=3,pady=10)
        right = Frame(frame, bg = "white", height = "500",width="420")
        right.pack(side=LEFT,padx=3,pady=10)
        
        button_cpu=Button(left,text="CPU",width=19,height=5,bg="white",command=showOnRight1)
        button_mem=Button(left,text="MEMORY",width=19,height=5,bg="white",command=showOnRight2)
        button_disk=Button(left,text="DISK",width=19,height=5,bg="white",command=showOnRight3)
        button_temp=Button(left,text="TEMPERATURE",width=19,height=5,bg="white",command=showOnRight4)

        button_cpu.place(x=5,y=10)
        button_mem.place(x=5,y=100)
        button_disk.place(x=5,y=190)
        button_temp.place(x=5,y=280)

        
    else:
        show(left)
        show(right)
        flag2=0

        
    
    
    
frame = Frame(app, bg = "gray", height = "500",width="550")

    
menubar = Menu(app)

menubar.add_command(label =' PROCESS ',command=process )
menubar.add_command(label =' PERFORMANCE ',command=performance )
menubar.add_command(label =' USERS ',command=hello )





app.config(menu = menubar)
app.mainloop()


