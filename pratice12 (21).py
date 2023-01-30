#creating the class
class Phone:
    def make_call(self):
        print("Making phone call")
    def play_game(self):
        print("playing game")
p1 = Phone()#instantiating the object
print(p1.make_call())#invoking methods through object
print(p1.play_game())
