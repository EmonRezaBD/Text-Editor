from tkinter import*

root = Tk()

#Root window, title and dimension
root.title("Welcome in GUI")
root.geometry('450x300')

#adding a label to root window

lbl = Label(root, text="Are u a geek?")
lbl.grid(column =1 , row=0 )

#adding entry field
txt = Entry(root, width=10)
txt.grid(column = 1, row = 1)

#function to display text when
#button is clicked

lebel = Label(root, text = " ")
lebel.grid(column=0,row=3)

def clicked():
	res = "You wrote "+txt.get()
	lebel.configure(text = res)

btn = Button(root, text = "Click me", fg = "red" , command=clicked)

btn.grid(column=0, row=1)




root.mainloop()