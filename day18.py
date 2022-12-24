with open("inputs/input18.txt") as file:
  cubeverse = {
    tuple([int(i) for i in l.split(",")]): 6 for l in file.read().split("\n")}

def get_closed_sides(neighbors):
  I = 0
  for neighbor in neighbors:
    if neighbor in cubeverse.keys():
        I += 1
  return I

for cube in cubeverse.keys():
  x, y, z = cube
  cubeverse[cube] -= get_closed_sides([(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)])
print(sum(cubeverse.values()))