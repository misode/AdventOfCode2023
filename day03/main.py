with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

G = [list(line) + ["."] for line in lines]

p1 = 0
p2 = 0

gears = dict()
part = ""
party = 0
partx = 0

for y, row in enumerate(lines):
  for x, char in enumerate(row):
    if char.isdigit():
      if part == "":
        party, partx = y, x
      part += char
    elif len(part) > 0:
      symbol = False
      for dy in range(-1, 2):
        for dx in range(-1, len(part)+1):
          yy = party+dy
          xx = partx+dx
          if xx < 0 or yy < 0 or xx >= len(G[0]) or yy >= len(G):
            continue
          c = G[yy][xx]
          if c != "." and not c.isdigit():
            symbol = True
          if c == "*":
            key = f"{yy} {xx}"
            if key in gears:
              p2 += gears[key] * int(part)
            else:
              gears[key] = int(part)
      if symbol:
        p1 += int(part)
      part = ""

print(p1)
print(p2)
