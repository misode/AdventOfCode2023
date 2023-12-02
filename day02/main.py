from collections import defaultdict

with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0

for i, line in enumerate(lines):
  (_, data) = line.split(":")
  possible = True
  mincubes = defaultdict(int)
  for grab in [g.strip() for g in data.split(";")]:
    cubes = defaultdict(int)
    for cube in [c.strip() for c in grab.split(",")]:
      (count, name) = cube.split(" ")
      cubes[name] = int(count)
      mincubes[name] = max(mincubes[name], cubes[name])
    if cubes["red"] > 12 or cubes["green"] > 13 or cubes["blue"] > 14:
      possible = False
  if possible:
    p1 += (i + 1)
  p2 += mincubes["red"] * mincubes["green"] * mincubes["blue"]

print(p1)
print(p2)
