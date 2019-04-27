from tkinter import *
from tkinter import ttk
from random import randint
from collections import deque

class User():

    up = False
    down = False

    def __init__(self, user_ID, no_of_floors):
        self.user_ID =  user_ID
        self.current_floor = randint(1, no_of_floors)
        self.destination_floor = randint(1, no_of_floors)
        self.desired_direction = self.check_floor()

    def check_floor(self):
        if self.current_floor > self.destination_floor:
            self.down = True
        elif self.current_floor < self.destination_floor:
            self.up = True

    def __str__(self):
        print("user id {} destination floor is {} and current floor is {}" \
                .format(self.user_ID, self.destination_floor, self.current_floor))
    '''def yrange(n):
        i = 0
        while i < n:
            yield i
            i += 1
        '''
class Elevator():

    lift_register = deque()
    direction = 1

    def __init__(self):
        self.current_floor = 0#randint(0, Building.no_of_floors)

    #def __str__(self):
     #   return '{} curent floor'.format(self.current_floor)
    def move(self):
        self.current_floor += self.direction

    def on_arrival(self):
        for user in self.lift_register:
            if self.current_floor == user.destination_floor:
                self.exit(self)

    def on_enter(self, user):
        self.lift_register.append(user)

    def exit(self, user):
        self.lift_register.popleft(user)

class Building():

    building_users = []

    def __init__(self, users, floors):

        self.no_of_users = users#int(input('enterr no of users'))

        self.no_of_floors = 5#ttk.Entry(root)#int(input('pls enter number of floors'))

        '''list of people entering the building'''
        for i in range(self.no_of_users):
            self.building_users.append(User(i, self.no_of_floors))
        self.lift = Elevator()


    def default(self):
        if self.lift.current_floor >= self.no_of_floors - 1:
            self.lift.direction = -1
        elif self.lift.current_floor >= 0:
            self.lift.direction = 1

    def enter_user(self):
        for user in self.building_users:
            if user.current_floor == self.lift.current_floor:
                self.lift.lift_register.append(user)
                self.building_users.remove(user)

    def run(self):
        self.enter_user()
        self.default()
        self.lift.move()
        self.lift.on_arrival()

    def output(self):

        while True:
            self.run()
            for i in self.building_users:
                print("building_users {}".format(self.building_users))
            if len(self.building_users) >= 0 and len(self.lift.lift_register) >= 0:
                break
class Application(Tk):
    """  A GUI application  """

    def __init__(self, root):

        self.root = root
        self.frame_content = ttk.Frame(root)
        self.frame_content.grid()
        '''
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
        self.u = StringVar()
        self.entry_users = Entry(self.frame_content)
        self.entry_users.grid(row=1, column=1)
        self.confirm_button_2 = Button(self.frame_content, text="Ok", command = self.get_users)
        self.confirm_button_2.grid(row = 1, column = 2)
        self.users_result = Label(self.frame_content, text="this many users:", textvariable=self.u)
        self.users_result.grid(row=1, column=7)
        #zgrada = Building(self.entry_users, self.entryFloor)
        '''
        self.frame_content_2 = Frame(root)
        self.feet = StringVar()
        self.v = StringVar()
        self.b = IntVar()
        self.b.set(self.floors)
        self.feet.set(Elevator.current_floor)
        self.label_1 = Label(self.frame_content_2, textvariable = self.feet)
        self.label_1.grid(row=3, column = 0)

        self.text_result = Label(self.frame_content_2, text=None, textvariable=self.v)
        self.text_result.grid(row=2, column=0, sticky=W, columnspan=2)

        self.text_label = Label(self.frame_content_2, text="Enter text:")
        self.text_label.grid(row=0, column=0, sticky=W)
        self.text_input = Entry(self.frame_content_2)
        # self.text_input.bind("<Enter>", self.text_input.enter)
        self.text_input.grid(row=0, column=1, sticky=W + E)
        self.text_button = Button(self.frame_content_2, text="Get text input", command=self.text_input_enter)
        self.text_button.grid(row=1, column=1, sticky=E)

def main():
    root = Tk()
    
    app = Application(root)
    root.mainloop()

if __name__== "__main__":

    main()
