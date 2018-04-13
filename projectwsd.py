
from Tkinter import *

root = Tk()


root.title("Ambiguity Resolver")
root.geometry("800x400")
root.config(background = "grey")
app = Frame(root, bg="grey")

app.grid()

def helloCallBack():
   input1 = txt1.get("1.0",END)
   input2 = txt2.get("1.0",END)
   # txt3.delete(0.0,END)
   txt3.insert(0.0, input1+input2) 
  # print input1 ,input2
   
def clearall():
    txt1.delete(0.0,END)
    txt2.delete(0.0,END)
    txt3.delete(0.0,END)
    
btn = Button(app, text="Resolve", font=("Comic Sans MS", 12), command = helloCallBack)
btn1 = Button(app,text="Clear", font=("Comic Sans MS", 12), command = clearall);
lb1 = Label(app, text="Enter The Sentence", font=("Comic Sans MS", 12))
lb2 = Label(app, text="Enter Word", font=("Comic Sans MS", 12))
lb3 = Label(app, text="Result", font=("Comic Sans MS", 12))
txt1 = Text(app, height=2, width=50, font=("Arial", 10))
txt2 = Text(app, height=2, width=50, font=("Arial", 10))
txt3 = Text(app, height=4, width=50, font=("Arial", 10))

lb1.grid(row=0, padx=6, pady=6)
txt1.grid(row=0,column=1, padx=6, pady=6)

lb2.grid(row=1, padx=4, pady=4)
txt2.grid(row=1,column=1, padx=6, pady=6)

lb3.grid(row=2, padx=4, pady=4)
txt3.grid(row=2,column=1, padx=6, pady=6)


btn.grid(row=3, column=1, padx=6, pady=6)
btn1.grid(row=4, column=1)




root.mainloop()