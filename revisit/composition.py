class Brick:
    def __init__(self, type_):
        self.type = type_

    def describe_brick(self):
        return f"I'm a {self.type} brick"

class Wall:
    brick_class = Brick

    def __init__(self, type_):
        self.bricks = self.brick_class("concrete")
        self.type = type_

    def describe_wall(self):
        return f"I'm a {self.type} wall made of {self.bricks.type} bricks"

class Building:
    wall_class = Wall

    def __init__(self):
        self.walls = self.wall_class("load-bearing")

    def describe_building(self):
        return f"I'm a Building with {self.walls.type} walls made of {self.walls.bricks.type} bricks"


class House(Building):
    wall_class = Wall

    def __init__(self):
        super().__init__()

    def describe_house(self):
        return f"I'm a House with {self.walls.type} walls made of {self.walls.bricks.type} bricks"
    
home1 = House()
print(home1.describe_house())
print(home1.describe_building())
print(home1.walls.describe_wall())
print(home1.walls.bricks.describe_brick())

print(home1.__dict__)

brick1 = Brick("red")
print(brick1.__dict__)