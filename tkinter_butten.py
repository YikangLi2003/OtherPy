import tkinter as tk
window = tk.Tk()
window.title("My window")
window.geometry("500x300")
var = tk.StringVar()
l = tk.Label(window, textvariable = var, bg="green", font=("Arial",12),width=30,height=12)
l.pack()


on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("You hitted me!")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

window.mainloop()



