with open("in.txt", "r") as f:
  line = f.read().strip()

def hash(s: str):
  n = 0
  for c in s:
    n += ord(c)
    n = n * 17
    n = n % 256
  return n

p1 = 0
for s in line.split(","):
  p1 += hash(s)
print(p1)

boxes = [dict() for _ in range(256)]

for s in line.split(","):
  if "=" in s:
    key, val = s.split("=")
    box = boxes[hash(key)]
    box[key] = int(val)
  else:
    key = s.split("-")[0]
    box = boxes[hash(key)]
    if key in box:
      del box[key]

p2 = 0
for i, box in enumerate(boxes):
  for j, lens in enumerate(box):
    p2 += (i + 1) * (j + 1) * box[lens]
print(p2)
