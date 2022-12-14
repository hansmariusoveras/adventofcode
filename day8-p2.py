import numpy as np
import matplotlib.pyplot as plt
with open("inputs/input8.txt") as file:
  text = file.read()
  trees = [[int(i) for i in list(line)] for line in text.split("\n")]
L, R, U, D = [[1 for i in range(len(trees[0]))] for j in range(len(trees))], [[1 for i in range(len(trees[0]))] for j in range(len(trees))], [[1 for i in range(len(trees[0]))] for j in range(len(trees))], [[1 for i in range(len(trees[0]))] for j in range(len(trees))]


def incr(treh):
  for i in range(10):
    treeh[i] += 1

for i in range(len(trees)):
  treeh = {i: 0 for i in range(0, 10)}
  for j in range(len(trees[0])):
    L[i][j] = max(1, min([treeh[s] for s in range(trees[i][j], 10)]))
    treeh[trees[i][j]] = 0
    incr(treeh)

for j in range(len(trees[0])):
  treeh = {i: 0 for i in range(0, 10)}
  for i in range(len(trees)):
    U[i][j] = max(1, min([treeh[s] for s in range(trees[i][j], 10)]))
    treeh[trees[i][j]] = 0
    incr(treeh)

for j in range(len(trees[0])):
  treeh = {i: 0 for i in range(0, 10)}
  for i in range(len(trees)-1, -1, -1):
    D[i][j] = max(1, min([treeh[s] for s in range(trees[i][j], 10)]))
    treeh[trees[i][j]] = 0
    incr(treeh)

for i in range(len(trees)):
  treeh = {i: 0 for i in range(0, 10)}
  for j in range(len(trees[0])-1, -1, -1):
    R[i][j] = max(1, min([treeh[s] for s in range(trees[i][j], 10)]))
    treeh[trees[i][j]] = 0
    incr(treeh)

print(max([(L[i][j] * R[i][j] * U[i][j] * D[i][j], i, j)] for i in range(len(D)) for j in range(len(D[0]))))
plt.imshow(np.array(U)+np.array(D)+np.array(L)+np.array(R))
plt.show()