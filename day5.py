import re
with open("inputs/input5.txt") as file:
  f = file.read()
  d, ins = f.split("\n\n")
stacks = {
  1: "VCDRZGBW",
  2:"GWFCBSTV",
  3:"CBSNW",
  4:"QGMNJVCP",
  5:"TSLFDHB",
  6:"JVTWMN",
  7:"PFLCSTG",
  8:"BDZ",
  9:"MNZW",
}
for i in stacks.keys():
  stacks[i] = list(stacks[i])
for instruction in ins.split("\n"):
  m = re.findall(r"move (\d+) from (\d+) to (\d+)", instruction)
  amount, move_from, move_to = m[0]
  amount, move_from, move_to = int(amount), int(move_from), int(move_to)
  x = stacks[move_from][-amount:]
  stacks[move_to].extend(x)
  stacks[move_from] = stacks[move_from][:-amount]
print([(i, s[-1]) for i, s in stacks.items()])