class Parent:
    def call():
        print('Hello! I am your Father')

class Child1:
    def call():
        print('Hello! I am your Elder son')


class Child2:
    def call():
        print('Hello! I am your Younger son')
        

class Raja:
    def call(self,daddy):
        daddy.call()

raja = Raja()
raja.call(Parent)
raja.call(Child1)
raja.call(Child2)
