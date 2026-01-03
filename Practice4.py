import tkinter as tk

root=tk.Tk()
root.title("登录界面布局演示")
root.geometry("300x150")

tk.Label(root,text="用户名: ").grid(row=0,column=0,padx=10,pady=10)
tk.Entry(root).grid(row=0,column=1)

tk.Label(root,text="密 码:").grid(row=1,column=0,padx=10,pady=10)
tk.Entry(root,show="*").grid(row=1,column=1)

tk.Button(root,text="登录").grid(row=2,column=0,columnspan=2,pady=10)
root.mainloop()


