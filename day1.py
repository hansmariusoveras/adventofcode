with open("inputs/input1.txt", "r") as file:
  elves = file.read().split("\n\n")
  sums = [sum([int(i) if i != "" else 0 for i in x.split("\n")]) for x in elves]
  print(sum(sorted(sums)[-3:]))