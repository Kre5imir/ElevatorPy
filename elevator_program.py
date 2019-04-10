from random import randint
from collections import deque

class Building():
    building_users = []
    no_of_users = int(input('enterr no of users'))
    no_of_floors = int(input('pls enter number of floors'))

class User():
    up = False
    down = False

    def __init__(self, user_ID):
        self.user_ID =  user_ID
        self.current_floor = randint(1, Building.no_of_floors)
        self.destination_floor = randint(1,Building.no_of_floors)

    def choice(self):
        if self.current_floor > self.destination_floor:
            return up
    '''def __str__(self):

            print("user id {} destination floor is {} and current floor is {}" \
                  .format(self.user_ID, self.destination_floor, self.current_floor))'''
    '''def yrange(n):
        i = 0
        while i < n:
            yield i
            i += 1
        '''
class Elevator():

    register_list = deque()
    current_floor = randint(0, Building.no_of_floors)
    direrction_UP = False
    direrction_DOWN = False

    def on_enter(self, reg_list):
        self/reg_list.append(self)

    def on_arrival(self, reg_list):
        self.register_list.popleft()

def main():
    B = Building()
    user_list = B.building_users
    no_of_users = B.no_of_users

    E = Elevator()
    on_inside = E.register_list


    for i in range(no_of_users):
        user_list.append(User(i))


    print(E.current_floor)
    print()
    for i in user_list:
        print("user id {} destination floor is {} and current floor is {} elvator current floor {}" \
              .format(i.user_ID, i.destination_floor, i.current_floor, E.current_floor))

        if E.current_floor < i.current_floor:
            #E.up = True
           # while True:
                if i.up == E.up:
                    on_inside.append(i)
                #False
    print("user id {} destination floor is {} and current floor is {} elvator current floor {}" \
          .format(i.user_ID, i.destination_floor, i.current_floor, E.current_floor))
    print(user_list[0])
if __name__== "__main__":

    main()
