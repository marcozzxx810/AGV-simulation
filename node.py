import math


class Carn:
    
    def __init__ (self, Carn_type, x, y):
        self.Carn_type = Carn_type
        self.x = x
        self.y = y

    def finddistance (self, node):
        distance = math.sqrt( (self.x - node.x) ** 2 + (self.y - node.y) ** 2 )
        return distance


class node:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def finddistance (self, node):
        distance = math.sqrt( (self.x - node.x) ** 2 + (self.y - node.y) ** 2 )
        return distance







