import tkinter as tk
from tkinter.messagebox import showinfo


window = tk.Tk()
window.geometry("1000x975")
window.title("J1T-midLA2")
window.resizable(height=False, width=False)

cars = (("BMW: $5,000.00", 5000.00), ("Subaru: $2500.00", 2500.00), ("Chevrolet: $4100.00", 4100.00))
interior_option = (("Leather: $550.00", 550.00), ("GPS: $1000.00", 1000.00))
exterior_finish = ("Hard Top", "Convertible")
exterior_option = (("Wheel Upgrade: $1000.00", 1000.00), ("Performance Package: $2000.00", 2000.00))

cars_var = tk.IntVar()
interior_option_var1 = tk.IntVar()
interior_option_var2 = tk.IntVar()
exterior_finish_var = tk.StringVar()
exterior_finish_var.set("N/A")
exterior_option_var1 = tk.IntVar()
exterior_option_var2 = tk.IntVar()

def Total():
    car_value = cars_var.get()
    interior_option_value = interior_option_var1.get() + interior_option_var2.get()
    exterior_option_value = exterior_option_var1.get() + exterior_option_var2.get()
    sum_total = car_value + interior_option_value + exterior_option_value
    lbl_price["text"] = f"Total Cost: ${sum_total:.2f}"

def Reset():
    cars_var.set(0)
    interior_option_var1.set(0)
    interior_option_var2.set(0)
    exterior_finish_var.set("N/A")
    exterior_option_var1.set(0)
    exterior_option_var2.set(0)
    lbl_price["text"] = ""

def Get_receipt():
    car_value = cars_var.get()
    interior_option_value = interior_option_var1.get() + interior_option_var2.get()
    exterior_finish_value = exterior_finish_var.get()
    exterior_option_value = exterior_option_var1.get() + exterior_option_var2.get()
    sum_total = car_value + interior_option_value + exterior_option_value
    print_car = f"Car (BMW): ${car_value:.2f}" if car_value == 5000.00\
        else f"Car (Subaru): ${car_value:.2f}" if car_value == 2500.00\
        else f"Car (Chevrolet): ${car_value:.2f}" if car_value == 4100.00\
        else "Car: N/A"
    print_interior_option = f"Interior Option (Leather): ${interior_option_value:.2f}" if interior_option_value == 550.00\
        else f"Interior Option (GPS): ${interior_option_value:.2f}" if interior_option_value == 1000.00\
        else f"Interior Option (Leather and GPS): ${interior_option_value:.2f}" if interior_option_value == 1550.00\
        else "Interior Option: N/A"
    print_exterior_option = f"Exterior Option (Wheel Upgrade): ${exterior_option_value:.2f}" if exterior_option_value == 1000.00\
        else f"Exterior Option (Performance Package): ${exterior_option_value:.2f}" if exterior_option_value == 2000.00\
        else f"Exterior Option (Wheel Upgrade and Performance Package): ${exterior_option_value:.2f}" if exterior_option_value == 3000.00\
        else "Exterior Option: N/A"
    showinfo(
        title="Receipt",
        message=f"{print_car}"
                f"\n{print_interior_option}"
                f"\nExterior Finish: {exterior_finish_value}"
                f"\n{print_exterior_option}"
                f"\nTotal Cost: ${sum_total:.2f}"
    )

frm_header = tk.Frame(
    master=window,
    bg="#F42B03",
    highlightbackground="Black",
    highlightthickness=4,
    width=1000,
    height=75
)
frm_header.place(x=0, y=0)

lbl_shop = tk.Label(
    master=frm_header,
    text="FOLLANTE'S CAR MAINTENANCE SERVICES",
    font=("Helvetica", 25),
    bg="#F42B03",
    fg="White"
)
lbl_shop.place(x=500, y=35, anchor="center")

frm_body = tk.Frame(
    master=window,
    bg="#FFF0C7",
    width=1000,
    height=925
)
frm_body.place(x=0, y=75)

lbl_cars = tk.Label(
    master=frm_body,
    text="Cars List",
    font=("Verdana", 20),
    bg="#FFF0C7"
)
lbl_cars.place(x=250, y=50, anchor="center")

frm_cars = tk.Frame(
    master=frm_body,
    highlightbackground="#FF8113",
    highlightthickness=2,
    bg="#FFF0C7"
)
frm_cars.place(x=250, y=250, anchor="center")

for c in cars:
    rdb_cars = tk.Radiobutton(
        master=frm_cars,
        text=c[0],
        value=c[1],
        variable=cars_var,
        bg="#FFF0C7",
        height=5,
        width=30,
        font=("Verdana", 12)
    )
    rdb_cars.pack()

lbl_interior_option = tk.Label(
    master=frm_body,
    text="Interior Option",
    font=("Verdana", 20),
    bg="#FFF0C7"
)
lbl_interior_option.place(x=250, y=470, anchor="center")

frm_interior_option = tk.Frame(
    master=frm_body,
    highlightbackground="#FF8113",
    highlightthickness=2,
    bg="#FFF0C7"
)
frm_interior_option.place(x=250, y=620, anchor="center")


chk_interior_option1 = tk.Checkbutton(
    master=frm_interior_option,
    text=interior_option[0][0],
    onvalue=interior_option[0][1],
    offvalue=0,
    variable=interior_option_var1,
    height=5,
    width=30,
    font=("Verdana", 12),
    bg="#FFF0C7"

)
chk_interior_option1.pack(padx=20)

chk_interior_option2 = tk.Checkbutton(
    master=frm_interior_option,
    text=interior_option[1][0],
    onvalue=interior_option[1][1],
    offvalue=0,
    variable=interior_option_var2,
    height=5,
    width=25,
    font=("Verdana", 12),
    bg="#FFF0C7"
)
chk_interior_option2.pack(padx=20)

lbl_exterior_finish = tk.Label(
    master=frm_body,
    text="Exterior Finish",
    font=("Verdana", 20),
    bg="#FFF0C7"
)
lbl_exterior_finish.place(x=750, y=50, anchor="center")

frm_exterior_finish = tk.Frame(
    master=frm_body,
    highlightbackground="#FF8113",
    highlightthickness=2,
    bg="#FFF0C7"
)
frm_exterior_finish.place(x=750, y=250, anchor="center")

for e_f in exterior_finish:
    rdb_exterior_finish = tk.Radiobutton(
        master=frm_exterior_finish,
        text=e_f,
        variable=exterior_finish_var,
        value=e_f,
        bg="#FFF0C7",
        height=8,
        width=30,
        font=("Verdana", 12)
    )
    rdb_exterior_finish.pack()

lbl_exterior_option = tk.Label(
    master=frm_body,
    text="Interior Option",
    font=("Verdana", 20),
    bg="#FFF0C7"
)
lbl_exterior_option.place(x=750, y=470, anchor="center")

frm_exterior_option = tk.Frame(
    master=frm_body,
    highlightbackground="#FF8113",
    highlightthickness=2,
    bg="#FFF0C7"
)
frm_exterior_option.place(x=750, y=620, anchor="center")

chk_exterior_option1 = tk.Checkbutton(
    master=frm_exterior_option,
    text=exterior_option[0][0],
    onvalue=exterior_option[0][1],
    offvalue=0,
    variable=exterior_option_var1,
    height=5,
    width=30,
    font=("Verdana", 12),
    bg="#FFF0C7"
)
chk_exterior_option1.pack(padx=20)

chk_exterior_option2 = tk.Checkbutton(
    master=frm_exterior_option,
    text=exterior_option[1][0],
    onvalue=exterior_option[1][1],
    offvalue=0,
    variable=exterior_option_var2,
    height=5,
    width=30,
    font=("Verdana", 12),
    bg="#FFF0C7"
)
chk_exterior_option2.pack(padx=20)


btn_total = tk.Button(
    master=frm_body,
    text="TOTAL",
    command=Total,
    font=("Segoe UI Black", 15),
    bg="#FF8113"
)
btn_total.place(x=500, y=790, anchor="center")

lbl_price = tk.Label(
    master=frm_body,
    text="",
    bg="#FFF0C7",
    font=("Verdana", 15),
)
lbl_price.place(x=500, y=850, anchor="center")

btn_reset = tk.Button(
    master=frm_body,
    text="RESET",
    command=Reset,
    font=("Segoe UI Black", 20),
    bg="#FF8113"
)
btn_reset.place(x=250, y=810, anchor="center")

btn_receipt = tk.Button(
    master=frm_body,
    text="GET RECEIPT",
    command=Get_receipt,
    font=("Segoe UI Black", 20),
    bg="#FF8113"
)
btn_receipt.place(x=750, y=810, anchor="center")

window.mainloop()