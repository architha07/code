class book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def func(self):
        return self.title
    def page(self):
        return self.pages*2
f1=book("mermaid","cb",80)
print(f1.func())
print(f1.page())


class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    
    def circumferance(self):
        return 2*3.14*self.radius
    
    def compare(self):
        if(self.radius<20):
            print("small")
        else:
            print("large")
f2=circle(2)
print(f2.area())
print(f2.circumferance())
print(f2.compare())
