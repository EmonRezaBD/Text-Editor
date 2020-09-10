from tkinter import*

root = Tk()

#Root window, title and dimension
root.title("Welcome in GUI")
root.geometry('450x300')

#adding a label to root window

lbl = Label(root, text="Are u a geek?")
lbl.grid()

#function to display text when
#button is clicked

def clicked():
	lbl.configure(text = "I just got thap")

btn = Button(root, text = "Click me", fg = "red" , command=clicked)

btn.grid(column=1, row=0)

root.mainloop()