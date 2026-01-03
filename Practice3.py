import tkinter as tk

def show_name():
    # 1. 获取输入框的内容
    name = entry.get()
    # 2. 修改标签文字
    result_label.config(text=f"你好, {name}!")

root = tk.Tk()
root.geometry("512x512")

# 提示文字
tk.Label(root, text="请输入你的名字:").pack(pady=6)

# --- 输入框 (Entry) ---
entry = tk.Entry(root)
entry.pack(pady=5)

# 按钮
btn = tk.Button(root, text="确定", command=show_name)
btn.pack(pady=10)

# 显示结果的标签
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

root.mainloop()