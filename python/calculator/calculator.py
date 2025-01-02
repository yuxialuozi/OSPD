import tkinter as tk
from tkinter import messagebox


class ProgrammerCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("程序员计算器")
        self.root.geometry("500x800")

        # 当前输入和结果
        self.current_input = ""
        self.result = 0

        # 显示框
        self.display = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief="sunken")
        self.display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")

        # 进制转换显示
        self.hex_label = tk.Label(root, text="HEX: 0", font=("Arial", 16), anchor="w")
        self.hex_label.grid(row=1, column=0, columnspan=4, sticky="w", padx=10)

        self.dec_label = tk.Label(root, text="DEC: 0", font=("Arial", 16), anchor="w")
        self.dec_label.grid(row=2, column=0, columnspan=4, sticky="w", padx=10)

        self.oct_label = tk.Label(root, text="OCT: 0", font=("Arial", 16), anchor="w")
        self.oct_label.grid(row=3, column=0, columnspan=4, sticky="w", padx=10)

        self.bin_label = tk.Label(root, text="BIN: 0", font=("Arial", 16), anchor="w")
        self.bin_label.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

        # 按钮布局
        buttons = [
            ("A", 5, 0), ("B", 5, 1), ("C", 5, 2), ("D", 5, 3),
            ("E", 6, 0), ("F", 6, 1), ("<<", 6, 2), (">>", 6, 3),
            ("7", 7, 0), ("8", 7, 1), ("9", 7, 2), ("/", 7, 3),
            ("4", 8, 0), ("5", 8, 1), ("6", 8, 2), ("*", 8, 3),
            ("1", 9, 0), ("2", 9, 1), ("3", 9, 2), ("-", 9, 3),
            ("+/-", 10, 0), ("0", 10, 1), (".", 10, 2), ("+", 10, 3),
            ("C", 11, 0), ("=", 11, 3)
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == "C":
            self.current_input = ""
            self.result = 0
        elif button_text == "=":
            try:
                # 计算表达式
                self.result = eval(self.current_input)
            except Exception as e:
                messagebox.showerror("错误", f"无效的表达式！\n错误信息：{e}")
        elif button_text in ["<<", ">>"]:
            # 位移操作
            if button_text == "<<":
                self.result = int(self.current_input) << 1
            elif button_text == ">>":
                self.result = int(self.current_input) >> 1
        elif button_text == "+/-":
            # 切换正负号
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
        else:
            # 添加输入
            self.current_input += button_text

        # 更新显示
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, str(self.result) if self.result else self.current_input)

        # 更新进制显示
        try:
            value = int(self.result if self.result else self.current_input)
            self.hex_label.config(text=f"HEX: {hex(value).upper()}")
            self.dec_label.config(text=f"DEC: {value}")
            self.oct_label.config(text=f"OCT: {oct(value)}")
            self.bin_label.config(text=f"BIN: {bin(value)}")
        except ValueError:
            self.hex_label.config(text="HEX: 0")
            self.dec_label.config(text="DEC: 0")
            self.oct_label.config(text="OCT: 0")
            self.bin_label.config(text="BIN: 0")


# 创建窗口
root = tk.Tk()
app = ProgrammerCalculator(root)
root.mainloop()
