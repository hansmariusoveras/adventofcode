const = 2000000
with open("inputs/input15.txt") as file:
  lines = file.read().split("\n")
spots = set()
for line in lines:
  line = line.replace(",", "").replace(":", "").replace("=", " ")
  sx, sy, bx, by = [int(n) for n in line.split() if len(n) > 1 and n[1:].isnumeric() or n.isnumeric()]
  v = abs(bx-sx) + abs(by-sy)
  #print(sx, sy, bx, by)
  d = v - abs(sy - const)
  if d <= 0:
    continue
  for x in range(sx-d, sx+d+1):
    #print("sensor:", sx, sy, "beacon:", bx, by, "dist:", d, "range:", v, "so:", x)
    spots.add((x))
  if by == const:
    spots.remove(bx)
print(len(sorted(list(spots))))
