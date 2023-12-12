with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0

for i, line in enumerate(lines):
  DP = dict()

  def arrangements(springs: str, groups: tuple[int], cur: int):
    if len(springs) == 0:
      return (len(groups) == 0 and cur == 0) or (len(groups) == 1 and cur == groups[0])
    key = (springs, groups, cur)
    if key in DP:
      return DP[key]
    a = 0
    if springs[0] in ".?":
      if cur > 0:
        if len(groups) > 0 and groups[0] == cur:
          a += arrangements(springs[1:], groups[1:], 0)
      else:
        a += arrangements(springs[1:], groups, 0)
    if springs[0] in "#?":
      if len(groups) > 0:
        a += arrangements(springs[1:], groups, cur + 1)
    DP[key] = a
    return a

  springs = line.split(" ")[0]
  groups = tuple(int(g) for g in line.split(" ")[1].split(","))
  p1 += arrangements(springs, groups, 0)

  springs = "".join(5 * [*springs + "?"])[:-1]
  groups = 5 * groups
  p2 += arrangements(springs, groups, 0)

print(p1)
print(p2)
