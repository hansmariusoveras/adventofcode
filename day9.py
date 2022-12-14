import matplotlib.pyplot as plt
import numpy as np
with open("inputs/input9.txt") as file:
  lines = file.readlines()
current = (0, 0)
tails = [(0, 0) for i in range(9)]

def align_tail(head, tail):
  if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
    st = (head[0] - tail[0], head[1] - tail[1])
    if head[0] != tail[0] and head[1] != tail[1]:
      st = (tail[0] + np.sign(st[0]), tail[1] + np.sign(st[1])) 
    else:
      st = (tail[0] + np.sign(st[0])*(abs(st[0])- 1) , tail[1] + np.sign(st[1]) * (abs(st[1])-1)) 
    return st
  return tail
TAIL = 8
positions = set()
wositions = set()
for line in lines:
  line = line.strip()
  letter, length = line.split()
  length = int(length)
  if letter == 'L':
    for i in range(length):
      current = (current[0] - 1, current[1])
      tails[0] = align_tail(current, tails[0])
      for i in range(1, len(tails)):
        tails[i] = align_tail(tails[i-1], tails[i])
      positions.add(tails[TAIL])
  elif letter == 'R':
    for i in range(length):
      current = (current[0] + 1, current[1])
      tails[0] = align_tail(current, tails[0])
      for i in range(1, len(tails)):
        tails[i] = align_tail(tails[i-1], tails[i])
      positions.add(tails[TAIL])
  elif letter == 'U':
    for i in range(length):
      current = (current[0], current[1] - 1)
      tails[0] = align_tail(current, tails[0])
      for i in range(1, len(tails)):
        tails[i] = align_tail(tails[i-1], tails[i])
      positions.add(tails[TAIL])
  elif letter == 'D':
    for i in range(length):
      current = (current[0], current[1] + 1)
      tails[0] = align_tail(current, tails[0])
      for i in range(1, len(tails)):
        tails[i] = align_tail(tails[i-1], tails[i])
      positions.add(tails[TAIL])
  

r = [[0 for i in range(512)] for i in range(512)]
print(len(positions))
for p in positions:
  r[p[0]+256][p[1]+256] = 1
plt.imshow(r)
plt.show()
