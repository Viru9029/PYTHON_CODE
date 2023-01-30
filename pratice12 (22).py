#Adding parameters to the class
class Phone:
    def set_color(self,color):
        self.set_color = color
    def set_cost(self,cost):
        self.set_cost = cost
    def show_color(self):
        return self.set_color
    def show_cost(self):
        return self.set_cost
    def make_call(self):
        print("Making phone call")
    def play_game(self):
        print("Playing game")
p2 = Phone()
p2.set_color('red')
p2.set_cost('Rs.12500')
print(p2.show_color())
print(p2.show_cost())
p2.make_call()
p2.play_game()