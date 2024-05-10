import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno

window = tk.Tk()
window.title("J1T-midLA3")
window.geometry("1000x540")
window.resizable(width=False, height=False)

def Open():
    filepath = filedialog.askopenfilename(title="Open a file", filetypes=[("text files", "*.txt"), ("all files", "*.*")])
    file = open(filepath, 'r')
    print(file)
    for i in file:
        listbox.insert(tk.END, i)
    file.close()

def Save():
    file = filedialog.asksaveasfile(title="Save a file", filetypes=[("text files", "*.txt"), ("all files", "*.*")])
    get_items = list(listbox.get(0, tk.END))
    for i in get_items:
        file.write(f"{i}\n")
    file.close()

window_counter = 0

def Add():
    global window_counter
    if window_counter == 0:
        window_add = tk.Tk()
        window_add.title("Add")
        window_add.geometry("300x170")
        window_add.resizable(width=False, height=False)
        window_add.config(bg="#C7E1BA")

        lbl_add_prompt = tk.Label(master=window_add, text="Add an Item", font=("Cascadia Mono", 25), bg="#C7E1BA")
        lbl_add_prompt.pack()

        ent_item = tk.Entry(master=window_add, justify="center", font=("Helvetica", 18))
        ent_item.pack()

        def Insert():
            listbox.insert(tk.END, ent_item.get())

        def Close():
            global window_counter
            window_counter -= 1
            window_add.destroy()

        btn_add = tk.Button(master=window_add, text="Add to Listbox", command=Insert)
        btn_add.pack(pady=5)
        btn_exit = tk.Button(master=window_add, text="Done", command=Close)
        btn_exit.pack(pady=10)
        window_counter += 1
        window_add.protocol("WM_DELETE_WINDOW", Close)
        window_add.mainloop()
    else:
        showinfo(title="Notice", message="You can toggle one menu function only.")

def Delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

def Edit_Item():
    global window_counter
    if window_counter == 0:
        window_edit = tk.Tk()
        window_edit.title("Edit")
        window_edit.geometry("300x170")
        window_edit.resizable(width=False, height=False)
        window_edit.config(bg="#C7E1BA")

        lbl_add_prompt = tk.Label(master=window_edit, text="Edit an Item", font=("Cascadia Mono", 25), bg="#C7E1BA")
        lbl_add_prompt.pack()

        ent_item = tk.Entry(master=window_edit, justify="center", font=("Helvetica", 18))
        ent_item.pack()

        def Modify():
            try:
                listbox.insert(listbox.curselection(), ent_item.get())
                listbox.delete(listbox.curselection())
            except:
                showinfo(title="Notice", message="You can only edit one item at a time.")

        def Close():
            global window_counter
            window_counter -= 1
            window_edit.destroy()

        btn_add = tk.Button(master=window_edit, text="Edit Item", command=Modify)
        btn_add.pack(pady=5)
        btn_exit = tk.Button(master=window_edit, text="Done", command=Close)
        btn_exit.pack(pady=10)
        window_counter += 1
        window_edit.protocol("WM_DELETE_WINDOW", Close)
        window_edit.mainloop()
    else:
        showinfo(title="Notice", message="You can toggle one menu function only.")

def Program_Info():
    global window_counter
    if window_counter == 0:
        window_info = tk.Tk()
        window_info.title("Program Information")
        window_info.geometry("700x570")
        window_info.resizable(width=False, height=False)
        window_info.config(bg="white")

        msg_greet = tk.Message(master=window_info, width=650, text="\nGreetings, User. This is Adrian Paolo S. Follante, the programmer who created this application\n\n"
                                                                    "This application is about manipulating listbox: adding, deleteing, and editing items.\n\n"
                                                                   "In this application, there are three main menu options: File, Edit, Help\n\n"
                                                                   "Each main menu options have sub-options that manipulates the listbox.\n\n", justify="center", font=("Cascadia Code", 9), bg="white")

        msg_greet.pack()

        msg_howto = tk.Message(master=window_info, width=650, text="File:\n"
                                                                    "Open: Obtain the items from the selected file and insert them to the listbox\n"
                                                                    "Save: Saves current list data items to a file\n\n"
                                                                    "Edit:\n"
                                                                    "Add: Opens a mini window that allows the user to type specific item name and add that to the listbox\n"
                                                                    "Delete: Allows the user to remove selected items from the listbox\n"
                                                                    "Save: Opens a mini window that allows the user to edit a selected item\n\n"
                                                                    "Help:\n"
                                                                    "Program Info: Opens a mini window that shows the information about the application\n\n"
                                                                    "NOTE: You can only toggle 1 mini window at a time.\n\n", font=("Cascadia Code", 9), bg="white")
        msg_howto.pack()
        msg_farewell = tk.Message(master=window_info, width=650, text="If you have any more inquiries about the program you can email me using this address: c23-1576-274@uphsl.edu.ph\n"
                                                                      "Thank you for using my program.\n", justify="center", font=("Cascadia Code", 9), bg="white")
        msg_farewell.pack()

        def Close():
            global window_counter
            window_counter -= 1
            window_info.destroy()

        btn_close = tk.Button(master=window_info, text="OK", command=Close, font=("Helvetica", 10))
        btn_close.pack()

        window_counter += 1
        window_info.protocol("WM_DELETE_WINDOW", Close)
        window_info.mainloop()
    else:
        showinfo(title="Notice", message="You can toggle one menu function only.")

def Exit():
    global window_counter
    if window_counter != 0:
        showinfo(title="Notice", message="Close all mini windows before closing the program")
    else:
        answer = askyesno(title="Prompt", message="Are you sure you want to close the program?")
        if answer == True:
            window.destroy()
        else:   
            pass

menubar = tk.Menu(master=window)

File = tk.Menu(master=menubar, tearoff=0)
File.add_command(label="Open", command=Open)
File.add_command(label="Save", command=Save)
menubar.add_cascade(label="File", menu=File)


Edit = tk.Menu(master=menubar, tearoff=0)
Edit.add_command(label="Add", command=Add)
Edit.add_command(label="Delete", command=Delete)
Edit.add_command(label="Edit an Item", command=Edit_Item)
menubar.add_cascade(label="Edit", menu=Edit)


Help = tk.Menu(master=menubar, tearoff=0)
Help.add_command(label="Program info", command=Program_Info)
menubar.add_cascade(label="Help", menu=Help)

window.config(menu=menubar)

frm_main = tk.Frame(master=window, bg="#397249")
frm_main.pack(fill=tk.X)

frm_listbox = tk.Frame(master=frm_main, bg="#628B61")
frm_listbox.pack(pady=50)

scrollbar = tk.Scrollbar(master=frm_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(master=frm_listbox, width=50, yscrollcommand=scrollbar.set, font=("Helvetica", 20), bg="#F6E4CC", selectmode=tk.MULTIPLE)
listbox.pack(padx=5, pady=5)

scrollbar.config(command=listbox.yview)

btn_exit = tk.Button(master=frm_main, text="Exit Program", font=("Helvetica", 20), command=Exit)
btn_exit.pack(pady=20)

window.protocol("WM_DELETE_WINDOW", Exit)

window.mainloop()