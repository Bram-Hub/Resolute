from tkinter import *
import os
import util

class resolute_gui:
    def __init__(self):
        # make "program_files" folder if it doesn't exist
        # if not os.path.exists("program_files"):
        #     os.makedirs("program_files")
        # try:
        #     defau = open("program_files/defaults.txt", 'r')
        #     defaults = defau.read().split('\n')
        #     defau.close()
        # except:
        #     defaults = ['1', "", "", "", "1", "1"]

        # master tkinter window
        self.master = Tk()
        self.master.title("Resolute")

        # variable for the color:
        self.background_color = "#CFF8FF"

        # set icon for master window
        ico_path = util.resource_path("img/favicon.ico")
        try:
            self.master.iconbitmap(ico_path)
        except:
            print("Couldn't load icon.")

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
        helpmenu.add_command(label="About...", command=self.about_window)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)


        # Tkinter graphics loop:
        mainloop()

    def about_window(self):
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(self.master)

        # sets the title of the
        # Toplevel widget
        newWindow.title("About")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        Label(newWindow, anchor = NE, wraplength = 200, justify = LEFT,
              text ="Resolute was created in 2021 by Matthew Youngbar, Gwyneth Yuen, and Connor Lenahan.\n This program was created for Professor Bram Van Heuveln as a part of Computability and Logic at RPI.").pack()
