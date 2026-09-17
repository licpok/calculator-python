import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("800x600")

var = tk.StringVar(value="")

l = tk.Label(
    window,
    textvariable=var,
    bg="yellow",
    font=("Arial", 30),
    width=20,
    height=5,
)

l.pack(pady=20)

on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me!")
    else:
        on_hit = False
        var.set("")


b = tk.Button(window, text="hit me", width=15, height=2, command=hit_me)
b.pack()

window.mainloop()
