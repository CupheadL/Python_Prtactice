import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# --- 定义动作 (函数) ---
def on_click():
    # config 可以动态修改组件的属性
    label.config(text="哎哟，你干嘛~！", fg="red")

# --- 添加组件 ---
label = tk.Label(root, text="准备好了吗？", font=("Arial", 16))
label.pack(pady=20)

# 关键点：command=on_click (注意不要加括号，只写函数名)
btn = tk.Button(root, text="点击变身", command=on_click)
btn.pack()

root.mainloop()