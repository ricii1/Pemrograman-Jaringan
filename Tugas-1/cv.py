a = input()
count_vowels = 0
for i in a:
  lower = i.lower()
  if lower == "a" or lower == "e" or lower == "i" or lower == "o" or lower == "u":
    count_vowels+=1
print(count_vowels)