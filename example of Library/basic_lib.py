class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print(self.x + ' ' + foo)

# a = A()               # We do not pass any argument to the __init__ method
# a.method_a('Sailor!') # We only pass a single argument
A()