import re

mystr="This is String!"

#x=re.search('This',mystr)
#x=re.search('this',mystr)
x=re.search('is',mystr)
#x=re.search('S',mystr)
print(x)



import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
