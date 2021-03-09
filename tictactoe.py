from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")

mat = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]


def new_Btns():
    b1 = Button(root, width=20, height=10,
                command=lambda: onClick(1), text=mat[0][0])
    b1.grid(row=1, column=1)

    b2 = Button(root, width=20, height=10, command=lambda: onClick(2))
    b2.grid(row=1, column=2)

    b3 = Button(root, width=20, height=10, command=lambda: onClick(3))
    b3.grid(row=1, column=3)

    b4 = Button(root, width=20, height=10, command=lambda: onClick(4))
    b4.grid(row=4, column=1)

    b5 = Button(root, width=20, height=10, command=lambda: onClick(5))
    b5.grid(row=4, column=2)

    b6 = Button(root, width=20, height=10, command=lambda: onClick(6))
    b6.grid(row=4, column=3)

    b7 = Button(root, width=20, height=10, command=lambda: onClick(7))
    b7.grid(row=8, column=1)

    b8 = Button(root, width=20, height=10, command=lambda: onClick(8))
    b8.grid(row=8, column=2)

    b9 = Button(root, width=20, height=10, command=lambda: onClick(9))
    b9.grid(row=8, column=3)
    return [
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
    ]


rsbtn = Button(root, width=10, height=2, command=lambda: reset(), text="RESET")
rsbtn.grid(row=12, column=1)


def greet(exited):
    if (exited):
        last = Tk()
        last.title("THANKS")
        thnx = Label(text="Thanks for Trying out my WEIRD App",
                     font="arial 20", width=30, height=10)
        thnx.grid(row=2, column=2)
        last.mainloop()
    else:
        messagebox.showinfo("Thanks",
                            "Thanks for Trying out my WEIRD App")


def myexit():
    global exited
    result = messagebox.askyesno(
        "EXIT", "Do you want to exit the GAME?")
    if (result):
        greet(False)
        exit()


exitbtn = Button(root, width=10, height=2,
                 command=lambda: myexit(), text="EXIT")
exitbtn.grid(row=12, column=3)


buttons = new_Btns()

activePalyer = "X"

currPlayerbtn = Label(root, text="Current Player: "+activePalyer)
currPlayerbtn.grid(row=12, column=2)

finished = False


def someoneWon():
    global mat, buttons
    for i in range(len(mat)):
        if (mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][2] != ""):
            buttons[i][0].config(bg="#0f0")
            buttons[i][1].config(bg="#0f0")
            buttons[i][2].config(bg="#0f0")
            return {"res": True, "name": mat[i][0]}
        if (mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and mat[2][i] != ""):
            buttons[0][i].config(bg="#0f0")
            buttons[1][i].config(bg="#0f0")
            buttons[2][i].config(bg="#0f0")
            return {"res": True, "name": mat[0][i]}
    if (mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] != ""):
        buttons[0][0].config(bg="#0f0")
        buttons[1][1].config(bg="#0f0")
        buttons[2][2].config(bg="#0f0")
        return {"res": True, "name": mat[0][0]}
    if (mat[0][2] == mat[1][1] and mat[2][0] == mat[1][1] and mat[1][1] != ""):
        buttons[0][2].config(bg="#0f0")
        buttons[1][1].config(bg="#0f0")
        buttons[2][0].config(bg="#0f0")
        return {"res": True, "name": mat[0][2]}
    tie = True
    for row in mat:
        for ele in row:
            if (ele == ""):
                tie = False

    return {"res": False, "name": "nobody", "tie": tie}


def changePlayer():
    global activePalyer
    if (activePalyer == "X"):
        activePalyer = "O"
    else:
        activePalyer = "X"


def reset():
    global mat, buttons, finished, activePalyer
    restart = messagebox.askyesno(
        "RESTART", "Do you want to restart the game?")
    if (restart):
        mat = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
        buttons = new_Btns()
        finished = False
        activePalyer = "X"


def onClick(number):
    global activePalyer, finished, mat, buttons

    if(mat[int((number-(((number-1) % 3)+1))/3)
           ][int((number - 1) % 3)] == "" and not finished):
        buttons[int((number-(((number-1) % 3)+1))/3)
                ][int((number - 1) % 3)].config(text=activePalyer, font="times 12")
        mat[int((number-(((number-1) % 3)+1))/3)
            ][int((number - 1) % 3)] = activePalyer
        changePlayer()
        currPlayerbtn.config(text="Current Player: "+activePalyer)
        if (someoneWon()["res"]):
            finished = True
            messagebox.showinfo("Congratulations",
                                someoneWon()["name"] + " won the match!")
            reset()
        elif (someoneWon()["tie"]):
            messagebox.showinfo("Tie",
                                "This match was a TIE")
            reset()


root.resizable(False, False)
root.mainloop()

greet(True)
