# Write a Python program to split a list into different variables.

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("day", "month", "hour"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1, var2, var3 = color
print(var1)
print(var2)
print(var3)


#------------------Using slicing---------------------

list_value = ['John', 'Alex', 43, True, 55.5, 34]
 
step_size = 3

for i in range(0, len(list_value), step_size):
    new_list = list_value[i:i + step_size]
    print("After Splitting List: ", new_list)
