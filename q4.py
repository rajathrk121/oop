class circle:
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14

    def area(self):

        return self.pi*(self.radius*self.radius)

circle1=circle(5)

print(circle1.area())