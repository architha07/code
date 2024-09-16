#this code generates a code for student from their data

dob=(input("Enter your DOB:"))
name=input("Enter your name:")
college=input("Enter your college name:")

personal_code=(dob[:3]+name[:3]+college[:3])
print(personal_code)

def add():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))

    return a+b
print(add())

    



    
