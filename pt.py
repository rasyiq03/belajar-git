import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

btn = tk.Button(window, text='Click me')
btn.pack()


window.mainloop()