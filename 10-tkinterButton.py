from tkinter import*

def hello():
    print("hello man")

tk = Tk()
btn = Button(tk, text="click me pls" command=hello)
btn.pack()
tk.mainloop()