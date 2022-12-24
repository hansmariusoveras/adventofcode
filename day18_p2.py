import queue
import matplotlib.pyplot as plt
world = [[[1 for i in range(24)] for j in range(24)] for k in range(24)]

with open("inputs/input18.txt") as file:
  lines = file.read().split("\n")
for line in lines:
  x, y, z = line.split(",")
  x, y, z = int(x), int(y), int(z)
  world[x+1][y+1][z+1] = 0

q = queue.Queue()
q.put((0, 0, 0))

def get_neighbors(pos):
  x, y, z = pos
  return [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]

while not q.empty():
  pos = q.get()
  for x, y, z in get_neighbors(pos):
    if x < 0 or y < 0 or z < 0 or x > 23 or y > 23 or z > 23:
      continue
    if world[x][y][z] <= 0:
      world[x][y][z] -= 1
    elif world[x][y][z] == 1:
      world[x][y][z] = 2
      q.put((x, y, z))
  x0, y0, z0 = pos

# 3D BFS,
# Every time a cube is visited from a new direction,
# Append 1
K = 0
for z in world:
  for y in z:
    for x in y:
      if x < 0:
        K += x
print(K)