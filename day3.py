with open("inputs/input3.txt", "r") as file:
  lines = file.readlines()
def part1():
  items = []
  for line in lines:
    line = line.strip()
    c1, c2 = list(line[:len(line)//2]), list(line[len(line)//2:])
    x = set(c1).intersection(c2).pop()
    items.append(x)

  print(sum([ord(i) - 96 if ord(i) >= 97 else ord(i) - 38 for i in items]))

def part2():
  s = 0
  for i in range(0, len(lines), 3):
    elves = [set(list(lines[i+j].strip())) for j in range(3)]
    badge = elves[0].intersection(elves[1].intersection(elves[2])).pop()
    s += ord(badge) - 96 if ord(badge) >= 97 else ord(badge) - 38
  print(s)


part2()