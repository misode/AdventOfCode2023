
with open("in.txt", "r") as f:
  input = [l.strip() for l in f.readlines()]

p1 = 0
for line in input:
  chars = [c for c in line.strip()]
  nums = [c for c in chars if c.isdigit()]
  p1 += int(nums[0] + nums[-1]) if nums else 0

print(p1)

NUMS = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

def getnum(s: str):
  if s[0].isdigit():
    return s[0]
  for k, v in NUMS.items():
    if s.startswith(k):
      return v
  return None

p2 = 0
for line in input:
  for i in range(len(line)):
    n = getnum(line[i:])
    if n:
      break
  for i in reversed(range(len(line))):
    m = getnum(line[i:])
    if m:
      break
  p2 += int(n + m)

print(p2)
