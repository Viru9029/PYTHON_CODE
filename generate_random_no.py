# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
import random2


def generate_rand_no(start, end, div):
    for i in range(3):
        a = random2.randrange(100, 999, 5)
        yield a


print(next(generate_rand_no(100, 99, 5)))
# print(generate_rand_no(100,999,5,3))
