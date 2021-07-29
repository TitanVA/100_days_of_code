import tkinter

window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I'm a label", font=("Arial", 24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text2")


def button_clicked():
    print("Clicked")
    new_test = entry_field.get()
    my_label.config(text=new_test)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

entry_field = tkinter.Entry(width=30)
entry_field.insert(1, string="Some text to begin with.")
entry_field.pack()

text_field = tkinter.Text(height=5, width=30)
text_field.focus()
text_field.insert(1.0, "Some text insert in textfield")
text_field.pack()


def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)


scale_field = tkinter.Scale(from_=0, to=100, command=scale_used)
scale_field.pack()


def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1",
                                   value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2",
                                   value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
