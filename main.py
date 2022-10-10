import tkinter
from tkinter import ttk


def clear(event):
    print('Se limpia')
    




window = tkinter.Tk()

window.columnconfigure(0, weight=3)
window.columnconfigure(0, weight=3)

userNameLabel = ttk.Label(window, text='username: ')
userNameLabel.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

userNameEntry = ttk.Entry(window)
userNameEntry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

userpasswordLabel = ttk.Label(window, text='password:  ')
userpasswordLabel.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

userpasswordEntry = ttk.Entry(window)
userpasswordEntry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

loginButton = ttk.Button(window, text='Loguearse')
loginButton.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)
selected = tkinter.StringVar()
r0 = ttk.Radiobutton(window, text='rad1', value='1', variable=selected)
r1 = ttk.Radiobutton(window, text='rad2', value='2', variable=selected)
r2 = ttk.Radiobutton(window, text='rad3', value='3', variable=selected)

r0.grid(columns=4, row=5, sticky=tkinter.W, padx=5, pady=5)
r1.grid(columns=4, row=6, sticky=tkinter.W, padx=5, pady=5)
r2.grid(columns=4, row=7, sticky=tkinter.W, padx=5, pady=5)


if clear == True:
   selected=0
   clear = False
   print('llego al if')

else:


    clearButton = ttk.Button(window, text='Reset')
    clearButton.grid(column=1, row=8, sticky=tkinter.E, padx=5, pady=5)
    clearButton.bind('<Button-1>', clear)

window.mainloop()
