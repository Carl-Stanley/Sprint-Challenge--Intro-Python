# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Dropping the Base class.

class Vehicle:
    pass

# Sub class FlightVehicle
class FlightVehicle(Vehicle):
    pass

# Sub class Starship
 
class Starship(FlightVehicle):
    pass

#Sub class Airplane

class Airplane(FlightVehicle):
    pass

#Sub class GroundVehicle
class GroundVehicle(Vehicle):
    pass

#Sub class Car
class Car(GroundVehicle):
    pass

#Sub class Motorcycle
class Motorcycle(GroundVehicle):
    pass