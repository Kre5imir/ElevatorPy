from random import randint
from collections import deque

class Building():
    building_users = []
    no_of_users = int(input('enterr no of users'))
    no_of_floors = int(input('pls enter number of floors'))

class User(Building):

    def __init__(self, user_ID):
        self.user_ID = user_ID
        self.current_floor = randint(1, Building.no_of_floors)
        self.destination_floor = randint(1,Building.no_of_floors)
        self.downwards = self.current_floor > self.destination_floor
        self.up = self.current_floor < self.destination_floor
    '''def __str__(self):

            print("user id {} destination floor is {} and current floor is {}" \
                  .format(self.user_ID, self.destination_floor, self.current_floor))'''
    def yrange(n):
        i = 0
        while i < n:
            yield i
            i += 1

class Elevator():
    down = False
    up = False

    register_list = []
    on_bord_list = deque()
    current_floor = randint(0, Building.no_of_floors)
    direrction_UP = False
    direrction_DOWN = False

    def on_enter(self, reg_list):
        self.on_bord_list.append(self)

    def on_arrival(self):
        self.on_bord_list.popleft()

def main():
    B = Building()
    user_list = B.building_users
    no_of_users = B.no_of_users

    gen_ID = User.yrange(no_of_users)
    U = User(gen_ID)

    E = Elevator()
    register_list = E.on_bord_list

    for i in range(no_of_users):
        user_list.append(User(User.yrange(no_of_users)))


    print(E.current_floor)
    print()
    for i in user_list:
        print("user id {} destination floor is {} and current floor is {}" \
              .format(i.user_ID, i.destination_floor, i.current_floor))

        if E.current_floor < i.current_floor:
            #E.up = True
           # while True:
                if i.up == i.up:
                    register_list.append(i.user_ID)
                #False

    for i in register_list:
        print(i)
if __name__== "__main__":

    main()
