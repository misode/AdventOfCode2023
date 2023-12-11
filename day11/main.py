with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

G = []
R = set()
C = set()

for row, line in enumerate(lines):
  for col, char in enumerate(line):
    if char == '#':
      G.append((row, col))
      R.add(row)
      C.add(col)

def solve(e: int):
  total = 0
  for i, g1 in enumerate(G):
    for g2 in G[i+1:]:
      re = sum(e for r in range(min(g1[0], g2[0]), max(g1[0], g2[0])+1) if r not in R)
      ce = sum(e for c in range(min(g1[1], g2[1]), max(g1[1], g2[1])+1) if c not in C)
      total += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1]) + re + ce
  return total

print(solve(1))
print(solve(999999))
