from test import Person, Women, Men

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
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

sex = tk.StringVar(value="None")
R1 = tk.Radiobutton(frame, text="Vīrietis", variable=sex, value="Vīrietis")
R1.grid(column=1, row=1, **options)


R2 = tk.Radiobutton(frame, text="Sieviete", variable=sex, value="Sieviete")
R2.grid(column=1, row=2, **options)


age = tk.StringVar(value="")
age_entry = ttk.Entry(frame, textvariable=age)
age_entry.grid(column=1, row=3, **options)
age_entry.focus()

newname = tk.StringVar(value="")
newname_entry = ttk.Entry(frame, textvariable=newname)
newname_entry.grid(column=3, row=0, **options)
newname_entry.focus()


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
    print(name1, sex1, age1)
    result_label.config(text=allpeople[-1].info())
    list()

def sexchange():
    if sex == "Vīriets":
        sex = "Sieviete"
    elif sex == "Sieviete":
        sex = "Vīriets"
    mainit_button_clicked()



def birthday():
    age2 = age.get()
    age2 += 1
    mainit_button_clicked(age2)



def namechange(newname):
    name = newname
    mainit_button_clicked()

def mainit_button_clicked(age2):
    name3 = name
    sex3 = sex
    age3 = age2
    Error=0
    try:
        int(age3)
    except ValueError:
        Error=1

    if sex3 == "None" or name3 == "":
        showinfo("Error", "Please fill all fields.")
        return
    elif Error == 1:
        showinfo("Error", "Please fill field age with a number.")
        return
    allpeople.append(Person(name3, sex3, age3))
    print(name3, sex3, age3)
    result_label.config(text=allpeople[-1].info())
    list()

production_button = ttk.Button(frame, text='Produce person')
production_button.grid(column=2, row=0, sticky='W', **options)
production_button.configure(command=razot_button_clicked)

sexchange_button = ttk.Button(frame, text='Sex change')
sexchange_button.grid(column=4, row=1, sticky='W', **options)
sexchange_button.configure(command=sexchange)

namechange_button = ttk.Button(frame, text='Name change')
namechange_button.grid(column=4, row=0, sticky='W', **options)
namechange_button.configure(command=namechange)

birthday_button = ttk.Button(frame, text='Birthday')
birthday_button.grid(column=4, row=3, sticky='W', **options)
birthday_button.configure(command=birthday)

result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=3, **options)


    
# def list():
#     tuple(allpeople)
#     var = tk.Variable(value=allpeople)

#     listbox = tk.Listbox(
#         root,
#         listvariable=var,
#         height=6,
#         selectmode=tk.EXTENDED
#     )

#     listbox.grid(column=0, row=4)

#     def items_selected(event):
#         # get all selected indices
#         selected_indices = listbox.curselection()
#         # get selected items
#         selected_langs = ",".join([listbox.get(i) for i in selected_indices])
#         msg = f'You selected: {selected_langs}'
#         showinfo(title='Information', message=msg)


#     listbox.bind('<<ListboxSelect>>', items_selected)

label2 = ttk.Label(frame)
label2.grid(row=3, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()