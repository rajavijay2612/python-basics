
class Animal:
    def __init__(self,name):
        self.name = name
    def get_eat(self,eat):
        return(eat)
    def get_sound(self,sound):
        return(sound)
    def get_sleep(self,sleep):
        return(sleep)

obj_animal = Animal("lion")
print(obj_animal.name)

class Childone(Animal):
    pass
obj_childone = Childone("Dog")
print(obj_childone.name,obj_childone.get_eat("pedigree"),obj_childone.get_sound("bark"),obj_childone.get_sleep("morning"))

class Childtwo(Animal):
    pass
obj_childtwo = Childtwo("cat")
print(obj_childtwo.name,obj_childtwo.get_eat("milk"),obj_childtwo.get_sleep("night"),obj_childtwo.get_sound("meow"))
