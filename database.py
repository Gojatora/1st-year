from tkinter import *
import sqlite3
from tkinter.messagebox import *
import re

#creates the table named "products" to the database as well as the column labels
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Price REAL NOT NULL,
                Quantity INTEGER NOT NULL
            )''')
    conn.commit()

#inserts the data from the following arguments to the table
def insert_product(conn, Name, Price, Quantity):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (Name, Price, Quantity) VALUES (?, ?, ?)", (Name, f"₱{Price}", Quantity))
    conn.commit()

#takes the data from the entries to be inserted
def add_product():
    Name = ent_name.get()
    Price = ent_price.get()
    Quantity = ent_quantity.get()
    pattern = r"[a-z]"
    check_price = re.search(pattern=pattern, string=Price)
    check_quantity = re.search(pattern=pattern, string=Quantity)
    #checks if all data is either empty or does not follows the correct pattern
    if Name and Price and Quantity:
        if check_price and check_quantity:
            showerror(title="Notice", message="Price and Quantity only accepts numbers.")
        else:
            insert_product(conn, Name, Price, Quantity)
            ent_name.delete(0, END)
            ent_price.delete(0, END)
            ent_quantity.delete(0, END)
            showinfo(title="Notice", message="Product added successfully")
    else:
        showerror(title="Notice", message="Fill out the following fields")

#returns all fetched records from the data base
def fetch_all_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return products

#inserts the fetched records to the listbox
def show_products():
    products = fetch_all_products(conn)
    if products:
        listbox.delete(0, END)
        for product in products:
            listbox.insert(END, f"ID: {product[0]} ; Product: {product[1]} ; Price: {product[2]} ; Quantity: {product[3]}")
    else:
        listbox.delete(0, END)
        showerror(title="Notice", message="No products found")

#variable that acts as a barrier from opening too many pop-up windows
window_counter = 0

#opens a separate window that provides interface to update products
def popup_update():
    global window_counter
    if window_counter == 0:
        update_window = Tk()
        update_window.title("Update product")
        update_window.geometry("900x500")
        update_window.resizable(width=False, height=False)

        #updates the selected product through ID with its arguments as replacement
        def update(conn, ID, New_Name, New_Price, New_Quantity):
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET Name = ? WHERE id = ?", (New_Name, ID))
            cursor.execute("UPDATE products SET Price = ? WHERE id = ?", (f"₱{New_Price}", ID))
            cursor.execute("UPDATE products SET Quantity = ? WHERE id = ?", (New_Quantity, ID))
            conn.commit()

        #takes the data from entries to be used to replace product information
        def update_product():
            global window_counter
            ID = ent_id.get()
            New_Name = ent_name.get()
            New_Price = ent_price.get()
            New_Quantity = ent_quantity.get()
            pattern = r"[a-z]"
            check_price = re.search(pattern=pattern, string=New_Price)
            check_quantity = re.search(pattern=pattern, string=New_Quantity)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            list_id = []
            rows = cursor.fetchall()
            # checks if all data is either empty or does not follows the correct pattern
            for row in rows:
                list_id.append(row[0])
            try:
                if int(ID) in list_id:
                    if New_Name:
                        if check_price and check_quantity:
                            showerror(title="Notice", message="Price and Quantity only accepts numbers.")
                        else:
                            update(conn, ID, New_Name, New_Price, New_Quantity)
                            ent_id.delete(0, END)
                            ent_name.delete(0, END)
                            ent_price.delete(0, END)
                            ent_quantity.delete(0, END)
                            list_id.clear()
                            showinfo(title="Notice", message="Product updated successfully")
                            window_counter -= 1
                            update_window.destroy()
                    else:
                        showerror(title="Notice", message="Fill out the following fields")
                else:
                    showerror(title="Notice", message="Enter Existing ID")
            except ValueError:
                showerror(title="Notice", message="Fill in the ID entry with numbers")

        #function for the root exit button that returns window_counter value to 0
        def Exit():
            global window_counter
            window_counter -= 1
            update_window.destroy()

        frm_label = Frame(update_window, bg="#003049")
        frm_label.place(x=225, y=174, anchor="center", )

        lbl_id = Label(frm_label, text="Product ID:", font=("Verdana", 16), fg="white", bg="#003049")
        lbl_id.pack(padx=200, pady=30)

        lbl_name = Label(frm_label, text="New Name:", font=("Verdana", 16), fg="white", bg="#003049")
        lbl_name.pack(padx=200, pady=30)

        lbl_price = Label(frm_label, text="New Price:", font=("Verdana", 16), fg="white", bg="#003049")
        lbl_price.pack(padx=200, pady=30)

        lbl_quantity = Label(frm_label, text="New Quantity:", font=("Verdana", 16), fg="white", bg="#003049")
        lbl_quantity.pack(padx=200, pady=30)

        frm_entries = Frame(update_window, bg="#003049")
        frm_entries.place(x=450, y=0)

        ent_id = Entry(frm_entries, font=("Verdana", 16), justify="center")
        ent_id.pack(padx=100, pady=30)

        ent_name = Entry(frm_entries, font=("Verdana", 16), justify="center")
        ent_name.pack(padx=100, pady=30)

        ent_price = Entry(frm_entries, font=("Verdana", 16), justify="center")
        ent_price.pack(padx=100, pady=30)

        ent_quantity = Entry(frm_entries, font=("Verdana", 16), justify="center")
        ent_quantity.pack(padx=100, pady=30)

        frm_button = Frame(update_window, bg="#d62828")
        frm_button.place(x=450, y=428, anchor="center")

        button_update_product = Button(frm_button, text="Update", font=("Verdana", 16), bg="#f77f00",
                                       command=update_product)
        button_update_product.pack(padx=405, pady=50, fill=X)

        update_window.protocol("WM_DELETE_WINDOW", Exit)

        window_counter += 1 #set the window_counter value to 1

    else:
        showerror(title="Notice", message="You can only open 1 pop-up window at a time.")

#opens a separate window that provides interface to delete products
def popup_delete():
    global window_counter
    if window_counter == 0:
        delete_window = Tk()
        delete_window.title("Update product")
        delete_window.geometry("500x185")
        delete_window.resizable(width=False, height=False)

        def delete(conn, ID):
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (ID,))
            conn.commit()

        def delete_product():
            global window_counter
            ID = ent_id.get()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            list_id = []
            rows = cursor.fetchall()
            # checks if all data is either empty or does not follows the correct pattern
            for row in rows:
                list_id.append(row[0])
            try:
                if int(ID) in list_id:
                    answer = askyesno(title="Notice", message="Are you sure you want to delete the product?")
                    if answer == True:
                        delete(conn, ID)
                        ent_id.delete(0, END)
                        list_id.clear()
                        showinfo(title="Notice", message="Product deleted successfully")
                        window_counter -= 1
                        delete_window.destroy()
                    else:
                        pass
                else:
                    showerror(title="Notice", message="Enter Existing ID")
            except ValueError:
                showerror(title="Notice", message="Fill in the ID entry with numbers")

        # function for the root exit button that returns window_counter value to 0
        def Exit():
            global window_counter
            window_counter -= 1
            delete_window.destroy()

        frm_label = Frame(delete_window, bg="#003049")
        frm_label.place(x=125, y=45, anchor="center", )

        lbl_id = Label(frm_label, text="Product ID:", font=("Verdana", 15), fg="white", bg="#003049")
        lbl_id.pack(padx=200, pady=30)

        frm_entries = Frame(delete_window, bg="#003049")
        frm_entries.place(x=235, y=0)

        ent_id = Entry(frm_entries, font=("Verdana", 15), justify="center", width=5)
        ent_id.pack(padx=100, pady=31)

        frm_button = Frame(delete_window, bg="#d62828")
        frm_button.place(x=250, y=138, anchor="center")

        button_update_product = Button(frm_button, text="Delete", font=("Verdana", 15), bg="#f77f00",
                                       command=delete_product)
        button_update_product.pack(padx=405, pady=25, fill=X)

        delete_window.protocol("WM_DELETE_WINDOW", Exit)

        window_counter += 1 #set the window_counter value to 1

    else:
        showerror(title="Notice", message="You can only open 1 pop-up window at a time.")

#function for the Exit button as well as the root's exit button that close the program and the database
def Exit():
    global window_counter
    if window_counter == 0:
        conn.close()
        root.destroy()
    else:
        showerror(title="Notice", message="Close all pop-up windows before closing the program")


conn = sqlite3.connect("inventory.db")
create_table(conn)

root = Tk()
root.title("Follante_finLA3")
root.geometry("900x847")
root.resizable(width=False, height=False)

frm_label = Frame(root, bg="#003049")
frm_label.place(x=225, y=130, anchor="center",)

lbl_name = Label(frm_label, text="Name:", font=("Verdana", 16), fg="white", bg="#003049")
lbl_name.pack(padx=200, pady=30)

lbl_price = Label(frm_label, text="Price:", font=("Verdana", 16), fg="white", bg="#003049")
lbl_price.pack(padx=200, pady=30)

lbl_quantity = Label(frm_label, text="Quantity:", font=("Verdana", 16), fg="white", bg="#003049")
lbl_quantity.pack(padx=200, pady=30)

frm_entries = Frame(root, bg="#003049")
frm_entries.place(x=450, y=0)

ent_name = Entry(frm_entries, font=("Verdana", 16), justify="center")
ent_name.pack(padx=100, pady=30)

ent_price = Entry(frm_entries, font=("Verdana", 16), justify="center")
ent_price.pack(padx=100, pady=30)

ent_quantity = Entry(frm_entries, font=("Verdana", 16), justify="center")
ent_quantity.pack(padx=100, pady=30)

frm_button = Frame(root, bg="#d62828")
frm_button.place(x=450, y=395, anchor="center")

btn_add_name = Button(frm_button, text="Add Product", font=("Verdana", 15), bg="#f77f00", command=add_product)
btn_add_name.pack(padx=380, pady=10, fill=X)

btn_view_products = Button(frm_button, text="View Available Products", font=("Verdana", 15), bg="#f77f00", command=show_products)
btn_view_products.pack(padx=380, pady=10, fill=X)

btn_update_product = Button(frm_button, text="Update Product", font=("Verdana", 15), bg="#f77f00", command=popup_update)
btn_update_product.pack(padx=380, pady=10, fill=X)

btn_delete_product = Button(frm_button, text="Delete Product", font=("Verdana", 15), bg="#f77f00", command=popup_delete)
btn_delete_product.pack(padx=380, pady=10, fill=X)

frm_listbox = Frame(root, bg="#fcbf49")
frm_listbox.place(x=450, y=650, anchor="center")

frm_scrollbar = Frame(frm_listbox, bg="#fcbf49")
frm_scrollbar.pack()

scrollbar = Scrollbar(frm_scrollbar)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frm_scrollbar, width=85, height=10, yscrollcommand=scrollbar.set, font=("Helvetica", 12), bg="#F6E4CC")
listbox.pack(padx=60, pady=30)


scrollbar.config(command=listbox.yview)

frm_exit = Frame(root, bg="#eae2b7")
frm_exit.place(x=450, y=812, anchor="center")

btn_exit = Button(frm_exit, text="EXIT", font=("Verdana", 14), bg="#f77f00", command=Exit)
btn_exit.pack(padx=420, pady=15)

root.protocol("WM_DELETE_WINDOW", Exit)

root.mainloop()
