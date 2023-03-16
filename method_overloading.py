class Person:
    def hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# Create object
person = Person()
# Call the method hello
person.hello()
# Call the method with a parameter
person.hello('vijay')