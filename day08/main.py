from math import lcm

with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

instructs = lines[0]
nodes: dict[str, tuple[str, str]] = dict()
for e in lines[2:]:
  k, v = e.split(" = ")
  nodes[k] = v[1:-1].split(", ")

n = "AAA"
i = 0
while n != "ZZZ":
  instr = instructs[i % len(instructs)]
  n = nodes[n][0 if instr == "L" else 1]
  i += 1
print(i)

starts = [n for n in nodes.keys() if n.endswith("A")]
cycle = []
for n in starts:
  i = 0
  while not n.endswith("Z"):
    instr = 0 if instructs[i % len(instructs)] == "L" else 1
    n = nodes[n][instr]
    i += 1
  cycle.append(i)
print(lcm(*cycle, len(instructs)))
