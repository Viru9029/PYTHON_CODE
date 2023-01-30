#creating a class with constructor
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary =salary
        self.gender = gender
    def employee_details(self):
        print("Name of employee : ",self.name)
        print("Age of employee : ",self.age)
        print("Salary of employee : ",self.salary)
        print("Gender of employee : ",self.gender)
e1 = Employee('Sam',25,"Rs.75000","Male")
print(e1.employee_details())