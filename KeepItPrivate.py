class myClass:
    __privateVar = 54

    def __privateMethod(self):
        print("Im inside of myClass")

    def hello(self):
        print("Private variable:",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privateMethod   