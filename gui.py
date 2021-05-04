from tkinter import *
import os
import util
from sentence import *

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
        self.sentence = Sentence()

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

        self.canvas_height = 400
        self.canvas_width = 400

        self.canvas = Canvas(self.master, bg="white", height=self.canvas_height, width=self.canvas_width)
        self.canvas.grid(row = 0, column = 0, columnspan=5)

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
        self.last_input_entry.grid(row = 4+self.num_input_boxes, column = 1, columnspan = 3)
        self.input_boxes.append(self.last_input_entry)

        self.num_input_boxes += 1
        self.therefore_label = Label(self.master, anchor = NE, justify = LEFT, text = "∴", bg = self.background_color)
        self.therefore_label.grid(row = 4+self.num_input_boxes, column = 0)
        self.input_boxes.append(self.therefore_label)
        var = StringVar()
        self.therefore_entry = Entry(self.master, textvariable = var, width=35)
        self.input_vars.append(var)
        self.therefore_entry.grid(row = 4+self.num_input_boxes, column = 1, columnspan = 3)
        self.input_boxes.append(self.therefore_entry)

        self.add_button = Button(self.master, text = "Add Sentence", command = self.make_input_box)
        self.add_button.grid(row = 3, column = 0)
        self.remove_button = Button(self.master, text = "Remove Sentence", command = self.remove_input_box)
        self.remove_button.grid(row = 3, column = 1, sticky = "W")


        self.solve_button = Button(self.master, text = "Solve", command = self.solve)
        self.solve_button.grid(row = 3, column = 2, stick="W")
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
        i.grid(row = 3+self.num_input_boxes, column = 1, columnspan = 3)
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

    def solve(self):
        print("Solving...")
        for v in self.input_vars:
            self.sentence.addStatement(v.get())
            print(v.get())
        self.sentence.createResolutionStart()
        self.sentence.printResolution()
        solution = self.sentence.solve()
        # print(solution)
        self.draw_graph(solution)

    def draw_graph(self, solution):
        locations = dict()
        level_counts = dict()
        for l in solution.values():
            if l[0] not in level_counts:
                level_counts[l[0]] = 1
            else:
                level_counts[l[0]] += 1
        y_spacing = (self.canvas_height )/(len(level_counts)+1)
        for level in level_counts.keys():
            x_spacing = (self.canvas_width)/(level_counts[level]+1)
            count = 0
            # print(count)
            for s in solution.keys():
                count += 1
                if (solution[s][0] == level):
                    node = str(s).replace("\',)", "}").replace("(", "{").replace(")", "}").replace("'", "")
                    loc = x_spacing * count, y_spacing * (level+1)
                    self.canvas.create_text(loc[0], loc[1], text = node)
                    locations[s] = loc
        print(level_counts)
        return
