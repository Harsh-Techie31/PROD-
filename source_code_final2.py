from cProfile import label
from platform import release
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
from tkinter import filedialog
import webbrowser
from dhooks import Webhook

def main_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit PROD++ ?"):
        root.destroy()


dark = 0


root = Tk()
root.withdraw()
root.geometry("720x400")
root.title("PROD++")


root.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\logo.ico")
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

welcome = Toplevel()
welcome.lift()
welcome.attributes('-topmost',True)
welcome.overrideredirect(True)
welcome.config(cursor="none")

window_x = int((welcome.winfo_screenwidth() / 2) - (920 / 2))
window_y = int((welcome.winfo_screenheight() / 2) - (600 / 2))

welcome.geometry(f"920x600+{str(window_x)}+{str(window_y)}")

image_bg = PhotoImage(master=welcome, file='logos//image.png')

label1 = Label(welcome, image=image_bg)
label1.place(x=0, y=0)


progress = Progressbar(welcome, orient=HORIZONTAL,
                       length=400, mode='determinate')

progress.pack(side=BOTTOM, pady=(10, 110))

# **********************************************************************
# Function responsible for the updation
# of the progress bar value
# change = 20

# for i in range(5):
#     progress['value'] = change
#     root.update_idletasks()
#     time.sleep(1)
#     change += 20


# def bar():
# progress['value'] = 20
# root.update_idletasks()
# time.sleep(1)

# progress['value'] = 40
# root.update_idletasks()
# time.sleep(1)

# progress['value'] = 50
# root.update_idletasks()
# time.sleep(1)

# progress['value'] = 60
# root.update_idletasks()
# time.sleep(1)

# progress['value'] = 80
# root.update_idletasks()
# time.sleep(1)
#     # progress['value'] = 100
# *******************************************************************
def bar():
    progress['value'] += 20
    root.update_idletasks()
    welcome.after(1000 , bar)


root.after(10, bar)
root.after(6500, welcome.destroy)


def welcome_screen():
    root.deiconify()


root.after(6550, welcome_screen)


# Genral function

calc_open = False
timer_running = False
stopwatch_running = False
todo_running = False
water_running = False
note_open = False


def on_closing_stopwatch():
    global stopwatch_running, running, seconds, number
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Stopwatch?"):
        new1.destroy()
        stopwatch_running = False
        running = False
        seconds = 0
        number = 1


def on_closing_timer():
    global ran, timer_running
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Timer?"):
        new3.destroy()
        timer_running = False
        # new.destroy()
        # ran = False


def on_closing_timer_a():
    global ran, timer_running
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Timer?"):
        # new3.destroy()
        new_timer.destroy()
        ran = False
        timer_running = False


def on_closing_water():
    global water_running, secs, cal
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Water Reminder?"):
        water_running = False
        new6.destroy()
        secs = 0

        cal.configure(state=NORMAL)


def on_closing_todo():
    global todo_running
    if messagebox.askokcancel("Quit", "Are you sure you want to quit TO-DO list?"):
        todo_running = False
        tasks.clear()
        new.destroy()


def on_closing_calc():
    global calc_open
    screen.delete(0, END)
    if messagebox.askokcancel("Quit", "Are you sure you want to quit Calculator?"):
        calc_open = False
        root_c.destroy()


# def closing_note():
#     global  note_open
#     try :
#         f = open("notepad.txt", "r")

#         if a.get("1.0", "end-1c") == f.read():
#             if messagebox.askokcancel("Quit", "Are you sure you want to close Notepad?"):
#                 f.close()
#                 new2.destroy()
#                 note_open = False
#         else:
#             f.close()

#             if messagebox.askyesno("Notepad by PROD++", "Would you like to save your changes ?"):
#                 f_new = open('notepad.txt', "w")
#                 f_new.write(str(a.get("1.0", "end-1c")))
#                 new2.destroy()
#                 f_new.close()
#                 note_open = False

#             else:
#                 f_new1 = open('notepad.txt' , "w")
#                 f_new1.write(str(old_text))
#                 new2.destroy()
#                 f_new1.close()
#                 note_open = False

#     except:
#         try :
#             f_t = open("notepad.txt", "a+")

#             if a.get("1.0", "end-1c") == f_t.read():
#                 if messagebox.askokcancel("Quit", "Are you sure you want to close Notepad?"):
#                     f_t.close()
#                     new2.destroy()
#                     note_open = False
#             else:
#                 f_t.close()

#                 if messagebox.askyesno("Notepad by PROD++", "Would you like to save your changes ?"):
#                     f_new_t = open('notepad.txt', "a+")
#                     f_new_t.write(str(a.get("1.0", "end-1c")))
#                     new2.destroy()
#                     f_new_t.close()
#                     note_open = False

#                 else:
#                     f_new1_t = open('notepad.txt' , "a+")
#                     f_new1_t.write(str(old_text))
#                     new2.destroy()
#                     f_new1_t.close()
#                     note_open = False

#         except :
#             messagebox.showerror("Notepad by PROD++","CLosing Notepad due to a error :/")
#             new2.destroy()
#             note_open = False

def main_dark():
    global root
    root.configure(bg="#000000")
    to_do_but.configure(bg="#D26CD0", fg="#000000")
    stopwatch_but.configure(bg="#D26CD0", fg="#000000")
    timer_but.configure(bg="#D26CD0", fg="#000000")
    calc_but.configure(bg="#D26CD0", fg="#000000")
    notepad_but.configure(bg="#D26CD0", fg="#000000")
    water_but.configure(bg="#D26CD0", fg="#000000")
    # dark_label.configure(bg="#000000", fg="white")
    # space.configure(bg="#000000")
    # welcome.configure(fg="#72DCDC", bg="black")
    welcome.configure(fg="#72DCDC", bg="#d3144d")


def main_light():
    global root
    root.configure(bg="#E35F5F")
    to_do_but.configure(bg="#82E0AA", fg="#000000")
    stopwatch_but.configure(bg="#82E0AA", fg="#000000")
    timer_but.configure(bg="#82E0AA", fg="#000000")
    calc_but.configure(bg="#82E0AA", fg="#000000")
    notepad_but.configure(bg="#82E0AA", fg="#000000")
    water_but.configure(bg="#82E0AA", fg="#000000")
    # dark_label.configure(bg="#E35F5F", fg="black")
    # space.configure(bg="#E35F5F")
    welcome.configure(bg="#023047", fg="#FFF200")


def dark_theme():
    global dark
    # no.config(bg="white")
    # yes.config(bg="#CC88DC")
    # yes.config(bg="#0071BC")
    dark = 1
    main_dark()


def light_theme():
    global dark
    # no.config(bg="#0071BC")
    # yes.config(bg="white")
    dark = 0
    main_light()

# functions for the respective features


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

    # b.configure(bg="#6efffa" , fg="black")
    b.configure(bg="#63e8e8", fg="black")
    apt.configure(bg="#f5d2d2", fg="black")

    if dark:
        b.configure(bg="#CC88DC", fg="black")
        apt.configure(bg="#2A2828", fg="black")


def all_done():
    for item in boxes:
        try:
            item.deselect()
        except Exception as e:
            pass
    # boxes.clear()
    # print(tasks)
    for items in tasks:
        try:
            # print(tasks.index(items))
            items.delete("1.0", "end")
        except EXCEPTION as e:
            # print("fail")
            print(e)


number = 1


def todo():
    global new, todo_running
    if todo_running:
        messagebox.showwarning("TO-DO list by PROD++",
                               "TO-DO List is already running!")
    else:
        todo_running = True
        new = Toplevel()
        new.geometry("550x750")
        new.configure(bg="#F0B27A")
        new.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\todo.ico")
        new.resizable(width=False, height=False)
        new.protocol("WM_DELETE_WINDOW", on_closing_todo)
        new.title("ToDo-List by PROD++")

        add_task = Button(
            new,
            text="Add Task",
            font=("Arial", 20),
            borderwidth=4,
            relief=SOLID,
            width=25,
            command=new_task,
            bg="#210070",
            fg="yellow")
        add_task.grid(row=0, ipady=10, pady=(10, 0), sticky=W, column=0)
        finish = Button(
            new,
            text="All Done",
            font=("Bahnschrift SemiLight SemiConde", 15),
            borderwidth=1,
            bg="#e55437",
            fg="white",
            command=all_done)
        finish.grid(row=0, padx=(10, 0), ipadx=10,
                    ipady=10, sticky=E, column=1)

        new.configure(bg="#f5d2d2")
        add_task.configure(bg="#fa749f", fg="black")
        finish.configure(bg="#e90e4f", fg="black")
        # .configure()
        # .configure()

        if dark:
            new.configure(bg="#2A2828")
            add_task.configure(bg="#67C3C3", fg="black")
            finish.configure(bg="#63C5DA", fg="black")
            # .configure
            # .configure


def stopwatchz():

    global new1, stopwatch_running
    if stopwatch_running:
        messagebox.showwarning("Stopwatch by PROD++",
                               "Stopwatch is already running!")
    else:
        stopwatch_running = True
        new1 = Toplevel()
        new1.title("Stopwatch")
        # new1.geometry("615x210")
        new1.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\stopw.ico")
        new1.protocol("WM_DELETE_WINDOW", on_closing_stopwatch)
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

        def laps():
            global running, hours, minutes, seconds, number, row_s
            # print(row_s , end="*****************")
            h_s = f"{hours}" if hours > 9 else f"0{hours}"
            m_s = f"{minutes}" if minutes > 9 else f"0{minutes}"
            s_s = f"{seconds}" if seconds > 9 else f"0{seconds}"
            a = Label(
                new1,
                text=f"#{number}      {h_s}:{m_s}:{s_s}",
                font=("Arial", 20, "bold"),
            )
            a.grid(row=row_s, columnspan=4)

            if dark:
                a.configure(bg="#1F1F78", fg="#77C4D1")

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
            bg="#AAE629")
        # ).pack(side=LEFT, ipadx=20, ipady=20)
        start_z.grid(row=1, column=0, ipadx=25, ipady=5)
        pause_z = Button(
            new1,
            text="Pause",
            font=("Arial", 20),
            command=pause,
            bg="#FF0000")
        # ).pack(side=LEFT, ipadx=20, ipady=20)
        pause_z.grid(row=1, column=1, ipadx=25, ipady=5)
        reset_z = Button(
            new1,
            text="Reset",
            font=("Arial", 20),
            command=reset,
            bg="#FFBF00")
        # ).pack(side=LEFT, ipadx=20, ipady=20)
        reset_z.grid(row=1, column=2, ipadx=25, ipady=5)
        split_z = Button(
            new1,
            text="Laps",
            font=("Arial", 20),
            command=laps,
            bg="#ff66ff")
        # ).pack(side=LEFT, ipadx=20, ipady=20)
        split_z.grid(row=1, column=3, ipadx=35, ipady=5)
        # close_z = Button(
        #     new1,
        #     text="Close",
        #     font=("Arial", 20),
        #     command=kill,
        #     bg="#26F5EA"
        #     # ).pack(side=LEFT, ipadx=20, ipady=20)
        # ).grid(row=1, column=4, ipadx=15, ipady=5)
        pass
        if dark:
            new1.configure(bg="#1F1F78")
            stopwatch_label.configure(bg="#1F1F78", fg="#77C4D1")
            start_z.configure(bg="#90C8EF", fg="#000000")
            pause_z.configure(bg="#90C8EF", fg="#000000")
            reset_z.configure(bg="#90C8EF", fg="#000000")
            split_z.configure(bg="#90C8EF", fg="#000000")
# def kill():
#     global new1, hours, minutes, seconds, running , stopwatch_running
#     hours, minutes, seconds = 0, 0, 0
#     running = False
#     new1.destroy()
#     stopwatch_running = False

# def saving():
#     # print(new2.winfo_height() ,new2.winfo_width())
#     # try:
#     #     f_saving = open("notepad.txt", "w")
#     #     f_saving.write(str(a.get("1.0", "end-1c")))
#     #     f_saving.close()
#     # except :
#     #     try :
#     #         f_saved = open("C:\\Program Files (x86)\\PROD++\\notepad.txt" , "w")
#     #         f_saved.write(str(a.get("1.0", "end-1c")))
#     #         f_saved.close()

#     #     except Exception as error:
#     #         print(error)
#     #         messagebox.showerror("Notepad by PROD++",f"Cannot access notepad due to corrupt installation of the Software .\
#     #                 Please perform a clean Re-installation !")
#     try:
#         f_saving = open("notepads.txt", "w")
#         f_saving.write(str(a.get("1.0", "end-1c")))
#         f_saving.close()
#     except :
#         # print("oooof")
#         try :
#             f_saved = open("notepad.txt" , "r+")
#             f_saved.write(str(a.get("1.0", "end-1c")))
#             f_saved.close()

#         except Exception as error:
#             print(error)
#             messagebox.showerror("Notepad by PROD++",f"Cannot access notepad due to corrupt installation of the Software .\
#                     Please perform a clean Re-installation !")


note_image_bg_light = PhotoImage(file='logos//light_theme.png')
note_image_bg_dark = PhotoImage(file='logos//dark_theme.png')

notepad_open = True


def closing_feature():
    global note_open
    note_open = False
    features.destroy()
    new2.destroy()


def close_notepad():
    global tool, notepad_open
    if notepad_open:
        if not tool:
            closing_open()
        else:
            closing_new()


def closing_open():
    global note_file, data, notepad_open, note_file_name, note_open, file_opened
    notepad_open = False

    note_file_closing = open(note_file_name, "r")
    text = note_file_closing.read()
    note_file_closing.close()
    # print("closing open triggered")
    if text == a.get("1.0", "end-1c"):
        if messagebox.askyesno("Close Notepad", "Are you sure you want to close notepad?"):
            a.delete("1.0", END)
            new2.destroy()
            note_open = False
            file_opened = False

    else:
        if messagebox.askyesno("Close Notepad", "Would u like to save your changes ?"):
            note_file_a = open(note_file_name, "w")
            note_file_a.write(str(a.get("1.0", "end-1c")))
            note_file_a.close()
            new2.destroy()
            note_open = False
            file_opened = False
        else:
            new2.destroy()
            note_open = False
            file_opened = False


def closing_new():
    global note_open, new_file_open, notepad_open
    # print("triggered closing new")
    notepad_open = False
    new2.destroy()
    note_open = False
    new_file_open = False


note_saved = False


def saving_custom():
    global note_saved
    # if not note_saved:
    if tool:
        note_saved = True
        saving_new()
    else:
        note_saved = True
        saving_open()


def saving_open():
    print("triggered saving open")
    global note_file_name
    note_file_x = open(note_file_name, "w")
    note_file_x.write(str(a.get("1.0", "end-1c")))
    note_file_x.close()


def saving_new():
    global note_open, new_file_open, tool
    # tool = 1
    new_file = filedialog.asksaveasfile(defaultextension='.txt',
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*"),
                                        ])
    if new_file == '':
        features.destroy()
        new2.destroy()
        note_open = False
        new_file_open = False
        return
    new_filetext = str(a.get(1.0, "end-1c"))
    new_file.write(new_filetext)
    new_file.close()
    closing_new()
    pass


def open_files():
    global note_open, file_opened, tool, note_file, data, note_file_name
    tool = 0
    note_file_name = filedialog.askopenfilename(defaultextension='.txt',
                                                filetypes=[
                                                    ("Text file", ".txt"),
                                                    ("HTML file", ".html"),
                                                    ("All files", ".*"),
                                                ])

    if note_file_name == '':
        features.destroy()
        new2.destroy()
        note_open = False
        file_opened = False
        return
    note_file = open(note_file_name, "r")

    # filetext = str(note.get(1.0,END))
    # filetext = input("Enter some text I guess: ") //use this if you want to use console window
    # file.write(filetext)
    data = note_file.read()
    a.insert("1.0", data)
    note_file.close()
    pass


tool = 0
file_opened = False
new_file_open = False


def open_file():
    global file_opened, notepad_open
    features.destroy()
    new2.deiconify()
    notepad_open = True
    if not file_opened:
        file_opened = True
        open_files()
    pass


def new_file():
    global new_file_open, notepad_open, tool
    tool = 1
    features.destroy()
    new2.deiconify()
    notepad_open = True
    if not new_file_open:
        new_file_open = True


def notepad():
    global a, new2, note_open, old_text, features
    if note_open:
        messagebox.showwarning("Notepad by PROD++", "Notepad already running!")
    else:
        note_open = True

        features = Toplevel()
        features.geometry("950x460")
        features.protocol("WM_DELETE_WINDOW", closing_feature)

        if not dark:
            dark_bg = Label(features, image=note_image_bg_light)
            dark_bg.place(x=0, y=0, height=460, width=950)
            # dark_bg.pack(expand=YES , fill=BOTH)
            open_note_b = Button(features, text="Open a existing file", font=(
                "helevetica", 35), bg="#fff200", fg="#88001b", command=open_file)
            open_note_b.pack(side=LEFT, padx=(25, 10))

            new_note_b = Button(features, text="Create a New File", font=(
                "helevetica", 35), bg="#a6fde9", fg="#001ac6", command=new_file)
            new_note_b.pack(side=LEFT)
        else:
            dark_bg = Label(features, image=note_image_bg_dark)
            dark_bg.place(x=0, y=0, height=460, width=950)
            # dark_bg.pack(expand=YES , fill=BOTH)
            open_note_b = Button(features, text="Open a existing file", font=(
                "helevetica", 35), bg="#ffbde0", fg="#000000", command=open_file)
            open_note_b.pack(side=LEFT, padx=(25, 10))

            new_note_b = Button(features, text="Create a New File", font=(
                "helevetica", 35), bg="#c4ff0e", fg="#074614", command=new_file)
            new_note_b.pack(side=LEFT)

        new2 = Toplevel()
        new2.title("Notepad by PROD++")
        new2.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\note.ico")
        new2.resizable(width=False, height=False)
        new2.protocol("WM_DELETE_WINDOW", close_notepad)
        new2.withdraw()

        w = Label(new2, text="Notepad by PROD++", font=("new times roman",
                                                        25, "bold"), width=40)
        w.grid(row=0, column=0,  ipadx=45, ipady=6)

        sav = Button(new2, text="Save", font=(
            "Arial", 20, "bold"), command=saving_custom)
        sav.grid(row=0, column=1, sticky=E,  ipadx=55)

        a = Text(new2, height=20, width=80, font=("Cooper Black", 16))
        a.grid(row=1, column=0, sticky=N + S + W + E, columnspan=2)
        a.configure(bg="#ffffcc", fg="black")

    old_text = a.get("1.0", "end-1c")
    w.configure(bg="#8effc7", fg="black")
    sav.configure(bg="#ff929d", fg="#d20000")

    if dark:
        new2.configure(bg="#344955")
        a.configure(bg="#344955", fg="#7CF0F0")
        sav.configure(bg="#ff863f")
        w.configure(bg="#ECBD1F")


def show():
    global ran, timer_running
    ran = False
    new_timer.destroy()
    messagebox.showinfo("Timer Countdown", "Time's Up")
    timer_running = False
    pass


ran = False


def get_hour():
    global h_f, options

    if options.get() == 0:
        a = f"start**{h_f.get('1.0','end-1c')}**end"
        print(a)
        # print(type(h_f.get("1.0","end-1c")))
        try:
            hour_final = int(h_f.get("1.0", "end-1c"))

        except:
            hour_final = 0
        h_f.delete("1.0", END)
    else:
        hour_final = int(options.get())

    return hour_final


def get_min():
    global m_f, options_1

    if options_1.get() == 0:
        try:
            min_final = int(m_f.get("1.0", "end-1c"))
            m_f.delete("1.0", "end-1c")
        except:
            min_final = 0

    else:
        min_final = int(options_1.get())

    return min_final


def get_sec():
    global s_f, options_2

    if options_2.get() == 0:
        try:
            sec_final = int(s_f.get("1.0", "end-1c"))
            s_f.delete("1.0", "end-1c")

        except:
            sec_final = 0

    else:
        sec_final = int(options_2.get())

    return sec_final
# trial = 1
# def set_time():

#     global h_f , m_f , s_f , trial


#     # print(options.get())
#     # print(type(options.get()))
#     # print("*",get_hour(),"*")
#     a =get_hour()
#     b =get_min()
#     c =get_sec()


#     h_done = a if a>9 else f"0{a}"
#     m_done = b if b>9 else f"0{b}"
#     s_done = c if c>9 else f"0{c}"


#     h_f.insert(END , h_done)
#     m_f.insert(END , m_done)
#     s_f.insert(END , s_done)

#     if trial != 1 :
#         h_f.delete("1.0",END)
#         m_f.delete("1.0",END)
#         s_f.delete("1.0",END)

# #     h_f.delete("1.0","2.0")
# #     m_f.delete("1.0","2.0")
# #     s_f.delete("1.0","2.0")
    # trial += 1

def timer_display():
    # get_hour()
    global h, m, s, temp, ran, lab, new_timer, h_f, m_f, s_f
    if ran:
        pass
    else:
        ran = True
        # h = int(h_f.get("1.0","2.0"))
        # m = int(m_f.get("1.0","2.0"))
        # s = int(s_f.get("1.0","2.0"))

        h = int(get_hour())
        m = int(get_min())
        s = int(get_sec())

        new3.destroy()
        new_timer = Toplevel()
        new_timer.title("TImer by PROD++")
        new_timer.configure(bg="#f1dbf2")
        new_timer.iconbitmap(
            "C:\\Program Files (x86)\\PROD++\\logos\\timer.ico")
        new_timer.protocol("WM_DELETE_WINDOW", on_closing_timer_a)
        new_timer.resizable(width=False, height=False)
        lab = Label(new_timer, text=f"{h}:{m}:{s}", font=(
            "Arial", 35, "bold"), bg="#f1dbf2", fg="black")
        lab.grid(row=1, columnspan=5, padx=40, ipadx=10)
        try:
            temp = int(h) * 3600 + int(m) * 60 + int(s)
        except Exception as e:
            pass
        running_timer()

        if dark:
            new_timer.configure(bg="#2B1052")
            lab.configure(bg="#2B1052", fg="white")


def running_timer():
    global temp, lab
    mins, secs = divmod(temp, 60)

    hours = 0
    if mins > 60:
        hours, mins = divmod(mins, 60)

    hs = f"{hours}" if hours > 9 else f"0{hours}"
    ms = f"{mins}" if mins > 9 else f"0{mins}"
    ss = f"{secs}" if secs > 9 else f"0{secs}"

    lab.config(text=f"{hs}:{ms}:{ss}")
    temp -= 1
    new3.after(1000, running_timer)

    if temp == -1:
        show()
        return
    pass


def timerz():
    global new3, droph, dropm, drops, a1, a2, options, options_1, options_2, setz, settings, timer_running, h_f, m_f, s_f
    if timer_running:
        messagebox.showwarning("Timer by PROD++", "Timer is already running!")
    else:
        timer_running = True

        new3 = Toplevel()
        new3.title("TImer by PROD++")
        new3.configure(bg="#42F0D7")
        new3.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\timer.ico")
        new3.protocol("WM_DELETE_WINDOW", on_closing_timer)
        new3.resizable(width=False, height=False)
        hours = [00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        minutes = [i for i in range(0, 61)]
        seconds = [i for i in range(0, 61)]

        settings = Label(
            new3, text="Set your desired time(HH:MM:SS) :", font=("arial", 20), bg="#42F0D7"
        )
        settings.grid(row=0, column=0, columnspan=8)

        inputs = LabelFrame(new3, bg="#42F0D7", borderwidth=0)
        inputs.grid(row=1, column=0, columnspan=8)

        h_f = Text(inputs, width=2, height=1, font=("arial", 30, "bold"))
        h_f.pack(side=LEFT, padx=(10, 4))
        # h_f.grid(row=1 ,column=0 , padx=(10,4))

        options = IntVar()
        options.set(hours[0])
        droph = OptionMenu(inputs, options, *hours)
        droph.pack(side=LEFT, ipadx=30, pady=(10, 10), ipady=10)

        a1 = Label(inputs, text=":", font=("arial", 20), bg="#42F0D7", width=2)
        # a1.grid(row=1, column=2, pady=(5, 5), sticky=W , padx=(5,0))
        a1.pack(side=LEFT)

        m_f = Text(inputs, width=2, height=1, font=("arial", 30, "bold"))
        m_f.pack(side=LEFT, padx=(10, 4))

        options_1 = IntVar()
        options_1.set(minutes[0])
        dropm = OptionMenu(inputs, options_1, *minutes)
        dropm.pack(side=LEFT, ipadx=30, pady=(10, 10), ipady=10)

        a2 = Label(inputs, text=":", font=("arial", 20), bg="#42F0D7")
        a2.pack(side=LEFT)

        s_f = Text(inputs, width=2, height=1, font=("arial", 30, "bold"))
        s_f.pack(side=LEFT, padx=(10, 4))

        options_2 = IntVar()
        options_2.set(seconds[0])
        drops = OptionMenu(inputs, options_2, *seconds)
        drops.pack(side=LEFT, ipadx=30, pady=(10, 10), ipady=10)

        s_timer = Button(
            new3,
            text="Start Timer",
            font=("Comicsans", 20),
            bg="#32FA12",
            fg="black",
            command=timer_display,
        )
        s_timer.grid(row=2, column=2, ipadx=30, columnspan=4)

        pass

        new3.configure(bg="#f1dbf2")
        droph.configure(bg="#f2b2d6", fg="black")
        dropm.configure(bg="#f2b2d6", fg="black")
        drops.configure(bg="#f2b2d6", fg="black")
        settings.configure(fg="black", bg="#f1dbf2")
        inputs.configure(bg="#f1dbf2")
        a1.configure(bg="#f1dbf2", fg="black")
        a2.configure(bg="#f1dbf2", fg="black")
        h_f.configure(bg="#ff7bc5", fg="black")
        m_f.configure(bg="#ff7bc5", fg="black")
        s_f.configure(bg="#ff7bc5", fg="black")
        # s_timer.configure(bg="#ca1b3e",fg="#f1dbf2")
        s_timer.configure(fg="#e03a15", bg="#ecff20")

        if dark:
            new3.configure(bg="#2B1052")
            droph.configure(bg="#D890E5", fg="black")
            dropm.configure(bg="#D890E5", fg="black")
            drops.configure(bg="#D890E5", fg="black")
            droph["menu"].configure(bg="#2B1052", fg="white")
            dropm["menu"].configure(bg="#2B1052", fg="white")
            drops["menu"].configure(bg="#2B1052", fg="white")
            settings.configure(fg="#fff200", bg="#2B1052")
            inputs.configure(bg="#2B1052")
            a1.configure(bg="#2B1052", fg="#fff200")
            a2.configure(bg="#2B1052", fg="#fff200")
            h_f.configure(bg="#d643f1", fg="black")
            m_f.configure(bg="#d643f1", fg="black")
            s_f.configure(bg="#d643f1", fg="black")
            # s_timer.configure(bg="#ca1b3e",fg="#f1dbf2")
            s_timer.configure(fg="black", bg="#53B8AC")


calc_done = True


def calc_func():
    global root_c, screen, calc_open
    if not calc_open:
        root_c = Toplevel()
        root_c.title("Calc by PROD++!")
        root_c.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\calc.ico")
        root_c.resizable(width=False, height=False)
        root_c.protocol("WM_DELETE_WINDOW", on_closing_calc)
        # root.iconbitmap('C:\\Program Files (x86)\\PROD++\\logos\\image.ico')

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
        calc_open = True

        def myclick(num):
            global calc_done, math
            if not calc_done:
                screen.delete(0, END)
                calc_done = True
                screen.insert(0, str(num))
                # print(screen.get())
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
            else:
                pass
        button_0 = Button(
            root_c,
            text="0",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(0),
            bg="black",
            fg="white")
        button_0.grid(row=4, column=0)
        button_1 = Button(
            root_c,
            text="1",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(1),
            bg="black",
            fg="white")
        button_1.grid(row=3, column=0)
        button_2 = Button(
            root_c,
            text="2",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(2),
            bg="black",
            fg="white")
        button_2.grid(row=3, column=1)
        button_3 = Button(
            root_c,
            text="3",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(3),
            bg="black",
            fg="white")
        button_3.grid(row=3, column=2)
        button_4 = Button(
            root_c,
            text="4",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(4),
            bg="black",
            fg="white")
        button_4.grid(row=2, column=0)
        button_5 = Button(
            root_c,
            text="5",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(5),
            bg="black",
            fg="white")
        button_5.grid(row=2, column=1)
        button_6 = Button(
            root_c,
            text="6",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(6),
            bg="black",
            fg="white")
        button_6.grid(row=2, column=2)
        button_7 = Button(
            root_c,
            text="7",
            padx=30,
            pady=13,
            font="A20al 18 bold",
            command=lambda: myclick(7),
            bg="black",
            fg="white")
        button_7.grid(row=1, column=0)
        button_8 = Button(
            root_c,
            text="8",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(8),
            bg="black",
            fg="white")
        button_8.grid(row=1, column=1)
        button_9 = Button(
            root_c,
            text="9",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=lambda: myclick(9),
            bg="black",
            fg="white")
        button_9.grid(row=1, column=2)

        button_add = Button(
            root_c,
            text="+",
            padx=30,
            pady=13,
            font="Arial 18 bold",
            command=add,
            bg="black",
            fg="#00ff00")
        button_add.grid(row=4, column=1)
        button_sub = Button(
            root_c,
            text="-",
            padx=33,
            pady=13,
            font="Arial 19 bold",
            command=sub,
            bg="black",
            fg="#00ff00")
        button_sub.grid(row=5, column=0)
        button_mul = Button(
            root_c,
            text="*",
            padx=33,
            pady=13,
            font="Arial 19 bold",
            command=mul,
            bg="black",
            fg="#00ff00")
        button_mul.grid(row=5, column=1)
        button_div = Button(
            root_c,
            text="/",
            padx=33,
            pady=13,
            font="Arial 19 bold",
            command=div,
            bg="black",
            fg="#00ff00")
        button_div.grid(row=5, column=2)

        button_eq = Button(
            root_c,
            text="=",
            padx=125,
            pady=15,
            font="Arial 18 bold",
            command=equal,
            bg="black",
            fg="white")
        button_eq.grid(row=6, column=0, columnspan=3)
        button_clear = Button(
            root_c,
            text="C",
            padx=28,
            pady=13,
            font="Arial 18 bold",
            command=clear_screen,
            bg="black",
            fg="red")
        button_clear.grid(row=4, column=2)

        pass
    else:
        messagebox.showwarning("Calculator by PROD++",
                               "Calculator is Already Running !")
    if not dark:
        button_0.configure(bg="#F5D8D8", fg="#000000")
        button_1.configure(bg="#F5D8D8", fg="#000000")
        button_2.configure(bg="#F5D8D8", fg="#000000")
        button_3.configure(bg="#F5D8D8", fg="#000000")
        button_4.configure(bg="#F5D8D8", fg="#000000")
        button_5.configure(bg="#F5D8D8", fg="#000000")
        button_6.configure(bg="#F5D8D8", fg="#000000")
        button_7.configure(bg="#F5D8D8", fg="#000000")
        button_8.configure(bg="#F5D8D8", fg="#000000")
        button_9.configure(bg="#F5D8D8", fg="#000000")
        button_eq.configure(bg="#2258A5", fg="#FFFFFF")
        button_clear.configure(bg="#F5D8D8", fg="#EF3B1A")
        button_div.configure(bg="#F5D8D8", fg="#430242")
        button_mul.configure(bg="#F5D8D8", fg="#430242")
        button_sub.configure(bg="#F5D8D8", fg="#430242")
        button_add.configure(bg="#F5D8D8", fg="#430242")
        screen.configure(bg="#F5D8D8", fg="#000000")


secs = 0
times = [i for i in range(1, 61)]

# def get_interval():
#     global options_g , gap

#     try :
#         interval = int(gap.get("1.0","2.0"))

#     except :

#         if options_g.get() == 1 :
#             try:
#                 interval = int(gap.get("1.0","end-1c"))
#             except:
#                 interval = 1
#         else :
#             interval = options_g.get()
#     # print(int(gap.get("1.0" , "end-1c")))
#     return interval
# trial = 1


def noti():
    global trial, t, message_entry, water_yes, water_no, cal
    cal.configure(state=DISABLED)
    a = t.get()
    b = message_entry.get()
    # if trial == 1 :
    # c = get_interval()
    c = options_g.get()
    # print(get_interval())
    print(f"*{c}*")
    global secs
    secs += 1
    # print(c)
    print(secs)
    if secs == c * 60:
        messagebox.showwarning(f"Drink water {a}", f"{b}")
        secs = 0

    update_time = new6.after(1000, noti)
    # trial += 1

    water_yes.configure(bg="#ffadce", fg="#e81543")
    water_no.configure(bg="white", fg="black")

    if dark:
        water_yes.configure(fg="#f2bea0", bg="#3f49e8")
        water_no.configure(bg="white", fg="black")


def notify():
    global new6, water_running, gap, options_g, t, message_entry, water_yes, water_no, cal
    if water_running:
        messagebox.showwarning("Water Reminder by PROD++",
                               "Water Reminder is already running!")
    else:
        water_running = True
        new6 = Toplevel()
        new6.title("Water Reminder by PROD++")
        new6.iconbitmap("C:\\Program Files (x86)\\PROD++\\logos\\water.ico")
        new6.resizable(width=False, height=False)
        new6.protocol("WM_DELETE_WINDOW", on_closing_water)
        # top = LabelFrame(root,text="top")
        top = LabelFrame(new6, borderwidth=0)
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
        inputs = LabelFrame(new6, bg="#14B2E1", borderwidth=0)
        inputs.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=W,
        )

        # Label and Entry for name
        name = Label(
            inputs, text="Enter the name :", font=("ubuntu", 11, "bold"), bg="#14B2E1")
        name.grid(row=3, column=0, sticky=W)

        t = Entry(inputs, width=35, text=("arial", 25))
        t.grid(row=3, column=1, sticky=W, columnspan=2)

        # Label and Entry for message
        mess = Label(
            inputs, text="Enter the message :", font=("ubuntu", 11, "bold"), bg="#14B2E1")
        mess.grid(row=4, column=0, sticky=W)
        message_entry = Entry(inputs, width=35, text=("arial", 15))
        message_entry.grid(row=4, column=1, columnspan=2)

        # Label and dropdown for interval
        interval = Label(
            inputs,
            text="Enter the interval(in minutes) :",
            font=("ubuntu", 11, "bold"),
            bg="#14B2E1")
        interval.grid(row=5, column=0, sticky=W)

        # gap = Text(inputs , width=3 , height=1, font=("Helevetic" , 17))
        # gap.grid(row=5 , column=1)

        options_g = IntVar()
        options_g.set(times[0])
        drop = OptionMenu(inputs, options_g, *times)
        drop.grid(row=5, column=2, sticky=W)

        cal = Button(
            new6,
            text="Start",
            bg="#1D1B1B",
            fg="#EC4D37",
            font="NewTimesRoman 13 bold",
            command=noti,
        )

        cal.grid(padx=5, pady=5, row=6, column=0,
                 columnspan=3, ipadx=70, ipady=2)

        status = LabelFrame(new6, borderwidth=0, bg="#14B2E1")
        status.grid(row=7, column=0, columnspan=3)

        work = Label(status, text="Running ? : ",
                     font=("arial", 15), bg="#14B2E1")

        work.pack(side=LEFT, padx=(0, 20))
        # Checkbutton1 = IntVar()
        # Checkbutton2 = IntVar(value=1)

        # Button1 = Checkbutton(status, text = "YES",
        #               variable = Checkbutton1)

        # Button2 = Checkbutton(status, text = "NO",
        #               variable = Checkbutton2)
        # Button2.select()
        # Button1.pack(side=LEFT)
        # Button2.pack(side=LEFT , padx=(20,0))

        water_yes = Label(status, text="YES", borderwidth=1,
                          relief="solid", font=("arial", 12))
        water_yes.pack(side=LEFT, padx=(10, 0), ipadx=11, ipady=2)

        water_no = Label(status, text="NO", borderwidth=1, relief="solid", font=(
            "arial", 12), bg="#ffadce", fg="#e81543")
        water_no.pack(side=LEFT, padx=(0, 0), ipadx=13, ipady=2)

        t.configure(bg="#ffda91", fg="black")
        message_entry.configure(bg="#ffda91", fg="black")
        # gap.configure(bg="#ffda91" , fg="black")
        drop.configure(bg="#57ffb6", fg="black")
        drop["menu"].configure(bg="#14B2E1", fg="black")

        if dark:
            new6.configure(bg="#1D1515")
            inputs.configure(bg="#1D1515")
            status.configure(bg="#1D1515")
            t.configure(bg="#ff99f3", fg="#000000")
            message_entry.configure(bg="#ff99f3", fg="#000000")
            # gap.configure(bg="#ff99f3" , fg="#000000")
            name.configure(bg="#1D1515", fg="#F8E756")
            mess.configure(bg="#1D1515", fg="#F8E756")
            interval.configure(bg="#1D1515", fg="#F8E756")
            drop["menu"].configure(bg="#1D1515", fg="white")
            drop.configure(bg="#ffeeab", fg="black")
            cal.configure(bg="#6BE59C", fg="#000000")
            # welcome_mess.configure(bg="#1D1515",fg="#F7C728")
            welcome_mess.configure(bg="#c2fb58", fg="#ec1c24")
            work.configure(bg="#1D1515", fg="white")
            water_no.configure(bg="#3f49e8", fg="#f2bea0")


# *****************WIDGETS*******************

hook = Webhook('https://discord.com/api/webhooks/942631995270385774/y9SJc3KreaLrVo4uaiYIuUTRs9-VfZ_bhG3SgrmM6GjE3Gs1IRAL2-uFlM5_EdOG1Nf3')
suggest_hook = Webhook('https://discord.com/api/webhooks/942632768729415691/-ugufGktstm7zxKJg8a_1Ty1T3ThCGbvM7trOm1am75zr-4CPBItt1QG-RVHO2w_9849')
# Menu Bar 
def callback(url):
    webbrowser.open_new(url)
def openLink():
    webbrowser.open('https://drive.google.com/file/d/1phR01b1gnDbgpA9s6o_AB1P-PGy7Vn3f/view?usp=sharing', new=2)
def donothing():
    pass
def sent():
    hook.send(a.get("1.0","end-1c"))
    bugging.destroy()
def info():
    infoScreen = Toplevel()
    infoScreen.config(bg="#baffbf")
    infoScreen.title('About Us')
    a = Label(infoScreen , text = "The software PROD++ has been developed by Harsh and designed by Shweta Agrawala." , font=("arial",15,"bold"),fg="#88001b",bg="#baffbf")
    a.grid(row=0 , column=0 , columnspan= 3 , sticky=W , pady=5)
    # b = Label(infoScreen , text="." , font=("arial",15,"bold"),fg="red")
    # b.grid(row=1 , column= 0 , columnspan= 3 , sticky=W)
    b = Label(infoScreen , text="You can contact us through the following social media :" , font=("arial",15,"bold"),fg="#88001b",bg="#baffbf")
    b.grid(row=2 , column= 0 , columnspan= 3 , sticky=W , pady=5)
    insta = Label(infoScreen , text="   Instagram : " , font=("ubuntu" , 14, "bold"),fg="#000000",bg="#baffbf").grid(row=3 , column=0 , pady=7 )
    instah = Label(infoScreen , text="Harsh" , borderwidth=3 , relief=GROOVE , font=("morrison" , 14),bg="#fac4ff",fg="#0633b0")
    instah.grid(row=3 , column=1 , ipadx=5 , ipady=2 , pady=7)
    instas = Label(infoScreen , text="Shweta" , borderwidth=3 , relief=GROOVE, font=("morrison" , 14),bg="#fac4ff",fg="#0633b0")
    instas.grid(row=3 , column=2 , ipadx=5 , ipady=2 , pady=7)
    dc = Label(infoScreen , text="Discord : ", font=("ubuntu" , 14, "bold") ,fg="#000000",bg="#baffbf").grid(row=4 , column=0)
    dch = Label(infoScreen , text="Harsh" , borderwidth=3 , relief=GROOVE, font=("morrison" ,14),bg="#fac4ff",fg="#0633b0")
    dch.grid(row=4 , column=1 , ipadx=5 , ipady=2 , pady=5)
    dcs = Label(infoScreen , text="Shweta" , borderwidth=3 , relief=GROOVE, font=("morrison" , 14),bg="#fac4ff",fg="#0633b0")
    dcs.grid(row=4 , column=2 , ipadx=5 , ipady=2 , pady=5)

    instah.bind("<Button-1>", lambda e: callback("https://www.instagram.com/checkmateforfun/"))
    instas.bind("<Button-1>", lambda e: callback("https://www.instagram.com/agrawalashweta/"))
    dch.bind("<Button-1>", lambda e: callback("https://discord.com/users/688669143029121034"))
    dcs.bind("<Button-1>", lambda e: callback("https://discord.com/users/847414665280487455"))

def reportBug():
    global a , bugging
    bugging = Toplevel(bg="#d3ecfc")
    Label(bugging , text="Please report the bug :" , font=("arial" , 20),bg="#fff5b7",fg="#000000").grid(row=0 , column=0, columnspan= 3,ipadx=160)
    a = Text(bugging , width=50 , height=10 , font=("arial", 16 ),bg="#d3ecfc",fg="#1C3BAC")
    a.grid(row=1 , column=0 , columnspan= 3)

    # Button(bugging , text="Done" , bg="#F6C3FF" , fg="black" , font=("arial", 14 , 'bold') , command=sent).grid(row=2 , column=1, ipadx= 40)
    Button(bugging , text="Done" , bg="#ffacac" , fg="#f40031" , font=("arial", 14 , 'bold') , command=sent).grid(row=2 , column=1, ipadx= 40)
    pass

def sents():
    suggest_hook.send(sa.get("1.0","end-1c"))
    suggesting.destroy()
def suggestion():
    global sa , suggesting
    suggesting = Toplevel(bg="#d3ecfc")
    Label(suggesting , text="Please enter your suggestions below :" , font=("arial" , 20),bg="#fff5b7",fg="#000000").grid(row=0 , column=0, columnspan= 3,ipadx=70)
    sa = Text(suggesting , width=50 , height=10 , font=("arial", 16 ),bg="#d3ecfc",fg="#1C3BAC")
    sa.grid(row=1 , column=0 , columnspan= 3)

    Button(suggesting , text="Done" , bg="#ffacac" , fg="#f40031"  , font=("arial", 14 , 'bold') , command=sents).grid(row=2 , column=1, ipadx= 40)
    pass

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)

settingmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="Theme", menu=settingmenu)
settingmenu.add_command(label="Dark",command=dark_theme)
settingmenu.add_command(label="Light",command=light_theme)

helpmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Text Guide",command=openLink)
helpmenu.add_command(label="Video Guide",command=donothing)

aboutmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="Contact Us", menu=aboutmenu)
aboutmenu.add_command(label="Report-A-Bug",command=reportBug)
# aboutmenu.add_separator()
aboutmenu.add_command(label="Suggestions",command=suggestion)
# aboutmenu.add_separator()
aboutmenu.add_command(label="About Us",command=info)


# root.config(bg="#12a4d9")
root.configure(bg="#E35F5F")
welcome = Label(
    root,
    text="Welcome to PROD++ ",
    font=("New times roman ", 35, "bold"),
    # bg="#12a4d9",
    # bg="#CC88DC",
    # bg="#E35F5F",
    fg="#fff200",
    borderwidth=2,
    relief=SOLID,
    bg="#023047"
)
welcome.grid(row=0, columnspan=2, sticky=E, ipadx=120)

to_do_but = Button(
    root,
    text="To-Do list",
    font=("Saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=todo,
    bg="#82E0AA",
    fg="#000000")
to_do_but.grid(row=1, column=0, ipadx=88, pady=(40, 0))

stopwatch_but = Button(
    root,
    text="Stopwatch",
    font=("Saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=stopwatchz,
    bg="#82E0AA",
    fg="#000000")
stopwatch_but.grid(row=1, ipadx=84, column=1, pady=(40, 0) , sticky=W)

timer_but = Button(
    root, text="Timer", font=("saab", 20), command=timerz, bg="#82E0AA", fg="#000000")
timer_but.grid(row=2, ipadx=110, column=0, pady=(40, 0))

calc_but = Button(
    root,
    text="Calculator",
    font=("saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=calc_func,
    bg="#82E0AA",
    fg="#000000")
calc_but.grid(row=2, ipadx=85, column=1, pady=(40, 0) , sticky=W)

water_but = Button(
    root,
    text="Water Reminder",
    font=("saab", 20),
    # borderwidth=4,
    # relief=SOLID,
    command=notify,
    bg="#82E0AA",
    fg="#000000")
water_but.grid(row=3, ipadx=50, column=0, pady=(40, 0))

# notepad_but = Button(
#     root, text="Notes", font=("Saab", 20), command=notepad, bg="#e2d810", fg="#000000"
# ).grid(row=6, ipadx=110, columnspan=2, pady=(20, 0))
notepad_but = Button(
    root, text="Notes", font=("Saab", 20), command=notepad, bg="#82E0AA", fg="#000000")
notepad_but.grid(row=3, ipadx=110, column=1, pady=(40, 0) , sticky=W)

# dark_label = Label(root, text="Theme :", font=(
#     "helevetica", 10, "bold"), bg="#E35F5F")
# dark_label.grid(row=7, column=0, columnspan=1, sticky=E)

# space = LabelFrame(root, width=40, bg="#E35F5F")
# space.grid(row=7, column=1, columnspan=1, sticky=W, padx=(10, 0), pady=(8, 10))

# yes = Button(space, text="Dark", font=(
#     "arial", 10, "bold"), command=dark_theme)
# yes.pack(side=LEFT, ipadx=20)
# no = Button(space, text="Light", bg="#0071BC", font=(
#     "arial", 10, "bold"), command=light_theme)
# no.pack(side=LEFT, ipadx=25)

mainloop()
