# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.


print("Enter the Multiple Decimal Points Comma Separate...")
dec = input("").split(",")
print("Maximum: ", max(dec))
print("Minimum: ", min(dec))


#-----------------------Using function----------------------------

def max_min(data):
  max = data[0]
  min = data[0]
  for num in data:
    if num> max:
      max = num
    elif num< min:
        min = num
  return max, min

print(max_min([0.5, 10.6, 15.7, 40.8, -5.98, 42, 17.90, 28, 75]))