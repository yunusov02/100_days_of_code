import tkinter 

window = tkinter.Tk()
window.title('Miles to kilometr convertor')
window.config(padx=20, pady=20)

mile_input = tkinter.Entry(width=7)
mile_input.grid(column=1, row=0)

miles_label = tkinter.Label(text='miles')
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

kilometr_result_label = tkinter.Label(text='0')
kilometr_result_label.grid(column=1, row=1)

kilometr_result = tkinter.Label(text='km')
kilometr_result.grid(column=2, row=1)


def calculate():
    miles = mile_input.get()
    km = round(float(miles) * 1.609)
    kilometr_result_label.config(text=str(km))


calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()

