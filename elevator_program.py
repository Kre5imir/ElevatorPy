from random import randint
from collections import deque

class Elevator(list):

    register_list = deque('')
    current_floor = 0
    direrction = 1

    def move(self):
        self.current_floor += self.direrction

    def search_floor(self, user):
        for people in self:
            if building_floor in
        self.register_list.append(self)

    def on_arrival(self):
        self.register_list.popleft()

class Building:

    snoop = Elevator()
    def __init__(self, building_floors, building_users):
        self.building_floors = building_floors
        self.building_users = building_users
        __class__.snoop.append(self)

    @property
    def getFloors(self):
        return self.building_floors

    @property
    def getUsers(self):
        return self.building_users

    def setFloores():
        building_floors = int(input())

    def setUsers():
        building_users = int(input())



class User(Building):

    current_floor = randint(1, 5)
    destination_floor = randint(1, 5)
    customer_ID = 0

    def yrange(n):
        while customer_ID < n:
            yield customer_ID
            customer_ID += 1
if __name__== "__main__":
    f = Building.setFloores()
    b = Building.setUsers()
    y = User.yrange(b)

    print(Elevator.register_list)


'''elevator = deque('abcdefghijklmnoprstuvz')
elevator.append('x')
elevator.popleft()
elevator.appendleft('1')
list(elevator)
a = elevator[0]
print(a)'''


