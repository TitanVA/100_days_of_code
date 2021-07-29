import tkinter


def button1_clicked():
    my_label.config(text="Click 1")

def button2_clicked():
    my_label.config(text="Click 2")


window = tkinter.Tk()
window.title("My GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = tkinter.Label(text='I am a Label', font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

button1 = tkinter.Button(text="Click me", command=button1_clicked)
button1.grid(column=1, row=1)

button2 = tkinter.Button(text="Click me", command=button2_clicked)
button2.grid(column=2, row=0)

input_field = tkinter.Entry(width=10)
input_field.grid(column=3, row=2)

window.mainloop()
