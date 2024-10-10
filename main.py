from test import Person, Women, Men

import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo

allpeople = []

root = tk.Tk()
root.title('People factory')
root.geometry('1280x720')
root.resizable(False, False)

frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

name_label = ttk.Label(frame, text='Name')
name_label.grid(column=0, row=0, sticky='W', **options)

sex_label = ttk.Label(frame, text='Sex')
sex_label.grid(column=0, row=1, sticky='W', **options)

age_label = ttk.Label(frame, text='Age')
age_label.grid(column=0, row=3, sticky='W', **options)

name = tk.StringVar(value="")
name_entry = ttk.Entry(frame, textvariable=name)
name_entry.grid(column=1, row=0, **options)
name_entry.focus()

new_name = tk.StringVar()
new_name_entry = ttk.Entry(frame, textvariable=new_name)
new_name_entry.grid(column=1, row=4, **options)
new_name_entry.focus()

sex = tk.StringVar(value="None")
R1 = tk.Radiobutton(frame, text="Vīrietis", variable=sex, value="Vīrietis")
R1.grid(column=1, row=1, **options)

R2 = tk.Radiobutton(frame, text="Sieviete", variable=sex, value="Sieviete")
R2.grid(column=1, row=2, **options)

age = tk.IntVar()
age_entry = ttk.Entry(frame, textvariable=age)
age_entry.grid(column=1, row=3, **options)
age_entry.focus()

def razot_button_clicked():
    name1 = name.get()
    sex1 = sex.get()
    age1 = age.get()
    Error=0
    try:
        int(age1)
    except ValueError:
        Error=1

    if sex1 == "None" or name1 == "":
        showinfo("Error", "Please fill all fields.")
        return
    elif Error == 1:
        showinfo("Error", "Please fill field age with a number.")
        return
    allpeople.append(Person(name1, sex1, age1))
    change_list()


def change_list():
    listbox.delete(0,END)
    for Person in allpeople:
        listbox.insert("end",f"{Person.name},{Person.sex},{Person.age}")

def name_change_button_clicked():

    newname = new_name.get()
    for selected in listbox.curselection():
        allpeople[selected].namechange(newname)

    change_list()

def sex_change_button_clicked():
    new_text = ""
    for selected in listbox.curselection():
        allpeople[selected].sexchange()
        new_text += allpeople[selected].info()
    change_list()

def birthday_button_clicked():
    new_text = ""
    for selected in listbox.curselection():
        allpeople[selected].birthday()
        new_text += allpeople[selected].info()
    change_list()

production_button = ttk.Button(frame, text='Produce person')
production_button.grid(column=2, row=0, sticky='W', **options)
production_button.configure(command=razot_button_clicked)

name_change_button = ttk.Button(frame, text='Name change')
name_change_button.grid(column=2, row=4, sticky='W', **options)
name_change_button.configure(command=name_change_button_clicked)

sex_change_button = ttk.Button(frame, text='Sex change')
sex_change_button.grid(column=3, row=4, sticky='W', **options)
sex_change_button.configure(command=sex_change_button_clicked)

birthday_button = ttk.Button(frame, text='Birthday')
birthday_button.grid(column=4, row=4, sticky='W', **options)
birthday_button.configure(command=birthday_button_clicked)

listbox = tk.Listbox(frame, height=6, selectmode=tk.EXTENDED)
listbox.grid(column=0, row=4, **options)

label2 = ttk.Label(frame)
label2.grid(row=4, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()