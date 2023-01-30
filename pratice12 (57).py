class A:
    def __init__(self, i = 0):
        self.i = i

class B(A):
    def __init__(self, j = 0):
        self.j = j
        super().__init__()

def main():
    b = B()
    print(b.j)
    print(b.i)

main()