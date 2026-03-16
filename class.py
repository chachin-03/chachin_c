class Room:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

room = Room(42.5, 30.8)
print("the room area is:",room.area())  
