
import os
from pathlib import Path
import tkinter as tk
import autosort



# gives the window some values
root = tk.Tk()
root.geometry('600x400')
root.config(bg="#5e5e5e")
root.resizable(0,0)
root.title("Download Folder Sorter")



# a label is text, where you can give it different arguments
lab = tk.Label(root, text="Download folder Sorter", font="courier 25 bold", bg="#5e5e5e")

#TODO need to find a way to loop the autosort or atleast get it running well
but = tk.Button(root, text="Sort!", font="courier 15 bold", bg="gray", command=lambda: autosort.main())

out = tk.StringVar()
#out.set(os.listdir(str(Path.home() / "Downloads")))

# you can also write the widget like this way
disp = tk.Message(
    root,
    width=250,
    textvariable=out,
    relief=tk.RIDGE,
    font=('courier', 15)
)


#grid section
lab.grid(row=0,pady=50, padx=15)
but.grid(row=1,pady=25, padx=265)
disp.grid(row=2,pady=20)

#shows window
root.mainloop()