class student:
    @staticmethod # not require self parameter coz we declare static method
    def getsum(a,b):
        print("Sum:",a+b)


st=student()
st.getsum(34,56)