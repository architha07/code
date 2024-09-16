

class person:
    def __init__(self,age,gender,address,height):

        self.age=age
        self.gender=gender
        self.address=address
        self.height=height


    def myintro(self):
        print("Hello, my gender is",self.gender)
        print("Hello, my age is",self.age)
        print("Hello, my address is", self.address)
        print("Hello, my height is", self.height)

harry=person(36,"male","24/7 street",167)

harry.myintro()

