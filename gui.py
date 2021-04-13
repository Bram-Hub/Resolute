from tkinter import *
import os

class resolute_gui:
    def __init__(self):
        # make "program_files" folder if it doesn't exist
        if not os.path.exists("program_files"):
            os.makedirs("program_files")
        try:
            defau = open("program_files/defaults.txt", 'r')
            defaults = defau.read().split('\n')
            defau.close()
        except:
            defaults = ['1', "", "", "", "1", "1"]

        # master tkinter window
        self.master = Tk()
        self.master.title("Resolute")

        # variable for the color:
        self.background_color = "#CFF8FF"

        # set icon for master window
        # try:
        #     master.iconbitmap('filename.ico')
        # except:
        #     print("Couldn't load icon.")
        self.master.configure(background=self.background_color)

        def donothing():
            pass

        # example menu bar:
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)


        # Tkinter graphics loop:
        mainloop()
