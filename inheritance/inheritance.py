class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, I'm {self.name}")


class Student(Person):
    
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


class Animal: 
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} says something generic")
        
        
class Dog(Animal):
    def make_sound(self):
         print(f"{self.name} says Woof!")        


class Cat(Animal):
    def make_sound(self):
         print(f"{self.name} says Meow!")        


dog = Dog("Troy")
cat = Cat("Crook") 

dog.make_sound()
cat.make_sound()
