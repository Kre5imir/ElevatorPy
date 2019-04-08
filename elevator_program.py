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
        self.down = False
        self.up = False
    '''def __str__(self):

            print("user id {} destination floor is {} and current floor is {}" \
                  .format(self.user_ID, self.destination_floor, self.current_floor))'''
    def yrange(n):
        i = 0
        while i < n:
            yield i
            i += 1
    def choose_direction(self):
        if self.destination_floor > self.current_floor:
             self.up = True
        else:
            self.down = True

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
    print(U)
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
            E.up = True
            while True:
                if User.choose_direction(user_list) == User.up:
                    register_list.append(i.user_ID)
                else:
                    register_list.append(i.user_ID)





    print(register_list)
if __name__== "__main__":

    main()
