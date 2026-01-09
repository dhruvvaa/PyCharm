"""
ATTRIBUTES:
occupants attribute which is 0 by default
floor attribute which is 0 by default

METHODS:
add_occupants
go to floor

PROPERTIES:
occupants can only be added if the occupants limit has not been exceeded
only floors from -5 to 50 exist
"""

class Elevator:
    occupancy_limit = 8

    def __init__(self, occupants = 0):
            self.floor = 0
            if occupants <= Elevator.occupancy_limit:
                self.occupants = occupants
            else:
                self.occupants = Elevator.occupancy_limit
                print("too many occupants",occupants-Elevator.occupancy_limit,"left outside")

    def add_occupants(self, num):
        self.occupants += num
        if self.occupants > Elevator.occupancy_limit:
            print("too many occupants",self.occupants-Elevator.occupancy_limit,"left outside")
            self.occupants = Elevator.occupancy_limit

    def remove_occupants(self, num):
        if self.occupants - num > 0:
            self.occupants -= num
        else:
            print("elevator empty")
            self.occupants = 0

    def go_to_floor(self,floor):
        if floor < -5 or floor > 50:
            print("floor out of bounds")
        else:
            self.floor = floor

elevator1 = Elevator(6)
elevator1.add_occupants(7)
elevator2 = Elevator(11)
elevator2.add_occupants(20)
elevator1.go_to_floor(20)
print(elevator1.__dict__)
print(elevator2.__dict__)