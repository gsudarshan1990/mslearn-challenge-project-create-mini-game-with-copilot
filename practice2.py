# Write a generate a 10 by 10 grid of letters.

import random
def generate_grid(size=10):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    grid = []
    for _ in range(size):
        row = [random.choice(letters) for _ in range(size)]
        grid.append(row)
    return grid
