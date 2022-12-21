import matplotlib.pyplot as plt


SEQ = []
with open("inputs/input17.txt") as file:
  for char in file.read():
    SEQ.append(-1 if char == '<' else 1)
    SEQ.append(0)

HEIGHT = 100000
def generate_hline(x, y):
  return [
    [x, y],
    [x+1, y],
    [x+2, y],
    [x+3, y]
  ]

def generate_plus(x, y):
  return [
    [x+1, y],
    [x+1, y+1],
    [x+2, y+1],
    [x, y+1],
    [x+1, y+2]
  ]

def generate_L(x, y):
  return [
    [x, y],
    [x+1, y],
    [x+2, y],
    [x+2, y+1],
    [x+2, y+2]
  ]

def generate_vline(x, y):
  return [
    [x, y],
    [x, y+1],
    [x, y+2],
    [x, y+3]
  ]

def generate_square(x, y):
  return [
    [x, y+1],
    [x+1, y+1],
    [x, y],
    [x+1, y]
  ]

def collides(map, object):
  for x, y in object:
    if map[y][x]:
      return True
  return False

TETRIS_HEIGHT = 0

def shape_stream():
  while True:
    for fnc in [generate_hline, generate_plus, generate_L, generate_vline, generate_square]:
      global TETRIS_HEIGHT
      yield fnc(3, TETRIS_HEIGHT+4)
COLOR = 1
T = 0
def tick(map, tet, move):
  if move == -1:
    new_tet = [[x-1, y] for x, y in tet]
  elif move == 1:
    new_tet = [[x+1, y] for x, y in tet]
  else:
    new_tet = [[x, y-1] for x, y in tet]
  if collides(map, new_tet):
    if move != 0:
      return tet
    global COLOR
    COLOR = ((COLOR + 1) % 7) + 1
    global TETRIS_HEIGHT
    for x1, y1 in tet:
      TETRIS_HEIGHT = max(TETRIS_HEIGHT, y1)
      map[y1][x1] = COLOR
    return None
  return new_tet


map1 = [[0 for i in range(9)] for j in range(HEIGHT)]
for i in range(9):
  map1[0][i] = 2
  map1[HEIGHT-1][i] = 2
for i in range(HEIGHT):
  map1[i][0] = 2
  map1[i][8] = 2

iterator = iter(shape_stream())
tet = None
tets = -1
sequence = SEQ.copy()
while tets < 1707 + 168:
  if tets == 1707:
    print(tets, TETRIS_HEIGHT)
  if tets == 1707 + 167:
    print(tets, TETRIS_HEIGHT)
  if not sequence:
    sequence = SEQ.copy()
  s = sequence.pop(0)
  T += 1
  if tet == None:
    tet = next(iterator)
    tets += 1
  tet = tick(map1, tet, s)
print(TETRIS_HEIGHT)