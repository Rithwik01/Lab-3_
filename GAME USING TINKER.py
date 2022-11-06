import tkinter as tk

window = tk.Tk()

window.title("tic tac toe")

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=2)
        frame.grid(row=i, column=j, padx=1, pady=1)
        label = tk.Label(master=frame)
        label.pack(padx=25, pady=25)