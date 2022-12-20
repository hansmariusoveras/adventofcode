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
def get_nexts(time_left, valve, active_list, actor):
  nexts = []
  for i, v in enumerate(ultra_matrix[valve]):
    if not (active_list & 1 << i) and rate_list[i] and v+1 <= time_left:
      nexts.append(
        (-(time_left-v-1)*rate_list[i], v+1, rate_list[i], i, actor)
      )
  return nexts

@cache
def sum_pressure(pressure, total):
  cum = 0
  for i,p in enumerate(pressure):
    cum += (total-i)*p
  return cum

# Explore tree
@cache
def explore(your_prev, elephant_prev, your_time, elephant_time, pressure, active_bits, depth=0):
  if your_time or elephant_time:
    pressure_max = 0
    L = (get_nexts(your_time, your_prev, active_bits, 0) + get_nexts(elephant_time, elephant_prev, active_bits, 1))
    for i,next in enumerate(L):
      if depth == 0:
        print(i/len(L))
      new_pressure = list(pressure)
      _, dist, p, current, actor = next
      ab = active_bits | (1 << current)
      if actor == 0 and dist > your_time or actor == 1 and dist > elephant_time:
        continue
      new_pressure[26-(elephant_time if actor else your_time)+dist] += p
      if actor == 0:
        pressure_max = max(
          explore(current, elephant_prev, your_time-dist, elephant_time, tuple(new_pressure), ab, depth+1), 
          pressure_max
        )
      else:
        pressure_max = max(
          explore(your_prev, current, your_time, elephant_time-dist, tuple(new_pressure), ab, depth+1), 
          pressure_max
        )
    if not pressure_max:
      return sum_pressure(pressure, 26)
    return pressure_max
  else:
    return sum_pressure(pressure, 26)

print("Result:", explore(0, 0, 26, 26, tuple([0 for i in range(27)]), active_bits))