
class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def bark(self):
        print(f"The {self._breed} named {self._name} says woof!")


dog1 = Dog("Wolf", "GSD")

dog2 = Dog("Pup", "Shitzu")

dog1.bark()
dog2.bark()

