numbers = [int(i) for i in input("Enter the numbers : ").split(",")] #split takes only str values so when you want to take more values so you have to make list compensation.
square = []
for i in numbers:
    square.append(i * i)
print(square)
print('\n')

#second way
squared = [i * i for i in numbers]
print(squared)