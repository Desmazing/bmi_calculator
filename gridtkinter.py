# what does grid do for tkinter
# grid places labels and frames in an orderly manner *
# different from place 

import tkinter as tk

window = tk.Tk()

for i in range(4):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()
