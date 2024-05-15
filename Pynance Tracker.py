# Import all the necessary modules to use its components.
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkinter import filedialog

window_counter = 0

# Function that toggles the "≡" menu located at the top left side of the window. Clicking this
# pops up a frame that contains the "Generate Report", "About", and "Exit" buttons.
def toggle_menu():
    global dd
    global category_dd
    global category_options
    #function that untoggles and hides the menu frame and reverts its icon and function
    def untoggle_menu():
        btn_menu_toggle.config(text="≡", command=toggle_menu)
        frm_menu_options.destroy()

    frm_menu_options = tk.Frame(root, bg="#74977E", width=250, height=root.winfo_height(),
                                highlightbackground="#294936", highlightthickness=5)
    frm_menu_options.place(x=-5, y=95)
    btn_menu_toggle.config(text="X", command=untoggle_menu)
    #Function that opens a seperate window containing summary of income and expenses
    def report():
        global window_counter
        if window_counter == 0:
            window_counter += 1
            window_report = tk.Tk()
            window_report.title("PYNANCE REPORT")
            window_report.geometry("900x450")
            window_report.resizable(width=False, height=False)

            frm_report = tk.Frame(window_report, height=90, bg="#294936")
            frm_report.pack(fill="x")

            lbl_rep = tk.Label(window_report, text="Pynance Tracker Report", bg="#294936", fg="white",
                               font=("Garamond", 28, "bold"))
            lbl_rep.place(x=55, y=25)

            date_rep = tk.Label(window_report, text=datetime.now().strftime("%B %d, %Y"), bg="#294936", fg="white",
                                font=("Garamond", 22, "bold"))
            date_rep.place(x=680, y=30)

            frm_main = tk.Frame(window_report, bg="#EDEBD7", height=550, width=900)
            frm_main.pack(pady=0)

            columns = ("DATE", "CATEGORY", "ITEM", "AMOUNT")

            frm_tree = tk.Frame(window_report, bg="#294936")
            frm_tree.pack(pady=5, padx=5, fill="both", expand=True)

            expenses_tree = ttk.Treeview(window_report, columns=columns, show="headings")
            expenses_tree.pack(fill="both", expand=True)
            expenses_tree.place(x=50, y=120)

            if os.path.exists("Pynance.txt"):
                expenses_tree.delete(*expenses_tree.get_children())
                with open("Pynance.txt", "r") as file:
                    for i, line in enumerate(file):
                        values = line.strip().split(",")
                        if len(values) == 4:
                            date, category, item, amount = values
                            amount = float(amount)
                            if i % 2 == 0:
                                expenses_tree.insert("", tk.END, values=(date, category, item, f'₱ {amount}'),
                                                     tags=('even',))
                            else:
                                expenses_tree.insert("", tk.END, values=(date, category, item, f'₱ {amount}'),
                                                     tags=('odd',))

            for col in columns:
                expenses_tree.heading(col, text=col)

            expenses_tree.tag_configure('even', background='#BDDBC9')
            expenses_tree.tag_configure('odd', background='#ffffff')
            #Function that shows the items under the selected category from the optionmenu widget.
            def show_items():
                selected_category = dd.get()
                expenses_tree.delete(*expenses_tree.get_children())

                if selected_category and selected_category != "Category":

                    if os.path.exists("Pynance.txt"):
                        total_expense = 0
                        total_income = 0
                        expenses_tree.delete(*expenses_tree.get_children())
                        with open("Pynance.txt", "r") as file:
                            for line in file:
                                values = line.strip().split(",")
                                if len(values) == 4:
                                    date, category, item, amount = values
                                    amount = float(amount)
                                    if item == "Add Income":
                                        amount = float(amount)
                                        total_income += amount
                                    if selected_category == category:
                                        expenses_tree.insert("", tk.END, values=(date, category, item, f'₱ {amount}'))
                                        total_expense += amount

                                    total_income = float(total_income)
                                    if total_income >= 0:
                                        remaining_income = total_income - total_expense
                                        if remaining_income >= 0:
                                            remaining.config(text=f"Remaining Income: ₱{remaining_income:.2f}", font=("Arial", 9, "bold"))
                                        else:
                                            remaining.config(text=f"Exceeded Income: ₱{-remaining_income:.2f}", font=("Arial", 9, "bold"))
                        income_total.config(text=f"Total Income: ₱{total_income:.2f}", font=("Arial", 9, "bold"))
                        amount_total.config(text=f"Total Amount: ₱{total_expense:.2f}", font=("Arial", 9, "bold"))
                else:
                    messagebox.showerror("Error", "Please select a category to view!")

            #Function that reveals all recorded items regardless of category.
            def all_items():
                if os.path.exists("Pynance.txt"):
                    total_expense = 0
                    total_income = 0
                    expenses_tree.delete(*expenses_tree.get_children())
                    with open("Pynance.txt", "r") as file:
                        for i, line in enumerate(file):
                            values = line.strip().split(",")
                            if len(values) == 4:
                                date, category, item, amount = values
                                if item == "Add Income":
                                    tag = 'income_row'
                                else:
                                    tag = 'expense_row'
                                expenses_tree.insert("", tk.END, values=(date, category, item, f'₱ {amount}'), tags=(tag,))
                                if item != "Add Income":
                                    amount = float(amount)
                                    total_expense += amount
                                elif item == "Add Income":
                                    amount = float(amount)
                                    total_income += amount

                                total_income = float(total_income)
                                if total_income >= 0:
                                    remaining_income = total_income - total_expense
                                    if remaining_income >= 0:
                                        remaining.config(text=f"Remaining Income: ₱{remaining_income:.2f}", font=("Arial", 9, "bold"))
                                    else:
                                        remaining.config(text=f"Exceeded Income: ₱{-remaining_income:.2f}", font=("Arial", 9, "bold"))

                income_total.config(text=f"Total Income: ₱{total_income:.2f}", font=("Arial", 9, "bold"))
                amount_total.config(text=f"Total Amount: ₱{total_expense:.2f}", font=("Arial", 9, "bold"))
                expenses_tree.tag_configure('income_row', foreground='red')
                expenses_tree.tag_configure('expense_row', foreground='black', background="#BDDBC9")

            dd = tk.StringVar()
            dd.set("Category")
            category_dd_report = tk.OptionMenu(window_report, dd, *category_options)
            category_dd_report.place(x=200, y=395)
            category_dd_report.config(font=("Helvetica", "11"))

            select_category_lbl = tk.Label(window_report, text="Select Category:", bg="#EDEBD7", font=("Helvetica", 11))
            select_category_lbl.place(x=80, y=400)

            update_button = tk.Button(window_report, text="View Items", command=show_items)
            update_button.place(x=265, y=400)

            view_all = tk.Button(window_report, text="View All Items", command=all_items)
            view_all.place(x=630, y=400)

            other_frm = tk.Frame(frm_main, height=900, bg="#294936", relief=tk.RAISED, borderwidth=2)
            other_frm.place(x=50, y=255, width=802)

            income_total = tk.Label(other_frm, text="Total Income: ", bg="#294936", fg="white", font=("Arial", 9, "bold"))
            income_total.grid(row=0, column=0, padx=10, pady=5)

            amount_total = tk.Label(other_frm, text="Total Amount: ", bg="#294936", fg="white", font=("Arial", 9, "bold"))
            amount_total.grid(row=0, column=1, padx=10, pady=5)

            remaining = tk.Label(other_frm, text="Remaining Income: ", bg="#294936", fg="white", font=("Arial", 9, "bold"))
            remaining.grid(row=0, column=2, padx=10, pady=5)

            other_frm.columnconfigure(0, weight=1)
            other_frm.columnconfigure(1, weight=1)
            other_frm.columnconfigure(2, weight=1)

            export_button = tk.Button(window_report, text="Export All Items", command=export_items)
            export_button.place(x=750, y=400)

            all_items()
            #function that exits the separate window.
            def exit_report():
                global window_counter
                window_counter -= 1
                window_report.destroy()

            window_report.protocol("WM_DELETE_WINDOW", exit_report)

            window_report.mainloop()
        else:
            messagebox.showerror(title="Error", message="You can only open a pop-up window one one at a time")

    #Function that opens a messagebox and shows information about the application
    def about():
        messagebox.showinfo(title="About", message="Greetings, User! We are Group 2 from section J1T who created this program.\n"
                                                   "We would like to express our gratitude for using our application 'Pynance Tracker.'\n"
                                                   "We are honored to provide service that aids in managing financial endavors.\n"
                                                   "If you have any inquiries, you can send email to this email address:\n"
                                                   "c23-1576-274@uphsl.edu.ph")
    #function that destroys and ends the main program
    def exit():
        global window_counter
        if window_counter == 0:
            root.destroy()
        else:
            messagebox.showerror(title="Error", message="Close all pop-up windows before closing the application")

    btn_generate_report = tk.Button(frm_menu_options, text="Generate Report", bg="#74977E", fg="white",
                                    font=("Garamond", 18, "bold"),
                                    bd=0, activebackground="#74977E", activeforeground="white", command=report)
    btn_generate_report.place(x=10, y=50)

    btn_about = tk.Button(frm_menu_options, text="About", bg="#74977E", fg="white", font=("Garamond", 18, "bold"), bd=0,
                          activebackground="#74977E", activeforeground="white", command=about)
    btn_about.place(x=10, y=150)

    btn_exit = tk.Button(frm_menu_options, text="Exit", bg="#74977E", fg="white", font=("Garamond", 18, "bold"), bd=0,
                         activebackground="#74977E", activeforeground="white", command=exit)
    btn_exit.place(x=10, y=250)

    btn_menu_toggle.config(text="X", command=untoggle_menu)

# Function that adds an item to the .txt file when the "Add Item" button is clicked.
# This also ensures that all the inputs of the user are correct.
def add_item():
    def add_update():
        add_button.config(text="Add Item", fg="black")
        add_button.place(x=522, y=170)

    category = dd.get()
    item = item_entry.get()
    amount = amount_entry.get()
    date = datetime.now().strftime("%Y-%m-%d - %H:%M")

    if category != "Category" and item:
        try:
            amount = float(amount)
            if amount >= 0:
                with open("Pynance.txt", "a") as file:
                    file.write(f"{date},{category},{item},{amount}\n")
                status_label.config(text="Item added successfully!", fg="green")
                status_label.place(x=670, y=170)
                dd.set("Category")
                item_entry.delete(0, tk.END)
                amount_entry.delete(0, tk.END)
                view_items()
                add_update()
            else:
                messagebox.showerror("Error", "Please enter a positive number!")
        except ValueError:
            messagebox.showerror("Error", "Please only put numbers in the Amount entry!")
    else:
        messagebox.showerror("Error", "Please complete all the fields properly!")

# Function that edits the details of the item selected on the treeview and also edits the details in txt file.
def edit_item():
    selected_item = expenses_tree.selection()
    if selected_item:
        item_text = expenses_tree.item(selected_item, "values")
        if item_text:
            date, category, item, amount = item_text
            dd.set(category)
            item_entry.insert(0, item)
            amount_entry.insert(0, amount)

            with open("Pynance.txt", "r") as file:
                lines = file.readlines()
            with open("Pynance.txt", "w") as file:
                for line in lines:
                    if f"{date},{category},{item},{amount}" not in line.strip():
                        file.write(line)

            status_label.config(text="Editing item...", fg="blue")
            status_label.place(x=700, y=170)
            add_button.config(text="Update Item", fg="blue")
            add_button.place(x=515, y=170)
        else:
            status_label.config(text="Invalid item format!", fg="red")
    else:
        messagebox.showerror("Error", "Please select an item to edit!")

# Function that deletes the selected item in the treeview and from the txt file.
def delete_item():
    selected_item = expenses_tree.selection()
    if selected_item:
        item_text = expenses_tree.item(selected_item, "values")
        if item_text:
            date, category, item, amount = item_text
            with open("Pynance.txt", "r") as file:
                lines = file.readlines()
            with open("Pynance.txt", "w") as file:
                for line in lines:
                    if f"{date},{category},{item},{amount}" not in line.strip():
                        file.write(line)
            status_label.config(text="Item deleted successfully!", fg="green")
            status_label.place(x=660, y=170)
            view_items()
        else:
            status_label.config(text="Invalid item format!", fg="red")
    else:
        messagebox.showerror("Error", "Please select an item to delete!")

# Function that gets the inputted values from the txt file and displays them to the treeview.
# This also calculates and displays the total amount of the inputted amounts by the user.
def view_items():
    global expenses_tree
    if os.path.exists("Pynance.txt"):
        total_expense = 0
        total_income = 0
        expenses_tree.delete(*expenses_tree.get_children())
        with open("Pynance.txt", "r") as file:
            for i, line in enumerate(file):
                values = line.strip().split(",")
                if len(values) == 4:
                    date, category, item, amount = values
                    if item == "Add Income":
                        tag = 'income_row'
                    else:
                        tag = 'expense_row'
                    expenses_tree.insert("", tk.END, values=(date, category, item, amount), tags=(tag,))
                    if item != "Add Income":
                        amount = float(amount)
                        total_expense += amount
                    elif item == "Add Income":
                        amount = float(amount)
                        total_income += amount

        total_label.config(text=f"Total Income: ₱{total_income:.2f}", font=("Garamond", 15, "bold"))
    else:
        total_label.config(text="No items recorded.")
        expenses_tree.delete(*expenses_tree.get_children())

    if os.path.exists("Pynance.txt"):
        try:
            total_income = float(total_income)
            if total_income >= 0:
                remaining = total_income - total_expense
                if remaining >= 0:
                    budget_status.config(text=f"Remaining Income: ₱{remaining:.2f}", fg="green")
                else:
                    budget_status.config(text=f"Exceeded Income: ₱{-remaining:.2f}", fg="red")
        except ValueError:
            pass

    expenses_tree.tag_configure('income_row', foreground='red')
    expenses_tree.tag_configure('expense_row', foreground='black', background="#BDDBC9")

# Function that adds the inputted budget to the txt file and calculates the remaining or exceeded budget
# of the user and displays it.
def add_income():
    global expenses_tree
    budget_input = budget_entry.get()
    income_date = datetime.now().strftime("%Y-%m-%d - %H:%M")
    income_category = "Income"
    income_item = "Add Income"

    if budget_input:
        try:
            budget_input = float(budget_input)
            with open("Pynance.txt", "a") as file:
                file.write(f"{income_date},{income_category},{income_item},{budget_input}\n")
        except ValueError:
            messagebox.showerror("Error", "Please only put numbers in the Income entry!")

    if os.path.exists("Pynance.txt"):
        expenses_tree.delete(*expenses_tree.get_children())
        with open("Pynance.txt", "r") as file:
            for line in file:
                values = line.strip().split(",")
                if len(values) == 4:
                    date, category, item, amount = values
                    amount = float(amount)
                    expenses_tree.insert("", tk.END, values=(date, category, item, amount))

    view_items()

# Exports the items in the treeview and saves it as a txt file.
def export_items():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write("Date,Category,Item,Amount\n")
            for item in expenses_tree.get_children():
                values = expenses_tree.item(item, "values")
                line = ",".join(values) + "\n"
                file.write(line)
        messagebox.showinfo("Export", "Items exported successfully!")

# Function that reads the categories in the txt file and append them to the list of category options.
def read_category():
    category_options.clear()
    if os.path.exists("categories.txt"):
        with open("categories.txt", "r") as file:
            categories = file.readlines()
            for category in categories:
                category_options.append(category.strip())
    else:
        with open("categories.txt", "w") as file:
            initial_categories = ["Food", "Transportation", "Bills"]
            for category in initial_categories:
                file.write(category + "\n")
            category_options.extend(initial_categories)
    update_option_menu()

# Function that clears the categories in the option menu and updates it with the new list of categories.
def update_option_menu():
    menu = category_dd["menu"]
    menu.delete(0, "end")
    for category in category_options:
        menu.add_command(label=category, command=tk._setit(dd, category))

# Function that adds the category to the txt file and creates the "add category" window.
def add_category():
    def add_option():
        new_category = add_category_ent.get()
        if new_category and new_category not in category_options:
            category_options.append(new_category)
            dd.set(new_category)
            messagebox.showinfo("Success", f"Category '{new_category}' added successfully!")
            with open("categories.txt", "a") as file:
                file.write(new_category + "\n")
            category_window.destroy()
            update_option_menu() 
        else:
            messagebox.showerror("Error", "Please enter a valid category!")

    category_window = tk.Toplevel(root)
    category_window.title("Add Category")

    add_category_label = tk.Label(category_window, text="Enter Category:", font=("Helvetica", "11"))
    add_category_label.pack()

    add_category_ent = tk.Entry(category_window, font=("Helvetica", "11"), justify="center")
    add_category_ent.pack(padx=10)

    add_category_btn = tk.Button(category_window, text="Add Category", command=add_option)
    add_category_btn.pack(pady=10)
# Function that requires the user close all pop-up windows first before exiting.
def exit():
    global window_counter
    if window_counter == 0:
        root.destroy()
    else:
        messagebox.showerror(title="Error", message="Close all pop-up windows before closing the application")

# Function that creates the log-in window to add the name of the user to menubar frame.
def login():
    global window_counter
    if window_counter == 0:
        window_counter += 1
        window_login = tk.Tk()
        window_login.title("Pynance Tracker")
        window_login.geometry("350x170")
        window_login.resizable(False, False)
        window_login.config(bg="#294936")

        def exit():
            global window_counter
            window_counter -= 1
            window_login.destroy()

        def add_user():
            global window_counter
            username = ent_username.get()
            if username != "":
                lbl_menu.config(text=f"{username}'s Pynance Tracker")
                btn_login_user.destroy()
                messagebox.showinfo(title="Log in", message="Log in successful")
                window_counter -= 1
                window_login.destroy()
            else:
                messagebox.showerror(title="Log in", message="Log in failed")

        frm_login = tk.Frame(window_login, bg="#294936")

        lbl_app_title = tk.Label(frm_login, text="Log into Pynance Tracker", font=("Garamond", 20, 'bold'), bg="#294936", fg="white")
        lbl_app_title.grid(row=0, column=0, columnspan=2, pady=10)

        lbl_username = tk.Label(frm_login, text="Username:", font=("Helvetica", 15), bg="#294936", fg="white")
        lbl_username.grid(row=2, column=0, pady=5, padx=5)
        ent_username = tk.Entry(frm_login)
        ent_username.grid(row=2, column=1, pady=5, padx=5)

        btn_password = tk.Button(frm_login, text="Log in", font=("Helvetica", 11), command=add_user)
        btn_password.grid(row=4, column=0, pady=20, columnspan=2)

        frm_login.pack()

        window_login.protocol("WM_DELETE_WINDOW", exit)

        window_login.mainloop()
    else:
        messagebox.showerror(title="Error", message="You can only open a pop-up window one one at a time")

# Creates the main window and sets its title and size.
root = tk.Tk()
root.title("Pynance Tracker")
root.geometry("900x550")
root.resizable(False, False)

# Menubar Frame
frm_menubar = tk.Frame(root, height=100, bg="#294936")
frm_menubar.pack(fill="x")

btn_menu_toggle = tk.Button(frm_menubar, text="≡", bg="#294936", fg="white", font=("Helvetica", 30, "bold"), bd=0,
                            activebackground="#294936", activeforeground="white", command=toggle_menu)
btn_menu_toggle.place(x=0, y=10)

# Title Label and Login Button
lbl_menu = tk.Label(frm_menubar, text="Pynance Tracker", bg="#294936", fg="white", font=("Garamond", 28, "bold"))
lbl_menu.place(x=55, y=25)
btn_login_user = tk.Button(frm_menubar, text="Log In", bg="#294936", fg="white", font=("Garamond", 12, "bold"), command=login)
btn_login_user.place(x=340, y=35)
date_menu = tk.Label(frm_menubar, text=datetime.now().strftime("%B %d, %Y"), bg="#294936", fg="white",
                     font=("Garamond", 22, "bold"))
date_menu.place(x=680, y=30)

# Frames
frm_main = tk.Frame(root, bg="#EDEBD7", height=550, width=900)
frm_main.pack(pady=0)
frm_preview = tk.Frame(frm_main, bg="#294936")
frm_preview.place(relx=0.5, rely=0.5, anchor="center")

# Tree Frame
frm_tree = tk.Frame(frm_preview, bg="#294936")
frm_tree.pack(pady=5, padx=5, fill="both", expand=True)
scr_tree = tk.Scrollbar(frm_tree)
scr_tree.pack(side=tk.RIGHT, fill=tk.Y)

# Creates the Budget Label and Entry.
budget_label = tk.Label(root, text="Income:", bg="#EDEBD7", font=("Helvetica", "11"))
budget_label.place(x=90, y=115)
budget_entry = tk.Entry(root)
budget_entry.place(x=90, y=140)

# Category Dropdown
category_options = ["Food", "Transportation", "Bills"]
dd = tk.StringVar()
dd.set("Category")
category_dd = tk.OptionMenu(root, dd, *category_options)
category_dd.place(x=290, y=120)
category_dd.config(font=("Helvetica", "11"))
read_category()

# Item Entry and Label
item_label = tk.Label(root, text="Item:", bg="#EDEBD7", font=("Helvetica", "11"))
item_label.place(x=490, y=115)
item_entry = tk.Entry(root)
item_entry.place(x=490, y=140)

# Amount Entry and Label
amount_label = tk.Label(root, text="Amount:", bg="#EDEBD7", font=("Helvetica", "11"))
amount_label.place(x=690, y=115)
amount_entry = tk.Entry(root)
amount_entry.place(x=690, y=140)

# Buttons
budget_button = tk.Button(root, text="Add Income", command=add_income)
budget_button.place(x=110, y=170)
btn_add_category = tk.Button(root, text="Add Category", command=add_category)
btn_add_category.place(x=300, y=170)
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.place(x=522, y=170)
edit_button = tk.Button(root, text="Edit Item", command=edit_item)
edit_button.place(x=650, y=460)
delete_button = tk.Button(root, text="Delete Item", command=delete_item)
delete_button.place(x=750, y=460)
export_button = tk.Button(root, text="Export All Items", command=export_items)
export_button.place(x=700, y=500)

# Treeview
columns = ("Date","Category", "Item", "Amount")
expenses_tree = ttk.Treeview(frm_tree, columns=columns, show="headings",yscrollcommand=scr_tree.set)
expenses_tree.heading("Date", text="Date")
expenses_tree.heading("Category", text="Category")
expenses_tree.heading("Item", text="Item")
expenses_tree.heading("Amount", text="Amount")
expenses_tree.pack(fill="both", expand=True)
scr_tree.config(command=expenses_tree.yview)

# Total Expense Label
total_label = tk.Label(root, text="", bg="#EDEBD7", relief="ridge", padx=5, pady=5, bd=4)
total_label.place(x=50, y=455)

# Budget Status Label
budget_status = tk.Label(root, text="", bg="#EDEBD7", font=("Garamond", 15, "bold"), relief="ridge", padx=5, pady=5, bd=4)
budget_status.place(x=50, y=490)

# Status Label
status_label = tk.Label(root, text="", fg="red", bg="#EDEBD7", font=("Garamond", 12, "bold"))
status_label.place(x=670, y=170)

# Creates the items.txt file if it does not exist yet.
if not os.path.exists("Pynance.txt"):
    with open("Pynance.txt", "w"):
        pass
# Creates the categories.txt file if it does not exist yet.
if not os.path.exists("categories.txt"):
    with open("categories.txt", "w"):
        pass
# Calls the function to display the items in the treeview and the total amount.
view_items()
# Requires the user to close all pop-up windows first before exiting the program.
root.protocol("WM_DELETE_WINDOW", exit)
# Starts the event loop of the program.
root.mainloop()
