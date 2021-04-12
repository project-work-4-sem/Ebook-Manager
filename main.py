from tkinter import *
from tkinter import ttk
import subprocess

def hello():
    print("HI")

def Kill():
    p2=subprocess.run(['./shell_scripts/kill_pid.sh {}'.format(pid)],shell=True,capture_output=True,text=True)
    process()
#global variables
frame=0
kill=0
label=0


app=Tk()
app.geometry("775x600")
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
        frame = Frame(app, bg = "gray", height = "600",width="600")
        frame.place(x=0,y=0)
    p1=subprocess.run('./shell_scripts/list_processes.sh', capture_output=True, text=True)
    processes=p1.stdout
    processes=processes.split('\n')
    processes=processes[:-1]
    final=[]
    for x in processes:
        y=x.split()
        a=[]
        a.append(y[0])
        a.append(y[1])
        a.append(y[2])
        a.append("".join(y[3:]))
        a=tuple(a)    
        final.append(a)      
  
    def onselect(event):
        
        curItem = table.selection()
        global pid
        pid=table.item(curItem)['values'][2]

    table=ttk.Treeview(frame,columns=(1,2,3,4),show="headings",height="25")
    table.pack()
    kill=Button(app,text="KILL",width=10,command=Kill)
    kill.place(x=335,y=550)
    

    table.heading("1",text="Memory")
    table.column("1", minwidth=0, width=100, stretch=NO)
    table.heading("2",text="%CPU")
    table.column("2", minwidth=0, width=100, stretch=NO)
    table.heading("3",text="PID")
    table.column("3", minwidth=0, width=150, stretch=NO)
    table.heading("4",text="Name")
    table.column("4", minwidth=0, width=420, stretch=NO)

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
        # mainlabel=Label(right,text="CPU",font=("Helvetica",25))
        # mainlabel.place(x=250,y=20)
        p1=subprocess.run('./shell_scripts/cpu.sh', capture_output=True, text=True,shell=True)
        label=Label(right,text=p1.stdout)
        label.place(x=100,y=20)
    global r1
    r1=app.after(1000, showOnRight1)


def showOnRight2():
    app.after_cancel(r1)
    global right,label
    remove_label()
    if label==0:
        p2=subprocess.run('./shell_scripts/mem.sh', capture_output=True, text=True,shell=True)
        label=Label(right,text=p2.stdout)
        label.place(x=100,y=20)

def showOnRight3():
    app.after_cancel(r1)
    global right,label
    remove_label()
    if label==0:
        p2=subprocess.run('./shell_scripts/disk.sh', capture_output=True, text=True,shell=True)
        disks=p2.stdout
        disks=disks.replace('\x1b[0m','')
        label=Label(right,text=disks)
        label.place(x=100,y=20)
        # final=[]
        # for x in disks:
        #     y=x.split()
        #     a=[]
        #     a.append(y[0])
        #     a.append(y[1])
        #     a.append(y[2])
        #     a.append(y[3])
        #     a.append(y[4])
        #     a.append(y[5])
        #     a.append(y[6])
        #     a=tuple(a)    
        #     final.append(a)
        # table=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7),show="headings",height="10")
        # table.pack()
        # table.heading("1",text="Filesystem")
        # table.column("1", minwidth=0, width=100, stretch=NO)
        # table.heading("2",text="Size")
        # table.column("2", minwidth=0, width=100, stretch=NO)
        # table.heading("3",text="Used")
        # table.column("3", minwidth=0, width=150, stretch=NO)
        # table.heading("4",text="Avail")
        # table.column("4", minwidth=0, width=150, stretch=NO)
        # table.heading("5",text="Use%")
        # table.column("5", minwidth=0, width=150, stretch=NO)
        # table.heading("6",text="Ratio")
        # table.column("6", minwidth=0, width=150, stretch=NO)
        # table.heading("7",text="Mounted On")
        # table.column("7", minwidth=0, width=150, stretch=NO)
        # for x in final:
        #     table.insert("","end",values=x)

def showOnRight4():
    app.after_cancel(r1)
    global right,label
    remove_label()
    if label==0:
        p2=subprocess.run('./shell_scripts/temp.sh', capture_output=True, text=True,shell=True)
        label=Label(right,text=p2.stdout)
        label.place(x=100,y=20)    

def performance():
    global frame,left,right
    hide()

    if frame==0:
        frame = Frame(app, bg = "gray", height = "600",width="600")
        frame.place(x=0,y=0)
        left = Frame(frame, bg = "lightblue", height = "500",width="150")
        left.pack(side=LEFT,padx=3,pady=3)
        right = Frame(frame, bg = "white", height = "500",width="610")
        right.pack(side=LEFT,padx=1,pady=3)
        
        button_cpu=Button(left,text="CPU",width=15,height=5,bg="white",command=showOnRight1)
        button_mem=Button(left,text="MEMORY",width=15,height=5,bg="white",command=showOnRight2)
        button_disk=Button(left,text="DISK",width=15,height=5,bg="white",command=showOnRight3)
        button_temp=Button(left,text="TEMPERATURE",width=15,height=5,bg="white",command=showOnRight4)

        button_cpu.place(x=2,y=0)
        button_mem.place(x=2,y=97)
        button_disk.place(x=2,y=192)
        button_temp.place(x=2,y=280)

        

    
menubar = Menu(app)

menubar.add_command(label =' PROCESS ',command=process )
menubar.add_command(label =' PERFORMANCE ',command=performance )
menubar.add_command(label =' USERS ',command=hello )





app.config(menu = menubar)

app.mainloop()


