a = int(input())
if a == 0:
  print("0")
elif a > 0:
  sum = 0
  for i in range (a+1):
    sum += i
  print(sum)
else:
  sum = 0
  for i in range (a, 0):
    sum += i
  print(sum)