with open("inputs/input15.txt") as file:
  lines = file.read().split("\n")
j = 0
info = []
for line in lines:
  line = line.replace(",", "").replace(":", "").replace("=", " ")
  sx, sy, bx, by = [int(n) for n in line.split() if len(n) > 1 and n[1:].isnumeric() or n.isnumeric()]
  v = abs(bx-sx) + abs(by-sy)
  info.append((sx, sy, v))
for Y in range(0, 4000000):
  if Y % 100000 == 0:
    print(Y/4000000 * 100, "% finished")
  ranges = []
  for inf in info:
    sx, sy, v = inf
    d = v - abs(sy - Y)
    if d <= 0:
      continue
    ranges.append((sx-d, sx+d+1))
  ranges.sort()
  while(ranges):
    f0, t0 = ranges[0]
    if len(ranges) == 1:
      break
    f1, t1 = ranges[1]
    if f1 < t0:
      ranges.pop(0)
      ranges[0] = (f0, max(t0, t1))
    else:
      # this only happens when we find the beacon
      print(t0*4000000+Y)
      ranges.pop(0)
