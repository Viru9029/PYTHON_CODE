#Muliple Inheritance
class Parent1():
    def assign_string_one(self,str1):
        self.str1 = str1
    def show_string_one(self):
        return self.str1
class Parent2():
    def assign_string_second(self,str2):
        self.str2 = str2
    def show_string_two(self):
        return self.str2
class Child(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3 = str3
    def show_string_three(self):
        return self.str3
p1 = Child()
p1.assign_string_one('One')
p1.assign_string_second('Two')
p1.assign_string_three('Three')
p1.show_string_one()
print(p1.show_string_one())
print(p1.show_string_two())
print(p1.show_string_three())

