import tkinter

def buttonClicked():
    label_resultinkm.config(text=f'{round(int(user_entry.get())*1.609, 1)}')

window = tkinter.Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=20, pady=20)

user_entry = tkinter.Entry(width=7)
user_entry.grid(row=0, column=1)

label_miles = tkinter.Label(text='Miles')
label_miles.grid(row=0, column=2)

label_isequalto = tkinter.Label(text='is equal to')
label_isequalto.grid(row=1, column=0)

label_resultinkm = tkinter.Label(text='')
label_resultinkm.grid(row=1, column=1)

label_km = tkinter.Label(text='Km')
label_km.grid(row=1, column=2)

button_calc = tkinter.Button(text='Calculate', command=buttonClicked)
button_calc.grid(row=2, column=1)

window.mainloop()
