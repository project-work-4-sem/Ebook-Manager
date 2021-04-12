from tkinter import *
from tkinter import ttk
import subprocess

app=Tk()
app.geometry("785x560")
app.configure(bg='white')
app.title("TASK MANAGER")

def hello():
    print("HI")

def Kill():
    p2=subprocess.run(['./shell_scripts/kill_pid.sh {}'.format(pid)],shell=True,capture_output=True,text=True)
    process()
    
def process():
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
    frame = Frame(app, bg = "white", height = "500",width="650")
    frame.place(x=0,y=0)

    table=ttk.Treeview(frame,columns=(1,2,3,4),show="headings",height="25")
    table.pack()

    table.heading("1",text="Memory")
    table.column("1", minwidth=0, width=80, stretch=NO)
    table.heading("2",text="%CPU")
    table.column("2", minwidth=0, width=100, stretch=NO)
    table.heading("3",text="PID")
    table.column("3", minwidth=0, width=150, stretch=NO)
    table.heading("4",text="Name")
    table.column("4", minwidth=0, width=450, stretch=NO)

    for x in final:
        table.insert("","end",values=x)

    table.bind('<<TreeviewSelect>>', onselect)    
    kill=Button(text="KILL",command=Kill)
    kill.place(x=700,y=525)

    app.after(4000, process)
    
menubar = Menu(app)

menubar.add_command(label =' PROCESS ',command=process )
menubar.add_command(label =' PERFORMANCE ',command=hello )
menubar.add_command(label =' USERS ',command=hello )





app.config(menu = menubar)
app.mainloop()


