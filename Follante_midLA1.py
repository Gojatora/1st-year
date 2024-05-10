import tkinter as tk
window = tk.Tk()
window.geometry("700x450")
window.title("J1T-midLA1")
window.resizable(width=False, height=False)

def display_text():
    text = ent_text.get()
    entry_checker = text.split()
    if len(entry_checker) != 1:
        lbl_displayed_text["text"] = "Enter 1 word only"
    else:
        lbl_displayed_text["text"] = f"{text}"

frm_student_name = tk.Frame(
    master=window,
    width=700,
    height=50,
    bg="#0077b6"
)
frm_student_name.place(x=0, y=0)

frm_outline1 = tk.Frame(
    master=window,
    width=700,
    height=5,
    bg="#03045e"
)
frm_outline1.place(x=0, y=0)

frm_outline2 = tk.Frame(
    master=window,
    width=5,
    height=50,
    bg="#03045e"
)
frm_outline2.place(x=0, y=0)

frm_outline3 = tk.Frame(
    master=window,
    width=5,
    height=50,
    bg="#03045e"
)
frm_outline3.place(x=695, y=0)

frm_outline4 = tk.Frame(
    master=window,
    width=700,
    height=5,
    bg="#03045e"
)
frm_outline4.place(x=0, y=45)

lbl_studentname = tk.Label(
    master=frm_student_name,
    text="Adrian Paolo S. Follante",
    bg="#0077b6",
    fg="white",
    font=("Arial", 20)
)
lbl_studentname.place(x=350, y=25, anchor="center")

frm_entry_display = tk.Frame(
    master=window,
    width=700,
    height=225,
    bg="#00b4d8"
)
frm_entry_display.place(x=0, y=50)

lbl_input_text = tk.Label(
    master=frm_entry_display,
    font=("Arial", 25),
    text="Input Text Here",
    bg="#00b4d8",
    fg="black"
)
lbl_input_text.place(x=350, y=45, anchor="center")

ent_text = tk.Entry(
        master=frm_entry_display,
        justify="center",
        font=("Arial", 15),
    width=50
)
ent_text.place(x=350, y=100, anchor="center")

btn_display = tk.Button(
    master=window,
    text="Display Text",
    bg="#caf0f8",
    font=("Arial", 20),
    command=display_text
)
btn_display.place(x=350, y=220, anchor="center")

frm_outline5 = tk.Frame(
    master=window,
    width=700,
    height=5,
    bg="#03045e"
)
frm_outline5.place(x=0, y=275)

frm_frame_output = tk.Frame(
    master=window,
    width=700,
    height=180,
    bg="#90e0ef"
    )
frm_frame_output.place(x=0, y=280)

lbl_display = tk.Label(
    master=frm_frame_output,
    text="Display",
    font=("Arial", 25),
    bg="#90e0ef"
)
lbl_display.place(x=350, y=35, anchor="center")

lbl_displayed_text = tk.Label(
    master=frm_frame_output,
    text="",
    wraplength=695,
    font=("Arial", 18),
    bg="#90e0ef",
)
lbl_displayed_text.place(x=350, y=100, anchor="center")

window.mainloop()