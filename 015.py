import math

def main(grid_size):
    points = (grid_size + 1)**2
    sol = math.sqrt(math.comb(points,grid_size))
    return sol

print(main(20))