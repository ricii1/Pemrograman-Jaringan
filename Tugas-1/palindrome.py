str = input()
str = str.lower()
if str == str[::-1]:
  print("Palindrome")
else:
  print("Not Palindrome")