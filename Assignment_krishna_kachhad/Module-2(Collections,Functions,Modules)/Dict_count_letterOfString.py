# Write a Python program to create a dictionary from a string.
  # Note: Track the count of the letters from the string.
  # Sample string: 'w3resource'
  # Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

st = input("Enter a string: ")

dic = {} #creates an empty dictionary

for ch in st:
    if ch in dic: #if next character is already in the dictionary
        dic[ch] += 1
    else: 
        dic[ch] = 1 #if ch appears for the first time

#Printing the count of characters in the string
print(dic)