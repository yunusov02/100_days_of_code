import tkinter

window = tkinter.Tk()
window.title("My first Programm")
window.minsize(width=500, height=300)


# Label
my_label = tkinter.Label(text="It's my label", font=('Arial', 24, 'bold'))
my_label.pack()

# Button

def button_clicked():
    # print('I got clicked')
    my_label['text'] = 'New Text'
    my_label.config(text='New text')

button = tkinter.Button(text='Click me', command=button_clicked)
button.pack()

# Entry

def btn_func():
    print(entry.get())

entry = tkinter.Entry()
entry.pack()

btn = tkinter.Button(text='btn', command=btn_func)
btn.pack()

window.mainloop()
