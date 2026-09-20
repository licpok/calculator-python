import tkinter as tk
import pickle

window = tk.Tk()
window.title("Welcome to Xiaomuji's world")
window.geometry("450x300")

canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file="welcome.gif")
image = canvas.create_image(0, 0, anchor="nw", image=image_file)
canvas.pack(side="top")

tk.Label(window, text="user name").place(x=50, y=150)
tk.Label(window, text="password").place(x=50, y=200)

var_usr_name = tk.StringVar()
var_usr_name.set("example@python.com")
var_password = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_password = tk.Entry(window, textvariable=var_password, show="*")
entry_usr_name.place(x=160, y=150)
entry_password.place(x=160, y=200)


def usr_login():
    usr_name = var_usr_name.get()
    usr_password = var_password.get()
    try:
        with open("usrs_info.pickle", "rb") as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open("usrs_info.pickle", "wb") as usr_file:
            usrs_info = {"admin": "admin"}
            pickle.dump(usrs_info, usr_file)


def usr_sign_up():
    pass


btn_login = tk.Button(window, text="login", command=usr_login)
btn_sign_up = tk.Button(window, text="sign up", command=usr_sign_up)
btn_login.place(x=170, y=230)
btn_sign_up.place(x=270, y=230)

window.mainloop()
