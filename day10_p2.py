with open("inputs/input10.txt") as file:
  lines = file.readlines()
c = 0
val = 1
vals = []
CRT = ['.' for i in range(40*6)]
for line in lines:
  line = line.strip()
  
  if line == "noop":
    if val - 1 <= c%40 <= val + 1:
      CRT[c] = "#"
    c += 1
    continue
  add, num = line.split()
  num = int(num)
  if val - 1 <= c%40 <= val + 1:
    CRT[c] = "#"
  c += 1
  if val - 1 <= c%40 <= val + 1:
    CRT[c] = "#"
  c += 1
  
  val += num
  
wrapped = ["".join(CRT[i*40:i*40+40]) for i in range(6)]
for x in wrapped:
  print(x)