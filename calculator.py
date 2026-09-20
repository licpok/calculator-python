import tkinter as tk
import math
from tkinter import messagebox

calculator = tk.Tk()
calculator.title("science calculator")
calculator.geometry("666x520")

# 符号简写
NAME = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "ln": math.log,
    "lg": math.log10,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "__builtins__": None,  # 禁用内置函数
}


# 显示屏
var = tk.StringVar()


# 显示区
display = tk.Entry(calculator, textvariable=var, font=("Arial", 24), justify="right")
display.pack(side="top", fill="x", padx=10, pady=10, ipady=20)


# 输入区
button = tk.Frame(calculator)
button.pack(side="bottom", fill="both", expand=True)


# 适配网格
for r in range(5):
    button.rowconfigure(r, weight=1)
for c in range(6):
    button.columnconfigure(c, weight=1)


# 输入模块
def press(target):
    cur = var.get()
    var.set(cur + target)


# 计算模块
def equal():
    global var
    expression = var.get()
    if expression == "":
        return
    if len(expression) > 32:
        messagebox.showerror(
            "input error", "the expression is too long!", parent=calculator
        )
        return
    try:
        result = eval(expression, NAME, {})
        if len(str(result)) > 32:
            messagebox.showerror(
                "output error", "the result is too long!", parent=calculator
            )
            return
        var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror(
            "calculate error", "zero can't be the division!", parent=calculator
        )
        var.set("")
    except Exception:
        messagebox.showerror(
            "input error", "please check your expression!", parent=calculator
        )
        var.set("")


# 退格模块
def backspace():
    cur = var.get()
    if cur:
        var.set(cur[:-1])


# 清除模块
def clear():
    global var
    var.set("")


# 制作按钮
def make_btn(text, r, c, cmd=None):
    if cmd is None:
        cmd = lambda t=text: press(t)
    b = tk.Button(button, text=text, command=cmd, font=("Arial", 18))
    b.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
    return b


#  按钮
make_btn("pi", 0, 0),
make_btn("e", 1, 0),
make_btn("abs", 2, 0),
make_btn("xʸ", 3, 0, lambda: press("**")),
make_btn("C", 4, 0, clear),
make_btn("tan", 0, 1),
make_btn("sin", 1, 1),
make_btn("cos", 2, 1),
make_btn("ln", 3, 1),
make_btn("lg", 4, 1),
make_btn("(", 0, 2),
make_btn("1", 1, 2),
make_btn("4", 2, 2),
make_btn("7", 3, 2),
make_btn("0", 4, 2),
make_btn(")", 0, 3),
make_btn("2", 1, 3),
make_btn("5", 2, 3),
make_btn("8", 3, 3),
make_btn(".", 4, 3),
make_btn("%", 0, 4),  # 注：此处%为取余号，而非百分号
make_btn("3", 1, 4),
make_btn("6", 2, 4),
make_btn("9", 3, 4),
make_btn("=", 4, 4, equal),
make_btn("⌫", 0, 5, backspace),
make_btn("+", 1, 5),
make_btn("-", 2, 5),
make_btn("*", 3, 5),
make_btn("/", 4, 5),


calculator.mainloop()
