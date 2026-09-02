class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Alexus: Hello there, I am Alexus, your fellow bystander.")
        print(f"Alexus: Oh what's this? {self.name} is barking!")
        print(f"{self.name}: Woof Woof!")

s = input("Hey there, what's your name? ")
n = input(f"Hey {s}, what's your dog's name? ")
a = int(input("How old is your dog? "))

d1 = Dog(n, a)

d1.bark()