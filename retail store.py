import tkinter as tk
window = tk.Tk()
window.title("AP's School Supplies Shop")
window.geometry("1000x750")
window.resizable(width=False, height=False)

def total():
    q1 = float(ent_pencil.get())
    q2 = float(ent_pen.get())
    q3 = float(ent_yellowpad.get())
    q4 = float(ent_bondpaper.get())
    q5 = float(ent_color.get())
    if q1 <= 50 and q2 <= 50 and q3 <= 50 and q4 <= 50 and q5 <= 50:
        amount1 = q1 * 15
        amount2 = q2 * 25
        amount3 = q3 * 20
        amount4 = q4 * 1
        amount5 = q5 * 45.50
        total_amount = (amount1 + (amount1 * 0.10)) + (amount2 + (amount2 * 0.10)) \
                    + (amount3 + (amount3 * 0.10)) + (amount4 + (amount4 * 0.10)) \
                    + (amount5 + (amount5 * 0.10))
        subtotal = amount1 + amount2 \
                    + amount3 + amount4 \
                    + amount5
        tax = total_amount - subtotal
        totalamountdue = subtotal + tax
        lbl_valtotal["text"] = f"₱{total_amount:.2f}"
        lbl_subtotalvalue["text"] = f"₱{subtotal:.2f}"
        lbl_taxvalue["text"] = f"₱{tax:.2f}"
        lbl_totalamountduevalue["text"] = f"₱{totalamountdue:.2f}"
        lbl_notice["text"] = " "
        lbl_changevalue["text"] =""
    else:
        lbl_notice["text"] = "Item Quantity Exceeded"
        lbl_valtotal["text"] = ""
        lbl_subtotalvalue["text"] = ""
        lbl_taxvalue["text"] = ""
        lbl_totalamountduevalue["text"] = ""

def pay():
    q1 = float(ent_pencil.get())
    q2 = float(ent_pen.get())
    q3 = float(ent_yellowpad.get())
    q4 = float(ent_bondpaper.get())
    q5 = float(ent_color.get())
    if q1 <= 50 and q2 <= 50 and q3 <= 50 and q4 <= 50 and q5 <= 50:
        amount1 = q1 * 15
        amount2 = q2 * 25
        amount3 = q3 * 2
        amount4 = q4 * 1
        amount5 = q5 * 45.50
        total_amount = (amount1 + (amount1 * 0.10)) + (amount2 + (amount2 * 0.10)) \
                       + (amount3 + (amount3 * 0.10)) + (amount4 + (amount4 * 0.10)) \
                       + (amount5 + (amount5 * 0.10))
        paid = float(ent_amount_paid.get())
        change = paid - total_amount
        if paid < total_amount:
            lbl_changevalue["text"] = "Insufficient Payment"
        else:
            lbl_changevalue["text"] = f"₱{change:.2f}"

def clear():
    lbl_changevalue["text"] = ""
    lbl_changevalue["text"] = ""
    lbl_notice["text"] = ""
    lbl_valtotal["text"] = ""
    lbl_subtotalvalue["text"] = ""
    lbl_taxvalue["text"] = ""
    lbl_totalamountduevalue["text"] = ""
    lbl_notice["text"] = ""
    ent_yellowpad.delete(0, 'end')
    ent_pen.delete(0, 'end')
    ent_pencil.delete(0, 'end')
    ent_bondpaper.delete(0, 'end')
    ent_color.delete(0, 'end')
    ent_amount_paid.delete(0, 'end')

frameheader = tk.Frame(
    master=window,
    bg="#234F1E",
    width=1000,
    height=75
)
frameheader.place(y=0)

lbl_store = tk.Label(
    master=frameheader,
    text="Welcome to AP's School Supplies Shop",
    font=('Helvetica', 25),
    bg="#234F1E",
    fg="#B0FC38"
)
lbl_store.place(x=220, y=15)

frameheaderoutline = tk.Frame(
    master=window,
    bg="black",
    width=1000,
)
frameheaderoutline.place(y=75)

framebody = tk.Frame(
    master=window,
    bg="green",
    width=1000,
    height=444
)
framebody.place(y=76)

lbl_category1 = tk.Label(
    master=window,
    text="Items",
    font=('Helvetica', 25),
    bg="green",
    fg="white"
)
lbl_category1.place(x=230, y=100)

lbl_category2 = tk.Label(
    master=window,
    text="Quantity (Max. of 50 only)",
    font=('Helvetica', 25),
    bg="green",
    fg="white"
)
lbl_category2.place(x=520, y=100)

lbl_pencil = tk.Label(
    master=window,
    text="Pencil         : ₱15.00",
    font=('Cascadia Code', 18),
    bg="green",
    fg="white"
)
lbl_pencil.place(x=110, y=170)

ent_pencil = tk.Entry(
    master=window,
    font=('Cascadia Code', 18),
    justify="center"
)
ent_pencil.place(x=564, y=170)

lbl_pen = tk.Label(
    master=window,
    text="Pen            : ₱25.00",
    font=('Cascadia Code', 18),
    bg="green",
    fg="white"
)
lbl_pen.place(x=110, y=220)

ent_pen = tk.Entry(
    master=window,
    font=('Cascadia Code', 18),
    justify="center"
)
ent_pen.place(x=564, y=220)

lbl_yellowpad = tk.Label(
    master=window,
    text="Yellow Pad     : ₱2.00",
    font=('Cascadia Code', 18),
    bg="green",
    fg="white"
)
lbl_yellowpad.place(x=110, y=270)

ent_yellowpad = tk.Entry(
    master=window,
    font=('Cascadia Code', 18),
    justify="center"
)
ent_yellowpad.place(x=564, y=270)

lbl_bondpaper = tk.Label(
    master=window,
    text="Bondpaper      : ₱1.00",
    font=('Cascadia Code', 18),
    bg="green",
    fg="white"
)
lbl_bondpaper.place(x=110, y=320)

ent_bondpaper = tk.Entry(
    master=window,
    font=('Cascadia Code', 18),
    justify="center"
)
ent_bondpaper.place(x=564, y=320)

lbl_color = tk.Label(
    master=window,
    text="Color          : ₱45.50",
    font=('Cascadia Code', 18),
    bg="green",
    fg="white"
)
lbl_color.place(x=110, y=370)

ent_color = tk.Entry(
    master=window,
    font=('Cascadia Code', 18),
    justify="center"
)
ent_color.place(x=564, y=370)

btn_checkout = tk.Button(
    master=window,
    text="Checkout",
    command=total,
    font=('Cascadia Code', 18),
    bg="#234F1E",
    fg="#99EDC3"
)
btn_checkout.place(x=435, y=440)

frame1 = tk.Frame(
    master=window,
    bg="black",
    width=1000
)
frame1.place(y=520)

frameleft = tk.Frame(
    master=window,
    bg="#B2D3C2",
    width=1000,
    height=229
)
frameleft.place(y=521)

lbl_total = tk.Label(
    master=window,
    text="Total Amount Due  :",
    font=('Cascadia Code', 18),
    bg="#B2D3C2"
)
lbl_total.place(x=45, y=560)

lbl_valtotal = tk.Label(
    master=window,
    text="0",
    font=('Cascadia Code', 18),
    bg="#B2D3C2"
)
lbl_valtotal.place(x=345, y=560)

lbl_subtotal = tk.Label(
    master=window,
    text="Subtotal  :",
    font=('Cascadia Code', 15),
    bg="#B2D3C2"
)
lbl_subtotal.place(x=45, y=610)

lbl_subtotalvalue = tk.Label(
    master=window,
    text="0",
    font=('Cascadia Code', 15),
    bg="#B2D3C2"
)
lbl_subtotalvalue.place(x=205, y=610)

lbl_tax = tk.Label(
    master=window,
    text="10% tax   :",
    font=('Cascadia Code', 15),
    bg="#B2D3C2"
)
lbl_tax.place(x=45, y=640)


lbl_taxvalue = tk.Label(
    master=window,
    text="0",
    font=('Cascadia Code', 15),
    bg="#B2D3C2"
)
lbl_taxvalue.place(x=205, y=640)

lbl_totalamountdue = tk.Label(
    master=window,
    text="Total     :",
    font=('Cascadia Code', 15),
    bg="#B2D3C2"
)
lbl_totalamountdue.place(x=45, y=670)

lbl_totalamountduevalue = tk.Label(
    master=window,
    text="0",
    font=('Cascadia Code', 15),
    bg="#B2D3C2"
)
lbl_totalamountduevalue.place(x=205, y=670)

lbl_notice = tk.Label(
    master=window,
    text=" ",
    font=('Cascadia Code', 13),
    bg="#B2D3C2"
)
lbl_notice.place(x=145, y=700)


frame2 = tk.Frame(
    master=window,
    bg="black",
    height=230
)
frame2.place(x=500, y=520)

lbl_amountpaid = tk.Label(
    master=window,
    text="Your Payment: ",
    font=('Cascadia Code', 18),
    bg="#B2D3C2"
)
lbl_amountpaid.place(x=540, y=560)

ent_amount_paid = tk.Entry(
    master=window,
    font=('Cascadia Code', 18),
    justify="center",
    width=10
)
ent_amount_paid.place(x=740, y=560)

btn_amount_paid = tk.Button(
    master=window,
    text="Pay",
    command=pay,
    font=('Cascadia Code', 15),
    bg="#99EDC3"
)
btn_amount_paid.place(x=900, y=555)

lbl_change = tk.Label(
    master=window,
    text="Your Change : ",
    font=('Cascadia Code', 14),
    bg="#B2D3C2"
)
lbl_change.place(x=540, y=620)

lbl_changevalue = tk.Label(
    master=window,
    text="0",
    font=('Cascadia Code', 14),
    bg="#B2D3C2"
)
lbl_changevalue.place(x=700, y=620)

btn_clear = tk.Button(
    master=window,
    text="CLEAR",
    command=clear,
    font=('Cascadia Code', 15),
    bg="Red"
)
btn_clear.place(x=700, y=670)

window.mainloop()
