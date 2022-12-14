with open("inputs/input8.txt") as file:
  text = file.read()
  trees = [[int(i) for i in list(line)] for line in text.split("\n")]
visib = [[0 for i in range(len(trees[0]))] for j in range(len(trees))]
for i in range(len(trees)):
  max_row = -1
  for j in range(len(trees[0])):
    if trees[i][j] > max_row:
      visib[i][j] = 1
    max_row = max(max_row, trees[i][j])

for j in range(len(trees[0])):
  max_row = -1
  for i in range(len(trees)):
    if trees[i][j] > max_row:
      visib[i][j] = 1
    max_row = max(max_row, trees[i][j])

for j in range(len(trees[0])-1 , -1, -1):
  max_row = -1
  for i in range(len(trees)-1, -1, -1):
    if trees[i][j] > max_row:
      visib[i][j] = 1
    max_row = max(max_row, trees[i][j])

for i in range(len(trees)-1, -1, -1):
  max_row = -1
  for j in range(len(trees[0])-1, -1, -1):
    if j==98:
      print(max_row, trees[i][j])
    if trees[i][j] > max_row:
      visib[i][j] = 1
    max_row = max(max_row, trees[i][j])
print(sum([sum(s) for s in visib]))