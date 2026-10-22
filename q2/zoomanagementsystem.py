class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def eat(self):
        return f"{self.__name} eats."  # Returns a string indicating that the animal eats.

    def make_sound(self):
        return f"{self.__name} makes a sound."  # Returns a string indicating that the animal makes a sound.

class Lion(Animal):
    def __init__(self, name):
        self.__name = name  # Private attribute
        super().__init__(name)  # Calls the constructor of the parent class Animal.

    def eat(self):
        return f"{self.__name} eats fresh meat."  # Returns a string indicating that the lion eats fresh meat.

    def make_sound(self):
        return f"{self.__name} roars loudly!"  # Returns a string indicating that the lion roars loudly.

class Elephant(Animal):
    def __init__(self, name):
        self.__name = name  # Private attribute
        super().__init__(name)  # Calls the constructor of the parent class Animal.

    def eat(self):
        return f"{self.__name} eats grass and fruits."  # Returns a string indicating that the elephant eats grass and fruits.

    def make_sound(self):
        return f"{self.__name} trumpets!"  # Returns a string indicating that the elephant trumpets.

class Monkey(Animal):
    def __init__(self, name):
        self.__name = name  # Private attribute
        super().__init__(name)  # Calls the constructor of the parent class Animal.

    def eat(self):
        return f"{self.__name} eats bananas."  # Returns a string indicating that the monkey eats bananas.

    def make_sound(self):
        return f"{self.__name} chatters!"  # Returns a string indicating that the monkey chatters.

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")