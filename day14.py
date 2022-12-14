import matplotlib.pyplot as plt
with open("inputs/input14.txt") as file:
  lines = file.read().split("\n")
grid = [[0 for i in range(700)] for j in range(600)]

def draw_line(x1, x2, y1, y2):
  #print(x1, x2, y1, y2)
  if x1 <= x2:
    for i in range(x1, x2+1):
      if y1 <= y2:
        for j in range(y1, y2+1):
          grid[j][i] = 1
      if y1 > y2:
        for j in range(y2, y1+1):
          grid[j][i] = 1
  
  if x1 > x2:
    for i in range(x2, x1+1):
      if y1 <= y2:
        for j in range(y1, y2+1):
          grid[j][i] = 1
      if y1 > y2:
        for j in range(y2, y1+1):
          grid[j][i] = 1

def move_sand(x, y):
    if not grid[y+1][x]:
      return (x, y+1)
    elif not grid[y+1][x-1]:
      return (x-1, y+1)
    elif not grid[y+1][x+1]:
      return (x+1, y+1)
    else:
      return (x, y)
      
ys = []
for line in lines:
  coord_list = line.split(" -> ")
  prev = None
  for coords in coord_list:
    x, y = coords.split(",")
    x, y = int(x), int(y)
    ys.append(y)
    if prev != None:
      px, py = prev
      draw_line(x, px, y, py)
    prev = (x, y)

draw_line(0, 690, max(ys)+2, max(ys)+2)
done = False
spx, spy = 500, 0
sands = 0
while not done:
  if spy > 590:
    abyss = True
  move = move_sand(spx, spy)
  if move == (spx, spy):
    if (spx, spy) == (500, 0):
      done = True
    sands += 1
    grid[spy][spx] = 5
    spx, spy = 500, 0
  else:
    spx, spy = move
  

plt.title(f"sands: {sands}")
plt.imshow(grid)
plt.show()

