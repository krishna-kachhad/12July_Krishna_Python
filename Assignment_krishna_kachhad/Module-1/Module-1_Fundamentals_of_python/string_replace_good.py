# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
  #if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))'''
#
'''str=input("Enter the string: ")
str1=str.index("not")
str2=str.index("poor")
for i in str:
     if str.index(i) == str1 and str.index(i) == str2:
          str=str.replace("not", "good")
          print(str)'''

str=input("Enter the string: ")
a=str.split()
print(a)
for i in a:
    if str.find("not") and str.find("poor"):
        new_str=str.replace("not", "good")
        print(new_str)
    else:
        print(str)
    

