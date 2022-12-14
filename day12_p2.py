from queue import PriorityQueue
import matplotlib.pyplot as plt
import numpy as np

with open("inputs/input12.txt") as file:
  map = [[[25-(ord(i) - 97), 500, (0,0)] for i in list(x)] for x in file.read().split("\n")]

def get_possible_neighbors(pos):
  posx, posy = pos
  neighbors = []
  for r,c in [(posx+1, posy), (posx-1, posy), (posx, posy+1), (posx, posy-1)]:
    if r < 0 or c < 0:
      continue
    try:
      neighbors.append((r, c)) if (map[r][c][0] - map[posx][posy][0]) <= 1 else 0
    except:
      pass

  return neighbors
  
def calculate(pos, E):
  return 0

S = (20, 120)
E = (0,0)
nodes = PriorityQueue()
current = (None, None, None)
nodes.put((calculate(S, E), 0, S))
while current[2] != E:
  current = nodes.get()
  h, dist, pos = current
  print(h, dist, pos)
  r,c = pos
  if map[r][c][0] == 25:
    print(h,dist,pos)
    break
  for n_pos in get_possible_neighbors(pos):
    
    r, c = n_pos
    if map[r][c][1] > dist+1:
      map[r][c][1] = dist+1
      map[r][c][2] = pos
      nodes.put((calculate(n_pos, E)+dist+1, dist+1, n_pos))
K = pos
#while K != S:
#  map[K[0]][K[1]][1] = 10000
#  K = map[K[0]][K[1]][2]



plt.imshow([ [s[1] for s in t] for t in map])
plt.show()