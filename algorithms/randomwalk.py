# a random walk using a monte carlo sim.:
import random
import math

def random_walk(n):
    # return coordinates afer walking 'n' blocks
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == "N":
            y = y + 1
        elif step == "S":
            y = y - 1
        elif step == "E":
            x = x + 1
        else:
            x = x - 1
    return [x,y]

# print(random_walk(10))

def find_distances(range_n, walk_n):
    distances = []
    for i in range(range_n):
        walk = random_walk(walk_n)
        distance = math.sqrt(abs((walk[0]^2+walk[1]^2)))
        distances.append(distance)
    return distances

print(find_distances(10,10)))