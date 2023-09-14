def getdata(data):
    print("ID:",data['id'])
    print("Name:",data['nm'])
    print("Subject:",data['sub'])
    print("City:",data['ct'])


getdata({'id':101,'nm':'Sanket','sub':'Python','ct':'Rajkot'}) #dict arguments given in{}, give key & value

# -------------(ppt)dict as parameter--------------------
def student(**dict):

   for key,value in dict.items():
       print(key,value)

student(name="Anjali",marks=99)