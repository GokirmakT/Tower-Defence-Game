import random
types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
type = []

for x in range(0, 5):

    random_type = random.choice(types)

    for t in type:
        if t == random_type:
            random_type = random.choice(types)

    type.append(random_type)

print(type)

