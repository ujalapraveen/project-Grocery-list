
from tkinter import *
from tkinter import messagebox
def addElement():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
def deleteElement():
    lb.delete(ANCHOR)
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Navgurukul Students List')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    fg='#464646',
    selectbackground='#a6a6a6',
    
)
lb.pack(side=LEFT, fill=BOTH)


my_entry = Entry( 
    ws,
    font=('times', 15)
    )

my_entry.pack(pady=25)

button_frame = Frame(ws)
button_frame.pack(pady=25)

addTask_btn = Button(
    button_frame,
    text='Add Element',
    bg='#c5f776',
  
    command=addElement
)
addTask_btn.pack(fill=BOTH, 
                 side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Element',
    bg='#ff8b61',
   
    command=deleteElement
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()