from tkinter import *
from tkinter import ttk

class Data(object):
    """  The data class  """

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.no_of_users = ttk.Entry(root)  # int(input('enterr no of users'))
        self.no_of_users.grid(row=0, column=1)


class Data2(object):
    """  The data class  """

    def __init__(self, name, value):
        self.name2 = name
        self.value2 = value

class RedFrame(Frame):
    def __init__(self, root):
        super(RedFrame, self).__init__()
        self["height"] = 150
        self["width"] = 150
        self["relief"] = RAISED
        self["bg"] = "red"
        self["bd"] = 8


class Application(Tk):
    """  A GUI application  """

    def __init__(self, root, other_instance, o2):
        self.root = root
        self.frame_content = ttk.Frame(root)
        self.frame_content.grid()

        self.floors = Label(self.frame_content, text = "how many floors:")
        self.floors.grid(row = 0, column = 0)
        self.f = StringVar()
        self.entryFloor = Entry(self.frame_content)
        self.entryFloor.grid(row = 0, column = 1)
        self.confirm_button_1 = Button(self.frame_content, text="Ok", command=self.get_floors)
        self.confirm_button_1.grid(row=0, column=2)
        self.floors_in_building = Label(self.frame_content, text="this many floors:", textvariable = self.f)
        self.floors_in_building.grid(row=0, column=7)

        self.users = Label(self.frame_content, text="how many users:")
        self.users.grid(row=1, column=0)
        #function get users will store in strinVar 'u' number from Entry 'entry_users'
        self.u = StringVar()
        self.entry_users = Entry(self.frame_content)
        self.entry_users.grid(row=1, column=1)
        self.confirm_button_2 = Button(self.frame_content, text="Ok", command = self.get_users)
        self.confirm_button_2.grid(row = 1, column = 2)
        self.users_result = Label(self.frame_content, text="this many users:", textvariable=self.u)
        self.users_result.grid(row=1, column=7)

        self.frame_content_2 = Frame(root)
        self.feet = StringVar()
        self.v = StringVar()
        self.b = IntVar()
        self.b.set(self.floors)
        self.feet.set(o2.name)
        self.label_1 = Label(self.frame_content_2, textvariable = self.feet)
        self.label_1.grid(row=3, column = 0)
        print(o2.name)


        self.text_result = Label(self.frame_content_2, text=None, textvariable=self.v)
        self.text_result.grid(row=2, column=0, sticky=W, columnspan=2)

        self.text_label = Label(self.frame_content_2, text="Enter text:")
        self.text_label.grid(row=0, column=0, sticky=W)
        self.text_input = Entry(self.frame_content_2)
        # self.text_input.bind("<Enter>", self.text_input.enter)
        self.text_input.grid(row=0, column=1, sticky=W + E)
        self.text_button = Button(self.frame_content_2, text="Get text input", command=self.text_input_enter)
        self.text_button.grid(row=1, column=1, sticky=E)

    def create(self):
        for x in range(3):
            for y in range(4):
                btn = RedFrame(self.frame_content)
                btn.grid(column=x, row=y, sticky=N + S + E + W)

    def get_floors(self):
        self.f.set(self.entryFloor.get())

    def get_users(self):
        self.u.set(self.entry_users.get())

    def text_input_enter(self):
        self.v.set(self.text_input.get())
        print("You entered: {}".format(self.text_input.get()))

if __name__ == "__main__":
    root = Tk()
    testRed = RedFrame(root)
    testData = Data(gui.u,gui.f)
    testData2 = Data("kresimir2", "some value2")
    print(testData2.name, testData.value)

    app = Application(root, testData, testData2)
    root.mainloop()



