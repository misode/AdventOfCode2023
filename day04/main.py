from collections import defaultdict

with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0
copies = defaultdict(lambda: 1)

for i, line in enumerate(lines):
  _, data = line.split(":")
  winning, ours = [set(int(n.strip()) for n in nums.split()) for nums in data.split("|")]
  matches = len(winning.intersection(ours))
  p1 += 2 ** (matches - 1) if matches > 0 else 0
  for j in range(matches):
    copies[i+j+1] += copies[i]
  p2 += copies[i]

print(p1)
print(p2)
