

# Duck typing and EAFP
# Code written in more Pythonic Way

class Duck:

    def quack(self):
        print "Quack, quack"

    def fly(self):
        print "Flap, flap"

class Person:

    def quack(self):
        print "Person is quacking like a duck"

    def fly(self):
        print "I'm flapping my arms"


def quack_and_fly(thing):

    try:
        thing.quack()
        thing.fly()
        thing.bark()  #Will not execute as bark() is not present

    except AttributeError as e:
        print e

    print


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)



