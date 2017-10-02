

class inout:

    def __init__(self):
        pass

    def getString(self):
        self.input = raw_input(">>>> ")

    def printString(self):
        return self.input.upper()

n = inout()

n.getString()

print n.printString()
