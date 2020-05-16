# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels
    # method drive
    def drive(self):
        return f"vroooom"


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# MotorCycle Class
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        self.num_wheels = num_wheels
    #BRAAAP!!! - That's a weird sound for a motorcyle to make. Is the service light on?
    def drive(self):
        return f"BRAAAP!!"


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# Printing from list
for i in vehicles:
    print(i.drive())
