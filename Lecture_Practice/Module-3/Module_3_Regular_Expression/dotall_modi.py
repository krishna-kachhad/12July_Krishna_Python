import re

mystr="This is Python!"

#x=re.findall('Py..n',mystr)
x=re.findall('This|That',mystr)
print(x)
