from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.title('Notepad')
root.geometry("800x500")
menu = Menu(root)
root.config(menu=menu)


def help():
    messagebox.showinfo("HELP", 'Сами решайте свои проблемы!\n Уверен вам не нужна помощь')


def click():
    window = Tk()
    window.title("New")
    window.geometry("800x500")
    text = Text(window)
    text.pack(expand=YES, fill=BOTH)


def exit():
    root.destroy()


file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=click)
file_menu.add_command(label='New Windows')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Save')
file_menu.add_command(label='Save as...')
file_menu.add_separator()
file_menu.add_command(label='Page setup...')
file_menu.add_command(label='Print...')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)


edit_menu = Menu(menu, tearoff=0)
edit_menu.add_command(label='Undo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Delete')
edit_menu.add_separator()
edit_menu.add_command(label='Search with Bing...')
edit_menu.add_command(label='Find...')
edit_menu.add_command(label='Find Next')
edit_menu.add_command(label='Find Previous')
edit_menu.add_command(label='Replace...')
edit_menu.add_command(label='Go To...')
edit_menu.add_separator()
edit_menu.add_command(label='Select all')
edit_menu.add_command(label='Time/Date')
format_menu = Menu(menu, tearoff=0)
format_menu.add_command(label='Word Wrap')
format_menu.add_command(label='Font...')
zoom_menu = Menu(menu, tearoff=0)
zoom_menu.add_cascade(label='Zoom In')
zoom_menu.add_cascade(label='Zoom Out')
zoom_menu.add_cascade(label='Restore Default Zoom')
view_menu = Menu(menu, tearoff=0)
view_menu.add_cascade(label='Zoom', menu=zoom_menu)
view_menu.add_command(label='Status Bar')
help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='View Help',  command=help)
help_menu.add_command(label='Send Feedback')
help_menu.add_separator()
help_menu.add_command(label='About Notepad')

text = Text(root)
text.pack(expand=YES, fill=BOTH)


menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Edit', menu=edit_menu)
menu.add_cascade(label='Format', menu=format_menu)
menu.add_cascade(label='View', menu=view_menu)
menu.add_cascade(label='Help', menu=help_menu)
root.mainloop()