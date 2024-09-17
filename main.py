from test import Person, Women, Men

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

allpeople = []
allpeople1 = ("afsd", "asdg", "ash")



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
age_label.grid(column=0, row=2, sticky='W', **options)

name = tk.StringVar()
name_entry = ttk.Entry(frame, textvariable=name)
name_entry.grid(column=1, row=0, **options)
name_entry.focus()

sex = tk.StringVar()
sex_entry = ttk.Entry(frame, textvariable=sex)
sex_entry.grid(column=1, row=1, **options)
sex_entry.focus()

age = tk.IntVar()
age_entry = ttk.Entry(frame, textvariable=age)
age_entry.grid(column=1, row=2, **options)
age_entry.focus()

def razot_button_clicked():
    name1 = name.get()
    sex1 = sex.get()
    age1 = age.get()
    allpeople.append(Person(name1, sex1, age1))
    print(name1, sex1, age1)
    result_label.config(text=allpeople[-1].info())
    list()

button = ttk.Button(frame, text='Produce person')
button.grid(column=2, row=0, sticky='W', **options)
button.configure(command=razot_button_clicked)

result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

def list():
    var = tk.Variable(value=allpeople1)

    listbox = tk.Listbox(
        root,
        listvariable=var,
        height=6,
        selectmode=tk.EXTENDED
    )

    listbox.grid(column=0, row=4)

    def items_selected(event):
        # get all selected indices
        selected_indices = listbox.curselection()
        # get selected items
        selected_langs = ",".join([listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'
        showinfo(title='Information', message=msg)


    listbox.bind('<<ListboxSelect>>', items_selected)




label2 = ttk.Label(frame)
label2.grid(row=3, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()