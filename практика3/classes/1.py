#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
class MyClass:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())    
# getString() - method takes user input and stores in input_string
#printString() - method to print the stored string in upper case letter        