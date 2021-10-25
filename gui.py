
import os
from pathlib import Path
import tkinter as tk
import autosort


errorMessage = "this is where errors will be seen"

# gives the window some values
root = tk.Tk()
root.geometry('600x400')
root.config(bg="#5e5e5e")
root.resizable(0,0)
root.title("Download Folder Sorter")


out = tk.StringVar()
out.set(errorMessage)

# a label is text, where you can give it different arguments
lab = tk.Label(root, text="Download folder Sorter", font="courier 25 bold", bg="#5e5e5e")

#TODO need to find a way to loop the autosort or atleast get it running well
but = tk.Button(root, text="Sort!", font="courier 15 bold", bg="gray", command=lambda:[autosort.main(), out.set(autosort.err)])


# you can also write the widget like this way
disp = tk.Message(
    root,
    width=250,
    textvariable=out,
    relief=tk.RIDGE,
    font=('courier', 15)
)

#TODO come back to this to center via a better method, probably whitespace with empty columns
#grid section
lab.grid(row=0,padx=90,pady=45)
but.grid(row=1,pady=15)
disp.grid(row=2,pady=25)

#shows window
root.mainloop()
