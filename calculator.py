import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry("200x200")

l = tk.Label(window, bg="yellow", width=30, text="empty")
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        l.config(text="I only love Python!")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):
        l.config(text="I only love C++!")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        l.config(text="I only love JAVA!")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):
        l.config(text="I don't like anything!")
    else:
        l.config(text="I love computer!")


var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(
    window, text="Python", variable=var1, onvalue=1, offvalue=0, command=print_selection
)
c2 = tk.Checkbutton(
    window, text="C++", variable=var2, onvalue=1, offvalue=0, command=print_selection
)
c3 = tk.Checkbutton(
    window, text="JAVA", variable=var3, onvalue=1, offvalue=0, command=print_selection
)
c1.pack()
c2.pack()
c3.pack()

window.mainloop()
