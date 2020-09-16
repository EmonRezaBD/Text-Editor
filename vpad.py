import tkinter as tk
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('800x600')
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


####Edit
##edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
copy_icon = tk.PhotoImage(file='icons2/copy.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')


edit = tk.Menu(main_menu, tearoff=False)



##view icons
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)



#### Color_Theme
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict = { #dictionary
	'Light Default': ('#000000' , '#fffffff'), #ff-> text color, ss->background color
	'Light Plus' : ('#474747', '#e0e0e0'),
	'Dark': ('#c4c4c4','#2d2d2d'),
	'Red': ('#2d2d2d','#ffe8e8'),
	'Monokai' :('#d3b774','#474747'),
	'Night Blue':('#ededed','#6b9dc2')
}




###cascade
main_menu.add_cascade(label = 'file', menu=file)
main_menu.add_cascade(label = 'edit', menu=edit)
main_menu.add_cascade(label = 'view', menu=view)
main_menu.add_cascade(label = 'color_theme', menu=color_theme)



############################# tootlbar #####################################

#print(type(tk.font.families()))

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X) #Will be placed in the upperside. tk.X for horizontally Fill.

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30,textvariable = font_family, state='readonly' )
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Times New Roman'))
font_box.grid(row=0,column=0, padx=5)

##Size Box

size_var  = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(8,81)) # ++ incraese
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

##bold button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

##italic Button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

##Underline Button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar,image = underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

##Font Color button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

##Align left
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

##Align Center
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7,padx=5)


##Algin Right
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)
############################ toolbar ending ###############################


############################# text editor #####################################
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief =tk.FLAT) # if word is getting full then it will start from next line.

scroll_bar = tk.Scrollbar(main_application) # scroll bar will appear in right side.
text_editor.focus_set() # cursor will blink
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command =text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionality
current_font_family = 'Times New Roman'
current_font_size = 12

def change_font(event = None): #main_application
	global current_font_family
	current_font_family = font_family.get() #which font be given by user is getting by this func
	text_editor.configure(font = (current_font_family,current_font_size) )

def change_fontsize(event=None):
	global current_font_size
	current_font_size = size_var.get() #which font be given by user is getting by this func
	text_editor.configure(font = (current_font_family,current_font_size) )



font_box.bind("<<ComboboxSelected>>",change_font) #Bind the function with combobox.
font_size.bind("<<ComboboxSelected>>", change_fontsize)

################## Buttons Functionality

#bold button functionality
def change_bold():
	text_property = tk.font.Font(font=text_editor['font'])
	if text_property.actual()['weight'] == 'normal':
		text_editor.configure(font = (current_font_family,current_font_size,'bold'))
	if text_property.actual()['weight'] == 'bold':
		text_editor.configure(font = (current_font_family,current_font_size,'normal'))

bold_btn.configure(command=change_bold) #This is a button, that's why we give a command.

##italic functionality
def change_italic():
	text_property = tk.font.Font(font =text_editor['font'])
	if text_property.actual()['slant'] == 'roman':
		text_editor.configure(font = (current_font_family,current_font_size,'italic'))
	if text_property.actual()['slant'] == 'italic':
		text_editor.configure(font = (current_font_family,current_font_size,'normal'))
italic_btn.configure(command=change_italic)

##Underline functionality
def change_underline():
	text_property = tk.font.Font(font =text_editor['font'])
	if text_property.actual()['underline'] == 0:
		text_editor.configure(font = (current_font_family,current_font_size,'underline'))
	if text_property.actual()['underline'] == 1:
		text_editor.configure(font = (current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)


##font color functionality
def change_font_color():
	color_var = tk.colorchooser.askcolor()
	# print(color_var) #this will show a tuple made with RGB val and a hexa color code.
	text_editor.configure(fg = color_var[1]) #1 because we take the hexa value.

font_color_btn.configure(command=change_font_color)

### Align functionality


text_editor.configure(font=('Times New Roman',12)) # By deafult will type in Arial.



############################ text editor ending ###############################

#############################  status bar #####################################
status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side = tk.BOTTOM) #When you know , where to place the thing then use pack otherwise use grid.














############################ main statur bar ending ###############################

############################# main menu functionality #####################################
############################ main menu functionality ending ###############################

##file command

file.add_command(label='New',image=new_icon,compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='open',image=open_icon,compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT, accelerator='Ctrl+Q')

##edit command

edit.add_command(label='Copy',image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit.add_command(label='Paste',image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+P')
edit.add_command(label='Cut',image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit.add_command(label='Find',image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')


##view checkbutton
view.add_checkbutton(label='Tool Bar',image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tk.LEFT)

#color theme
count = 0
for i in color_dict:
	color_theme.add_radiobutton(label= i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
	count+=1

main_application.config(menu=main_menu)
main_application.mainloop()