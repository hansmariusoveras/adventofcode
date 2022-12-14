import ast
import functools
with open("inputs/input13.txt") as file:
  strings = file.read().split("\n\n")

def compare(L, R):
  # both are ints, simple compare
  if isinstance(L, int) and isinstance(R, int):
    return L - R
  # R is a list, convert L to list as well
  elif isinstance(L, int):
    return compare([L], R) 
  # L is a list, convert R to list as well
  elif isinstance(R, int):
    return compare(L, [R])
  # loop through list to compare each element recursively
  for i in range(min(len(L), len(R))):
    z = compare(L[i], R[i])
    if z != 0:
      return z
  return len(L) - len(R)

counter = 0
all = []
for j, lr in enumerate(strings):
  # parse input
  left, right = (ast.literal_eval(i) for i in lr.split("\n"))
  # add to list of all
  all.extend([left, right])
  # compare and increment counter
  if compare(left, right) < 0:
    counter += j+1

# part 1
print(counter)

# part 2
all.extend([[[2]], [[6]]])
all.sort(key=functools.cmp_to_key(compare))
print(all.index([[2]]))
print(all.index([[6]]))