class Car:
    def move(self):
        print("The car drives on the road.") # Outputs "The car drives on the road." when the move method is called

class Boat:
    def move(self):
        print("The boat sails on water.") # Outputs "The boat sails on water." when the move method is called

class Drone:
    def move(self):
        print("The drone flies in the air.") # Outputs "The drone flies in the air." when the move method is called

def start_trip(vehicle):
    vehicle.move() # Calls the move method of the vehicle object

car1 = Car() # Creates an object of the Car class
boat1 = Boat() # Creates an object of the Boat class
drone1 = Drone() # Creates an object of the Drone class

start_trip(car1) # Calls the start_trip function with car1 as an argument
start_trip(boat1) # Calls the start_trip function with boat1 as an argument
start_trip(drone1) # Calls the start_trip function with drone1 as an argument
