class student:
    
    def getdata(self,city): # method overloading: Same method name but argument different
        print("City:",city)
    
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

st=student()
#st.getdata("Rajkot")
st.getdata(1,'Sanket')