class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        print(self.a - self.b)

    def mul(self):
        print(self.a * self.b)

    def div(self):
        print(self.a / self.b)


result = Calculator(10,20)
result.add()
result.sub()
result.div()
result.mul()