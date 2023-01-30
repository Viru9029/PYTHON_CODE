#over-riding init method
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_details(self):
        print("Vehicle here")
        print("Mileage of Vehicle : ",self.mileage)
        print("Cost of Vehicle : ",self.cost)
class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,HoursPower):
        super().__init__(mileage,cost)
        self.tyres = tyres
        self.HoursPower = HoursPower
    def show_car_details(self):
        print("Car here")
        print("Company of Tyre : ",self.tyres)
        print("Horse Power of car : ",self.HoursPower)
c1 = Car(50,"Rs.152436.00","MRF",1500)
print(c1.show_details())
print(c1.show_car_details())