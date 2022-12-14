with open("inputs/input11.txt") as file:
  instructions = file.read().split("\n\n")
monkeys = [{} for i in range(len(instructions))]
for instruction in instructions:
  monkey, starting, operation, test, true, false = instruction.split("\n")

  # monkey
  monkey = int(monkey.split()[1][0])
  # starting values
  monkeys[monkey]['items'] = [int(i) for i in starting[18:].split(", ")]

  # operation
  operation = operation.split()[4:]
  operation, operand = operation[0], int(operation[1]) if operation[1].isnumeric() else operation[1]
  if operation == '+':
    monkeys[monkey]['command'] = lambda x, o=operand: x + o
  elif operand == 'old':
    monkeys[monkey]['command'] = lambda x: x * x
  else:
    monkeys[monkey]['command'] = lambda x, o=operand: x * o
  # test
  monkeys[monkey]['test'] = int(test.split()[3])
  monkeys[monkey]['true'] = int(true.split()[5])
  monkeys[monkey]['false'] = int(false.split()[5])
  monkeys[monkey]['count'] = 0

# for i, monkey in enumerate(monkeys):
#   print(f"Monkey {i}")
#   print("items", monkey['items'])
#   print("command", monkey['command'](1))
#   print("test", monkey['test'](36))
#   print("true", monkey['true'])
#   print("false", monkey['false'])
#   print()

# run monkeys
for i in range(10000):
  for n,monkey in enumerate(monkeys):
    #print(monkey['items'])
    for item in monkey['items'].copy():
      monkey['count'] += 1
      monkey['items'].remove(item)
      z = lambda Z: 1 if len(Z) == 0 else Z[0]*z(Z[1:])
      
      item = item % (z([m['test'] for m in monkeys]))
      item = monkey['command'](item)
      if item % monkey['test'] == 0:
        monkeys[monkey['true']]['items'].append(item)
      else:
        monkeys[monkey['false']]['items'].append(item)

# for i, monkey in enumerate(monkeys):
#   print(f"Monkey {i}")
#   print("items", monkey['items'])
#   print("command", monkey['command'](1))
#   print("test", monkey['test'](36))
#   print("true", monkey['true'])
#   print("false", monkey['false'])
#   print()
      
print(sorted([m['count'] for m in monkeys]))
