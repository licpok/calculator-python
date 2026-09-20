import tkinter as tk

calculator = tk.Tk()
calculator.title("science calculator")
calculator.geometry("480x800")


# 显示屏
var = tk.StringVar()


# 显示区
display = tk.Entry(calculator, textvariable=var, font=("Arial", 24), justify="right")
display.pack(side="top", fill="x", padx=10, pady=10, ipady=20)


# 输入区
button = tk.Frame(calculator)
button.pack(side="bottom", fill="both", expand=True)


# 适配网格
for r in range(4):
    button.rowconfigure(r, weight=1)
for c in range(4):
    button.columnconfigure(c, weight=1)


# 输入模块
def press(target):
    cur = var.get()
    if cur == "" and target in "+*/":
        return
    var.set(cur + target)


# 计算模块
def equal():
    global var
    expression = var.get()
    if expression == "":
        return
    try:
        result = eval(expression)
        var.set(str(result))
    except ZeroDivisionError:
        var.set("0 can't be the division!")
    except Exception:
        var.set("the expression is wrong")


# 制作按钮
def make_btn(text, r, c, cspan=1, cmd=None):
    if cmd == None:
        cmd = lambda t=text: press(t)
    b = tk.Button(button, text=text, command=cmd, font=("Arial", 18))
    b.grid(row=r, column=c, columnspan=cspan, sticky="nsew", padx=2, pady=2)
    return b


# 数字
make_btn("1", 0, 0), make_btn("2", 0, 1), make_btn("3", 0, 2),
make_btn("4", 1, 0), make_btn("5", 1, 1), make_btn("6", 1, 2),
make_btn("7", 2, 0), make_btn("8", 2, 1), make_btn("9", 2, 2),
# 0 扩展两格
make_btn("0", 3, 0, 2)
# 运算符
make_btn("+", 0, 3), make_btn("-", 1, 3), make_btn("*", 2, 3),
make_btn("/", 3, 3), make_btn("=", 3, 2, 1, equal)


calculator.mainloop()
