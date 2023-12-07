from functools import cmp_to_key
from collections import Counter

def get_type(hand: str, jokers: bool):
  filtered = filter(lambda c: c != "J", hand) if jokers else hand
  j = hand.count("J") if jokers else 0
  counts = [t[1] for t in Counter(filtered).most_common()]
  if j == 5 or counts[0] + j == 5:
    return 6 # five of a kind
  if counts[0] + j == 4:
    return 5 # four of a kind
  if counts[0] + j == 3 and counts[1] == 2:
    return 4 # full house
  if counts[0] + j == 3:
    return 3 # three of a kind
  if counts[0] + j == 2 and counts[1] == 2:
    return 2 # two pairs
  if counts[0] + j == 2:
    return 1 # one pair
  return 0 # high card

def compare(a: str, b: str, jokers: bool, order: str):
  ta, tb = get_type(a, jokers), get_type(b, jokers)
  if ta != tb:
    return ta - tb
  for ca, cb in zip(a, b):
    if ca != cb:
      return order.index(cb) - order.index(ca)
  return 0

with open("in.txt", "r") as f:
  lines = [l.strip() for l in f.readlines()]

players = [tuple(l.split()) for l in lines]

def solve(jokers: bool, order: str):
  players.sort(key=cmp_to_key(lambda a, b: compare(a[0], b[0], jokers, order)))
  return sum([int(p[1]) * (i+1) for i, p in enumerate(players)])

print(solve(False, "AKQJT98765432"))
print(solve(True, "AKQT98765432J"))
