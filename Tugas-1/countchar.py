n = input()
n = n.lower()
map = {}
for i in n:
  if i in map:
    map[i] += 1
  else:
    map[i] = 1
for i in map:
  print(f"{i}={map[i]}")