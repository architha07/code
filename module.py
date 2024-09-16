
class person:
    age=10
    gender='male'
harry=person()
sarrah=person()
print(harry.age)
print(sarrah.age)


class Person:
  def __init__(self, age, gender):
    self.age = age
    self.gender = gender

herry = Person(36,"male")

sarrah = Person(34, "female")

print(herry.age)
print(sarrah.age)

class person:
    def __init__(self,age,gender):
        self.age=age
        self.gender=gender

    def myintro(self):
        print("Hello, my gender is",self.gender)
        print("Hello, my age is",self.age)
harry=person(36,"male")
sarrah=person(34,"female")
harry.myintro()
sarrah.myintro()




class person:
    def __init__(self,age,gender):
        self.age=age
        self.gender=gender

    def myintro(self):
        print("Hello, my age is", self.age)
        print("Hello, my gender is", self.gender)
harry=person(36,"male")
sarrah=person(34,"female")
del harry.age
harry=person(24,"male")
harry.myintro()
sarrah.myintro()
