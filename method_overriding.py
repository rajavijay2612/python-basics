class Parent:
    def call(self):
        print('Hello! Iam the parent class')

class Child(Parent):
    def call(self):
        print('Hello! Iam the child class')

child = Child()
child.call()
child = Parent()
child.call()

    

    