from functools import cache
import time

with open("inputs/input16.txt") as file:
  lines = file.read().split("\n")
valves = {}
for line in lines:
  line = line.split()
  valve = line[1]
  rate = int(line[4].split("=")[1][:-1])
  tunnels = [t.replace(",", "") for t in line[9:]]
  valves[valve] = {'rate': rate, 'tunnels': tunnels, 'active': False}
index_list = sorted(valves.keys())
indices = {k:i for i,k in enumerate(index_list)}
ultra_matrix = [[1000 for _ in range(len(indices))] for _ in range(len(indices))]

# Initialize matrix
for valve_name in indices.keys():
  valve = valves[valve_name]
  for neighbor_name in valve['tunnels']:
    neighbor = valves[neighbor_name]
    v_i, n_i = indices[valve_name], indices[neighbor_name]
    ultra_matrix[v_i][n_i] = 1
    ultra_matrix[n_i][v_i] = 1
    ultra_matrix[v_i][v_i] = 0

# Floyd-Warshall
for v0 in indices.values():
  for v1 in indices.values():
    for v2 in indices.values():
      ultra_matrix[v0][v2] =  min(ultra_matrix[v0][v2], ultra_matrix[v0][v1] + ultra_matrix[v1][v2])
      ultra_matrix[v2][v0] =  min(ultra_matrix[v2][v0], ultra_matrix[v0][v1] + ultra_matrix[v1][v2])
active_bits = 0
rate_list = tuple([valves[i]['rate'] for i in index_list])

@cache
def get_nexts(time_left, valve, active_list):
  for i, v in enumerate(ultra_matrix[valve]):
    if not (active_list & 1 << i) and rate_list[i] and v+1 <= time_left:
      yield ((-(time_left-v-1)*rate_list[i], v+1, rate_list[i], i))

# Explore tree
def explore(prev, time_left, pressure, cum_pressure, active_bits, depth=0):
  if time_left > 0:
    pressure_max = 0
    for next in get_nexts(time_left, prev, active_bits):
      al = active_bits
      _, dist, rate, current = next
      al |= 1 << current
      al |= 1 << current
      pressure_max = max(
        explore(current, time_left-dist, pressure+rate, cum_pressure+pressure*dist, al, depth+1), 
        pressure_max
      )
    if not pressure_max:
      return cum_pressure + time_left * pressure
    return pressure_max
  else:
    return cum_pressure

print("Result:", explore(0, 30, 0, 0, active_bits))