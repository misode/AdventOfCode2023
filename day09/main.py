with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

p1 = 0
p2 = 0

for line in lines:
  D = [[int(x) for x in line.split(" ")]]
  while not all(n == 0 for n in D[-1]):
    D.append([D[-1][i+1] - D[-1][i] for i in range(len(D[-1]) - 1)])

  D[-1].append(0)
  for i in reversed(range(len(D)-1)):
    D[i].append(D[i][-1] + D[i+1][-1])
  p1 += D[0][-1]

  D[-1].insert(0, 0)
  for i in reversed(range(len(D)-1)):
    D[i].insert(0, D[i][0] - D[i+1][0])
  p2 += D[0][0]

print(p1)
print(p2)
