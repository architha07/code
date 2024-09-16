def function():
 
 import math

x1=int(input("Enter the value of x1:"))
y1=int(input("Enter the value of y1:"))
x2=int(input("Enter the value of x2:"))
y2=int(input("Enter the value of y2:"))

import math
d= math.sqrt((x2-x1)+(y2-y1))

print(d)





def code():
    id=input("Enter student id:")
    name=input("Enter student's first name:")
    last=input("Enter student's last name:")

    data=input("Are you new student in whitecliffe college? If yes, then enter “I am a newbie in Whitecliffe College !”")

    if "Whitecliffe" in data and "College" in data:
        personal_code= (id[:2]+ last[:3])
    print(personal_code)

    
if __name__ == "__main__":
   function()
   code()

   
   



    

    


