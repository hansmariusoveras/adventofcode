with open("inputs/input10.txt") as file:
  lines = file.readlines()
c = 0
val = 1
vals = []
CRT_POS = 0
ll = [20, 60, 100, 140, 180, 220]
for line in lines:
  line = line.strip()
  
  if line == "noop":
    c += 1
    if sum([c == l for l in ll]) > 0:
      vals.append(val*c)
      print(c, val*c)
    continue
  add, num = line.split()
  num = int(num)
  c += 1
  if sum([c == l for l in ll]) > 0:
    vals.append(val*c)
    print(c, val*c)
  
  c+=1
  if sum([c == l for l in ll]) > 0:
    vals.append(val*c)
    print(c, val, val*c)
  val += num
  
  
print(sum(vals))