import copy
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
for valve_name in indices.keys():
  valve = valves[valve_name]
  for neighbor_name in valve['tunnels']:
    neighbor = valves[neighbor_name]
    v_i, n_i = indices[valve_name], indices[neighbor_name]
    ultra_matrix[v_i][n_i] = 1
    ultra_matrix[n_i][v_i] = 1
    ultra_matrix[v_i][v_i] = 0
for j in range(2, 4):
  for v0 in indices.values():
    for v1 in indices.values():
      for v2 in indices.values():
        ultra_matrix[v0][v2] =  min(ultra_matrix[v0][v2], ultra_matrix[v0][v1] + ultra_matrix[v1][v2])
        ultra_matrix[v2][v0] =  min(ultra_matrix[v2][v0], ultra_matrix[v0][v1] + ultra_matrix[v1][v2])

active_list = [0 for i in index_list]
rate_list = [valves[indices[i]]['rate'] for i in index_list]

def get_nexts(t, valve, valves):
  return sorted([(-min(t-v-1,t)*valves[index_list[i]]['rate']*(not valves[index_list[i]]['active']), v, valves[index_list[i]]['rate'], index_list[i]) for i, v in enumerate(ultra_matrix[indices[valve]]) if valves[index_list[i]]['rate'] and not valves[index_list[i]]['active']])
Nn = 0
def backtracking(prev, T, RATE, TOT_RATE, valves, depth=0):
  global Nn
  Nn += 1
  if T > 0:
    N = get_nexts(T, prev, valves)
    X = []
    for i,next in enumerate(N):
      if depth==0:
        print(X)
      if depth==1:
        print(i/len(N))
      t, r, tr, V = T, RATE, TOT_RATE, copy.deepcopy(valves)
      val, dist, rate, current = next
      rate *= not V[current]['active']
      dist += not V[current]['active']
      if dist > T:
        continue
      
      V[current]['active'] = True
      dist = max(dist, 1)
      X.append(backtracking(current, t-dist, r+rate, tr+r*dist, V, depth+1))
      #print(f"Time: {t-dist}. Went to {current} with rate {rate}, took {dist} time. This wins {val} points.")
      #print(f"Current pressure is {r} and so far accumulated {tr}")
    if not X:
      return TOT_RATE + T*RATE
    return max(X)
  else:
    return TOT_RATE
print("Result:", backtracking('AA', 30, 0, 0, valves))
print(Nn)