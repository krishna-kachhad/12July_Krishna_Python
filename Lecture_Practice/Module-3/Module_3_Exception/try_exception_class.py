try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",A+b)
except Exception as e: #called type error, return error like compiler
    print(e)
else:
    print("This is finally block!")