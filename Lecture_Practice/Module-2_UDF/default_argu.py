#-------------------Types of function------------------
def getdata(id,name,sub='Python',city='Rajkot'):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)
    print("City:",city)


#getdata(101,'Sanket') #default arguments
#getdata(101,'Sanket','PHP') #positional arguments(according to position[sequence])


#getdata(id=101,name='Nirav') #keyword arguments

getdata(name='Sanket',id=45) #keyword arguments