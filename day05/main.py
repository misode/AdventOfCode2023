
with open("in.txt", "r") as f:
  lines = f.read()

seeds, *maps = lines.strip().split("\n\n")
seeds = [int(s) for s in seeds.split(":")[1].strip().split(" ")]

S = seeds[::]
D = [False for _ in seeds]
for map in maps:
  ranges = map.split("\n")[1:]
  matches = []
  for r in ranges:
    d, s, sl = [int(x) for x in r.split(" ")]
    d, s, l = [int(x) for x in r.split(" ")]
    for i, n in enumerate(S):
      if n >= s and n < s + l and not D[i]:
        S[i] = n - s + d
        D[i] = True
  D = [False for _ in S]
print(min(S))

P = [(seeds[2*i], seeds[2*i+1]) for i in range(len(seeds)//2)]
for map in maps:
  matches = []
  for r in map.split("\n")[1:]:
    d, s, sl = [int(x) for x in r.split(" ")]
    leftover = []
    for i, (n, nl) in enumerate(P):
      if n + nl >= s and n < s + sl:
        s1 = max(s, n)
        s2 = min(s + sl, n + nl)
        matches.append((s1 - s + d, s2 - s1))
        if n < s:
          leftover.append((n, s - n))
        if n + nl > s + sl:
          leftover.append((s + sl, n + nl - (s + sl)))
      else:
        leftover.append((n, nl))
    P = leftover
  P = matches + P
print(min(P)[0])
