from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import vacation

# Data sets needed
file_read = open('country_names.txt','r')
country_list = []
for line in file_read:
    name = line.split()[0]
    country_list.append(name)


file_read2 = open('country_code.txt','r')
country_codelist =[]
for line1 in file_read2:
    code = line1.split()[0]
    country_codelist.append(code)

# generate window
window = Tk()
window.title("Welcome To Vacation Planner")

# Generate labels
lbl = Label(window, text="Country Name" )
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Year")
lbl2.grid(column=1, row=0)

lbl3 = Label(window, text="Number of Vacation Days")
lbl3.grid(column=2, row=0)

# generate combos
name_variable = StringVar()
combo = ttk.Combobox(window, values=country_list, textvariable=name_variable)
combo.current()
combo.focus()
c = combo.get()
combo.grid(column=0, row=1)


# 2 combo
year_var = IntVar()
combo_year = ttk.Combobox(window, values=[i for i in range(2020, 2050)], textvariable=year_var)
combo_year.grid(column=1, row=1)

# Spinbox for number of vacation days
day_var = IntVar()
spin = Spinbox(window, from_=1, to=200, width=5, textvariable=day_var)
spin.grid(column=2, row=1)

# 0utput
lbl = Label(window, text ="Output")
lbl.grid(column=0, row=2)

list_op = Listbox(window, height=6, width=60)
list_op.grid(column=1, row=3, rowspan=5, columnspan=2)

# function call
def clicked():
    country_name = name_variable.get()
    year = year_var.get()
    number_of_days = day_var.get()
    n = country_list.index(country_name)
    country_code = country_codelist[n]
    vac = vacation.Vacation()
    p = vac.get_vacation_options(number_of_days, country_code, year)
    list_op.delete(0, END)

    for lists in p:
        for element in lists:
            out_string = "Start date : " + element["Start Date"] + "  End date : " + element["End Date"] + "  Duration : " + element["Total days"]
            list_op.insert(END, out_string)


# Generate a button
btn = ttk.Button(window, text="Calculate", command=clicked)
btn.grid(column=0, row=3)
btn_6 = Button(window, text="Close", command=window.destroy)
btn_6.grid(column=0, row=4)

# scrollbar
sb1 = Scrollbar(window)
sb1.grid(column=3, row=2, rowspan=6)

list_op.configure(yscrollcommand=sb1)
sb1.configure(command=list_op.yview)
list_op.bind('<<ListboxSelect>>', clicked)

window.mainloop()