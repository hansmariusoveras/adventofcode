with open("inputs/input7.txt") as file:
  lines = file.readlines()

def add_all_parents(dict, c, n):
  while c != "":
    dict[c]["size"] += n
    c = dict[c]["parent"]

files = {".": {"parent": "", "size": 0}}
current_dir = "."
for line in lines[1:]:
  line = line.strip()
  if line == "$ cd ..":
    current_dir = files[current_dir]["parent"]
  elif line[:4] == "$ cd":
    files[current_dir + "/" + line[5:]] = {"parent": current_dir, "size": 0}
    current_dir = current_dir + "/" + line[5:]
  elif line[0].isnumeric():
    n = int(line.split(" ")[0])
    add_all_parents(files, current_dir, n)
print(("\n".join([": ".join((k, str(files[k]["size"]))) for k in files.keys()])))
    
sizes = [v["size"] for v in files.values()]
print(sum(filter(lambda x: x <= 100000, sizes)))
Z = max(sizes) - 40000000
print(min(filter(lambda x: x >= Z, sizes)))