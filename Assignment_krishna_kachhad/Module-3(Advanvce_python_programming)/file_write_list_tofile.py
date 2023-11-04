# Write a Python program to write a list to a file.


l1=["welcome","to","tops","technology"]
f=open("pyth_file.txt", "r+")

for l in l1:
    f.write(f"{l}\n")
print(f.read())

print("list is successfully added")

#-----------------------------------OR---------------------------------------

l1=["welcome","to","tops","technology"]
f=open("pyth_file.txt", "w+")
for items in l1:
        f.write('%s\n' %items)

print("list is successfully added")
f.close()
