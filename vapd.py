import tkinter as tk
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('vpad text Editor')

############################# main menu #####################################
############################ main menu ending ###############################

#file

main_menu = tk.Menu()

#file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')



file = tk.Menu(main_menu, tearoff=False) #True leads to separate the menu bar.

file.add_command(label='New',image=new_icon,compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='open',image=open_icon,compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT, accelerator='Ctrl+Q')



edit = tk.Menu(main_menu, tearoff=False)
view = tk.Menu(main_menu, tearoff=False)
color_theme = tk.Menu(main_menu, tearoff=False)

###cascade
main_menu.add_cascade(label = 'file', menu=file)
main_menu.add_cascade(label = 'edit', menu=edit)
main_menu.add_cascade(label = 'view', menu=view)
main_menu.add_cascade(label = 'color_theme', menu=color_theme)






############################# tootlbar #####################################
############################ toolbar ending ###############################

############################# text editor #####################################
############################ text editor ending ###############################

############################# main status bar #####################################
############################ main statur bar ending ###############################

############################# main menu functionality #####################################
############################ main menu functionality ending ###############################


main_application.config(menu=main_menu)
main_application.mainloop()
