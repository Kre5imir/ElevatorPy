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
                self.exit()

    def on_enter(self, user):
        self.lift_register.append(user)

    def exit(self, user):
        self.lift_register.popleft(user)

class Building():

    building_users = []

    def __init__(self):
        self.no_of_users = int(input('enterr no of users'))
        self.no_of_floors = int(input('pls enter number of floors'))
        '''list of people entering the building'''
        for i in range(self.no_of_users):
            self.building_users.append(User(i, self.no_of_floors))
        self.lift = Elevator()

    def default(self):
        if self.lift.current_floor < self.no_of_floors:
            self.lift.direction = 1
        elif self.lift.current_floor >= 0:
            self.lift.direction = -1

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
            if len(self.building_users) > 0 or len(self.lift.lift_register) > 0:
                break

def main():

    B = Building()
    B.output()

if __name__== "__main__":

    main()
