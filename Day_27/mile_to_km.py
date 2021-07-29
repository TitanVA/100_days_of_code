import tkinter


def button_clicked():
    mile = float(entry_field.get())
    km = mile * 1.60934
    label4.config(text=round(km, 2))


window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text="", font=("Arial", 14))
label.grid(column=0, row=0)
label1 = tkinter.Label(text="is equal to", font=("Arial", 14))
label1.grid(column=0, row=1)
label2 = tkinter.Label(text="Miles", font=("Arial", 14))
label2.grid(column=2, row=0)
label3 = tkinter.Label(text="     Km       ", font=("Arial", 14))
label3.grid(column=2, row=1)
label4 = tkinter.Label(text="0", font=("Arial", 14))
label4.grid(column=1, row=1)

entry_field = tkinter.Entry(width=10)
entry_field.insert(1, string="0")
entry_field.grid(column=1, row=0)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
