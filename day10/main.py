with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

# hardcode based on input
start_shape = "-"
inside_offset = (-1, 0)

G = [[False for _ in range(len(lines[0])*3)] for _ in range(len(lines)*3)]

for i, row in enumerate(lines):
  for j, c in enumerate(row):
    if c == "S":
      c = start_shape
      start = (i, j)
    if c == "-":
      G[i*3+1][j*3] = True
      G[i*3+1][j*3+1] = True
      G[i*3+1][j*3+2] = True
    elif c == "|":
      G[i*3][j*3+1] = True
      G[i*3+1][j*3+1] = True
      G[i*3+2][j*3+1] = True
    elif c == "L":
      G[i*3][j*3+1] = True
      G[i*3+1][j*3+1] = True
      G[i*3+1][j*3+2] = True
    elif c == "J":
      G[i*3][j*3+1] = True
      G[i*3+1][j*3+1] = True
      G[i*3+1][j*3] = True
    elif c == "7":
      G[i*3+1][j*3] = True
      G[i*3+1][j*3+1] = True
      G[i*3+2][j*3+1] = True
    elif c == "F":
      G[i*3+1][j*3+2] = True
      G[i*3+1][j*3+1] = True
      G[i*3+2][j*3+1] = True

def flood_fill(start: tuple[int, int], predicate):
  V = set()
  Q = [start]
  while len(Q) > 0:
    p = Q.pop(0)
    if p[0] < 0 or p[1] < 0 or p[0] >= len(G) or p[1] >= len(G[0]):
      assert False, "outside"
    if p in V or not predicate(p[0], p[1]):
      continue
    V.add(p)
    for n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      Q.append((p[0] + n[0], p[1] + n[1]))
  return V

pos = (start[0]*3+1, start[1]*3+1)
border = flood_fill(pos, lambda i, j: G[i][j])
p1 = len(border) // 6
print(p1)

inside_start = (pos[0]+inside_offset[0], pos[1]+inside_offset[1])
inside = flood_fill(inside_start, lambda i, j: (i, j) not in border)
p2 = len([1 for i, j in inside if i % 3 == 1 and j % 3 == 1])
print(p2)
