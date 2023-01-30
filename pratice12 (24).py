#example of single inheritance
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_details(self):
        print("*********** I am a Vehicle **********")
        print("Mileage of Vehicle is : ",self.mileage)
        print("Cost of Vehicle is : ",self.cost)
class Car(Vehicle):
    def show_car(self):
        print("Car is here")
c1=Car(20,'Rs.2530.200')
print(c1.show_details())
print(c1.show_car())