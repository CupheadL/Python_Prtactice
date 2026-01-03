import tkinter as tk
from tkinter import ttk, messagebox
import random


class WordRecitationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("背单词软件")
        self.root.geometry("400x500")

        # --- 数据准备 (模拟数据库) ---
        # 格式: {'单词': ['中文释义', 错误次数]}
        self.word_db = {
            'advise': ['建议', 2],
            'apple': ['苹果', 1],
            'ball': ['球', 0],
            'bone': ['骨头', 1],
            'boy': ['男孩', 0],
            'breath': ['呼吸', 0],
            'carrot': ['胡萝卜', 0],
            'celebrate': ['庆祝', 0],
            'cheap': ['便宜', 2],
            'check': ['检查', 2],
            'cheer': ['欢呼', 1],
            'consider': ['考虑', 2],
            'defend': ['防守', 0],
            'dog': ['狗', 0]
        }

        # 转换成列表方便随机抽取
        self.word_list = list(self.word_db.keys())
        self.current_word = ""
        self.score = 6  # 初始积分 (参考图片)

        # --- 界面布局 ---
        self.create_widgets()
        self.next_question()

    def create_widgets(self):
        # 1. 顶部大标题
        tk.Label(self.root, text="背单词，赢积分", font=("SimHei", 20, "bold")).pack(pady=20)

        # 2. 积分显示
        self.score_label = tk.Label(self.root, text=f"当前积分:  {self.score}", font=("Arial", 14), fg="gray")
        self.score_label.pack(pady=5)

        self.score_val_label = tk.Label(self.root, text=str(self.score), font=("Arial", 24))
        # (这里为了简单，直接把分数值放在上面label里了，也可以单独放)

        # 3. 模式选择 (单选框)
        self.mode_var = tk.StringVar(value="EtoC")
        frame_mode = tk.Frame(self.root)
        frame_mode.pack(pady=10, anchor="w", padx=40)

        modes = [("英译中", "EtoC"), ("中译英", "CtoE"), ("拼写填空", "Spell")]
        for text, val in modes:
            tk.Radiobutton(frame_mode, text=text, variable=self.mode_var, value=val).pack(anchor="w")

        # 4. 题目显示区域 (显示英文单词)
        self.question_label = tk.Label(self.root, text="ready...", font=("Arial", 24, "bold"), bg="#f0f0f0", width=15)
        self.question_label.place(x=150, y=110)  # 绝对定位以模仿图片布局

        # 5. 输入框
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14), width=20)
        self.answer_entry.pack(pady=40)
        self.answer_entry.bind('<Return>', lambda event: self.check_answer())  # 回车键确认

        # 6. 反馈标签 ("太棒了！")
        self.feedback_label = tk.Label(self.root, text="", font=("SimHei", 16), fg="red")
        self.feedback_label.pack(pady=5)

        # 7. 按钮区域
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="确定", font=("SimHei", 12), width=8, command=self.check_answer).grid(row=0, column=0,
                                                                                                        padx=10)
        tk.Button(btn_frame, text="退出", font=("SimHei", 12), width=8, command=self.root.quit).grid(row=0, column=1,
                                                                                                     padx=10)

        # 8. 查看错词表按钮
        tk.Button(self.root, text="查看错词表", font=("SimHei", 12), command=self.open_error_list).pack(pady=10)

    def next_question(self):
        """随机抽取下一个单词"""
        self.current_word = random.choice(self.word_list)
        # 根据模式显示内容，这里默认演示 英译中
        if self.mode_var.get() == "EtoC":
            self.question_label.config(text=self.current_word)
        elif self.mode_var.get() == "CtoE":
            self.question_label.config(text=self.word_db[self.current_word][0])

        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        """检查答案逻辑"""
        user_ans = self.answer_entry.get().strip()
        correct_meaning = self.word_db[self.current_word][0]

        # 简单判断：如果输入内容包含在正确释义中 (模糊匹配)
        if user_ans and user_ans in correct_meaning:
            self.score += 1
            self.feedback_label.config(text="太棒了！", fg="green")
            self.root.after(1000, self.next_question)  # 1秒后自动下一题
        else:
            self.score -= 1
            self.word_db[self.current_word][1] += 1  # 增加错误次数
            self.feedback_label.config(text=f"错了，是: {correct_meaning}", fg="red")

        self.score_label.config(text=f"当前积分:  {self.score}")

    def open_error_list(self):
        """打开错词表窗口 (右侧界面)"""
        top = tk.Toplevel(self.root)
        top.title("本次练习错词表")
        top.geometry("400x400")

        tk.Label(top, text="本次练习错词表", font=("SimHei", 18)).pack(pady=10)

        # 使用 Treeview 表格组件
        columns = ("english", "chinese", "count")
        tree = ttk.Treeview(top, columns=columns, show="headings", height=15)

        tree.heading("english", text="英文")
        tree.heading("chinese", text="中文")
        tree.heading("count", text="错误次数")

        tree.column("english", width=120)
        tree.column("chinese", width=120)
        tree.column("count", width=80, anchor="center")

        tree.pack(pady=10)

        # 填充数据 (只显示错误次数 > 0 的)
        for word, info in self.word_db.items():
            if info[1] > 0:
                tree.insert("", tk.END, values=(word, info[0], info[1]))

        # 返回按钮
        tk.Button(top, text="返回", font=("SimHei", 12), command=top.destroy).pack(pady=10, anchor="e", padx=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = WordRecitationApp(root)
    root.mainloop()