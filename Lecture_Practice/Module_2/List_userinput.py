city=[]  # OR   city=list()

n=int(input("Enter number of city:"))

#dynamic list
for i in range(n):
    x=input("Enter your city:")
    city.append(x)
    city.sort()

print(city)