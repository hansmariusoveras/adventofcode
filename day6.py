with open("inputs/input6.txt") as file:
  thing = file.read()

for i in range(len(thing)):
  if len(set(list(thing[i:i+14]))) == 14:
    print(thing[i:i+14])
    print(i+14)
    break