from tkinter import *
from tkinter import ttk
from random import randint

class User():
    '''user will get ID from length of users entered on input entry
        it ha a current floor, destination floor and class variable for direction'''
    up = False
    down = False

    def __init__(self, user_ID, no_of_floors):
        self.user_ID =  user_ID
        self.current_floor = randint(1, no_of_floors)
        self.destination_floor = randint(1, no_of_floors)
        self.check_floor()

    def check_floor(self):
        """"compare current floor with destination floor
         to get desired direction of each user"""
        if self.current_floor > self.destination_floor:
            self.down = True
        elif self.current_floor < self.destination_floor:
            self.up = True

    def __str__(self):
        print("user id {} destination floor is {} and current floor is {}" \
                .format(self.user_ID, self.destination_floor, self.current_floor))

class Elevator():
    '''Elevator has his list that will add user if matched with current floor and remove it if
        destination floor is met'''
    lift_register = list()
    direction = 1

    def __init__(self):
        ''' initialize current floor of elevator
        '''
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
        self.lift_register.remove(user)

class Building():
    '''Building has a list of user, number of users and floors'''
    building_users = []

    def __init__(self, users, floors):

        self.no_of_users = users #int(input('enterr no of users'))

        self.no_of_floors = floors #int(input('pls enter number of floors'))

        '''list of people entering the building'''
        for i in range(self.no_of_users):
            self.building_users.append(User(i, self.no_of_floors)) # i represents ID of user, number of floors
                                                                    # is needed not to go over with random
        self.lift = Elevator()


    def default(self):
        """"moving from floor to floor, top to bottom, default strategy"""
        if self.lift.current_floor >= self.no_of_floors - 1:
            self.lift.direction = -1
        elif self.lift.current_floor >= 0:
            self.lift.direction = 1

    def enter_user(self):
        '''check from list of users is elevator on same floor
        as user so he can be copied to lift register list, and removed '''
        for user in self.building_users:
            if user.current_floor == self.lift.current_floor:
                self.lift.lift_register.append(user)
                self.building_users.remove(user)

    def run(self):
        self.enter_user() #compare current floor of user and elevator this (function beongs to Buildeing class)
        self.default() #move elevator one floor up or down(this function beongs to Buildeing class)
        self.lift.move() #move by direction Elevetor object function
        self.lift.on_arrival() #remove user if on desired floor, Elevators function

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

        '''this is entry for floors '''
        self.floors = Label(self.frame_content, text = "how many floors:")
        self.floors.grid(row = 0, column = 0)
        self.f = IntVar()
        self.entryFloor = Entry(self.frame_content)
        self.entryFloor.grid(row = 0, column = 1)
        self.confirm_button_1 = Button(self.frame_content, text="Ok", command=self.get_floors)
        self.confirm_button_1.grid(row=0, column=2)
        self.floors_in_building = Label(self.frame_content, text="this many floors:", textvariable = self.f)
        self.floors_in_building.grid(row=0, column=7)
        '''this is entry for users '''
        self.users = Label(self.frame_content, text="how many users:")
        self.users.grid(row=1, column=0)
        self.u = IntVar()
        self.entry_users = Entry(self.frame_content)
        self.entry_users.grid(row=1, column=1)
        self.confirm_button_2 = Button(self.frame_content, text="Ok", command = self.get_users)
        self.confirm_button_2.grid(row = 1, column = 2)
        self.users_result = Label(self.frame_content, text="this many users:", textvariable=self.u)
        self.users_result.grid(row=1, column=7)
        ''' button to run program'''
        self.text_button = Button(self.frame_content, text="elevator works", command=self.do_job)
        self.text_button.grid(row=2, column=1, sticky=E)

    def do_job(self):
        '''this function to create building and start elevator'''
        B = Building(self.f.get(), self.u.get())
        B.output()

    def get_floors(self):
        '''entry on button to collect number of floors'''
        self.f.set(self.entryFloor.get())

    def get_users(self):
        '''entry to collect number of users'''
        self.u.set(self.entry_users.get())

def main():
    root = Tk()
    app = Application(root)
    root.mainloop()

if __name__== "__main__":

    main()
