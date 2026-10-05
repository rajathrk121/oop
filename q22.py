class Shape:
    def area(self):
        pass

class circle(Shape):
    def area(self):
        pi=3.14
        radius=int(input("Enter radius of the circle: "))
        area=pi*(radius*radius)
        print("Area of the circle is: ",area)

class rectangle(Shape):
    def area(self):
        length=int(input("Enter length of the recatngle: "))
        width=int(input("Enter width of the ractangle: "))
        area=length*width
        print("Area of the rectangle: ",area)
class triangle(Shape):
    def area(self):
        breadth=int(input("Enter breadth of the triangle: "))
        height=int(input("Enter height of the triangle: "))
        area=1/2*(breadth*height)
        print('Area of the triangle: ',area)

print("1. Circle \n2. Rectangle \n3. Triangle")
choice = int(input("Enter your choice: " ))
match choice :
    case 1:
        Area=circle()
    case 2:
        Area=rectangle()
    case 3:
        Area=triangle()
    case _:
        print("Invalid choice !!! Enter a valid choice...")
        exit()
Area.area()
