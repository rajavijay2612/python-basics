class Animal:
    def __init__(self,name,eat,sleep,sound):
        self.name = name
        self.eat = eat
        self.sleep = sleep
        self.sound = sound

obj_animal = Animal("Lion","hunting","eight_hours","roar")
print(obj_animal.name,obj_animal.eat,obj_animal.sleep,obj_animal.sound)

class Childone(Animal):
    pass
obj_child = Childone("Dog","Pedigree","morning","bark")
print(obj_child.name,obj_child.eat,obj_child.sleep,obj_child.sound)

class Childtwo(Animal):
    pass
obj_child_two = Childtwo("cat","milk","night","meow")
print(obj_child_two.name,obj_child_two.eat,obj_child_two.sleep,obj_child_two.sound)