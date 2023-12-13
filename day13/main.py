with open("in.txt", "r") as f:
  grids = [p.strip().split("\n") for p in f.read().split("\n\n")]

def transpose(g: list[str]):
  return ["".join(row[c] for row in g) for c in range(len(g[0]))]

def solve(grid: list[str], smudge: int):
  for i in range(1, len(grid[0])):
    s = 0
    for row in grid:
      for j in range(min(i, len(grid[0]) - i)):
        if row[i-j-1] != row[i+j]:
          s += 1
    if s == smudge:
      return i

for smudge in (0, 1):
  total = 0
  for i, grid in enumerate(grids):
    total += solve(grid, smudge) or (100 * solve(transpose(grid), smudge))
  print(total)
