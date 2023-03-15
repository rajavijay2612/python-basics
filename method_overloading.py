class Person:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create object
person = Person()
# Call the method hello
person.Hello()
# Call the method with a parameter
person.Hello('vijay')