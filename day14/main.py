with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

N = len(lines)
CYCLES = 1000000000
DIRS = {
  "north": lambda x, y: (x, y),
  "west": lambda x, y: (y, N-x-1),
  "south": lambda x, y: (N-x-1, N-y-1),
  "east": lambda x, y: (N-y-1, x),
}

walls = set()
rocks = set()
for i, line in enumerate(lines):
  for j, cell in enumerate(line):
    if cell == "#":
      walls.add((j, i))
    elif cell == "O":
      rocks.add((j, i))

def tilt(dir: str):
  T = DIRS[dir]
  top = [0 for _ in range(N)]
  for y in range(N):
    for x in range(N):
      if T(x, y) in walls:
        top[x] = y + 1
      elif T(x, y) in rocks:
        rocks.remove(T(x, y))
        rocks.add(T(x, top[x]))
        top[x] += 1

def load():
  return sum(N - r[1] for r in rocks)

def cycle():
  for dir in DIRS:
    tilt(dir)

tilt("north")
print(load())

SEEN = [str(sorted(rocks))]
for c in range(CYCLES):
  cycle()
  key = str(sorted(rocks))
  if key in SEEN:
    first = SEEN.index(key)
    remaining = (CYCLES - first) % (c + 1 - first)
    for _ in range(remaining):
      cycle()
    break
  SEEN.append(key)
print(load())
