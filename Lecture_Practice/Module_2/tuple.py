# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
tdata=("java", "python", "ruby", "android", "c")

print(tdata)
print(tdata[0])
print(tdata[-1])
#slicing
print(tdata[-2:-1])
print(tdata[1:4])
print(tdata[4:])
print(tdata[:3])
print(tdata[1:4:2])#with 2 jump
print(tdata[::2])#outpur:java, ruby,c
print(tdata[4:0:-2])#output:c,ruby

print(len(tdata))
print(tdata.count("python"))

#-------------------------------------------------
print(tdata.index("python"))

for i in tdata:
    print(f"Index[{tdata.index(i)}] = {i}")
#output Index[0] = java
#       Index[1] = python.........


del tdata

