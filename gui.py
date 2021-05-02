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
        # window = Toplevel(self.master)
        # window.geometry("500x500")
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

        self.input_boxes = []
        self.num_input_boxes = 0
        self.input_vars = []

        self.num_input_boxes += 1
        self.last_input_label = Label(self.master, anchor = NE, justify = LEFT, text = "Sentence " + str(self.num_input_boxes), bg = self.background_color)
        self.last_input_label.grid(row = 4+self.num_input_boxes, column = 0)
        self.input_boxes.append(self.last_input_label)
        var = StringVar()
        self.last_input_entry = Entry(self.master, textvariable = var, width=35)
        self.input_vars.append(var)
        self.last_input_entry.grid(row = 4+self.num_input_boxes, column = 1)
        self.input_boxes.append(self.last_input_entry)

        self.num_input_boxes += 1
        self.therefore_label = Label(self.master, anchor = NE, justify = LEFT, text = "∴", bg = self.background_color)
        self.therefore_label.grid(row = 4+self.num_input_boxes, column = 0)
        self.input_boxes.append(self.therefore_label)
        var = StringVar()
        self.therefore_entry = Entry(self.master, textvariable = var, width=35)
        self.input_vars.append(var)
        self.therefore_entry.grid(row = 4+self.num_input_boxes, column = 1)
        self.input_boxes.append(self.therefore_entry)

        self.add_button = Button(self.master, text = "Add Sentence", command = self.make_input_box)
        self.add_button.grid(row = 3, column = 0)
        self.remove_button = Button(self.master, text = "Remove Sentence", command = self.remove_input_box)
        self.remove_button.grid(row = 3, column = 1, sticky = "W")
        # self.make_input_box()
        # self.make_input_box()
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
        newWindow.geometry("200x100")

        # A Label widget to show in toplevel
        Label(newWindow, anchor = NE, wraplength = 200, justify = LEFT,
              text ="Resolute was created in 2021 by Matthew Youngbar, Gwyneth Yuen, and Connor Lenahan.\n This program was created for Professor Bram Van Heuveln as a part of Computability and Logic at RPI.").pack()

    def make_input_box(self):
        self.num_input_boxes += 1
        l = Label(self.master, anchor = NE, justify = LEFT, text = "Sentence " + str(self.num_input_boxes - 1), bg = self.background_color)
        l.grid(row = 3+self.num_input_boxes, column = 0)
        self.input_boxes.append(l)
        var = StringVar()
        i = Entry(self.master, textvariable = var, width=35)
        self.input_vars.append(var)
        i.grid(row = 3+self.num_input_boxes, column = 1)
        self.input_boxes.append(i)
        self.therefore_label.grid(row = 4+self.num_input_boxes, column = 0)
        self.therefore_entry.grid(row = 4+self.num_input_boxes, column = 1)

    def remove_input_box(self):
        if (self.num_input_boxes > 2):
            last_input_entry = self.input_boxes.pop()
            last_input_label = self.input_boxes.pop()
            self.input_vars.pop()
            last_input_entry.destroy()
            last_input_label.destroy()
            self.num_input_boxes -= 1
