import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

btn = tk.Button(window, text='Click me')
btn.pack()

btn2 = tk.Button(window, text='Click me')
btn2.pack()

btn3 = tk.Button(window, text='Click me')
btn3.pack()

btn1 = tk.Button(window, text='Click me')
btn1.pack()


window.mainloop()