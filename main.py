from tkinter import *
from tkinter import font
from tkinter import messagebox
import time


def main_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit PROD++ ?"):
        root.destroy()


root = Tk()
root.title("PROD++")
root.iconbitmap("logos//m.ico")
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", main_closing)
row_no = 1
boxes = []
tasks = []

hours = 0
minutes = 0
seconds = 0

running = False
row_s = 3
# function


def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Stopwatch?"):
        new1.destroy()


def on_closing_timer():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Timer?"):
        new3.destroy()


def on_closing_water():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Water Reminder?"):
        new6.destroy()


def on_closing_calc():
    screen.delete(0, END)
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Calculator?"):
        root_c.destroy()


def new_task():
    global row_no
    global b

    b = Text(
        new,
        width=30,
        height=2,
        borderwidth=4,
        font=("Bahnschrift Light ", 15),
        bg="#30110d",
        fg="#cd7700",
    )
    b.grid(row=row_no, columnspan=2, column=0,
           sticky=W, pady=(10, 2), padx=(10, 5))
    var = StringVar()
    apt = Checkbutton(
        new,
        variable=var,
        onvalue="ON",
        offvalue="OFF",
        borderwidth=0,
        bg="#F0B27A",
        fg="black",
    )

    apt.grid(row=row_no, column=1, sticky=E)
    apt.deselect()
    boxes.append(apt)
    tasks.append(b)
    row_no += 1
    pass


def all_done():
    for item in boxes:
        try:
            item.deselect()
        except Exception as e:
            pass
    # boxes.clear()
    print(tasks)
    for items in tasks:
        items.delete("1.0", "end")


number = 1


def todo():
    global new
    new = Toplevel()
    new.geometry("550x750")
    new.configure(bg="#F0B27A")
    new.iconbitmap("logos//todo.ico")
    new.resizable(width=False, height=False)

    add_task = Button(
        new,
        text="Add Task",
        font=("Arial", 20),
        borderwidth=4,
        relief=SOLID,
        width=25,
        command=new_task,
        bg="#210070",
        fg="yellow",
    ).grid(row=0, ipady=10, pady=(10, 0), sticky=W, column=0)
    finish = Button(
        new,
        text="All Done",
        font=("Bahnschrift SemiLight SemiConde", 15),
        borderwidth=1,
        bg="#e55437",
        fg="white",
        command=all_done,
    ).grid(row=0, padx=(10, 0), ipadx=10, ipady=10, sticky=E, column=1)


def stopwatchz():

    global new1
    new1 = Toplevel()
    new1.title("Stopwatch")
    # new1.geometry("615x210")
    new1.iconbitmap("logos//stopw.ico")
    new1.protocol("WM_DELETE_WINDOW", on_closing)
    new1.resizable(width=False, height=False)

    def start():
        # stopwatch_label.after(1000)
        global running
        if not running:

            update()
            running = True

    def pause():
        global running

        if running:
            stopwatch_label.after_cancel(update_time)
            running = False

    def reset():
        global running, hours, minutes, seconds
        if running:
            stopwatch_label.after_cancel(update_time)
            running = False
        hours, minutes, seconds = 0, 0, 0
        stopwatch_label.config(text="00:00:00")

    def update():
        global hours
        global minutes
        global seconds
        seconds += 1

        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0

        hour_s = f"{hours}" if hours > 9 else f"0{hours}"
        minute_s = f"{minutes}" if minutes > 9 else f"0{minutes}"
        second_s = f"{seconds}" if seconds > 9 else f"0{seconds}"

        stopwatch_label.config(text=f"{hour_s}:{minute_s}:{second_s}")
        global update_time

        update_time = stopwatch_label.after(1000, update)

    def lapse():
        global running, hours, minutes, seconds, number, row_s
        # print(row_s , end="*****************")
        a = Label(
            new1,
            text=f"#{number}      {hours}:{minutes}:{seconds}",
            font=("Arial", 20, "bold"),
        )
        a.grid(row=row_s, columnspan=4)

        # print(f"#{row_s}   {hours}:{minutes}:{seconds}")
        hours, minutes, seconds = 0, 0, 0
        number += 1
        row_s += 1
        pass

    # ***widgets****
    stopwatch_label = Label(new1, text="00:00:00",
                            font=("ubuntu", 80), borderwidth=10)
    stopwatch_label.grid(row=0, columnspan=5)

    start_z = Button(
        new1,
        text="Start",
        font=("Arial", 20),
        command=start,
        bg="#AAE629"
        # ).pack(side=LEFT, ipadx=20, ipady=20)
    ).grid(row=1, column=0, ipadx=15, ipady=5)
    pause_z = Button(
        new1,
        text="Pause",
        font=("Arial", 20),
        command=pause,
        bg="#FF0000"
        # ).pack(side=LEFT, ipadx=20, ipady=20)
    ).grid(row=1, column=1, ipadx=15, ipady=5)
    reset_z = Button(
        new1,
        text="Reset",
        font=("Arial", 20),
        command=reset,
        bg="#FFBF00"
        # ).pack(side=LEFT, ipadx=20, ipady=20)
    ).grid(row=1, column=2, ipadx=15, ipady=5)
    split_z = Button(
        new1,
        text="Lapse",
        font=("Arial", 20),
        command=lapse,
        bg="#ff66ff"
        # ).pack(side=LEFT, ipadx=20, ipady=20)
    ).grid(row=1, column=3, ipadx=15, ipady=5)
    close_z = Button(
        new1,
        text="Close",
        font=("Arial", 20),
        command=kill,
        bg="#26F5EA"
        # ).pack(side=LEFT, ipadx=20, ipady=20)
    ).grid(row=1, column=4, ipadx=15, ipady=5)
    pass


def kill():
    global new1, hours, minutes, seconds, running
    hours, minutes, seconds = 0, 0, 0
    running = False
    new1.destroy()
    pass


def notepad():

    new2 = Toplevel()
    new2.title("Notepad by PROD++")
    new2.iconbitmap("logos//note.ico")
    new2.resizable(width=False, height=False)
    a = Text(new2, height=15, width=60, font=("Cooper Black", 20))
    a.grid(row=0, column=0, sticky=N + S + W + E)
    a.configure(bg="#ffffcc", fg="black")


def show():

    messagebox.showinfo("Timer Countdown", "Time's Up")
    new3.destroy()
    pass


def update_timerz():
    global h, m, s

    try:

        temp = int(h) * 3600 + int(m) * 60 + int(s)
    except:
        print("Please input the right value")
    while temp > -1:

        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hs = f"{hours}" if hours > 9 else f"0{hours}"
        ms = f"{mins}" if mins > 9 else f"0{mins}"
        ss = f"{secs}" if secs > 9 else f"0{secs}"

        lab.config(text=f"{hs}:{ms}:{ss}")
        global update_time

        root.update()
        time.sleep(1)
        temp -= 1

        if temp == -1:
            show()


def timer_display():
    global new3, droph, dropm, drops, a1, a2, options_2, options_1, options, h, m, s, lab

    h = options.get()
    m = options_1.get()
    s = options_2.get()
    droph.destroy()
    dropm.destroy()
    drops.destroy()
    a1.destroy()
    a2.destroy()
    setz.destroy()
    settings.destroy()

    lab = Label(new3, text=f"{h}:{m}:{s}", font=(
        "Arial", 35, "bold"), bg="#42F0D7")
    lab.grid(row=1, columnspan=5, padx=40, ipadx=10)
    update_timerz()

    pass


def timerz():
    global new3, droph, dropm, drops, a1, a2, options, options_1, options_2, setz, settings
    new3 = Toplevel()
    new3.title("TImer by PROD++")
    new3.configure(bg="#42F0D7")
    new3.iconbitmap("logos//timer.ico")
    new3.protocol("WM_DELETE_WINDOW", on_closing_timer)
    new3.resizable(width=False, height=False)
    hours = [00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    minutes = [i for i in range(0, 61)]
    seconds = [i for i in range(0, 61)]

    settings = Label(
        new3, text="Set your desired time(HH:MM:SS) :", font=("arial", 20), bg="#42F0D7"
    )
    settings.grid(row=0, column=0, columnspan=5, sticky=W)

    options = IntVar()
    options.set(hours[0])
    droph = OptionMenu(new3, options, *hours)
    droph.grid(row=1, column=0, ipadx=30, pady=(10, 10), ipady=10)

    a1 = Label(new3, text=":", font=("arial", 20), bg="#42F0D7")
    a1.grid(row=1, column=1, pady=(10, 10))
    a2 = Label(new3, text=":", font=("arial", 20), bg="#42F0D7")
    a2.grid(row=1, column=3, pady=(10, 10))
    # a = Label(new3, text=":" , font=("arial" , 20)).grid(row=1 , column = 5)
    options_1 = IntVar()
    options_1.set(minutes[0])
    dropm = OptionMenu(new3, options_1, *minutes)
    dropm.grid(row=1, column=2, ipadx=30, pady=(10, 10), ipady=10)

    options_2 = IntVar()
    options_2.set(seconds[0])
    drops = OptionMenu(new3, options_2, *seconds)
    drops.grid(row=1, column=4, ipadx=30, pady=(10, 10), ipady=10)
    setz = Button(
        new3,
        text="Set",
        font=("Comicsans", 15),
        bg="#32FA12",
        fg="black",
        command=timer_display,
    )
    setz.grid(row=2, column=2, ipadx=30, ipady=10)

    pass


calc_done = True


def calc_func():
    global root_c, screen
    root_c = Toplevel()
    root_c.title("Calc by PROD++!")
    root_c.iconbitmap("logos//calc.ico")
    root_c.resizable(width=False, height=False)
    root_c.protocol("WM_DELETE_WINDOW", on_closing_calc)
    # root.iconbitmap('image.ico')

    screen = Entry(
        root_c,
        width=18,
        borderwidth=4,
        relief=GROOVE,
        font="Arial 20 bold",
        bg="black",
        fg="white",
    )
    screen.grid(row=0, column=0, columnspan=3, ipady=20)

    def myclick(num):
        global calc_done , math 
        if not calc_done:
            screen.delete(0, END)
            calc_done = True
            screen.insert(0, str(num))
            print(screen.get())
            math = "lol"
        else:
            a = screen.get()
            screen.delete(0, END)
            screen.insert(0, str(a) + str(num))

    def clear_screen():
        screen.delete(0, END)

    def add():
        global f_num
        global math
        math = "+"
        f_num = int(screen.get())
        screen.delete(0, END)

    def sub():
        global f_num
        global math
        math = "-"
        f_num = int(screen.get())
        screen.delete(0, END)

    def mul():
        global f_num
        global math
        math = "*"
        f_num = int(screen.get())
        screen.delete(0, END)

    def div():
        global f_num
        global math
        math = "/"
        f_num = int(screen.get())
        screen.delete(0, END)

    def equal():
        global calc_done
        if math == "+":
            s_num = int(screen.get())
            screen.delete(0, END)
            screen.insert(0, f"{str(f_num)}+{str(s_num)}={f_num + s_num}")
            calc_done = False

        elif math == "-":
            s_num = int(screen.get())
            screen.delete(0, END)
            screen.insert(0, f"{str(f_num)}-{str(s_num)}={f_num - s_num}")
            calc_done = False

        elif math == "*":
            s_num = int(screen.get())
            screen.delete(0, END)
            screen.insert(0, f"{str(f_num)}*{str(s_num)}={f_num * s_num}")
            calc_done = False

        elif math == "/":
            s_num = int(screen.get())
            screen.delete(0, END)
            screen.insert(0, f"{str(f_num)}/{str(s_num)}={f_num / s_num}")
            calc_done = False
        else :
            pass
    button_0 = Button(
        root_c,
        text="0",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(0),
        bg="black",
        fg="white",
    ).grid(row=4, column=0)
    button_1 = Button(
        root_c,
        text="1",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(1),
        bg="black",
        fg="white",
    ).grid(row=3, column=0)
    button_2 = Button(
        root_c,
        text="2",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(2),
        bg="black",
        fg="white",
    ).grid(row=3, column=1)
    button_3 = Button(
        root_c,
        text="3",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(3),
        bg="black",
        fg="white",
    ).grid(row=3, column=2)
    button_4 = Button(
        root_c,
        text="4",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(4),
        bg="black",
        fg="white",
    ).grid(row=2, column=0)
    button_5 = Button(
        root_c,
        text="5",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(5),
        bg="black",
        fg="white",
    ).grid(row=2, column=1)
    button_6 = Button(
        root_c,
        text="6",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(6),
        bg="black",
        fg="white",
    ).grid(row=2, column=2)
    button_7 = Button(
        root_c,
        text="7",
        padx=30,
        pady=13,
        font="A20al 18 bold",
        command=lambda: myclick(7),
        bg="black",
        fg="white",
    ).grid(row=1, column=0)
    button_8 = Button(
        root_c,
        text="8",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(8),
        bg="black",
        fg="white",
    ).grid(row=1, column=1)
    button_9 = Button(
        root_c,
        text="9",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=lambda: myclick(9),
        bg="black",
        fg="white",
    ).grid(row=1, column=2)

    button_add = Button(
        root_c,
        text="+",
        padx=30,
        pady=13,
        font="Arial 18 bold",
        command=add,
        bg="black",
        fg="#00ff00",
    ).grid(row=4, column=1)
    button_sub = Button(
        root_c,
        text="-",
        padx=33,
        pady=13,
        font="Arial 19 bold",
        command=sub,
        bg="black",
        fg="#00ff00",
    ).grid(row=5, column=0)
    button_mul = Button(
        root_c,
        text="*",
        padx=33,
        pady=13,
        font="Arial 19 bold",
        command=mul,
        bg="black",
        fg="#00ff00",
    ).grid(row=5, column=1)
    button_div = Button(
        root_c,
        text="/",
        padx=33,
        pady=13,
        font="Arial 19 bold",
        command=div,
        bg="black",
        fg="#00ff00",
    ).grid(row=5, column=2)

    button_eq = Button(
        root_c,
        text="=",
        padx=125,
        pady=15,
        font="Arial 18 bold",
        command=equal,
        bg="black",
        fg="white",
    ).grid(row=6, column=0, columnspan=3)
    button_clear = Button(
        root_c,
        text="C",
        padx=28,
        pady=13,
        font="Arial 18 bold",
        command=clear_screen,
        bg="black",
        fg="red",
    ).grid(row=4, column=2)

    pass


mins, secs = 0, 0
times = [i for i in range(1, 61)]


def noti():
    global new6
    new6 = Toplevel()
    new6.title("Water Reminder by PROD++")
    new6.iconbitmap("logos//water.ico")
    new6.resizable(width=False, height=False)
    new6.protocol("WM_DELETE_WINDOW", on_closing_water)
    # top = LabelFrame(root,text="top")
    top = LabelFrame(new6)
    top.grid(row=0, column=0)
    new6.configure(bg="#14B2E1")
    welcome_mess = Label(
        top,
        text="Welcome to Water Reminder by PROD++ !",
        borderwidth=3,
        font=("Saab", 20, "bold"),
        bg="#3C1A5B",
        fg="#FFF748",
    )
    welcome_mess.grid(row=1, column=0)

    # creating a Frame
    inputs = LabelFrame(new6, bg="#14B2E1")
    inputs.grid(
        row=1,
        column=0,
        columnspan=2,
        sticky=W,
    )

    # Label and Entry for name
    name = Label(
        inputs, text="Enter the name :", font=("ubuntu", 11, "bold"), bg="#14B2E1"
    ).grid(row=3, column=0, sticky=W)
    t = Entry(inputs, width=35)
    t.grid(row=3, column=1, sticky=W)

    # Label and Entry for message
    mess = Label(
        inputs, text="Enter the message :", font=("ubuntu", 11, "bold"), bg="#14B2E1"
    ).grid(row=4, column=0, sticky=W)
    m = Entry(inputs, width=35)
    m.grid(row=4, column=1)

    # Label and dropdown for interval
    interval = Label(
        inputs,
        text="Enter the interval(in minutes) :",
        font=("ubuntu", 11, "bold"),
        bg="#14B2E1",
    ).grid(row=5, column=0, sticky=W)
    options = IntVar()
    options.set(times[0])
    drop = OptionMenu(inputs, options, *times)
    drop.grid(row=5, column=1)

    def noti():
        a = t.get()
        b = m.get()
        c = options.get()
        global secs
        secs += 1
        # print(b)
        if secs == c * 60:
            messagebox.showwarning(f"Drink water {a}", f"{b}")
            secs = 0

        update_time = new6.after(1000, noti)

    cal = Button(
        new6,
        text="Start",
        bg="#1D1B1B",
        fg="#EC4D37",
        font="NewTimesRoman 13 bold",
        command=noti,
    )

    cal.grid(padx=5, pady=5, row=6, column=0, columnspan=2, ipadx=70, ipady=2)

    # ex = Button(new6, text="Cick to Exit!", command=new6.destroy).grid(
    #     row=7, column=0, columnspan=2
    # )
    pass


# *****************WIDGETS*******************
root.config(bg="#12a4d9")
welcome = Label(
    root,
    text="Welcome to PROD++ !",
    font=("New times roman ", 25, "bold"),
    bg="#12a4d9",
    fg="#322e2f",
)
welcome.grid(row=0, columnspan=2)

to_do_but = Button(
    root,
    text="To-Do list",
    font=("Saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=todo,
    bg="#e2d810",
    fg="#000000",
).grid(row=1, ipadx=88, columnspan=2, pady=(10, 0))

stopwatch_but = Button(
    root,
    text="Stopwatch",
    font=("Saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=stopwatchz,
    bg="#e2d810",
    fg="#000000",
).grid(row=2, ipadx=84, columnspan=2, pady=(20, 0))

timer_but = Button(
    root, text="Timer", font=("saab", 20), command=timerz, bg="#e2d810", fg="#000000"
).grid(row=3, ipadx=110, columnspan=2, pady=(20, 0))

calc_but = Button(
    root,
    text="Calculator",
    font=("saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=calc_func,
    bg="#e2d810",
    fg="#000000",
).grid(row=4, ipadx=85, columnspan=2, pady=(20, 0))

water_but = Button(
    root,
    text="Water Reminder",
    font=("saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=noti,
    bg="#e2d810",
    fg="#000000",
).grid(row=5, ipadx=50, columnspan=2, pady=(20, 0))

notepad_but = Button(
    root, text="Notes", font=("Saab", 20), command=notepad, bg="#e2d810", fg="#000000"
).grid(row=6, ipadx=110, columnspan=2, pady=(20, 10))


mainloop()
