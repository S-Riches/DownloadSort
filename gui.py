
import os
from pathlib import Path
import tkinter as tk
import autosort


errorMessage = "this is where errors will be seen"

# gives the window some values
root = tk.Tk()
root.geometry('575x500')
root.config(bg="#5e5e5e")
root.resizable(0,0)
root.title("Download Folder Sorter")


out = tk.StringVar()
out.set(errorMessage)

# a label is text, where you can give it different arguments
lab = tk.Label(root, text="Download folder Sorter", font="consolas 25 bold", bg="#5e5e5e")

# you can also write the widget like this way
disp = tk.Message(
    root,
    width=250,
    textvariable=out,
    relief=tk.RIDGE,
    font=('consolas', 15)
)
# instead of trying to get the variable from the autosort script, we return the value from the script and get it that way
but = tk.Button(root, text="Sort!", font="consolas 15 bold", bg="gray", command=lambda:out.set(autosort.main() or errorMessage))


#TODO come back to this to center via a better method, probably whitespace with empty columns
#grid section
lab.grid(row=0,padx=90,pady=45)
but.grid(row=1,pady=15)
disp.grid(row=2,pady=25)

#shows window
root.mainloop()
