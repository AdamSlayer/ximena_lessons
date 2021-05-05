#---------------------------[Exercise1]------------------------------

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        self.name=name

    # def seating_capacity(self, capacity):
    #     return f'The seating capacity of a {self.name} is {capacity} passengers'

modelX = Vehicle('ModelX', 300, 2200)
print(modelX.max_speed, modelX.mileage)

#---------------------------[Exercise2]------------------------------

#class Vehicle:
#    pass

#---------------------------[Exercise3]------------------------------

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
            return super().seating_capacity(capacity=50)





Batman_bus = Bus("Batman v2.0", 100, 30000)
print(Batman_bus.seating_capacity)

mybus = Bus("Volvo bus", 180, 12)
print(mybus.max_speed, mybus.mileage)
