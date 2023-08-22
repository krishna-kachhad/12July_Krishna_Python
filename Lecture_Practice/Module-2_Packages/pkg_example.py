# pkg_example is the main py file

#-------------get output from topspkg folder----------
from topspkg import mylib,newlib

mylib.getdata(1,'Sanket','Python')

newlib.getsum(34,56)
newlib.production(45,67)



#--------------get output from topspkg/general folder---------
from topspkg.general import mylib,newlib

mylib.getdata(1,'Nirav','PHP')

newlib.getsum(34,56)