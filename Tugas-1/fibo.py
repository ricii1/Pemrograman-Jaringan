n = int(input())
a = 0
b = 1
c = 2
for i in range(n):
  a, b, c = b, c, b + c
print(a)
