# Activity 2 POYLMORPHISM

## 1. Answer the following questions:
a. What is duck typing, as explained in the video?

- As explained in the video, duck typing is an alternative way to achieve polymorphism in Python without relying on inheritance. Rather than checking an object's specific class type or parent class, Python simply verifies whether the object possesses the minimum necessary attributes and methods required to perform a given action—following the idea that "if it looks like a duck and quacks like a duck, it must be a duck.".

b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

- To work inside the same loop as Dog and Cat without inheriting from the Animal class, the Car class needed to implement the exact members the loop accessed on every object: a speak() method (defined to print "HONK!") and an alive attribute (initially set to False and later changed to True when printed inside the loop).

## 2. Create a python code
[View the python code here!](activity2.py)

## 3. How does the code in 2.2 demonstrate polymorphism?

- It demonstrates polymorphism from the different methods in each class through duck typing, and the method start_trip() calls the methods of each object to print the move() of each vehicle.