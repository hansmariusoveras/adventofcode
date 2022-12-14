with open("inputs/input4.txt") as file:
  lines = file.readlines()
s = 0
k = 0
for line in lines:
  line = line.strip()
  r1, r2 = [[int(i) for i in r.split("-")] for r in line.split(",")]
  s += r1[0] <= r2[0] and r1[1] >= r2[1] or r1[0] >= r2[0] and r1[1] <= r2[1]
  k += r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1] or r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1]
print(s)
print(k)