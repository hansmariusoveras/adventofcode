outcomes = {
  ("A", "X"): 3,
  ("A", "Y"): 6,
  ("A", "Z"): 0,

  ("B", "X"): 0,
  ("B", "Y"): 3,
  ("B", "Z"): 6,

  ("C", "X"): 6,
  ("C", "Y"): 0,
  ("C", "Z"): 3,
}

scores = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

win_state_outcomes = {
  ("A", "X"): 3,
  ("A", "Y"): 1,
  ("A", "Z"): 2,

  ("B", "X"): 1,
  ("B", "Y"): 2,
  ("B", "Z"): 3,

  ("C", "X"): 2,
  ("C", "Y"): 3,
  ("C", "Z"): 1
}

with open("inputs/input2.txt", "r") as file:
  lines = file.readlines()
score = 0
for line in lines:
  opponent, outcome = line.strip().split()
  score += win_state_outcomes[(opponent, outcome)]
  if outcome == "Z":
    score += 6
  elif outcome == "Y":
    score += 3
print(score)