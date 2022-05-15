import random
from random import sample
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def remove(arr):

    kill = random.randint(0, len(arr) - 1)
    if kill == len(arr) - 1:
        remove(arr)
    else:
        arr.pop(kill)


for x in range(0, 9):
    remove(arr)
    print(arr)