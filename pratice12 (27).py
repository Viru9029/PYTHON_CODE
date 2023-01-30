#Multi-level Inheritance
class Parent():
    def assign_name(self,name):
        self.name = name
    def show_name(self):
        return self.name
class Child(Parent):
    def assign_age(self,age):
        self.age = age
    def show_age(self):
        return self.age
class Grandchild(Child):
    def assign_gender(self,gender):
        self.gender = gender
    def show_gender(self):
        return self.gender
gc = Grandchild()
gc.assign_name("SAM")
gc.assign_age(25)
gc.assign_gender("Male")
print(gc.show_name())
print(gc.show_age())
print(gc.show_gender())