# polymorphism => Duck Typing
# Same as interface as java need to give definition of method

class Pycharm:

    def execute(self):
        print("Compiled")
        print("Execute")

class VSCode:
    def execute(self):
        print("Line checker")
        print("Symbol generator")
        print("Debugger")

class Laptop:
    def code(self,ide):
        ide.execute()

p1=Pycharm()
v1=VSCode()

lap=Laptop()
lap.code(p1)
lap.code(v1)


# Compiled
# Execute
# Line checker
# Symbol generator
# Debugger