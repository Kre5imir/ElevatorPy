from random import randint
from collections import deque

print('enter number of floors')

class Building:

    building_floors = int(input())

class Elevator(Building):

    register_list = deque('')
    current_floor = 0
    direrction = 1

    def move(self):
        self.current_floor += self.direrction

    def register_user(self, customer):
        self.register_list.append(customer.customer_ID)

    def on_arrival(self):
        self.register_list.popleft()

class Customer(Building):

    def __init__(self, customer_ID, current_floor, destination_floor):
        self.customer_ID =+ 1
        self.current_floor = current_floor #randint(1, Building.building_floors )
        self.destination_floor = destination_floor #randint(1, Building.building_floors )
