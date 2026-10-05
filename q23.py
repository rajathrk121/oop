class Animal():
    def sound(self):
        print("Anima sound")
class Dog(Animal):
    def sound(self):
        print("Bow Bow")
class Cat(Animal):
    def sound(self):
        print("Meowww")

class Cow(Animal):
    def sound(self):
        print("Moooo")

Dog=Dog()
Cat=Cat()
Cow=Cow()

Dog.sound()
Cat.sound()
Cow.sound()
