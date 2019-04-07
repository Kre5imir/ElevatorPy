from random import randint
from collections import deque

class Building():
    building_users = []
    no_of_users = int(input('enterr no of users'))
    no_of_floors = int(input('pls enter number of floors'))

class User(Building):

    down = False
    up = False

    def __init__(self, user_ID):
        self.user_ID = user_ID
        self.current_floor = randint(1, Building.no_of_floors)
        self.destination_floor = randint(1,Building.no_of_floors)

    def __str__(self):

            print("user id {} destination floor is {} and current floor is {}" \
                  .format(self.user_ID, self.destination_floor, self.current_floor))

    def yrange(n):
        i = 0
        while i < n:
            yield i
            i += 1

class Elevator():
    register_list = []
    on_bord_list = deque
    current_floor = 0
    direrction_UP = False
    direrction_DOWN = False

    def on_enter(self, reg_list):
        self.on_bord_list.append(self)

    def on_arrival(self):
        self.on_bord_list.popleft()



if __name__== "__main__":

    a = Building.building_users
    for i in User.yrange(Building.no_of_users):
        a.append(User(i))

    c = Elevator.on_bord_list

    ele = Elevator()
    for i in range(a):
        print(a[1])
    if ele.current_floor < a[0].current_floor :
           print("you ca get out")
