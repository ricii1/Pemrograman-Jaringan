n = int(input())
res = ''  

while n > 0:
    res = str(n & 1) + res
    n >>= 1
print(res)