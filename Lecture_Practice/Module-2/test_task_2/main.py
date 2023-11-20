import child

empty_str = str()
print("Role: 1. User".center(55))
print("Role: 2. Staff".center(55))
print(empty_str)
display = input ("Select role:")

if display == '1':
    child.mydata()

elif display == '2':
    child.mydata2()