from functools import cache
with open("inputs/input19.txt") as file:
  blueprints = file.read().split("\n")
  blueprints = [[int(x) for x in b.split(" ") if x.isnumeric()] for b in blueprints]

BUY_LVL = 0
@cache
def round(blueprint, robs, ores, time):
  ore_r_cost, clay_r_cost, obsidian_r_cost_ore, obsidian_r_cost_clay, geode_r_cost_ore, geode_r_cost_obsidian = blueprint
  ore_robs, clay_robs, obsidian_robs, geode_robs = robs
  ore, clay, obsidian, geode = ores
  global BUY_LVL
  if geode_robs == 0 and BUY_LVL > time:
    return -1
  if time == 0:
    return geode
  max_geodes = 0
  if ore >= geode_r_cost_ore and obsidian >= geode_r_cost_obsidian:
    BUY_LVL = max(time, BUY_LVL)
    return round(
      blueprint, 
      (ore_robs, clay_robs, obsidian_robs, geode_robs+1), 
      (
        ore + ore_robs - geode_r_cost_ore,
        clay + clay_robs,
        obsidian + obsidian_robs - geode_r_cost_obsidian,
        geode + geode_robs
      ),
      time - 1
    )
  if ore >= obsidian_r_cost_ore and clay >= obsidian_r_cost_clay and obsidian_robs < geode_r_cost_obsidian:
    max_geodes = max(round(
      blueprint, 
      (ore_robs, clay_robs, obsidian_robs+1, geode_robs), 
      (
        ore + ore_robs - obsidian_r_cost_ore,
        clay + clay_robs - obsidian_r_cost_clay,
        obsidian + obsidian_robs,
        geode + geode_robs
      ),
      time - 1
    ), max_geodes)
  if ore >= clay_r_cost and clay_robs < obsidian_r_cost_clay:
    max_geodes = max(round(
      blueprint, 
      (ore_robs, clay_robs+1, obsidian_robs, geode_robs), 
      (
        ore + ore_robs - clay_r_cost,
        clay + clay_robs,
        obsidian + obsidian_robs,
        geode + geode_robs
      ),
      time - 1
    ), max_geodes)
  if ore >= ore_r_cost and ore_robs < max(ore_r_cost, clay_r_cost, obsidian_r_cost_ore, geode_r_cost_ore):
    max_geodes = max(round(
      blueprint, 
      (ore_robs+1, clay_robs, obsidian_robs, geode_robs), 
      (
        ore + ore_robs - ore_r_cost,
        clay + clay_robs,
        obsidian + obsidian_robs,
        geode + geode_robs
      ),
      time - 1
      ), max_geodes)
  max_geodes = max(round(
    blueprint, 
    (ore_robs, clay_robs, obsidian_robs, geode_robs), 
    (
      ore + ore_robs,
      clay + clay_robs,
      obsidian + obsidian_robs,
      geode + geode_robs
    ),
    time - 1
  ), max_geodes)
  return max_geodes
  
def stats(time, ore, clay, obsidian, geode, ore_robs, clay_robs, obsidian_robs, geode_robs):
  print(f"[{time}]\n  {ore} / {clay} / {obsidian} / {geode}.\n  {ore_robs} / {clay_robs} / {obsidian_robs} / {geode_robs}")


def run_simulation(blueprint):
  global BUY_LVL
  BUY_LVL = 0
  ore_r_cost, clay_r_cost, obsidian_r_cost_ore, obsidian_r_cost_clay, geode_r_cost_ore, geode_r_cost_obsidian = blueprint
  print(f"\n\nBlueprint {i}:\nEach ore robot costs {ore_r_cost} ore.\nEach clay robot costs {clay_r_cost} ore.\nEach obsidian robot costs {obsidian_r_cost_ore} ore and {obsidian_r_cost_clay} clay.\nEach geode robot costs {geode_r_cost_ore} ore and {geode_r_cost_obsidian} obsidian.\n")
  round.cache_clear()
  return round(tuple(blueprint), (1, 0, 0, 0), (0, 0, 0, 0), 32)
S = 1
for i,blueprint in enumerate(blueprints[:3]):
  k = run_simulation(blueprint)
  S *= k
  print(k)
print(S)