import tkinter as tk
from cProfile import label

root = tk.Tk()
root.geometry('300x300')

label=tk.Label(root,text="你好,Python!",font=("Arial",20))
label.pack()

btn=tk.Button(root,text="点我试试")
btn.pack(pady=20)
root.mainloop()