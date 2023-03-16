class Duck:
    def greet(self):
        print('Hello! I am your Duck')

#class Vijay:
    #def greet(self):
        #print('Hello! I am your Elder son')


#class Vikas:
    #def greet(self):
        #print('Hello! I am your Younger son')
        

class Raja:
    def greet(self,any_animal): #the parameter any_friend accepts any object. this is called as dynamic typing
        any_animal.greet() # raja is not any_friend but he is calling call method of any_friend object

raja = Raja()
duck = Duck()
raja.greet(duck) # ducktyping

any_animal = 3
any_animal = "raja" #dynamic typing

#raju = Raju()
#vijay= Vijay()
#vikas = Vikas()

#duck.greet(raju)
#duck.greet(vijay)
#duck.greet(vikas)
