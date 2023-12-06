with open("in.txt", "r") as f:
  lines = f.readlines()

times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

def findsum(time, record):
  n = 0
  for i in range(time + 1):
    d = i * (time - i)
    if d > record:
      n += 1
  return n

p1 = 1
for time, record in zip(times, distances):
  p1 *= findsum(time, record)
print(p1)

time = int("".join(str(t) for t in times))
record = int("".join(str(t) for t in distances))

p2 = findsum(time, record)
print(p2)
